<template>
    <Modal title="Edytuj profil">
        <form
            @submit.prevent="updateProfile"
            class="form editForm"
        >
            <div class="form__input-group">
                <label>Zdjęcie profilowe</label>
                <p 
                    class="form__input-error-msg"
                    v-for="error in avatarImgErrors"
                    :key="error"
                >
                    {{ error }}
                </p>
                <ImageInput 
                    @upload="handleUploadAvatarImg"
                    @remove="handleRemoveUploadedAvatarImg"
                    :uploaded-file-src="avatarImgSrc"
                    class="editImageInput-avatar" 
                />
            </div>
            <div class="form__input-group">
                <label>Baner</label>
                <p 
                    class="form__input-error-msg"
                    v-for="error in bannerImgErrors"
                    :key="error"
                >
                    {{ error }}
                </p>
                <ImageInput 
                    @upload="handleUploadBannerImg"
                    @remove="handleRemoveUploadedBannerImg"
                    :uploaded-file-src="bannerImgSrc"
                    class="editImageInput-banner"
                />
            </div>
            <div class="form__input-group">
                <label>Wyrożniony produkt</label>
                <p 
                    class="form__input-error-msg"
                    v-for="error in bannerProductErrors"
                    :key="error"
                >
                    {{ error }}
                </p>
                <select ref="bannerProductInputRef">
                    <option 
                        :selected="bannerProductInputValue ? false : true"
                        value=""
                    >
                        Brak wyróżnienia
                    </option>
                    <option
                        v-for="product in products"
                        :key="product.id"
                        :value="product.id"
                        :selected="bannerProductInputValue === product.id ? true : false"
                    >
                        {{ product.title }}
                    </option>
                </select>
            </div>
            <div class="form__input-group">
                <label>Tekst widoczny na banerze</label>
                <p 
                    class="form__input-error-msg"
                    v-for="error in bannerTextErrors"
                    :key="error"
                >
                    {{ error }}
                </p>
                <input
                    type="text"
                    ref="bannerTextInputRef"
                    :value="bannerTextInputValue"
                >
            </div>
            <div class="form__input-group">
                <label>Kim jesteś ?</label>
                <p 
                    class="form__input-error-msg"
                    v-for="error in whoYouAreErrors"
                    :key="error"
                >
                    {{ error }}
                </p>
                <input 
                    type="text"
                    ref="whoYouAreInputRef"
                    :value="whoYouAreInputValue"
                >
            </div>
            <div class="form__input-group">
                <label>Bio</label>
                <p 
                    class="form__input-error-msg"
                    v-for="error in bioErrors"
                    :key="error"
                >
                    {{ error }}
                </p>
                <textarea 
                    ref="bioInputRef"
                    :value="bioInputValue"
                />
            </div>
            <button
                type="submit"
                class="btn btn-block btn__primary editForm__submit"
            >
                Zaktualizuj profil
            </button>
        </form>
    </Modal>
</template>
<script>
import { computed, ref } from 'vue'
import { useStore } from 'vuex'
import { actionsTypes } from '../store/actions'

import Modal from '@/components/Modal'
import ImageInput from './ImageInput'


export default {
    components: { Modal, ImageInput },
    setup () {
        const store = useStore()

        const bioInputValue = computed(() => {
            return store.state.profile.bio
        })

        const whoYouAreInputValue = computed(() => {
            return store.state.profile.who_you_are
        })

        const bannerTextInputValue = computed(() => {
            return store.state.profile.banner_text
        })

        const bannerProductInputValue = computed(() => {
            const bannerProduct = store.state.profile.banner_product

            return bannerProduct && bannerProduct.id
        })

        const products = computed(() => {
            return store.state.products
        })

        const avatarImgSrc = computed(() => {
            const avatarImg = store.state.profile.avatar_img

            return avatarImg ? avatarImg.path : null
        })

        const bannerImgSrc = computed(() => {
            const bannerImg = store.state.profile.banner_img

            return bannerImg ? bannerImg.path : null
        })

        const avatarImgFile = ref(null)

        const updatedAvatarImg = ref(false)

        const handleUploadAvatarImg = (file) => {
            avatarImgFile.value = file
            updatedAvatarImg.value = true
        }
        
        const handleRemoveUploadedAvatarImg = () => {
            avatarImgFile.value = null
            updatedAvatarImg.value = true
        }

        const bannerImgFile = ref(null)

        const updatedBannerImg = ref(false)

        const handleUploadBannerImg = (file) => {
            bannerImgFile.value = file
            updatedBannerImg.value = true
        }

        const handleRemoveUploadedBannerImg = () => {
            bannerImgFile.value = null
            updatedBannerImg.value = true
        }
        
        const bioInputRef = ref(null)   
        const whoYouAreInputRef = ref(null)
        const bannerTextInputRef = ref(null)    
        const bannerProductInputRef = ref(null)

        const updateProfile = () => {
            updatedBannerImg.value && store.dispatch(
                actionsTypes.UPDATE_PROFILE_BANNER_IMG,
                { bannerImg: bannerImgFile.value }
            )

            bannerImgFile.value = null

            updatedAvatarImg.value && store.dispatch(
                actionsTypes.UPDATE_PROFILE_AVATAR_IMG,
                { avatarImg: avatarImgFile.value }
            )

            avatarImgFile.value = null
            
            const bioInput = bioInputRef.value
            const whoYouAreInput = whoYouAreInputRef.value
            const bannerTextInput = bannerTextInputRef.value
            const bannerProductInput = bannerProductInputRef.value

            store.dispatch(
                actionsTypes.UPDATE_PROFILE,
                {
                    bannerProduct: bannerProductInput.value,
                    bio: bioInput.value ? bioInput.value : null,
                    whoYouAre: whoYouAreInput.value ? whoYouAreInput.value : null,
                    bannerText: bannerTextInput.value ? bannerTextInput.value : null
                }
            )
        }

        const avatarImgErrors = computed(() => {
            return store.state.errors.avatar_img
        })

        const bannerImgErrors = computed(() => {
            return store.state.errors.banner_img
        })

        const bannerProductErrors = computed(() => {
            return store.state.errors.banner_product
        })

        const bannerTextErrors = computed(() => {
            return store.state.errors.banner_text
        })

        const whoYouAreErrors = computed(() => {
            return store.state.errors.who_you_are
        })

        const bioErrors = computed(() => {
            return store.state.errors.bio
        })

        return { 
            products,
            bioErrors,
            bioInputRef,
            avatarImgSrc,
            bannerImgSrc,
            bioInputValue,
            updateProfile,
            whoYouAreErrors,
            avatarImgErrors,
            bannerImgErrors,
            updatedBannerImg,
            updatedAvatarImg,
            bannerTextErrors,
            whoYouAreInputRef,
            bannerTextInputRef,
            bannerProductErrors,
            whoYouAreInputValue,
            bannerTextInputValue,
            bannerProductInputRef,
            handleUploadAvatarImg,
            handleUploadBannerImg,
            bannerProductInputValue,
            handleRemoveUploadedAvatarImg,
            handleRemoveUploadedBannerImg
        }
    }
}
</script>
