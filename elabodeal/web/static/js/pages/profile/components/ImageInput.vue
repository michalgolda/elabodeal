<template>
    <div 
        class="editImageInput"
        :class="{ 'editImageInput-empty': isEmpty }"
    >   
        <input 
            @change="uploadFile"
            type="file"
            ref="fileInputRef"
            style="display: none"
        >
        <img
            v-show="!isEmpty"
            class="editImageInput__img"
            ref="imageElmRef"
            :src="uploadedFileSrc"
        >
        <div 
            v-show="isEmpty" 
            class="editImageInput__empty"
        >
            <i class="fas fa-image" />
        </div>
        <template v-if="isEmpty">
            <div class="editImageInput__btnGroup">
                <button
                    @click="selectFile"
                    type="button"
                    class="btn btn__secondary"
                >
                    Prześlij
                </button>
            </div>
        </template>
        <template v-else>
            <div class="editImageInput__btnGroup">
                <button
                    @click="selectFile"
                    type="button"
                    class="btn btn__secondary"
                >
                    Zmień
                </button>
                <button
                    @click="removeUploadedFile"
                    type="button"
                    class="btn btn__primary"
                >
                    Usuń
                </button>
            </div>
        </template>
    </div>
</template>
<script>
import { ref, toRefs } from 'vue'


export default {
    emits: ['upload', 'remove'],
    props: {
        uploadedFileSrc: {
            type: String,
            default: null
        }
    },
    setup (props, { emit }) {
        const { uploadedFileSrc } = toRefs(props)
        
        const imageElmRef = ref(null)
        const fileInputRef = ref(null)
        const isEmpty = ref(uploadedFileSrc.value ? false : true)

        const selectFile = () => fileInputRef.value.click()
        const uploadFile = () => {
            const file = fileInputRef.value.files[0]
            
            isEmpty.value = false
            
            const fileReader = new FileReader()

            fileReader.addEventListener('load', () => {
                imageElmRef.value.src = fileReader.result
            })

            fileReader.readAsDataURL(file)

            emit('upload', file)
        }
        const removeUploadedFile = () => {
            isEmpty.value = true

            imageElmRef.value.src = ''

            emit('remove')
        }

        return {
            isEmpty,
            selectFile,
            uploadFile,
            imageElmRef,
            fileInputRef,
            removeUploadedFile
        }
    }
}
</script>
