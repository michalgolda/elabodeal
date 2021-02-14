import Vue from "vue";


const Modal = {
	install ( Vue, options ) {
		var mountedModalComponent = null;

		Vue.prototype.$modal = {
			show( e = null, Component ) {
				if ( Component === undefined )
					throw new Error( "Component argument must not be empty" );

				const mountElement = document.createElement( "div" );

				document.body.prepend( mountElement );

				const ModalComponent = Vue.extend( Component );
				
				mountedModalComponent = new ModalComponent( {
					el: mountElement,
					data() {
						return e ? {...e.target.dataset} : null;
					}
				} )
			},
			hide() {
				if ( mountedModalComponent )
					mountedModalComponent.$el.remove();
			}
		}
	}
}

export default Modal;