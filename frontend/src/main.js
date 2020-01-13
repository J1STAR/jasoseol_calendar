import Vue from 'vue'
import {router} from 'routes/route'
import App from './App.vue'
import axios from 'axios'

Vue.config.productionTip = false;
Vue.prototype.$http = axios;

new Vue({
    router,
    render: h => h(App),
}).$mount('#app');
