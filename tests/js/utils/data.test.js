import { getApplicationData } from '../../../elabodeal/web/static/js/utils/data'


test('getApplicationData', () => {
    const stringData = JSON.stringify({ test: 'test' })

    document.body.innerHTML = `
        <script 
            id="application-data"
            type="application/json"
        >
            ${stringData}
        </script>
    `

    const applicationData = getApplicationData()

    const expectedResult = JSON.parse(stringData)

    expect(applicationData).toEqual(expectedResult)
})