//跨域代理前缀
//const API_PROXY_PREFIX='/api'
//const BASE_URL = process.env.NODE_ENV === 'production' ? process.env.VUE_APP_API_BASE_URL : API_PROXY_PREFIX
const BASE_URL = process.env.VUE_APP_API_BASE_URL
module.exports = {
  ROUTES: `${BASE_URL}/routes`,

  LOGIN: `${BASE_URL}/User/SignIn/`,
  REGISTER: `${BASE_URL}/User/SignUp/`,
  EDITPROFILE: `${BASE_URL}/User/EditProfile/`,
  NEWPOST: `${BASE_URL}/Post/NewPost/`,
  QUERYPOST: `${BASE_URL}/Post/QueryPost/`,
  POSTGET: `${BASE_URL}/Post/PostGet/`,
  LIKE: `${BASE_URL}/Post/Like/`,
  LIKECOMMENT: `${BASE_URL}/Post/LikeComment/`,
  UNLIKE: `${BASE_URL}/Post/Unlike/`,
  UNLIKECOMMENT: `${BASE_URL}/Post/UnlikeComment/`,
  UPLOADIMG: `${BASE_URL}/User/UploadImage/`,

  GETNOWNOTICE: `${BASE_URL}/Notice/GetNowNotice/`,
  READNOTICE: `${BASE_URL}/Notice/ReadNotice/`,
}
