import * as path from '@/services/api'
import { request, METHOD, removeAuthorization } from '@/utils/request'

/**
 * 登录服务
 * @param name 账户名
 * @param password 账户密码
 * @returns {Promise<AxiosResponse<T>>}
 */
export async function login(name, password) {
  return request(path.LOGIN, METHOD.POST, {
    "user_name": name,
    "password": password,
  })
}

export async function register(name, password, email) {
  return request(path.REGISTER, METHOD.POST, {
    "user_name": name,
    "password": password,
    "email": email
  })
}

export async function getRoutesConfig() {
  return request(path.ROUTES, METHOD.GET)
}

export async function editProfile(before_name, name, password) {
  return request(path.EDITPROFILE, METHOD.POST, {
    "before_name": before_name, // 旧用户名
    "new_name": name,
    "new_password": password
  })
}
/* ----------------------------- 帖子部分 ------------------------- */

export async function newPost(name, title, content, board, tags) {
  return request(path.NEWPOST, METHOD.POST, {
    "user_name": name,
    "title": title,
    "content": content,
    "board": board,
    "tags": tags
  })
}

/**
 * @brief 查询帖子简介信息 用于展示
 * @param {string} user_name 用户名 
 * @param board 版块名
 * @param tags 标签
 */
export async function queryPost(title_keyword="",user_name="", board="", tags=[]) {
  return request(path.QUERYPOST, METHOD.GET, {
    "title_keyword":title_keyword,
    "user_name": user_name,
    "board": board,
    "tags": tags
  })
}

export async function postGet(post_id) {
  return request(path.POSTGET, METHOD.GET, {
    "post_id": post_id
  })
}

/* ----------------------------- 点赞部分 ------------------------- */

/**
 * @brief 用户点赞帖子
 * @param {string} user_name 用户名 
 * @param {int} post_id 帖子id
 */
export async function likePost(user_name, post_id) {
  return request(path.LIKE, METHOD.POST, {
    "user_name": user_name,
    "post_id": post_id
  })
}

/**
 * @brief 用户取消点赞帖子
 * @param {string} user_name 用户名 
 * @param {int} post_id 帖子id
 */
export async function unlikePost(user_name, post_id) {
  return request(path.UNLIKE, METHOD.POST, {
    "user_name": user_name,
    "post_id": post_id
  })
}

/**
 * @brief 用户点赞评论
 * @param {string} user_name 用户名 
 * @param {int} comment_id 帖子id
 */
export async function likeComment(user_name, comment_id) {
  return request(path.LIKECOMMENT, METHOD.POST, {
    "user_name": user_name,
    "comment_id": comment_id
  })
}

/**
 * @brief 用户取消点赞评论
 * @param {string} user_name 用户名 
 * @param {int} comment_id 帖子id
 */
export async function unlikeComment(user_name, comment_id) {
  return request(path.UNLIKECOMMENT, METHOD.POST, {
    "user_name": user_name,
    "comment_id": comment_id
  })
}

export async function uploadImage(file) {
  return request(path.UPLOADIMG, METHOD.POST, file)
}

/* ----------------------------- 通知部分 ------------------------- */
/**
 * @brief 获取某用户的消息list
 * @param {string} user_name 用户名
 * @return {JSON} 消息list
 */
export async function getNowNotice(user_name) {
  return request(path.GETNOWNOTICE, METHOD.GET, {
    "user_name": user_name
  })
}

async function readNotice(user_name, notice_id) {
  return request(path.READNOTICE, METHOD.POST, {
    "user_name": user_name,
    "notice_id": notice_id
  })
}
/**
 * 退出登录
 */
export function logout() {
  localStorage.removeItem(process.env.VUE_APP_ROUTES_KEY)
  localStorage.removeItem(process.env.VUE_APP_PERMISSIONS_KEY)
  localStorage.removeItem(process.env.VUE_APP_ROLES_KEY)
  removeAuthorization()
}
export default {
  login,
  logout,
  getRoutesConfig,
  register,
  newPost,
  queryPost,
  postGet,
  likePost,
  likeComment,
  unlikePost,
  unlikeComment,
  uploadImage,
  getNowNotice,
  readNotice
}
