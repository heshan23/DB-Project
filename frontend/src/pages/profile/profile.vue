<template>
    <div class="fullPage">
        <div class="profileTop">
            <div class="user_info">
                <img class="user_avatar" src="@/assets/img/avatar.jpg" />
                <div class="userText">
                    <div class="userName">
                        <span>{{ username }}</span>
                    </div>
                    <div class="signature">
                        <span>个性签名：{{ signature }}</span>
                    </div>
                </div>
            </div>
            <div class="editButton">
                <a-space size="small">
                    <a-button :loading="loading" ghost>上传头像</a-button>
                    <a-button :loading="loading" @click="edit" ghost>修改信息</a-button>
                    <a-modal v-model="visible" title="Edit Information" :confirm-loading="confirmLoading"
                        @ok="handleCreate">
                        <a-form :layout="formLayout" :form="form">
                            <a-form-item label="更改信息" :label-col="formItemLayout.labelCol"
                                :wrapper-col="formItemLayout.wrapperCol">
                            </a-form-item>
                            <a-form-item label="用户名" :label-col="formItemLayout.labelCol"
                                :wrapper-col="formItemLayout.wrapperCol">
                                <a-input placeholder="input placeholder" />
                            </a-form-item>
                            <a-form-item label="旧密码" :label-col="formItemLayout.labelCol"
                                :wrapper-col="formItemLayout.wrapperCol">
                                <a-input placeholder="input placeholder" />
                            </a-form-item>
                            <a-form-item label="新密码" :label-col="formItemLayout.labelCol"
                                :wrapper-col="formItemLayout.wrapperCol">
                                <a-input placeholder="input placeholder" />
                            </a-form-item>
                            <a-form-item :wrapper-col="buttonItemLayout.wrapperCol">
                                <a-button type="primary" @click="submit">
                                    Submit
                                </a-button>
                            </a-form-item>
                        </a-form>
                    </a-modal>
                </a-space>
            </div>

            <div class="profileStatistic">
                <div class="profileStatisticItem">
                    <div class="profileStatisticItemTitle">关注</div>
                    <div class="profileStatisticItemNum">0</div>
                </div>
                <div class="profileStatisticItem">
                    <div class="profileStatisticItemTitle">粉丝</div>
                    <div class="profileStatisticItemNum">0</div>
                </div>
                <div class="profileStatisticItem">
                    <div class="profileStatisticItemTitle">发布量</div>
                    <div class="profileStatisticItemNum">0</div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
export default {
    data() {
        return {
            username: "heshan",
            signature: "you",
            loading: false,
            visible: false,
            confirmLoading: false,
            formLayout: 'horizontal',
            form: this.$form.createForm(this)
        }
    },
    computed: {
        formItemLayout() {
            const { formLayout } = this;
            return formLayout === 'horizontal'
                ? {
                    labelCol: { span: 4 },
                    wrapperCol: { span: 14 },
                }
                : {};
        },
        buttonItemLayout() {
            const { formLayout } = this;
            return formLayout === 'horizontal'
                ? {
                    wrapperCol: { span: 14, offset: 4 },
                }
                : {};
        },
    },
    methods: {
        edit() {
            // this.$message.success('success');
            this.visible = true
        },
        handleCancel() {
            // open.value = false;
            this.visible = false
        },
        handleCreate() {
            this.visible = false;
        },
        submit() {
            // const name = this.form.getFieldValue('name')
            // const password = this.form.getFieldValue('password')
        }
    }
}
</script>

<!-- <template>
    <div>
      <a-button type="primary" @click="showModal">Open Modal with async logic</a-button>
      <a-modal v-model:open="open" title="Title" :confirm-loading="confirmLoading" @ok="handleOk">
        <p>{{ modalText }}</p>
      </a-modal>
    </div>
  </template>
  <script lang="ts" setup>
  import { ref } from 'vue';
  const modalText = ref<string>('Content of the modal');
  const open = ref<boolean>(false);
  const confirmLoading = ref<boolean>(false);
  
  const showModal = () => {
    open.value = true;
  };
  
  const handleOk = () => {
    modalText.value = 'The modal will be closed after two seconds';
    confirmLoading.value = true;
    setTimeout(() => {
      open.value = false;
      confirmLoading.value = false;
    }, 2000);
  };
  </script>
  
   -->
<style>
.fullPage {
    background-color: #adb2b9;
}

.profileTop {
    width: 1000px;
    height: 240px;
    margin-top: 30px;
    padding-top: 20px;
    background-image: url("../../assets/img/background.jpg");
    /* margin-top: auto; */
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    border-radius: 5px;
}

.user_info {
    width: 300px;
    height: 100px;
    margin-top: 110px;
    /* margin-left: 10px; */
    position: absolute;
    left: 18%;
    transform: translateX(-50%);
    display: flex;
    border-radius: 5px;
}

.user_avatar {
    width: 80px;
    height: 80px;
    background-color: #707884;
    overflow: hidden;
    border-radius: 50%;
}

.userText {
    margin-left: 20px;
    margin-top: 10px;
}

.userName {
    font-weight: bold;
    font-size: 24px;
    color: #ffffff;
}

.signature {
    font-size: 14px;
    color: #ffffff;
}

.editButton {
    width: 100px;
    height: 25px;
    margin-top: 160px;
    /* margin-left: 20px; */
    position: absolute;
    left: 82%;
    transform: translateX(-50%);
    display: flex;
    border-radius: 5px;
}

.profileStatistic {
    width: 1000px;
    height: 70px;
    background-color: #ffffff;
    margin-top: 220px;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    border-radius: 5px;
}

.profileStatisticItem {
    width: 33%;
    height: 100%;
    display: flex;
    flex-direction: column;
    margin-right: 20px;
    margin-left: 20px;
    align-items: center;
    justify-content: center;
}

/* .Information {
    margin-top: 300px;
    width: 1000px;
    height: 300px;
    background-color: #ffffff;
} */
</style>