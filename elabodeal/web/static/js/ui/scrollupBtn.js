export default class ScrollUpBtnUIComponent {
    constructor() {
        this.elements = this.loadElements();
        this.handlers = this.loadHandlers();

        this.bindUIActions();
    }

    bindUIActions() {
        this.elements.btn.on( 'click', this.handlers.handleClick );
    }

    loadElements() {
        return {
            btn: $( '#js-scrollup-btn' )
        }
    }

    loadHandlers() {
        return {
            handleClick: () => {
                $( 'html, body' ).animate( {
                    scrollTop: 0
                }, 1000 );
            }
        }
    }
}