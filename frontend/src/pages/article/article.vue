<template>
  <a-row class="outside">
    <a-col :span="9" style="margin-left: 120px; position: fixed;">
      <a-carousel>
        <div v-for="(item, key) in images" :key="key">
          <img class="top-img" :src=item.url />
        </div>
      </a-carousel>
    </a-col>
    <a-col :span="10" class="right_part">
      <div style="margin-top: 10px;margin-left: 10px;margin-bottom: 20px;margin-right: 10px;">
        <a-avatar slot="avatar" :src="writer_avatar" />
        <span style="font-size: larger; font-weight: 600;margin-left: 10px;">{{ writer }}</span>
        <a-button html-type="submit" :loading="submitting" type="primary" @click="handleLike" style="float: right;">
          <span v-if="liked">已点赞</span>
          <span v-else>点赞</span>
        </a-button>
      </div>
      <a-divider />
      <div style="margin-left: 20px; margin-right: 20px;">
        <h1 class="title">{{ title }}</h1>
        <span class="content">
          {{ content }}
        </span>
        <div style="margin-top: 20px;">
          <a-tooltip :title="this.moment">
            <span style="font-size: small;">发布于：{{ this.moment }}</span>
          </a-tooltip>
        </div>
        <a-divider />
        <AddComment :data="this.$data" />
        <div v-for="(item, key) in comments" :key="key">
          <commentList :data="item" />
        </div>
      </div>
    </a-col>
  </a-row>
</template>
<script>
import AddComment from './addComment.vue';
import commentList from './comment.vue';
import { postGet, likePost, unlikePost, hasLiked } from '../../services/user';
import { mapGetters } from 'vuex';
export default {
  components: {
    AddComment,
    commentList,
  },
  created() {
    console.log(this.$route.query.post_id)
    const post_id = this.$route.query.post_id
    postGet(post_id).then(
      res => {
        const articleData = res.data.data
        console.log(articleData)
        this.$data.writer = articleData.user_name
        this.$data.writer_avatar = articleData.user_avatar
        this.$data.user_avatar = this.user.avatar
        this.$data.title = articleData.title
        this.$data.content = articleData.content
        // this.$data.comments = articleData.comments
        this.$data.images = []
        this.$data.moment = articleData.create_date
        for (let i = 0; i < articleData.images.length; i++) {
          this.$data.images.push({ url: articleData.images[i] })
        }
        for (let i = 0; i < articleData.comments.length; i++) {
          this.$data.comments.push({
            post_id: post_id,
            comment_id: articleData.comments[i].comment_id,
            author: articleData.comments[i].user_name,
            avatar: articleData.comments[i].avatar,
            content: articleData.comments[i].content,
            likes: articleData.comments[i].likes,
            // dislikes: articleData.comments[i].dislikes,
            moment: articleData.comments[i].create_date,
            reply: articleData.comments[i].reply
          })
        }
      }
    ).catch(
      err => {
        console.log(err)
        this.$message.error("获取文章失败", 1)
      }
    )
    hasLiked(this.user.user_name, post_id).then(
      res => {
        if (res.data.data == true) {
          this.liked = true
        }
      }
    ).catch(
      err => {
        console.log(err)
        this.$message.error("获取文章点赞信息失败", 1)
      })
  },
  computed: {
    ...mapGetters('account', ['user']),
  },
  data() {
    var post_id = this.$route.query.post_id;
    console.log(post_id)
    return {
      writer: '',
      writer_avatar: '',
      post_id: post_id,
      user_avatar: '',
      title: "",
      content: '',
      moment: '',
      images: [
      ],
      comments: [
      ],
      liked: false,
    }
  },
  methods: {
    handleLike() {
      this.liked = !this.liked;
      if (this.liked) {
        likePost(this.user.user_name, this.post_id)
      } else {
        unlikePost(this.user.user_name, this.post_id)
      }
    },
  }
}
</script>
<style scoped>
/* For demo */
.ant-carousel>>>.slick-slide {
  background-color: #fff;
}

.ant-carousel>>>.slick-slide h3 {
  color: #fff;
}


.top-img {
  width: 570px;
  height: 650px;
  border-radius: 12px;
}

.right_part {
  margin-left: 700px;
  max-height: 650px;
  overflow: auto;
  border: 1px solid #92B0DD;
  border-radius: 12px;
}

::-webkit-scrollbar {
  display: none;
}

.outside {
  margin-top: 30px;
  margin-bottom: 30px;
}

.title {
  font-size: 1.6rem;
  font-weight: 600;
  text-align: left;
}

.content {
  font-size: larger;
  line-height: 40px
}
</style>
  

  