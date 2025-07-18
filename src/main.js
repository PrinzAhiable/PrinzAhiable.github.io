import { createApp } from 'vue'
import App from './App.vue'
import router from './router'

//  Import AOS
import AOS from 'aos'
import 'aos/dist/aos.css'

const app = createApp(App)

app.use(router)

//  Initialize AOS globally
app.mount('#app')
AOS.init({
  duration: 800,     // animation duration
  once: false,        // whether animation should happen only once
  easing: 'ease-out' // easing function
})
