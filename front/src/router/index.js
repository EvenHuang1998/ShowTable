import Vue from 'vue'
import Router from 'vue-router'
import ShowTable from "@/views/ShowTable"
Vue.use(Router)

export default new Router({
  mode:"history",
  routes: [
    {
      path: "/",
      name: "homepage",
      component: ShowTable
    }
  ]
})
