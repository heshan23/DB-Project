<template>
    <a-layout id="components-layout-demo-fixed-sider">
        <a-layout-sider :style="{ overflow: 'auto', height: '100vh', position: 'fixed', left: 0 }" :width=700>
            <pictures />
        </a-layout-sider>
        <a-layout :style="{ marginLeft: '700px' }">
            <a-layout-content :style="{ margin: '24px 16px 0', overflow: 'initial' }">
                <div>
                    <h1>{{ title }}</h1>
                    <span>
                        {{ contend }}
                    </span>
                    <AddComment />
                    <commentList />
                    <commentList />
                    <commentList />
                    <commentList />
                </div>
            </a-layout-content>
        </a-layout>
    </a-layout>
</template>
<script>
import pictures from './pictures.vue';
import AddComment from './addComment.vue';
import commentList from './comment.vue';
export default {
    components: {
        pictures,
        AddComment,
        commentList,
    },
    data() {
        return {
            title: '项目介绍',
            contend: '这是项目介绍',
        }
    }
}
</script>
<style>

</style>

  