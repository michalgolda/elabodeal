import { createStore } from 'vuex';
import { uiModule } from './modules';
import { getApplicationData } from '@/utils/data';
import { userService } from '@/services';


const initialState = () => {
    const { 
        supported_countries: supportedCountries 
    } = getApplicationData();

    return {
        supportedCountries
    }
};


const store = createStore({
    namespaced: true,
    state: initialState(),
    modules: {
        ui: uiModule
    },
    actions: {
        createPublisher (ctx, { firstName, lastName, country, accountNumber, swift }) {
            const data = new FormData();
            
            data.append('swift', swift);
            data.append('country', country);
            data.append('last_name', lastName);
            data.append('first_name', firstName);
            data.append('account_number', accountNumber);
        
            userService.createPublisher(data, {
                successCallback: () => {
                    window.location = '/m/';
                },
                errorCallback: ({ data }) => {
                    ctx.commit(
                        'ui/setErrors', 
                        data.error.details,
                        {root:true}
                    );
                }
            });
        }
    }
});

export default store;


