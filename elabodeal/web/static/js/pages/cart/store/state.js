import { getApplicationData } from '@/utils/data'


function state () {
    const applicationData = getApplicationData()

    const products = applicationData.products

    return {
        products,
        errors: {},
        loading: false
    }
}

export default state