import { createNamespacedTypes, globalPropertiesWrapper } from '../../../elabodeal/web/static/js/utils/store'


test('globalPropertiesWrapper', () => {
    const store = { install: jest.fn() }

    const properties = ['test']

    const wrappedStore = globalPropertiesWrapper(
        store, 
        properties
    )

    const app = { config: { globalProperties: { test: 'test' } } }

    wrappedStore.install(app)

    expect(store.install).toBeCalled()
    expect(store.install.mock.calls[0][0]).toEqual(app)
    expect(store.hasOwnProperty(properties[0])).toBe(true)
})

test('createNamespacedTypes', () => {
    const typesNamespace = 'test'
    
    const typesDefinition = {
        actions: { TEST: 'TEST' },
        getters: { TEST: 'TEST' },
        mutations: { TEST: 'TEST' }
    }

    const createdNamespacedTypes = createNamespacedTypes(
        typesNamespace,
        typesDefinition
    )

    const expectedResult = {
        actions: { TEST: 'test/TEST' },
        getters: { TEST: 'test/TEST' },
        mutations: { TEST: 'test/TEST' }
    }

    expect(createdNamespacedTypes).toEqual(expectedResult)
    expect(createdNamespacedTypes).not.toEqual(typesDefinition)
})