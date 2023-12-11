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
      <div style="margin-left: 20px; margin-right: 20px;">
        <h1 class="title">{{ title }}</h1>
        <span class="content">
          {{ content }}
        </span>
        <a-divider />
        <AddComment :user_avatar="user_avatar" />
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
import { postGet } from '../../services/user';
export default {
  components: {
    AddComment,
    commentList,
  },
  data() {
    // let post_id = this.$route.query.post_id;
    // console.log(post_id)
    // var ret
    // postGet(post_id).then(
    //   res => {
    //     console.log(res.data)
    //     const articleData = res.data.data
    //     // this.title = res.data.title
    //     // this.content = res.data.content
    //     // this.images = res.data.images
    //     // this.comments = res.data.comments
    //   }
    // ).catch(
    //   err => {
    //     console.log(err)
    //   }
    // )
    return {
      user_avatar: require('@/assets/img/avatar.jpg'),
      title: '奇山峻岭',
      content: "看山，普通总是仰起头来看的。然而黄山不同，常常要低下头去看。因为黄山是群山，登上一个高峰，就可俯瞰群山。这教人想起杜甫的诗句“会当凌绝顶，一览众山小！”而精神为之兴奋，胸襟为之开朗。我在黄山盘桓了十多天，登过紫云峰、立马峰、天都峰、玉屏峰、光明顶、狮子林、眉毛峰等山，常常爬到绝顶，有如苏东坡游赤壁的“履版岩，披蒙茸，踞虎豹，登虬龙，攀栖鹘之危巢，俯冯夷之幽宫。在黄山中，不但要低头看山，还要面面看山。因为方向一改变，山的样子就不同，有时竟完全两样，",
      images: [
        { url: require('@/assets/img/avatar.jpg') },
        { url: require('@/assets/img/logo.png') },
        { url: require('@/assets/img/test1.png') },
      ],
      comments: [
        {
          author: 'heshan',
          avatar: require('@/assets/img/avatar.jpg'),
          content: '写的真好下次我也去！',
          likes: 1000,
          dislikes: 10000,
          // moment,
        },
        {
          author: 'shan',
          avatar: require('@/assets/img/avatar.jpg'),
          content: '写的真烂，拉黑了！',
          likes: 100,
          dislikes: 20,
          // moment,
        },
      ]
    }
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
  

  