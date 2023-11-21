<template>
    <div class="clearfix">
        <a-upload action="https://localhost:8081" list-type="picture-card" :file-list="fileList" @preview="handlePreview"
            @change="handleChange">
            <div v-if="fileList.length < 8">
                <a-icon type="plus" />
                <div class="ant-upload-text">
                    Upload
                </div>
            </div>
        </a-upload>
        <a-modal :visible="previewVisible" :footer="null" @cancel="handleCancel">
            <img alt="example" style="width: 100%" :src="previewImage" />
        </a-modal>
    </div>
</template>
<script>
function getBase64(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.readAsDataURL(file);
        reader.onload = () => resolve(reader.result);
        reader.onerror = error => reject(error);
    });
}
export default {
    data() {
        return {
            previewVisible: false,
            previewImage: '',
            fileList: [

            ],
        };
    },
    methods: {
        handleCancel() {
            this.previewVisible = false;
        },
        async handlePreview(file) {
            if (!file.url && !file.preview) {
                file.preview = await getBase64(file.originFileObj);
            }
            this.previewImage = file.url || file.preview;
            this.previewVisible = true;
        },
        handleChange({ fileList }) {
            this.fileList = fileList;
        },
    },
};
</script>
<style>
/* you can make up upload button and sample style by using stylesheets */
.ant-upload-select-picture-card i {
    font-size: 32px;
    color: #999;
}

.ant-upload-select-picture-card .ant-upload-text {
    margin-top: 8px;
    color: #666;
}
</style>
  