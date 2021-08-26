import { createStore } from 'vuex';
import { savedCartService } from '@/services';
import { getApplicationData } from '@/utils/data';

const initialState = () => {
    const { sc: sharedCart } = getApplicationData();
    
    return {
        shareURLPath: sharedCart ? sharedCart.sup : null
    }
};


const store = createStore({
    namespaced: true,
    state: initialState(),
    getters: {
        getShareURLPath (state) {
            return state.shareURLPath;
        }
    },
    actions: {
        shareCart (ctx, { cartId }) {
            const shareURLPath = ctx.getters.getShareURLPath;
            const actionType = shareURLPath ? 'SHOW_SHARED_DATA' : 'CREATE_NEW_SHARE';

            switch (actionType) {
                case 'SHOW_SHARED_DATA':
                    var modalContext = { shareURLPath };

                    this.$modalManager.show(
                        'sharedCartModal', 
                        modalContext
                    );

                    break;
                case 'CREATE_NEW_SHARE':
                    var data = new FormData();

                    data.append('savedCartId', cartId);
                
                    savedCartService.share(data, {
                        successCallback: ({ data }) => {
                            const modalContext = {
                                shareURLPath: data.share_url_path
                            };

                            this.$modalManager.show('sharedCartModal', modalContext);
                        }
                    });

                    break;
            }

        },
        deleteCart (ctx, { cartId }) {
            const data = new FormData();

            data.append('savedCartId', cartId);

            savedCartService.delete(data, {
                successCallback: () => {
                    window.location = '/carts/';
                }
            });
        }
    }
});

export default store;