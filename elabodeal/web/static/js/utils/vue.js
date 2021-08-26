import { mount } from 'mount-vue-component';


/**
 * A function which mount and replace mount element with component.
 * This function use mount function from mount-vue-component library which
 * allow mount many of components using one app context.
 * 
 * @param {VueApp} app
 * @param {Object} components
 */
export function mountComponents (app, components) {
	for (var componentKey in components) {
		const component = components[componentKey]
		const mountElement = document.getElementById(componentKey)

		if (mountElement) {
			const vMountElement = mountElement.cloneNode(true)

			vMountElement.innerHTML = ''

			mount(component, {
				app,
				element: vMountElement,
				props: { ...mountElement.dataset }
			})

			const vMountElementChildNodes = vMountElement.childNodes

			const vMountElementHasFragment = vMountElementChildNodes.length > 1

			if (vMountElementHasFragment) {
				const vFragment = document.createElement('div')

				vFragment.append(...vMountElementChildNodes)

				vMountElement.innerHTML = ''
				vMountElement.appendChild(vFragment)
			}

			const vMountedComponent = vMountElementChildNodes[0]

			mountElement.replaceWith(vMountedComponent)
		}
	}
}

