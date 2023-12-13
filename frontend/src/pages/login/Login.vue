<template>
  <!-- <div class="login-container"> -->
  <common-layout>
    <div class="top">
      <div class="header">
        <img alt="logo" class="logo" src="@/assets/img/logo.png" />
        <span class="title">航Happen信息交流平台</span>
      </div>
      <div class="desc">航Happen 是北航最具影响力的信息交流平台</div>
    </div>
    <div class="login">
      <a-form @submit="onSubmit" :form="form">
        <a-tabs size="large" :tabBarStyle="{ textAlign: 'center' }" style="padding: 0 2px;">
          <a-tab-pane tab="账户密码登录" key="1">
            <a-alert type="error" :closable="true" v-if="error" :message="error" @close='onClose' showIcon
              style="margin-bottom: 24px;" />
            <a-form-item>
              <a-input autocomplete="autocomplete" size="large" placeholder="admin"
                v-decorator="['name', { rules: [{ required: true, message: '请输入账户名', whitespace: true }] }]">
                <a-icon slot="prefix" type="user" />
              </a-input>
            </a-form-item>
            <a-form-item>
              <a-input size="large" placeholder="888888" autocomplete="autocomplete" type="password"
                v-decorator="['password', { rules: [{ required: true, message: '请输入密码', whitespace: true }] }]">
                <a-icon slot="prefix" type="lock" />
              </a-input>
            </a-form-item>
          </a-tab-pane>
          <a-tab-pane tab="手机号登录" key="2">
            <a-form-item>
              <a-input size="large" placeholder="mobile number">
                <a-icon slot="prefix" type="mobile" />
              </a-input>
            </a-form-item>
            <a-form-item>
              <a-row :gutter="8" style="margin: 0 -4px">
                <a-col :span="16">
                  <a-input size="large" placeholder="captcha">
                    <a-icon slot="prefix" type="mail" />
                  </a-input>
                </a-col>
                <a-col :span="8" style="padding-left: 4px">
                  <a-button style="width: 100%" class="captcha-button" size="large">获取验证码</a-button>
                </a-col>
              </a-row>
            </a-form-item>
          </a-tab-pane>
        </a-tabs>
        <div>
          <a-checkbox :checked="true">自动登录</a-checkbox>
          <router-link style="float: right" to="/register">注册账户</router-link>
        </div>
        <a-form-item>
          <a-button :loading="logging" style="width: 100%;margin-top: 24px" size="large" htmlType="submit"
            type="primary">登录</a-button>
        </a-form-item>
      </a-form>
    </div>
  </common-layout>
  <!-- </div> -->
</template>

<script>
import CommonLayout from '@/layouts/CommonLayout'
import { login, getRoutesConfig } from '@/services/user'
import { setAuthorization } from '@/utils/request'
import { loadRoutes } from '@/utils/routerUtil'
import { mapMutations } from 'vuex'

export default {
  name: 'Login',
  components: { CommonLayout },
  data() {
    return {
      logging: false,
      error: '',
      form: this.$form.createForm(this)
    }
  },
  methods: {
    ...mapMutations('account', ['setUser', 'setPermissions', 'setRoles']),
    onSubmit(e) {
      e.preventDefault()
      this.form.validateFields((err) => {
        if (!err) {
          this.logging = true
          const name = this.form.getFieldValue('name')
          const password = this.form.getFieldValue('password')
          login(name, password).then(this.afterLogin).catch((err) => {
            this.logging = false
            this.error = err.code
            this.$message.error(err.response.data.reason, 1).then(() => {
              location.reload()
            })
          })
        }
      })
    },
    afterLogin(res) {
      /* 目前 permission、roles、auth 都是假数据，该部分待后端接口完成后再修改 */
      this.logging = false
      const loginRes = res.data
      const user = loginRes.user
      const permissions = [{ id: 'queryForm', operation: ['add', 'edit'] }]
      const roles = [{ id: 'admin', operation: ['add', 'edit', 'delete'] }]
      this.setUser(user)
      this.setPermissions(permissions)
      this.setRoles(roles)
      const auth = {
        token: 'Authorization:' + Math.random(),
        expireAt: new Date(new Date().getTime() + 30 * 60 * 1000)
      }
      setAuthorization(auth)
      // 获取路由配置
      getRoutesConfig().then(result => {
        const routesConfig = result.data.data
        loadRoutes(routesConfig)
        this.$router.push('/square')
        this.$message.success(loginRes.reason, 3)
      })
    },
    onClose() {
      this.error = false
    }
  }
}
</script>



<style lang="less" scoped>
// .login-container {
//   background-image: url('../../assets/img/login-background.png');
//   background-size: cover;
//   /* 其他样式属性 */
// }

.common-layout {
  // background-image: url('../../assets/img/login-background.png');
  // background-size: cover;

  .top {
    text-align: center;

    .header {
      height: 44px;
      line-height: 44px;

      a {
        text-decoration: none;
      }

      .logo {
        height: 44px;
        vertical-align: top;
        margin-right: 16px;
      }

      .title {
        font-size: 33px;
        color: @title-color;
        font-family: 'Myriad Pro', 'Helvetica Neue', Arial, Helvetica, sans-serif;
        font-weight: 600;
        position: relative;
        top: 2px;
      }
    }

    .desc {
      font-size: 14px;
      color: @text-color-second;
      margin-top: 12px;
      margin-bottom: 40px;
    }
  }

  .login {
    width: 368px;
    margin: 0 auto;

    @media screen and (max-width: 576px) {
      width: 95%;
    }

    @media screen and (max-width: 320px) {
      .captcha-button {
        font-size: 14px;
      }
    }

    .icon {
      font-size: 24px;
      color: @text-color-second;
      margin-left: 16px;
      vertical-align: middle;
      cursor: pointer;
      transition: color 0.3s;

      &:hover {
        color: @primary-color;
      }
    }
  }
}
</style>
