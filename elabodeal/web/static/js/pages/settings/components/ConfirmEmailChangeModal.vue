<template>
    <Modal
        title="Potwierdzenie zmiany adresu email"
    >
        <CodeInput 
            :class="{'code-invalid': codeErrors}"
            @complete="handleComplete"
            @change="() => clearSectionError()"
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
            codeErrors: state => state.section.error.code
        })
    },
    methods: {
        ...mapUiMutations(['clearSectionError']),
        ...mapUserSettingsActions([
            'confirmChangeEmail',
            'resendChangeEmailCode'
        ]),
        handleComplete (code) {
            this.clearSectionError();

            this.confirmChangeEmail({
                code,
                email: this.email
            });
        },
        handleResendCode () {
            this.resendChangeEmailCode({ email: this.email });
        }
    }
}
</script>