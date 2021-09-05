import mutations, { mutationsTypes } from '@/pages/profile/store/mutations'


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


describe('UPDATE_PROFILE', () => {
    test(mutationsTypes.UPDATE_PROFILE_REQUEST, () => {
        const state = { loading: false, errors: { test: 'test' } }

        mutations[mutationsTypes.UPDATE_PROFILE_REQUEST](state)

        expect(state).toStrictEqual({ loading: true, errors: {} })
    })

    test(mutationsTypes.UPDATE_PROFILE_SUCCESS, () => {
        const state = { loading: true, profile: {} }

        document.body.innerHTML = `
            <span id="bio"></span>
            <span id="who-you-are"></span>
            <span id="banner-text"></span>
            <div class="profileBanner__content"></div>
        `

        mutations['$modalManager'] = { hide: jest.fn() }

        mutations[mutationsTypes.UPDATE_PROFILE_SUCCESS](state, {
            profile: {
                bio: 'test',
                banner_text: 'test',
                who_you_are: 'test',
                banner_product: { cover_img: { path: 'test' } }
            }
        })

        const bioElm = document.querySelector('#bio')
        const whoYouAreElm = document.querySelector('#who-you-are')
        const bannerTextElm = document.querySelector('#banner-text')

        const bannerProductElm = document.querySelector('.profileBanner__productHighlight')

        expect(state).toStrictEqual({
            loading: false,
            profile: {
                bio: 'test',
                banner_text: 'test',
                who_you_are: 'test',
                banner_product: { cover_img: { path: 'test' } }
            }
        })

        expect(bioElm.textContent).toBe('test')
        expect(whoYouAreElm.textContent).toBe('test')
        expect(bannerTextElm.textContent).toBe('test')
        expect(bannerProductElm.src).toBe('http://localhost/test')
        expect(mutations.$modalManager.hide).toBeCalled()
    })

    test(mutationsTypes.UPDATE_PROFILE_FAILURE, () => {
        const state = { loading: true, errors: {} }

        mutations[mutationsTypes.UPDATE_PROFILE_FAILURE](state, {
            test: 'test'
        })

        expect(state).toStrictEqual({
            loading: false,
            errors: { test: 'test' }
        })
    })
})

describe('UPDATE_PROFILE_BANNER_IMG', () => {
    test(mutationsTypes.UPDATE_PROFILE_BANNER_IMG_REQUEST, () => {
        const state = { loading: false, errors: { test: 'test' } }

        mutations[mutationsTypes.UPDATE_PROFILE_BANNER_IMG_REQUEST](state)

        expect(state).toStrictEqual({
            loading: true,
            errors: {}
        })
    })

    test(mutationsTypes.UPDATE_PROFILE_BANNER_IMG_SUCCESS, () => {
        const state = { loading: true, profile: {} }

        document.body.innerHTML = `<div class="profileBanner__img"></div>`

        mutations[mutationsTypes.UPDATE_PROFILE_BANNER_IMG_SUCCESS](state, {
            profile: { banner_img: { path: 'test' } }
        })

        const bannerImgElm = document.querySelector('.profileBanner__img')

        expect(state).toStrictEqual({
            loading: false,
            profile: { banner_img: { path: 'test' } }
        })

        expect(bannerImgElm.src).toBe('http://localhost/test')
    })

    test(mutationsTypes.UPDATE_PROFILE_BANNER_IMG_FAILURE, () => {
        const state = { loading: true, errors: {} }

        mutations[mutationsTypes.UPDATE_PROFILE_BANNER_IMG_FAILURE](state, {
            test: 'test'
        })

        expect(state).toStrictEqual({
            loading: false,
            errors: { test: 'test' }
        })
    })
})

describe('UPDATE_PROFILE_AVATAR_IMG', () => {
    test(mutationsTypes.UPDATE_PROFILE_AVATAR_IMG_REQUEST, () => {
        const state = { loading: false, errors: { test: 'test' } }

        mutations[mutationsTypes.UPDATE_PROFILE_AVATAR_IMG_REQUEST](state)

        expect(state).toStrictEqual({
            loading: true,
            errors: {}
        })
    })

    test(mutationsTypes.UPDATE_PROFILE_AVATAR_IMG_SUCCESS, () => {
        const state = { loading: true, profile: {} }

        document.body.innerHTML = `<div class="profileBadge__avatar"></div>`

        mutations[mutationsTypes.UPDATE_PROFILE_AVATAR_IMG_SUCCESS](state, {
            profile: { avatar_img: { path: 'test' } }
        })

        const avatarImgElm = document.querySelector('.profileBadge__avatar')

        expect(state).toStrictEqual({
            loading: false,
            profile: { avatar_img: { path: 'test' } }
        })

        expect(avatarImgElm.src).toBe('http://localhost/test')
    })

    test(mutationsTypes.UPDATE_PROFILE_AVATAR_IMG_FAILURE, () => {
        const state = { loading: true, errors: {} }

        mutations[mutationsTypes.UPDATE_PROFILE_AVATAR_IMG_FAILURE](state, {
            test: 'test'
        })

        expect(state).toStrictEqual({
            loading: false,
            errors: { test: 'test' }
        })
    })
})