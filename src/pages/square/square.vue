<template>
    <div class="card">
        <a-card hoverable style="width: 300px">
            <img slot="cover" alt="example" src="@/assets/img/logo.png" @click="onclick" />
            <a-card-meta :title=title :description=writer @click="onclick">
                <a-avatar slot="avatar" :src="require('@/assets/img/avatar.jpg')" />
            </a-card-meta>
            <template v-for="{ type, text } in actions" slot="actions">
                <span :key="type">
                    <a-icon :type="type" style="margin-right: 8px" />
                    {{ text }}
                </span>
            </template>
        </a-card>
    </div>
</template>
<script>
export default {
    data() {
        return {
            title: '项目介绍',
            //avatar:'@/assets/img/avatar.jpg',
            //picture:'@/assets/img/logo.png',
            writer: 'heshan',
            actions: [
                { type: 'like-o', text: '156' },
                { type: 'star-o', text: '156' },
                { type: 'message', text: '2' },
            ],
        }
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

  