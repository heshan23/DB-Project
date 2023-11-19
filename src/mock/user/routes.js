import Mock from 'mockjs'

Mock.mock(`${process.env.VUE_APP_API_BASE_URL}/routes`, 'get', () => {
  let result = {}
  result.code = 0
  result.data = [{
    router: 'root',
    children: ['square',
      {
        router: 'parent1',
        children: [
          {
            router: 'demo1',
            name: '休闲娱乐',
            authority: {
              permission: 'demo',
              role: 'admin'
            }
          },
          {
            router: 'demo2',
            name: '信息科技'
          },
          {
            router: 'demo3',
            name: '生活时尚'
          },
          {
            router: 'demo4',
            name: '课程交流'
          }
        ]
      },
      {
        router: 'parent2',
        children: [
          {
            router: 'demo5',
            name: '查询文章'
          },
          {
            router: 'demo6',
            name: '查询用户'
          }
        ]
      },
      {
        router: 'exception',
        children: ['exp404', 'exp403', 'exp500'],
      },
      'post',
      {
        router: 'demo',
        icon: 'file-ppt',
        path: 'auth/demo',
        name: '验权页面',
        authority: {
          permission: 'form',
          role: 'manager'
        }
      }
    ]
  }]
  return result
})
