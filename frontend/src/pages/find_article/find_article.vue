<template>
    <div style="margin-top: 20px;">
        <a-row style="background-color: white; border-radius: 12px;">
            <div style="margin-left: 20px; margin-top: 20px;">
                <a-form @submit="onSubmit" :form="form">
                    <a-form-item>
                        <span style="margin-right: 10px;">标题:</span>
                        <a-input style="width: 500px; " autocomplete=false size="large" placeholder="请输入帖子名称"
                            v-decorator="['title', rules.title]">
                        </a-input>
                    </a-form-item>
                    <div>
                        <span style="margin-right: 10px;">板块:</span>
                        <a-radio-group button-style="solid" v-model="value">
                            <a-radio-button value="不限">
                                不限
                            </a-radio-button>
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
                    <div style="margin-top: 20px;">
                        <span style="margin-right: 10px;">标签:</span>
                        <template v-for="tag in tags">
                            <a-checkable-tag :key="tag" :checked="selectedTags.indexOf(tag) > -1"
                                @change="checked => handleTagChange(tag, checked)">
                                {{ tag }}
                            </a-checkable-tag>
                        </template>
                    </div>
                    <a-form-item style="width: 100px;">
                        <a-button :loading="logging" style="width: 100%;margin-top: 24px" size="large" htmlType="submit"
                            type="primary">查询</a-button>
                    </a-form-item>
                </a-form>
            </div>
        </a-row>
        <a-row style="margin-top: 20px;">
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
                            <img slot="extra" style="width: 200px;height: 180px;" alt="logo" :src="item.picture"
                                @click="onClick(item.post_id)" />
                            <a-list-item-meta>
                                <a slot="title">{{ item.writer }}</a>
                                <a-avatar slot="avatar" :src="item.avatar" />
                            </a-list-item-meta>
                            <div @click="onClick(item.post_id)">
                                <h1>{{ item.title }}</h1>
                                {{ item.content }}
                            </div>
                        </a-list-item>
                    </a-list>
                </div>
            </div>
        </a-row>
    </div>
</template>
<script>
import { queryPost } from '../../services/user';
var contents = []
queryPost().then(res => {
    console.log(res.data)
    const dataArray = res.data.contents
    for (let i = 0, len = dataArray.length; i < len; i++) {
        contents.push({
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
export default {
    data() {
        return {
            form: this.$form.createForm(this),
            contents,
            value: '不限',
            tags: ['学习交流', '美食分享', '生活经验', '物品交换'],
            selectedTags: [],
            rules: {
                title: {
                    rules: [{ required: false, message: '标题不能为空', whitespace: true }],
                    trigger: 'blur',
                }
            },
            pagination: {
                onChange: page => {
                    console.log(page);
                },
                pageSize: 3,
            },
        }
    },
    methods: {
        onSubmit() {
            const title = this.form.getFieldValue('title')
            var block_name = this.value
            if (block_name == '不限') {
                block_name = undefined
            }
            const tag_name = this.selectedTags
            this.contents = []
            queryPost(title, undefined, block_name, tag_name).then(res => {
                console.log(res.data)
                const dataArray = res.data.contents
                for (let i = 0, len = dataArray.length; i < len; i++) {
                    this.contents.push({
                        title: dataArray[i].title,
                        avatar: dataArray[i].avatar,
                        picture: dataArray[i].picture,
                        writer: dataArray[i].writer,
                        content: dataArray[i].content.substr(0, 210),
                        actions: [
                            { type: 'like-o', text: dataArray[i].like_count },
                            { type: 'star-o', text: dataArray[i].star_count },
                            { type: 'message', text: dataArray[i].comment_count },
                        ],
                        post_id: dataArray[i].post_id
                    })
                }
            }).catch(err => {
                console.log(err)
                this.error("请求失败, 请尝试刷新页面", 1);
            })
            console.log(title)
        },
        handleTagChange(tag, checked) {
            const { selectedTags } = this;
            const nextSelectedTags = checked
                ? [...selectedTags, tag]
                : selectedTags.filter(t => t !== tag);
            console.log('You are interested in: ', nextSelectedTags);
            this.selectedTags = nextSelectedTags;
        },
        onClick(post_id) {
            this.$router.push({
                path: "/article",
                query: { "post_id": post_id }
            })
        }
    }
}
</script>

  