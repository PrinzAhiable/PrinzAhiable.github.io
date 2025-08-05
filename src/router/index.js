import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import About from '../views/About.vue'
import Projects from '../views/Projects.vue'
import Contact from '../views/Contact.vue'
import Skills from '../views/Skills.vue'
import Landingpage from '../views/Landingpage.vue'

const routes = [
  { path: '/home', component: Home },
  { path: '/about', component: About },
  { path: '/projects', component: Projects },
  { path: '/contact', component: Contact },
  { path: '/skills', component: Skills },
  { path: "/", name: "Landingpage", component: Landingpage },
]

export default createRouter({
  history: createWebHistory(),
  routes,
})