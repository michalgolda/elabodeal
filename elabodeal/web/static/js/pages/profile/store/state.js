import { getApplicationData } from '@/utils/data'


function state () {
    const {
        charts,
        profile,
        products,
        current_user_already_following: currentUserAlreadyFollowing
    } = getApplicationData()

    return {
        charts,
        profile,
        products,
        errors: {},
        loading: false,
        currentUserAlreadyFollowing
    }
}

export default state