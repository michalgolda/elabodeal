import { createStore } from 'vuex';
import { appData } from '@/utils/data';
import { publisherService } from '@/services';


const initialState = () => {
    const { userAlreadyFollowing } = appData;

    return {
        userAlreadyFollowing: userAlreadyFollowing
    }
};

const store = createStore({
    state: initialState(),
    mutations: {
        toggleUserAlreadyFollowing (state) {
            state.userAlreadyFollowing = !state.userAlreadyFollowing;
        },
        incrementFollowersCount () {
            const followersElement = document.getElementById('followers');
            const followers = Number(followersElement.textContent);

            followersElement.innerHTML = followers + 1;
        },
        decrementFollowersCount () {
            const followersElement = document.getElementById('followers');
            const followers = Number(followersElement.textContent);

            followersElement.innerHTML = followers - 1;
        }
    },
    actions: {
        followPublisherProfile (ctx, { publisherId }) {
            const data = new FormData();

            data.append('publisher_id', publisherId);

            publisherService.follow(data, {
                successCallback: () => {
                    ctx.commit('incrementFollowersCount');
                    ctx.commit('toggleUserAlreadyFollowing');
                }
            });
        },
        unFollowPublisherProfile (ctx, { publisherId }) {
            const data = new FormData();

            data.append('publisher_id', publisherId);

            publisherService.unFollow({ data }, {
                successCallback: () => {
                    ctx.commit('decrementFollowersCount');
                    ctx.commit('toggleUserAlreadyFollowing');
                }
            })
        }
    }
});

export default store;