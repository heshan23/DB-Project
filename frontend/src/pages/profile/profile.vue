<template>
    <div class="fullPage" style="margin-top: 20px;">

        <!-- <div class="profileStatistic">
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
            </div> -->
        <!-- </div> -->
        <a-row style="background-color: white; border-radius: 12px;">
            <div class="profileTop">
                <div class="user_info">
                    <img class="user_avatar" :src=avatar />
                    <div class="userText">
                        <div class="userName">
                            <span>{{ user_name }}</span>
                        </div>
                        <div class="e-mail">
                            <span>邮箱：{{ email }}</span>
                        </div>
                    </div>
                </div>
                <div class="editButton">
                    <a-space size="small">
                        <a-upload name="file" :showUploadList=false :file-list="fileList" :customRequest="customRequest">
                            <a-button :loading="loading" ghost>上传头像</a-button>
                        </a-upload>
                        <a-button :loading="loading" @click="edit" ghost>修改信息</a-button>
                        <a-modal v-model="visible" title="Edit Information" :confirm-loading="confirmLoading"
                            @ok="handleCreate">
                            <a-form :layout="formLayout" :form="form">
                                <a-form-item label="更改信息" :label-col="formItemLayout.labelCol"
                                    :wrapper-col="formItemLayout.wrapperCol">
                                </a-form-item>
                                <a-form-item label="用户名" :label-col="formItemLayout.labelCol"
                                    :wrapper-col="formItemLayout.wrapperCol">
                                    <a-input placeholder="请输入新用户名 留空则不变" v-decorator="['new_name', rules.user_name]" />
                                </a-form-item>
                                <a-form-item label="旧密码" :label-col="formItemLayout.labelCol"
                                    :wrapper-col="formItemLayout.wrapperCol">
                                    <a-input placeholder="请输入旧密码" v-decorator="['old_password', rules.old_password]" />
                                </a-form-item>
                                <a-form-item label="新密码" :label-col="formItemLayout.labelCol"
                                    :wrapper-col="formItemLayout.wrapperCol">
                                    <a-input placeholder="请输入新密码 留空则不变"
                                        v-decorator="['new_password', rules.new_password]" />
                                </a-form-item>
                                <a-form-item :wrapper-col="buttonItemLayout.wrapperCol">
                                </a-form-item>
                            </a-form>
                        </a-modal>
                    </a-space>
                </div>
            </div>
        </a-row>
        <div class="myPosts" style="margin-top: 30px;">
            <div style="background-color: white; border-radius: 12px;">
                <div style=" margin-left:10px;margin-right: 10px;margin-bottom: 10px;">
                    <a-list item-layout="vertical" size="large" :pagination="pagination" :data-source="contents">
                        <a-list-item slot="renderItem" key="item.title" slot-scope="item">
                            <template v-for="{ type, text } in item.actions" slot="actions">
                                <span :key="type">
                                    <a-icon :type="type" style="margin-right: 8px;" />
                                    {{ text }}
                                </span>
                            </template>
                            <a-button slot="extra" type="danger" style="margin-right: 15px"
                                @click="showConfirm(item.post_id)" ghost>
                                删除
                            </a-button>
                            <img slot="extra" style="width: 200px;height: 180px;" alt="logo" :src="item.picture"
                                @click="onClick(item.post_id)" />
                            <a-list-item-meta>
                                <a slot="title">{{ item.writer }}</a>
                                <a-avatar slot="avatar" :src="item.avatar" />
                            </a-list-item-meta>
                            <h1>{{ item.title }}</h1>
                            {{ item.content }}
                        </a-list-item>
                    </a-list>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
import { editProfile, logout } from '@/services/user'
import { mapGetters } from 'vuex';
// import { state } from '../../store/index'
import { queryPost, deletePost, UploadAvator } from '../../services/user';

export default {
    created() {
        this.$data.user_name = this.user.user_name
        this.$data.avatar = this.user.avatar
        this.$data.email = this.user.email
        queryPost(undefined, this.user.user_name, undefined, undefined).then(res => {
            console.log(res.data)
            const dataArray = res.data.contents
            for (let i = 0, len = dataArray.length; i < len; i++) {
                this.$data.contents.push({
                    title: dataArray[i].title,
                    avatar: dataArray[i].avatar,
                    picture: dataArray[i].picture,
                    writer: dataArray[i].writer,
                    actions: [
                        { type: 'like-o', text: dataArray[i].like_count },
                        { type: 'star-o', text: dataArray[i].star_count },
                        { type: 'message', text: dataArray[i].comment_count },
                    ],
                    content: dataArray[i].content,
                    post_id: dataArray[i].post_id
                })
            }
        }).catch(err => {
            console.log(err)
            this.error("请求失败, 请尝试刷新页面", 1);
        })
    },
    data() {
        return {
            contents: [],
            user_name: "loading...",
            // username: this.user.user_name,
            avatar: "",
            fileList: [

            ],
            email: "you",
            loading: false,
            visible: false,
            confirmLoading: false,
            formLayout: 'horizontal',
            form: this.$form.createForm(this),
            rules: {
                user_name: {
                    rules: [{ required: false, message: '不允许包含空白符', whitespace: true }],
                    trigger: 'blur',
                },
                old_password: {
                    rules: [{ required: true, message: '请输入密码', whitespace: true }],
                    trigger: 'blur',
                },
                new_password: {
                    rules: [
                        { required: true, message: '请确认密码', whitespace: true },
                        // { validator: this.checkPwd2, trigger: 'blur' }
                    ],
                    trigger: 'blur',
                }
            }
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
        ...mapGetters('account', ['user']),
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
            const beforename = this.user.user_name;
            const name = this.form.getFieldValue('new_name');
            // 目前没有对旧密码校验
            // const oldPassword = this.form.getFieldValue('旧密码');
            const newPassword = this.form.getFieldValue('new_password');
            editProfile(beforename, name, newPassword).then(() => {
                this.$message.success('修改成功！', 1)
                logout()
                this.$router.push('/login')
            }).catch((err) => {
                this.error = err.code
                this.$message.error(err.response.data.reason, 1);
            })
            this.visible = false;
        },
        customRequest(data) {
            //上传完文件还需要刷新一下
            const formData = new FormData();
            formData.append('avator', data.file);
            formData.append('user_name', this.user.user_name);
            UploadAvator(formData).then(() => {
                this.$message.success('修改成功！', 1)
                logout()
                this.$router.push('/login')
            }
            ).catch((err) => {
                this.$message.error(err.response.code)
            })
        },
        onClick(post_id) {
            this.$router.push({
                path: "/article",
                query: { "post_id": post_id }
            })
        },
        showConfirm(data) {
            const name = this.$data.user_name
            this.$confirm({
                title: 'Do you want to delete these article?',
                // content: 'When clicked the OK button, this dialog will be closed after 1 second',
                content: '注意, 删除文章操作执行后不可撤销, 点击确认以执行删除操作!',
                onOk() {
                    deletePost(name, data).then((res) => {
                        this.success(res.data.reason, 1).then(() => {
                            location.reload()
                        })
                    }
                    ).catch(
                        (err) => {
                            this.error(err.response.data.reason, 1)
                        }
                    )
                    return new Promise((resolve, reject) => {
                        setTimeout(Math.random() > 0.5 ? resolve : reject, 1000);
                    }).catch(() => console.log('Oops errors!'));
                },
                onCancel() { },
            });
        },
    }
}
</script>

<style>
.profileTop {
    /* width: 1000px; */
    height: 240px;
    padding-top: 20px;
    background-image: url("../../assets/img/background.jpg");
    /* margin-top: auto; */
    /* position: absolute;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    border-radius: 5px; */
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
    /* background-color: #707884; */
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

.e-mail {
    font-size: 14px;
    color: #ffffff;
}

.editButton {
    width: 100px;
    height: 25px;
    margin-top: 160px;
    /* margin-left: 20px; */
    position: absolute;
    left: 84%;
    transform: translateX(-50%);
    display: flex;
    border-radius: 5px;
}

/* .profileStatistic {
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
} */

.myPosts {
    background-color: #ffffff;
}

/* .Information {
    margin-top: 300px;
    width: 1000px;
    height: 300px;
    background-color: #ffffff;
} */
</style>