<template>
    <div>
        <a-form @submit="onSubmit">
            <a-form-item>
                <a-input autocomplete=false size="large" placeholder="请输入帖子名称">
                </a-input>
                <mymenu />
                <a-textarea placeholder="请输入正文" :rows="12" />
            </a-form-item>
            <a-divider />
            <postImage />
            <mytag />
            <a-form-item>
                <a-button :loading="logging" style="width: 100%;margin-top: 24px" size="large" htmlType="submit"
                    type="primary">发帖</a-button>
            </a-form-item>
        </a-form>
    </div>
</template>
<script>
import mytag from './tag.vue';
import postImage from './image.vue';
import mymenu from './menu.vue';
import { mapGetters } from 'vuex';
export default {
    name: 'post',
    computed: {
        ...mapGetters('account', ['user']),
    },
    components: {
        mytag,
        postImage,
        mymenu,
    },
    methods: {
        onSubmit() {
            // const name=this.user.name
            // const title=""
            // const content=""
            // const bname=""
            // const tname=""
            this.$message.success('发帖成功！', 1)
            this.$router.push('/square')
        },
    }
}
</script>
<style></style>