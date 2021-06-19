import { mount } from 'mount-vue-component';


const Modal = {
	install: function ( app ) {
		var destroyMountedModalComponent;

		app.config.globalProperties.modal = {
			show: function ( ModalComponent ) {
				const { destroy } = mount(
					ModalComponent,
					{
						app,
						element: document.body
					}
				);

				destroyMountedModalComponent = destroy;
			},
			hide: () => {
				destroyMountedModalComponent();
			}
		}
	}
}

export default Modal;