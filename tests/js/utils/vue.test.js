import { createApp } from 'vue'
import { mountComponents } from '../../../elabodeal/web/static/js/utils/vue'


test('mountComponents', () => {
    const components = { 'hello-world': { template: '<p id="hello-world">hello, world!</p>' } }

    const app = createApp()

    document.body.innerHTML = `<div id="hello-world"></div>`
    
    mountComponents(app, components)

    const helloWorldElm = document.getElementById('hello-world')

    expect(helloWorldElm.textContent).toBe('hello, world!')
})