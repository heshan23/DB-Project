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
  DELETEPOST: `${BASE_URL}/Post/DeletePost/`,
  QUERYPOST: `${BASE_URL}/Post/QueryPost/`,
  POSTGET: `${BASE_URL}/Post/PostGet/`,
  NEWCOMMENT: `${BASE_URL}/Post/NewComment/`,

  LIKE: `${BASE_URL}/User/Like/`,
  LIKECOMMENT: `${BASE_URL}/User/LikeComment/`,
  UNLIKE: `${BASE_URL}/User/Unlike/`,
  UNLIKECOMMENT: `${BASE_URL}/User/UnlikeComment/`,
  UPLOADIMG: `${BASE_URL}/User/UploadImage/`,

  GETNOWNOTICE: `${BASE_URL}/Notice/GetNowNotice/`,
  READNOTICE: `${BASE_URL}/Notice/ReadNotice/`,
}
