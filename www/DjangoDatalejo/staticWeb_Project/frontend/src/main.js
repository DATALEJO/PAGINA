// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import router from './router'
import BootstrapVue from 'bootstrap-vue'

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'
import VueAnalytics from 'vue-analytics'



/*axios.defaults.xsrfHeaderName = "X-CSRFTOKEN"
axios.defaults.xsrfCookieName = "csrftoken"*/

Vue.config.productionTip = false
Vue.use(BootstrapVue);

//Configuration VueAnalytics
Vue.use(VueAnalytics, {
  id: 'UA-171029601-1',
  router
})

// eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
/*
new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
*/


