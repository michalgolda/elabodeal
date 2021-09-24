<template>
    <Modal title="Edytuj profil">
        <form
            class="form editForm"
            @submit.prevent="updateProfile"
        >
            <div class="form__input-group">
                <label>Zdjęcie profilowe</label>
                <InputErrorsWrapper :errors="errors.avatarImg">
                    <ImageInput 
                        @upload="handleUploadAvatarImg"
                        @remove="handleRemoveUploadedAvatarImg"
                        :uploaded-file-src="avatarImgSrc"
                        class="editImageInput-avatar" 
                    />
                </InputErrorsWrapper>
            </div>
            <div class="form__input-group">
                <label>Baner</label>
                <InputErrorsWrapper :errors="errors.bannerImg">
                    <ImageInput
                        @upload="handleUploadBannerImg"
                        @remove="handleRemoveUploadedBannerImg"
                        :uploaded-file-src="bannerImgSrc"
                        class="editImageInput-banner"
                    />
                </InputErrorsWrapper>
            </div>
            <div class="form__input-group">
                <label>Wyrożniony produkt</label>
                <InputErrorsWrapper :errors="errors.bannerProduct">
                    <select v-model="bannerProductInputValue">
                        <option 
                            value=""
                            :selected="bannerProductInputValue ? false : true"
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
                </InputErrorsWrapper>
            </div>
            <div class="form__input-group">
                <label>Tekst widoczny na banerze</label>
                <InputErrorsWrapper :errors="errors.bannerText">
                    <CharCounter
                        v-slot="charCounter"
                        :max-value="50"
                        :initial-value="bannerTextInputValue.length"
                    >
                        <input
                            type="text"
                            :maxlength="50"
                            @input="charCounter.update"
                            v-model="bannerTextInputValue"
                        >
                    </CharCounter>
                </InputErrorsWrapper>
            </div>
            <div class="form__input-group">
                <label>Kim jesteś ?</label>
                <InputErrorsWrapper :errors="errors.whoYouAre">
                    <CharCounter
                        v-slot="charCounter"
                        :max-value="50"
                        :initial-value="whoYouAreInputValue.length"
                    >
                        <input
                            type="text"
                            :maxlength="50"
                            @input="charCounter.update"
                            v-model="whoYouAreInputValue"
                        >
                    </CharCounter>
                </InputErrorsWrapper>
            </div>
            <div class="form__input-group">
                <label>Bio</label>
                <InputErrorsWrapper :errors="errors.bio">
                    <CharCounter
                        v-slot="charCounter"
                        :max-value="100"
                        :initial-value="whoYouAreInputValue.length"
                    >
                        <textarea 
                            :maxlength="100"
                            v-model="bioInputValue" 
                            @input="charCounter.update"
                        />
                    </CharCounter>
                </InputErrorsWrapper>
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
import { useStore } from 'vuex'
import { computed, reactive, toRefs } from 'vue'
import { actionsTypes } from '../store/actions'

import ImageInput from './ImageInput'
import Modal from '@/components/Modal'
import CharCounter from '@/components/CharCounter'
import InputErrorsWrapper from '@/components/InputErrorsWrapper'


export default {
    name: 'EditModal',
    components: { 
        Modal,
        ImageInput,
        CharCounter,
        InputErrorsWrapper
    },
    setup () {
        const store = useStore()

        const state = reactive({
            bioInputValue: store.state.profile.bio,
            whoYouAreInputValue: store.state.profile.who_you_are,
            bannerTextInputValue: store.state.profile.banner_text,
            bannerProductInputValue: computed(() => {
                const product = store.state.profile.banner_product

                return product ? product.id : null
            }),
            products: computed(() => store.state.products),
            avatarImgSrc: computed(() => {
                const avatarImg = store.state.profile.avatar_img

                return avatarImg ? avatarImg.path : null
            }),
            bannerImgSrc: computed(() => {
                const bannerImg = store.state.profile.banner_img

                return bannerImg ? bannerImg.path : null
            }),
            avatarImg: { file: null, updated: false },
            bannerImg:  { file: null, updated: false },
            errors: {
                bio: computed(() => store.state.errors.bio),
                avatarImg: computed(() => store.state.errors.avatar_img),
                bannerImg: computed(() => store.state.errors.banner_img),
                whoYouAre: computed(() => store.state.errors.who_you_are),
                bannerText: computed(() => store.state.errors.banner_text),
                bannerProduct: computed(() => store.state.errors.banner_product)
            }
        })

        const handleUploadAvatarImg = (file) => {
            state.avatarImg.file = file
            state.avatarImg.updated = true
        }
        
        const handleRemoveUploadedAvatarImg = () => {
            state.avatarImg.file = null
            state.avatarImg.updated = true
        }

        const handleUploadBannerImg = (file) => {
            state.bannerImg.file = file
            state.bannerImg.updated = true
        }

        const handleRemoveUploadedBannerImg = () => {
            state.bannerImg.file = null
            state.bannerImg.updated = true
        }
        
        const updateProfile = () => {
            state.bannerImg.updated && store.dispatch(
                actionsTypes.UPDATE_PROFILE_BANNER_IMG,
                { bannerImg: state.bannerImg.file }
            )

            state.avatarImg.updated && store.dispatch(
                actionsTypes.UPDATE_PROFILE_AVATAR_IMG,
                { avatarImg: state.avatarImg.file }
            )

            store.dispatch(
                actionsTypes.UPDATE_PROFILE,
                {
                    bannerProduct: state.bannerProductInputValue,
                    bio: state.bioInputValue ? state.bioInputValue : null,
                    whoYouAre: state.whoYouAreInputValue ? state.whoYouAreInputValue : null,
                    bannerText: state.bannerTextInputValue ? state.bannerTextInputValue : null
                }
            )
        }

        return {
            ...toRefs(state),
            updateProfile,
            handleUploadAvatarImg,
            handleUploadBannerImg,
            handleRemoveUploadedAvatarImg,
            handleRemoveUploadedBannerImg
        }
    }
}
</script>
