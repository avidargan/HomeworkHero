import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import TeacherPortal from '../views/Teacher.vue'
import StudentLogin from '../views/StudentLogin.vue'
import StudentCode from '../views/StudentCode.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/teacher',
    name: 'TeacherPortal',
    component: TeacherPortal
  },
  {
    path: '/studentlogin',
    name: 'StudentLogin',
    component: StudentLogin
  },
  {
    path: '/studentcode',
    name: 'StudentCode',
    component: StudentCode
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
