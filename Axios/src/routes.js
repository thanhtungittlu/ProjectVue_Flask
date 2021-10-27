import Home from './components/Home'
import Admin from './components/Admin'
import Login from './components/Login'
import Register from './components/Register'

export const routes = [
    {path:'/', name: 'home', component: Login},
    {path:'/home', name: 'home', component: Home},
    {path:'/admin', name: 'admin', component: Admin},
    {path:'/register', name: 'register', component: Register},

]