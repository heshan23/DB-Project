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
          'board1',
          'board2',
          'board3',
          'board4',
        ]
      },
      {
        router: 'parent2',
        children: [
          'find_article'
          // {
          //   router: 'demo6',
          //   name: '查询用户'
          // }
        ]
      },
      'post',
      'profile',
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
