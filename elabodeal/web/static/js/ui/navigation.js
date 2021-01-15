export default class NavigationUIComponent {
    constructor() {
        this.elements = this.loadElements();
        this.handlers = this.loadHandlers();

        this.bindUIActions();
    }

    bindUIActions() {
        this.elements.showMenuBtn.on( 'click', () => {
            var isHidden = this.elements.menu.is( ':hidden' );

            if ( isHidden ) this.handlers.handleShowMenu()
            else this.handlers.handleHideMenu();
        } );

        this.elements.menu.hover( null, this.handlers.handleHideMenu );
    }

    loadElements() {
        return {
            menu: $( '#js-menu' ),
            showMenuBtn: $( '#js-show-menu' ),
            arrowIcon: {
                up: $( '#js-show-menu' ).children( 'fa-angle-down' ),
                down: $( '#js-show-menu').children( 'fa-angle-up' )
            }
        }
    }

    loadHandlers() {
        return {
            handleShowMenu: () => {
                this.elements.menu.show();
    
                this.elements.arrowIcon.up.hide();
                this.elements.arrowIcon.down.show();
            },
    
            handleHideMenu: () => {
                this.elements.menu.hide();
    
                this.elements.arrowIcon.up.show();
                this.elements.arrowIcon.down.hide();
            }
        }
    }
}