<template>
    <div class="clearfix">
        <a-upload action="https://localhost:8081" list-type="picture-card" :file-list="fileList" @preview="handlePreview"
            @change="handleChange" :customRequest="customRequest">
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
import { uploadImage } from '@/services/user'
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
        customRequest(data) {
            const formData = new FormData();
            formData.append('file', data.file);
            uploadImage(formData).then((res) => {
                this.$message.success(res.data.reason)
                /**
                 * 使用 res.data.url 获取图片地址
                 * 使用 res.data.id 获取图片id (用作查询图片的 url)
                 */
            }
            ).catch((err) => {
                this.$message.error(err.response.code)
            })
        },
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
  