<template>
    <div>
        <a-comment>
            <a-avatar slot="avatar" :src="user_avatar" />
            <div slot="content">
                <a-form-item>
                    <a-textarea :rows="3" v-model="value" style="background-color:aliceblue;" />
                </a-form-item>
                <a-form-item>
                    <a-button html-type="submit" :loading="submitting" type="primary" @click="handleSubmit">
                        Add Comment
                    </a-button>
                </a-form-item>
            </div>
        </a-comment>
    </div>
</template>
<script>
import moment from 'moment';
import { newComment } from '../../services/user';
import { mapGetters } from 'vuex';
export default {
    props: ['data'],
    created() {
        this.$data.user_avatar = this.user.avatar
    },
    data() {
        return {
            submitting: false,
            value: '',
            user_avatar: this.$parent.user_avatar,
            post_id: this.data.post_id,
            moment,
        };
    },
    computed: {
        ...mapGetters('account', ['user'])
    },
    methods: {
        handleSubmit() {
            if (!this.value) {
                return;
            }

            this.submitting = true;
            console.log(this.$data.post_id);
            newComment(this.user.user_name, this.$data.post_id, this.value).then(res => {
                this.submitting = false;
                this.$message.success(res.data.reason, 1).then(() => {
                    location.reload()
                })
            }).catch(err => {
                console.log(err)
                this.submitting = false;
                this.$message.error(err.response.data.reason, 1).then(() => {
                    location.reload()
                })
            })
        }
    }
};
</script>
  