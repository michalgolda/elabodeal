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
	const componentsKeys = Object.keys(components)

	for (var componentKey of componentsKeys) {
		const component = components[componentKey]
		const componentMountElm = document.getElementById(componentKey)

		if (componentMountElm) {
			const vComponentMountElm = componentMountElm.cloneNode(true)

			vComponentMountElm.innerHTML = ''

			mount(component, {
				app,
				element: vComponentMountElm,
				props: { ...componentMountElm.dataset }
			})

			const vComponentMountElmChildNodes = vComponentMountElm.childNodes
			
			const vComponentMountElmHasNotFragment = vComponentMountElmChildNodes !== 1

			if (vComponentMountElmHasNotFragment) {
				const vFragment = document.createElement('div')

				vFragment.append(...vComponentMountElmChildNodes)

				vComponentMountElm.innerHTML = ''
				vComponentMountElm.appendChild(vFragment)
			}

			const vMountedComponent = vComponentMountElmChildNodes[0]

			componentMountElm.replaceWith(vMountedComponent)
		}
	}
}