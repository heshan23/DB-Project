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
    name: '查询',
    icon: 'form',
    component: view.blank
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
  square: {
    name: '广场',
    path: '/square',
    icon: 'rise',
    component: () => import('@/pages/square')
  },
  article: {
    name: '文章',
    path: '/article',
    component: () => import('@/pages/article')
  },
  board1:{
    path:'/board1',
    name:'休闲娱乐',
    component: () => import('@/pages/board1')
  },
  board2:{
    path:'/board2',
    name:'信息科技',
    component: () => import('@/pages/board2')
  },
  board3:{
    path:'/board3',
    name:'生活时尚',
    component: () => import('@/pages/board3')
  },
  board4:{
    path:'/board4',
    name:'课程交流',
    component: () => import('@/pages/board4')
  },
  board5:{
    path:'/board5',
    name:'原神天地',
    component: () => import('@/pages/board5')
  },
  find_article:{
    path:'/find_article',
    name:'查询文章',
    component:()=>import('@/pages/find_article')
  }
}
export default routerMap
