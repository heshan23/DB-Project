import Mock from 'mockjs'
import '@/mock/extend'

Mock.mock(`${process.env.VUE_APP_API_BASE_URL}/register`, 'post', ({ body }) => {
    let result = { data: {} }
    const { name, password } = JSON.parse(body)

    let success = false
    if (name == 'admin' || password == '88888888') {
        success = false
    } else {
        success = true
    }
    if (success) {
        result.code = 0
        //result.message = Mock.mock('@TIMEFIX').CN + '，欢迎回来'
        //result.data.user = user
        //result.data.token = 'Authorization:' + Math.random()
        //result.data.expireAt = new Date(new Date().getTime() + 30 * 60 * 1000)
    } else {
        result.code = -1
        result.message = '用户名重复'
    }
    return result
})
