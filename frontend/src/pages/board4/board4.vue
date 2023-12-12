<template>
    <div class="card">
        <a-card hoverable style="width: 300px;margin: 2px;" v-for="(item, key) in contents " :key=key>
            <img class="img" slot="cover" alt="example" :src="item.picture" @click="onclick(item.post_id)" />
            <a-card-meta :title=item.title :description=item.writer @click="onclick(item.post_id)">
                <a-avatar slot="avatar" :src=item.avatar />
            </a-card-meta>
            <template v-for="{ type, text } in item.actions" slot="actions">
                <span :key="type">
                    <a-icon :type="type" style="margin-right: 8px" />
                    {{ text }}
                </span>
            </template>
        </a-card>
    </div>
</template>
<script>
import { queryPost } from '../../services/user';
export default {
    data() {
        var ret = []
        queryPost(undefined,undefined, "课程交流", undefined).then(res => {
            console.log(res.data)
            const dataArray = res.data.contents
            for (let i = 0, len = dataArray.length; i < len; i++) {
                ret.push({
                    title: dataArray[i].title,
                    avatar: dataArray[i].avatar,
                    picture: dataArray[i].picture,
                    writer: dataArray[i].writer,
                    actions: [
                        { type: 'like-o', text: dataArray[i].like_count },
                        { type: 'star-o', text: dataArray[i].star_count },
                        { type: 'message', text: dataArray[i].comment_count },
                    ],
                    post_id: dataArray[i].post_id
                })
            }
            console.log(ret)
        }).catch(err => {
            console.log(err)
            this.error("请求失败, 请尝试刷新页面", 1);
        })
        return {
            contents: ret
        }
    },
    methods: {
        onclick(post_id) {
            this.$router.push({
                path: "/article",
                query: { "post_id": post_id }
            })
        }
    }
}
</script>
<style>
.card {
    display: flex;
    flex-wrap: wrap;
    justify-content: flex-start;
}

.img {
    height: 310px;
}
</style>  

  