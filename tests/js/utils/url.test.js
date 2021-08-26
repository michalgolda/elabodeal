import { 
    setCurrentURLParam, 
    getCurrentURLParams, 
    setCurrentURLParams, 
    getCurrentURLParamValue} from '../../../elabodeal/web/static/js/utils/url'


afterEach(() => {
    window.history.pushState(
        null, 
        null, 
        'http://localhost/'
    )
})

test('setCurrentURLParam', () => {
    const paramKey = 'test'
    const paramValue = 'test'

    setCurrentURLParam(paramKey, paramValue)
    
    const expectedValue = 'http://localhost/?test=test'

    const currentLocationHref = window.location.href

    expect(currentLocationHref).toEqual(expectedValue)
})

test('setCurrentURLParams', () => {
    const params = {
        'test1': 'test1',
        'test2': 'test2'
    }

    setCurrentURLParams(params)

    const expectedValue = 'http://localhost/?test1=test1&test2=test2'

    const currentLocationHref = window.location.href

    expect(currentLocationHref).toEqual(expectedValue)
})

test('getCurrentURLParams', () => {
    window.history.pushState(
        null,
        null,
        'http://localhost/?test=test'
    )

    const currentURLParams = getCurrentURLParams()

    const expectedValue = { test: 'test' }

    expect(currentURLParams).toEqual(expectedValue)
})

test('getCurrentURLParamValue', () => {
    window.history.pushState(
        null,
        null,
        'http://localhost/?test=test'
    )

    const currentParamValue = getCurrentURLParamValue('test')

    const expectedValue = 'test'

    expect(currentParamValue).toEqual(expectedValue)
})