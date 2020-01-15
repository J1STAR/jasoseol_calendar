import Vue from 'vue'
import VueRouter from "vue-router";
import {routes} from './routes/routes'
import App from './App.vue'
import axios from 'axios'

Vue.config.productionTip = false;
Vue.prototype.$http = axios;
Vue.use(VueRouter);

const router = new VueRouter({
    mode: 'history',
    routes: routes,
});

new Vue({
    router,
    render: h => h(App),
}).$mount('#app');
