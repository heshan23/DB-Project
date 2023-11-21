//跨域代理前缀
//const API_PROXY_PREFIX='/api'
//const BASE_URL = process.env.NODE_ENV === 'production' ? process.env.VUE_APP_API_BASE_URL : API_PROXY_PREFIX
const BASE_URL = process.env.VUE_APP_API_BASE_URL
module.exports = {
  LOGIN: `${BASE_URL}/User/SignIn/`,
  ROUTES: `${BASE_URL}/routes`,
  REGISTER: `${BASE_URL}/User/SignUp/`,
}
