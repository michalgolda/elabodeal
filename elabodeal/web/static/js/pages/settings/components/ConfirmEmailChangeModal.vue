<template>
    <Modal
        title="Kod potwierdzający zmianę adresu email"
    >
        <CodeInput 
            @complete="handleComplete"
            @change="() => clearSectionError()"
            :class="{'code-invalid': invalidCode}"
        />
        <div class="flex-center">
            <button
                class="btn btn__secondary-outline"
                type="button"
                @click="handleResendCode"
            >
                Wyślij kod ponownie
            </button>
        </div>
    </Modal>
</template>
<script>
import { createNamespacedHelpers } from 'vuex';

import Modal from '../../../components/Modal.vue';
import CodeInput from '../../../components/CodeInput.vue';


const { mapState: mapUiState,
        mapMutations: mapUiMutations } = createNamespacedHelpers('ui');
const { mapActions: mapUserSettingsActions } = createNamespacedHelpers('userSettings');

export default {
    components: {
        Modal,
        CodeInput
    },
    computed: {
        email () {
            return this.context.email
        },
        ...mapUiState({
            invalidCode: state => state.section.error.code === 'invalidCode'
        })
    },
    methods: {
        ...mapUiMutations(['clearSectionError']),
        ...mapUserSettingsActions([
            'confirmChangeEmail',
            'resendChangeEmailCode'
        ]),
        handleComplete (code) {
            this.confirmChangeEmail({
                code,
                email: this.email
            });
        },
        handleResendCode () {
            this.resendChangeEmailCode({
                email: this.email
            });
        }
    }
}
</script>