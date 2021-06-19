<template>
    <Modal
        title="Kod potwierdzający zmianę adresu email"
    >
        <form>
            <CodeInput 
                @complete="handleComplete"
            />
            <div class="flex-center">
                <button
                    class="btn btn__secondary-outline modal-btn"
                    type="button"
                >
                    Wyślij kod ponownie
                </button>
            </div>
        </form>
    </Modal>
</template>
<script>
import { mapState } from "vuex";

import Alert from "../../../alert";
import userService from "../../../services/user";

import CodeInput from "../../../components/CodeInput.vue";
import Modal from "../../../components/Modal.vue";


export default {
    computed: mapState( {
        user: state => state.user,
        email: state => state.forms.user.fields.email.value
    } ),
    components: {
        Modal,
        CodeInput
    },
    data: function () {
        return {
            code: ''
        }
    },
    methods: {
        handleComplete: function ( value ) {
            this.code = value;

            const formData = this._createFormDataObject();

            userService.confirmEmailChangeRequest
                .setFormData( formData )
                .setSuccessHandler( () => {
                    this.modal.hide();

                    user.email = this.email;

                    Alert.success( "Adres email został pomyślnie zmieniony." );
                } )
                .execute()
        },
        _createFormDataObject: function () {
            const formData = new FormData();

            formData.append("email", this.email);
            formData.append("code", this.code);

            return formData;
        }
    }
}
</script>