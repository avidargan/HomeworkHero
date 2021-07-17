import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import TeacherPortal from '../views/Teacher.vue'
import StudentLogin from '../views/StudentLogin.vue'
import StudentCode from '../views/StudentCode.vue'
import Question1 from '../views/Question1.vue'
import Question2 from '../views/Question2.vue'
import Question3 from '../views/Question3.vue'
import Question4 from '../views/Question4.vue'
import Question5 from '../views/Question5.vue'
import Question6 from '../views/Question6.vue'
import Question7 from '../views/Question7.vue'
import Question8 from '../views/Question8.vue'
import Question9 from '../views/Question9.vue'
import Question10 from '../views/Question10.vue'
import Results from '../views/Results.vue'

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
  {
    path: '/q1',
    name: 'Question1',
    component: Question1
  },
  {
    path: '/q2',
    name: 'Question2',
    component: Question2
  },
  {
    path: '/q3',
    name: 'Question3',
    component: Question3
  },
  {
    path: '/q4',
    name: 'Question4',
    component: Question4
  },
  {
    path: '/q5',
    name: 'Question5',
    component: Question5
  },
  {
    path: '/q6',
    name: 'Question6',
    component: Question6
  },
  {
    path: '/q7',
    name: 'Question7',
    component: Question7
  },
  {
    path: '/q8',
    name: 'Question8',
    component: Question8
  },
  {
    path: '/q9',
    name: 'Question9',
    component: Question9
  },
  {
    path: '/q10',
    name: 'Question10',
    component: Question10
  },
  {
    path: '/results',
    name: 'Results',
    component: Results
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
