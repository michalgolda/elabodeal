import mutations, { mutationsTypes } from '../../../../../elabodeal/web/static/js/pages/profile/store/mutations'


describe('FOLLOW_PUBLISHER_PROFILE', () => {
    test(mutationsTypes.FOLLOW_PUBLISHER_PROFILE_REQUEST, () => {
        const state = { loading: false }

        mutations[mutationsTypes.FOLLOW_PUBLISHER_PROFILE_REQUEST](state)

        expect(state).toStrictEqual({ loading: true })
    })

    test(mutationsTypes.FOLLOW_PUBLISHER_PROFILE_SUCCESS, () => {
        const state = { loading: true, userAlreadyFollowing: false }

        document.body.innerHTML = `<span id="followers">0</span>`

        mutations[mutationsTypes.FOLLOW_PUBLISHER_PROFILE_SUCCESS](state)

        const followersElm = document.getElementById('followers')

        expect(state).toStrictEqual({ 
            loading: false,
            userAlreadyFollowing: true
        })
        expect(followersElm.textContent).toBe('1')
    })

    test(mutationsTypes.FOLLOW_PUBLISHER_PROFILE_FAILURE, () => {
        const state = { loading: true, errors: {} }

        mutations[mutationsTypes.FOLLOW_PUBLISHER_PROFILE_FAILURE](state, {
            test: 'test'
        })

        expect(state).toStrictEqual({
            loading: false,
            errors: { test: 'test' }
        })
    })
})


describe('UNFOLLOW_PUBLISHER_PROFILE', () => {
    test(mutationsTypes.UNFOLLOW_PUBLISHER_PROFILE_REQUEST, () => {
        const state = { loading: false }

        mutations[mutationsTypes.UNFOLLOW_PUBLISHER_PROFILE_REQUEST](state)

        expect(state).toStrictEqual({ loading: true })
    })

    test(mutationsTypes.UNFOLLOW_PUBLISHER_PROFILE_SUCCESS, () => {
        const state = { loading: true, userAlreadyFollowing: true }

        document.body.innerHTML = `<span id="followers">1</span>`

        mutations[mutationsTypes.UNFOLLOW_PUBLISHER_PROFILE_SUCCESS](state)

        const followersElm = document.getElementById('followers')

        expect(state).toStrictEqual({ 
            loading: false,
            userAlreadyFollowing: false
        })
        expect(followersElm.textContent).toBe('0')
    })

    test(mutationsTypes.UNFOLLOW_PUBLISHER_PROFILE_FAILURE, () => {
        const state = { loading: true, errors: {} }

        mutations[mutationsTypes.UNFOLLOW_PUBLISHER_PROFILE_FAILURE](state, {
            test: 'test'
        })

        expect(state).toStrictEqual({
            loading: false,
            errors: { test: 'test' }
        })
    })
})