<template>
    <div>
        <a-form @submit="onSubmit" :form="form">
            <a-form-item>
                <a-input autocomplete=false size="large" placeholder="请输入帖子名称" v-decorator="['title', rules.title]">
                </a-input>
            </a-form-item>
            <div>
                <a-radio-group default-value="a" button-style="solid" v-model="value">
                    <a-radio-button value="休闲娱乐">
                        休闲娱乐
                    </a-radio-button>
                    <a-radio-button value="信息科技">
                        信息科技
                    </a-radio-button>
                    <a-radio-button value="生活时尚">
                        生活时尚
                    </a-radio-button>
                    <a-radio-button value="课程交流">
                        课程交流
                    </a-radio-button>
                </a-radio-group>
            </div>
            <a-textarea placeholder="请输入正文" v-model="content" :auto-size="{ minRows: 12, maxRows: 20 }" />
            <a-divider />
            <postImage />
            <div>
                <span :style="{ marginRight: 8 }">标签:</span>
                <template v-for="tag in tags">
                    <a-checkable-tag :key="tag" :checked="selectedTags.indexOf(tag) > -1"
                        @change="checked => handleTagChange(tag, checked)">
                        {{ tag }}
                    </a-checkable-tag>
                </template>
            </div>
            <a-form-item>
                <a-button :loading="logging" style="width: 100%;margin-top: 24px" size="large" htmlType="submit"
                    type="primary">发帖</a-button>
            </a-form-item>
        </a-form>
    </div>
</template>

import {newPost} from '@/services/user';
<script>
import { newPost } from '../../services/user';
import postImage from './image.vue';
import { mapGetters } from 'vuex';
export default {
    name: 'post',
    data() {
        return {
            form: this.$form.createForm(this),
            content: '',
            value: '休闲娱乐',
            tags: ['学习交流', '美食分享', '生活经验', '物品交换'],
            selectedTags: [],
            rules: {
                title: {
                    rules: [{ required: true, message: '标题不能为空', whitespace: true }],
                    trigger: 'blur',
                }
            }
        }
    },
    computed: {
        ...mapGetters('account', ['user']),
    },
    components: {
        postImage,
    },
    methods: {
        onSubmit(e) {
            e.preventDefault()
            this.form.validateFields((err) => {
                if (!err) {
                    const name = this.user.name
                    const title = this.form.getFieldValue('title')
                    const content = this.content
                    const block_name = this.value
                    const tag_name = this.selectedTags//返回一个数组
                    newPost(name, title, content, block_name, tag_name).then(() => {
                        this.$message.success('发帖成功！', 1)
                        this.$router.push('/square')
                    }).catch((err) => {
                        this.error = err.code
                        this.$message.error(err.response.data.reason, 1);
                    })
                }
            })
        }, handleTagChange(tag, checked) {
            const { selectedTags } = this;
            const nextSelectedTags = checked
                ? [...selectedTags, tag]
                : selectedTags.filter(t => t !== tag);
            console.log('You are interested in: ', nextSelectedTags);
            this.selectedTags = nextSelectedTags;
        },
    }
}
</script>
<style></style>