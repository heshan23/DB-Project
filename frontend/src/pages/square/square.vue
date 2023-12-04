<template>
    <div class="card">
        <a-card hoverable style="width: 300px;" v-for="(item, key) in contents " :key=key>
            <img slot="cover" alt="example" :src="item.picture" @click="onclick" />
            <a-card-meta :title=item.title :description=item.writer @click="onclick">
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
        queryPost().then(res => {
            const dataArray = res.data.content
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
        // return {
        //     contents: [
        //         {
        //             title: '旅途风光',
        //             avatar: require('@/assets/img/avatar.jpg'),
        //             picture: require('@/assets/img/test1.png'),
        //             writer: 'heshan',
        //             actions: [
        //                 { type: 'like-o', text: '2' },
        //                 { type: 'star-o', text: '23' },
        //                 { type: 'message', text: '234' },
        //             ],
        //         },
        //         {
        //             title: '摄影技巧',
        //             avatar: require('@/assets/img/avatar.jpg'),
        //             picture: require('@/assets/img/test2.png'),
        //             writer: 'heshan',
        //             actions: [
        //                 { type: 'like-o', text: '156' },
        //                 { type: 'star-o', text: '1990' },
        //                 { type: 'message', text: '21' },
        //             ],
        //         },
        //         {
        //             title: '奇山峻岭',
        //             avatar: require('@/assets/img/avatar.jpg'),
        //             picture: require('@/assets/img/test3.png'),
        //             writer: 'heshan',
        //             actions: [
        //                 { type: 'like-o', text: '156' },
        //                 { type: 'star-o', text: '156' },
        //                 { type: 'message', text: '2' },
        //             ],
        //         },
        //         {
        //             title: '璀璨星空',
        //             avatar: require('@/assets/img/avatar.jpg'),
        //             picture: require('@/assets/img/test4.png'),
        //             writer: 'heshan',
        //             actions: [
        //                 { type: 'like-o', text: '1256' },
        //                 { type: 'star-o', text: '16' },
        //                 { type: 'message', text: '26' },
        //             ],
        //         },
        //         {
        //             title: '项目介绍',
        //             avatar: require('@/assets/img/avatar.jpg'),
        //             picture: require('@/assets/img/logo.png'),
        //             writer: 'heshan',
        //             actions: [
        //                 { type: 'like-o', text: '18' },
        //                 { type: 'star-o', text: '120' },
        //                 { type: 'message', text: '1283' },
        //             ],
        //         },
        //     ],
        // }
    },
    methods: {
        onclick() {
            this.$router.push("/article")
        }
    }
}
</script>
<style>
.card {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-between;
}
</style>  

  