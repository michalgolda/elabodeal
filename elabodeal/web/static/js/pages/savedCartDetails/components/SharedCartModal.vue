<template>
    <Modal title="Udostępnianie koszyka">
        <label>Link</label>
        <div class="flex-center">
            <input 
                type="text" 
                :value="shareURLPath" 
                readonly 
            >
            <button 
                ref="copyLinkBtn"
                :data-clipboard-text="shareURLPath"
                class="btn btn__primary modal-btn"
            >
                <i class="fas fa-copy" />
            </button>
        </div>
    </Modal>
</template>
<script>
import Alert from '@/alert';
import Modal from '@/components/Modal';


export default {
    components: {
        Modal
    },
    computed: {
        shareURLPath () {
            return this.context.shareURLPath;
        }
    },
    mounted () {
        const { copyLinkBtn } = this.$refs;

        // eslint-disable-next-line
        this.clipboardJS = new ClipboardJS(copyLinkBtn);

        this.clipboardJS.on('success', this.handleSuccessCopyLink);
    },
    methods: {
        handleSuccessCopyLink () {
            Alert.success('Link został pomyślnie skopiowany');
        }
    }
}
</script>