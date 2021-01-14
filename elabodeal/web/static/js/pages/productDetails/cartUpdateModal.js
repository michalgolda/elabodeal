export default class CartUpdateModalUIComponent {
    constructor() {
        this.elements = this.loadElements();
        
        this.bindUIActions();
    }

    bindUIActions() {
        this.elements.hideModalBtn.on(
            'click',
            () => this.elements.modal.remove()
        );

        this.elements.continueShoppingBtn.on(
            'click',
            () => this.elements.modal.remove()
        );
    }

    loadElements() {
        return {
            modal: $( '#js-cart-update-modal' ),
            hideModalBtn: $( '#js-hide-cart-update-modal' ),
            continueShoppingBtn: $( '#js-continue-shopping' )
        }
    }
}