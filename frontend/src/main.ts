import { createApp } from 'vue'
import App from './App.vue'
import './index.css'

// Library
import * as VueRouter from 'vue-router'
import axios from 'axios'

import routes from './routes'

axios.defaults.baseURL = 'http://localhost:5000'

const router = VueRouter.createRouter({
  // 4. Provide the history implementation to use. We are using the hash history for simplicity here.
  history: VueRouter.createWebHashHistory(),
  routes, // short for `routes: routes`
})

createApp(App).provide('$axios', axios).use(router).mount('#app')
