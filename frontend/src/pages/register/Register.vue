<template>
  <common-layout>
    <div class="top">
      <div class="header">
        <img alt="logo" class="logo" src="@/assets/img/logo.png" />
        <span class="title">航Happen信息交流平台</span>
      </div>
      <div class="desc">航Happen是北航最具影响力的信息交流平台</div>
    </div>
    <div class="register">
      <a-form @submit="onSubmit" :form="form">
        <a-form-item>
          <a-input id="user" autocomplete=false size="large" placeholder="请输入用户名" v-decorator="['name', rules.user]">
            <a-icon slot="prefix" type="user" />
          </a-input>
        </a-form-item>
        <a-form-item>
          <a-input id="pwd1" size="large" placeholder="请输入密码" autocomplete=false type="password"
            v-decorator="['password1', rules.pwd1]">
            <a-icon slot="prefix" type="lock" />
          </a-input>
        </a-form-item>
        <a-form-item>
          <a-input id="pwd2" size="large" placeholder="请确认密码" autocomplete=false type="password"
            v-decorator="['password2', rules.pwd2]">
            <a-icon slot="prefix" type="lock" />
          </a-input>
        </a-form-item>
        <a-form-item>
          <a-button :loading="logging" style="width: 100%;margin-top: 24px" size="large" htmlType="submit"
            type="primary">注册</a-button>
        </a-form-item>
      </a-form>
    </div>
  </common-layout>
</template>


<script>
import CommonLayout from '@/layouts/CommonLayout'
import { register } from '../../services/user'
export default {
  name: 'Register',
  components: { CommonLayout },
  data() {
    return {
      logging: false,
      error: '',
      form: this.$form.createForm(this),
      rules: {
        user: {
          rules: [{ required: true, message: '请输入账户名', whitespace: true }],
          trigger: 'blur',
        },
        pwd1: {
          rules: [{ required: true, message: '请输入密码', whitespace: true }],
          trigger: 'blur',
        },
        pwd2: {
          rules: [
            { required: true, message: '请确认密码', whitespace: true },
            { validator: this.checkPwd2, trigger: 'blur' }
          ],
          trigger: 'blur',
        }
      }
    }
  },
  methods: {
    onSubmit(e) {
      e.preventDefault()
      this.form.validateFields((err) => {
        if (!err) {
          this.logging = true
          const name = this.form.getFieldValue('name')
          const password = this.form.getFieldValue('password1')
          //还需要检查用户名是否已存在
          register(name, password).then(this.afterRegister)
        }
      })
    },

    afterRegister(res) {
      this.logging = false
      const registerRes = res.data
      if (registerRes.code >= 0) {
        this.$message.success('注册成功！', 1)
        this.$router.push('/login')
      } else {
        this.error = registerRes.message
        this.$message.error('用户名重复', 1)
      }
    },

    checkPwd2(rules, value, callback) {
      if (!value) {
        callback();
      }
      const pwd1 = this.form.getFieldValue('password1')
      if (value != null && value != pwd1) {
        callback(new Error('两次密码输入不一致'))
      }
      callback();
    }
  }
}
</script>

<style lang="less" scoped>
.common-layout {
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

  .register {
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
  }
}
</style>