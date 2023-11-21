// 视图组件
const view = {
  tabs: () => import('@/layouts/tabs'),
  blank: () => import('@/layouts/BlankView'),
  page: () => import('@/layouts/PageView')
}

// 路由组件注册
const routerMap = {
  login: {
    authority: '*',
    path: '/login',
    component: () => import('@/pages/login')
  },
  register: {
    name: '注册页',
    path: '/register',
    component: () => import('@/pages/register')
  },
  demo: {
    name: '发帖',
    renderMenu: false,
    component: () => import('@/pages/demo')
  },
  exp403: {
    authority: '*',
    name: 'exp403',
    path: '403',
    component: () => import('@/pages/exception/403')
  },
  exp404: {
    name: 'exp404',
    path: '404',
    component: () => import('@/pages/exception/404')
  },
  exp500: {
    name: 'exp500',
    path: '500',
    component: () => import('@/pages/exception/500')
  },
  root: {
    path: '/',
    name: '首页',
    redirect: '/login',
    component: view.tabs
  },
  parent1: {
    name: '板块',
    icon: 'dashboard',
    component: view.blank
  },
  parent2: {
    name: '控制面板',
    icon: 'form',
    component: view.page
  },
  exception: {
    name: '异常页',
    icon: 'warning',
    component: view.blank
  },
  profile: {
    name: '个人中心',
    path: '/profile',
    component: () => import('@/pages/profile')
  },
  post: {
    name: '发帖',
    path: '/post',
    icon: 'edit',
    component: () => import('@/pages/post')
  },
  square:{
    name:'广场',
    path:'/square',
    icon:'rise',
    component:()=>import('@/pages/square')
  },
}
export default routerMap
