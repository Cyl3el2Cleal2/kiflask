import { createApp } from 'vue'
import App from './App.vue'
import './index.css'

import * as VueRouter from 'vue-router'

import routes from './routes'

const router = VueRouter.createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: VueRouter.createWebHashHistory(),
  routes, // short for `routes: routes`
})

createApp(App).use(router).mount('#app')
