import { createStore } from 'vuex'
import { uiModule, mainModule } from './modules'


const modules = {
    ui: uiModule,
    main: mainModule
}

const store = createStore({ modules });

export default store;