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
                            <h1>{{ title }}</h1>
                            <span>
                                {{ content }}
                            </span>
                            <AddComment />
                            <commentList />
                            <commentList />
                            <commentList />
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
            title: '项目介绍',
            content: '这是项目介绍',
            images: [
                { url: require('@/assets/img/avatar.jpg') },
                { url: require('@/assets/img/avatar.jpg') }
            ],
            comments:[
                
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
  

  