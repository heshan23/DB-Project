<template>
    <a-row style=" margin-top: 50px; margin-bottom: 50px;">
        <a-col :span="20" style="margin-left: 120px;">
            <a-layout id="components-layout-demo-fixed-sider">
                <a-layout-sider :style="{ position: 'fixed' }" :width=600>
                    <a-carousel>
                        <div v-for="(item, key) in images" :key="key">
                            <img :src=item.url />
                        </div>
                    </a-carousel>
                </a-layout-sider>
                <a-layout :style="{ marginLeft: '600px' }">
                    <a-layout-content :style="{ margin: '24px 16px 0', overflow: 'initial' }">
                        <div>
                            <h1 style="font-size: large; text-align: center;">{{ title }}</h1>
                            <span style="font-size:larger;line-height: 40px">
                                {{ content }}
                            </span>
                            <AddComment />
                            <commentList />
                            <commentList />
                        </div>
                    </a-layout-content>
                </a-layout>
            </a-layout>
        </a-col>
    </a-row>
</template>
<script>
import AddComment from './addComment.vue';
import commentList from './comment.vue';
export default {
    components: {
        AddComment,
        commentList,
    },
    data() {
        return {
            title: '奇山峻岭',
            content: "看山，普通总是仰起头来看的。然而黄山不同，常常要低下头去看。因为黄山是群山，登上一个高峰，就可俯瞰群山。这教人想起杜甫的诗句“会当凌绝顶，一览众山小！”而精神为之兴奋，胸襟为之开朗。我在黄山盘桓了十多天，登过紫云峰、立马峰、天都峰、玉屏峰、光明顶、狮子林、眉毛峰等山，常常爬到绝顶，有如苏东坡游赤壁的“履版岩，披蒙茸，踞虎豹，登虬龙，攀栖鹘之危巢，俯冯夷之幽宫。在黄山中，不但要低头看山，还要面面看山。因为方向一改变，山的样子就不同，有时竟完全两样，",
            images: [
                { url: require('@/assets/img/avatar.jpg') },
                { url: require('@/assets/img/avatar.jpg') }
            ],
            comments: [

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
</style>
  

  