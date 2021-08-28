import { getApplicationData } from '@/utils/data'


function state () {
    const {
        charts, 
        userAlreadyFollowing } = getApplicationData()

    return {
        charts,
        errors: {},
        loading: false,
        userAlreadyFollowing
    }
}

export default state