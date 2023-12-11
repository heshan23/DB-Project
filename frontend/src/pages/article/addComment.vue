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
export default {
    props: ['user_avatar'],
    data() {
        return {
            submitting: false,
            value: '',
            moment,
        };
    },
    methods: {
        handleSubmit() {
            if (!this.value) {
                return;
            }

            this.submitting = true;
            console.log(this.value);
            setTimeout(() => {
                this.submitting = false;
                this.value = '';
            }, 1000);
        }
    },
};
</script>
  