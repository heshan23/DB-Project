<template>
    <a-comment>
        <template slot="actions">
            <span key="comment-basic-like">
                <a-tooltip title="Like">
                    <a-icon type="like" :theme="action === 'liked' ? 'filled' : 'outlined'" @click="like" />
                </a-tooltip>
                <span style="padding-left: '8px';cursor: 'auto'">
                    {{ likes }}
                </span>
            </span>
            <!-- <span key="comment-basic-dislike">
                <a-tooltip title="Dislike">
                    <a-icon type="dislike" :theme="action === 'disliked' ? 'filled' : 'outlined'" @click="dislike" />
                </a-tooltip>
                <span style="padding-left: '8px';cursor: 'auto'">
                    {{ dislikes }}
                </span>
            </span> -->
            <span key="comment-basic-reply-to" @click="reply">Reply to</span>
        </template>
        <a slot="author">{{ author }}</a>
        <a-avatar slot="avatar" :src="avatar" />
        <p slot="content">
            {{ content }}
        </p>
        <a-tooltip slot="datetime" :title="this.moment">
            <span>{{ this.moment }}</span>
        </a-tooltip>
        <a-modal :title="replyTitle" :visible="visible" :confirm-loading="confirmLoading" @ok="handleOk"
            @cancel="handleCancel">
            <a-textarea :rows="3" v-model="replyContent" style="background-color:aliceblue;" />
        </a-modal>
    </a-comment>
</template>
<script>
export default {
    //需要上传的数据是点赞的变化，可以最后根据action来判断，然后后端加一或减一或不变即可
    //时间展示接口有待商榷
    props: ['data'],
    data() {
        return {
            author: this.data.author,
            avatar: this.data.avatar,
            content: this.data.content,
            likes: this.data.likes,
            // dislikes: 0,
            action: null,
            moment:this.data.moment,
            visible: false,
            confirmLoading: false,
            replyContent: '',
        };
    },
    methods: {
        like() {
            if (this.action == 'liked') {
                this.likes = this.likes - 1;
                this.action = null;
                return;
            }
            this.likes = this.likes + 1;
            if (this.action == 'disliked') {
                this.dislikes = this.dislikes - 1;
            }
            this.action = 'liked';
        },
        // dislike() {
        //     if (this.action == 'disliked') {
        //         this.dislikes = this.dislikes - 1;
        //         this.action = null;
        //         return;
        //     }
        //     this.dislikes = this.dislikes + 1;
        //     if (this.action == 'liked') {
        //         this.likes = this.likes - 1;
        //     }
        //     this.action = 'disliked';
        // },
        reply() {
            this.replyTitle = '回复' + this.author + ':'
            this.visible = true
        },
        handleOk() {
            this.confirmLoading = true;
            console.log(this.replyContent)
            setTimeout(() => {
                this.visible = false;
                this.confirmLoading = false;
            }, 2000);
        },
        handleCancel() {
            this.visible = false;
        },
    },
};
</script>
  