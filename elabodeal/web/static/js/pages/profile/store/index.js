import { createStore } from 'vuex'
import { mainModule, chartsModule } from './modules'


const modules = { 
    main: mainModule,
    charts: chartsModule
}

const store = createStore({ modules })

export default store