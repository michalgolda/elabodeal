import { createStore } from 'vuex';
import { cartModule, uiModule } from './modules';


const modules = { 
    ui: uiModule,
    cart: cartModule
}

const store = createStore({ modules })

export default store