import TabsView from '@/layouts/tabs/TabsView'
import BlankView from '@/layouts/BlankView'
import PageView from '@/layouts/PageView'


// 路由配置
const options = {
  routes: [
    {
      path: '/login',
      name: '登录页',
      component: () => import('@/pages/login')
    },
    {
      path: '/register',
      name: '注册页',
      component: () => import('@/pages/register'),
    },
    {
      path: '/profile',
      name: '个人中心',
      component: () => import('@/pages/profile')
    },
    {
      path: '*',
      name: '404',
      component: () => import('@/pages/exception/404'),
    },
    {
      path: '/403',
      name: '403',
      component: () => import('@/pages/exception/403'),
    },
    {
      path:'/post',
      name:'发帖',
      component:()=>import('@/pages/post'),
    },
    {
      path: '/',
      name: '首页',
      component: TabsView,
      redirect: '/login',
      children: [
        {
          path: 'square',
          name: '广场',
          meta: {
            icon: 'file-ppt'
          },
          component: () => import('@/pages/square')
        },
        {
          path: 'parent1',
          name: '父级路由1',
          meta: {
            icon: 'dashboard',
          },
          component: BlankView,
          children: [
            {
              path: 'demo1',
              name: '演示页面1',
              component: () => import('@/pages/demo'),
            },
            {
              path: 'demo2',
              name: '演示页面2',
              component: () => import('@/pages/demo'),
            },
            {
              path: 'demo3',
              name: '演示页面3',
              component: () => import('@/pages/demo'),
            },
            {
              path: 'demo4',
              name: '演示页面4',
              component: () => import('@/pages/demo'),
            }
          ]
        },
        {
          path: 'parent2',
          name: '父级路由2',
          meta: {
            icon: 'form'
          },
          component: PageView,
          children: [
            {
              path: 'demo5',
              name: 'children1',
              component: () => import('@/pages/demo'),
            },
            {
              path: 'demo6',
              name: 'children2',
              component: () => import('@/pages/demo'),
            }
          ]
        },
        {
          path: 'exception',
          name: '异常页',
          meta: {
            icon: 'warning',
          },
          component: BlankView,
          children: [
            {
              path: '404',
              name: 'Exp404',
              component: () => import('@/pages/exception/404')
            },
            {
              path: '403',
              name: 'Exp403',
              component: () => import('@/pages/exception/403')
            },
            {
              path: '500',
              name: 'Exp500',
              component: () => import('@/pages/exception/500')
            }
          ]
        },
        {
          path: 'post',
          name: '发帖',
          meta: {
            icon: 'file-ppt'
          },
          component: () => import('@/pages/post')
        },
        {
          name: '验权页面',
          path: 'auth/demo',
          meta: {
            icon: 'file-ppt',
            authority: {
              permission: 'form',
              role: 'manager'
            },
            component: () => import('@/pages/demo')
          }
        }
      ]
    }
  ]
}

export default options
