import { mount } from 'mount-vue-component';


function ModalManagerStorage () {
	this.storageKey = '__modal__';
}

ModalManagerStorage.prototype.set = function (value) {
	value = JSON.stringify(value);

	localStorage.setItem(this.storageKey, value);
};

ModalManagerStorage.prototype.get = function () {
	const value = localStorage.getItem(this.storageKey);

	if (!value) return;

	const parsedValue = JSON.parse(value);

	return parsedValue;
};

ModalManagerStorage.prototype.clear = function () {
	localStorage.removeItem(this.storageKey);
};

function ModalManager ({ modals } = {}) {
	this.app = null;
	this.mountedModal = null;
	this.modalRegistry = {};
	this.storage = new ModalManagerStorage();

	if (modals) {
		const modalsNames = Object.keys(modals);

		for (var modalName of modalsNames) {
			const modalComponent = modals[modalName];

			this.register(modalName, modalComponent);
		}
	}
}

ModalManager.prototype.install = function (app) {
	this.app = app;

	app.config.globalProperties.$modalManager = this;

	app.mixin({
		mounted: () => this.restore()
	});
};

ModalManager.prototype.restore = function () {
	const modal = this.storage.get();

	if (!modal) return;

	const { name, context } = modal;

	this.show(name, context);
};

ModalManager.prototype.register = function (modalName, modalComponent) {
	this.modalRegistry[modalName] = modalComponent;
};

ModalManager.prototype.show = function (modalName, modalContext = {}) {
	if (this.mountedModal) return;

	const modalComponent = this.modalRegistry[modalName];

	if (!modalComponent) {
		console.warn(`You want show ${modalName} modal which aren't registered.`);
		
		return;
	}

	modalComponent.props = {
		context: {
			type: Object,
			default: {}
		}
	};

	this.mountedModal = mount(
		modalComponent,
		{
			app: this.app,
			element: document.body,
			props: { context: modalContext }
		}
	);

	this.storage.set({
		name: modalName,
		context: modalContext
	});
};


ModalManager.prototype.hide = function () {
	if (!this.mountedModal) {
		console.warn(`You are want hide modal, but any modal isn't visible.`);

		return;
	}

	this.mountedModal.destroy();
	this.mountedModal = null;

	this.storage.clear();
};

const createModalManager = (options) => {
	return new ModalManager(options);
};

export default createModalManager;