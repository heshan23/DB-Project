<template>
    <div>
        <a-divider />
        <a-row>
            <a-col :span=16 class="border1">
                <a-form @submit="onSubmit" :form="form">
                    <a-form-item>
                        <a-input style="width: 790px; " autocomplete=false size="large" placeholder="请输入帖子名称"
                            v-decorator="['title', rules.title]">
                        </a-input>
                    </a-form-item>
                    <div>
                        <a-radio-group button-style="solid" v-model="value">
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
                    <a-textarea placeholder="请输入正文" v-model="content" :auto-size="{ minRows: 12, maxRows: 20 }"
                        style="width: 790px;" />
                    <a-divider />
                    <postImage v-on:upload="getImageId" v-on:delete="delImageId" />
                    <div>
                        <span :style="{ marginRight: 8 }">标签:</span>
                        <template v-for="tag in tags">
                            <a-checkable-tag :key="tag" :checked="selectedTags.indexOf(tag) > -1"
                                @change="checked => handleTagChange(tag, checked)">
                                {{ tag }}
                            </a-checkable-tag>
                        </template>
                    </div>
                    <a-form-item style="width: 100px;">
                        <a-button :loading="logging" style="width: 100%;margin-top: 24px" size="large" htmlType="submit"
                            type="primary">发帖</a-button>
                    </a-form-item>
                </a-form>
            </a-col>
            <a-col :span=7 class="border2">
                <h1 style="text-align: center;font-size:large;line-height: 40px">社区公约</h1>
                <span
                    style="font-size: larger;line-height: 20px;">社区里鼓励真诚地表达、专业地讨论、友善地互动，反对不友善、低质、低俗、抄袭、侵权、虚假认证、恶意营销导流等破坏社区生态的内容与行为，禁止一切违法违规行为。</span>
            </a-col>
        </a-row>
    </div>
</template>

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
            image_ids: [],
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
                    const name = this.user.user_name
                    const title = this.form.getFieldValue('title')
                    const content = this.content
                    const block_name = this.value
                    const tag_name = this.selectedTags//返回一个数组
                    const image_ids = this.image_ids
                    console.log(this.image_ids)
                    newPost(name, title, content, block_name, tag_name, image_ids).then(() => {
                        this.$message.success('发帖成功！', 1)
                        this.$router.push('/square')
                        this.image_ids = []
                    }).catch((err) => {
                        this.error = err.code
                        this.$message.error(err.response.data.reason, 1);
                    })
                }
            })
        },
        handleTagChange(tag, checked) {
            const { selectedTags } = this;
            const nextSelectedTags = checked
                ? [...selectedTags, tag]
                : selectedTags.filter(t => t !== tag);
            console.log('You are interested in: ', nextSelectedTags);
            this.selectedTags = nextSelectedTags;
        },
        getImageId(data) {
            console.log(data)
            this.image_ids.push(data)
        },
        delImageId(data) {
            console.log(data)
            let idx = this.image_ids.indexOf(data)
            let newImgIds = this.image_ids.slice()
            newImgIds.splice(idx, 1)
            this.image_ids = newImgIds.slice()
        }
    }
}
</script>
<style>
.border1 {
    background-color: white;
    border: 0.7rem solid white;
    border-radius: 12px;
}

.border2 {
    float: right;
    margin-right: 3%;
    background-color: white;
    border: 0.7rem solid white;
    border-radius: 12px;
}
</style>