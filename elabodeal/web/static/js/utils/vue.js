import { mount } from 'mount-vue-component';

 
export const mountPageComponents = (vueInstance, components) => {
	const keys = Object.keys(components);

	for (var key of keys) {
		const vueComponent = components[key];
		const mountElement = document.getElementById(key);

		if (mountElement) {
			const vMountElement = mountElement.cloneNode(true);

			vMountElement.innerHTML = '';

			mount(vueComponent, {
				app: vueInstance,
				props: { ...mountElement.dataset },
				element: vMountElement
			});

			let vMountElementChildNodes = vMountElement.childNodes;
			const vMountElementHasFragment = vMountElementChildNodes.length === 1;

			if (!vMountElementHasFragment) {
				const fragment = document.createElement('div');

				fragment.append(...vMountElementChildNodes);

				vMountElement.innerHTML = '';
				vMountElement.appendChild(fragment);
			}

			mountElement.replaceWith(vMountElementChildNodes[0]);
		}
	}
};