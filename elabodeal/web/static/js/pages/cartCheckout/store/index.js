import { createStore } from 'vuex'
import { 
	uiModule,
	mainModule, 
	paymentModule, 
	deliveryModule } from './modules'


const modules = {
	ui: uiModule,
	main: mainModule,
	payment: paymentModule,
	delivery: deliveryModule
}

const store = createStore({ modules })

export default store