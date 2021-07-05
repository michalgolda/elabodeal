const Alert = new class {
    constructor() {
        this.options = {
            visibleDuration: 5000,
            limit: 6,
        }
    }
    
    success( message, title = 'Sukces!' ) {
        this.show( message, title, 'success' );
    }

    error( message, title = 'Coś poszło nie tak!' ) {
        this.show( message, title, 'error' );
    }

    info( message, title = 'Informacja!' ) {
        this.show( message, title, 'info' );
    }

    show( message, title, type ) {
        var container = this._getContainer();
        
        if ( container.childElementCount >= this.options.limit ) return;
        
        var { element, elementCloseBtn } = this._createElement(
            message, 
            title, 
            type
        );

        var resetRemoveTimeout = () => {
            clearTimeout( element.removeTimeout );
        }

        var removeElement = () =>  {
            resetRemoveTimeout();

            this._removeElement( element );
        }

        var addRemoveTimeout = () => {
            element.removeTimeout = setTimeout( 
                removeElement,
                this.options.visibleDuration
            );
        }

        addRemoveTimeout();

        element.addEventListener( 'mouseover', resetRemoveTimeout );

        element.addEventListener( 'mouseout', addRemoveTimeout );

        elementCloseBtn.addEventListener( 'click', removeElement );

        container.append( element );
    }

    _removeElement( element ) {
        var container = this._getContainer();

        if ( container.childElementCount === 1 )
            this._removeContainer();

        element.remove();
    }

    _createElement( message, title, type ) {
        var stringHTMLElement = (
            `
            <div class="alert alert-${ type }">
                <div class="alert__header">
                    <div class="flex-center" style="justify-content: right;">
                        <h3 class="alert__title">${ title }</h3>
                    </div>
                    <i class="alert__close fas fa-times"></i>
                </div>
                <div class="alert__body">
                    <p class="alert__msg">${ message }</p>
                </div>
            </div>
            `
        );

        var element = $.parseHTML( stringHTMLElement.trim() )[ 0 ];
        var elementCloseBtn = $( element ).find( '.alert__close' )[ 0 ];

        return { element, elementCloseBtn };
    }    
    
    _getContainer() {
        var container = document.getElementById( 'alert-container' );

        return container ? container : this._createContainer();
    }

    _createContainer() {
        var container = document.createElement( 'div' );
        container.id = 'alert-container';
        
        document.body.appendChild( container );

        return container;
    }

    _removeContainer() {
        var container = this._getContainer();

        container.remove();
    }
}

export default Alert;