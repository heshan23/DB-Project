<template>
    <div>
      <a-form :form="testForm">
        <a-form-item label="上传头像">
          <a-upload
            action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
            listType="picture-card"
            @preview="handlePreview"
            v-decorator="[
              'headImage',
              {
                rules: [
                  { required: true, message: '请上传相关文件' }
                ],
                initialValue: fileList,
                valuePropName: 'fileList',
                getValueFromEvent: normFiles
              }
            ]"
          >
            <div v-if="fileList.length < 1 && uploadingFile == false">
              <a-icon type="plus" />
              <div class="ant-upload-text">Upload</div>
            </div>
          </a-upload>
        </a-form-item>
        <a-form-item label="批量上传文件">
          <a-upload-dragger
            name="file"
            :multiple="true"
            action="https://www.mocky.io/v2/5cc8019d300000980a055e76"
            v-decorator="[
              'batchFiles',
              {
                rules: [
                  { required: true, message: '请上传相关文件' }
                ],
                initialValue: batchFileList,
                valuePropName: 'fileList',
                getValueFromEvent: normBatchFiles
              }
            ]"
          >
            <p class="ant-upload-drag-icon">
              <a-icon type="inbox" />
            </p>
            <p class="ant-upload-text">Click or drag file to this area to upload</p>
            <p class="ant-upload-hint">
              Support for a single or bulk upload. Strictly prohibit from uploading company data or other
              band files
            </p>
          </a-upload-dragger>
        </a-form-item>
        <a-form-item>
          <a-button type="primary" @click="submitFunc">提交</a-button>
        </a-form-item>
      </a-form>
      <a-modal :visible="previewVisible" :footer="null" @cancel="handleCancel">
        <img alt="example" style="width: 100%" :src="previewImage" />
      </a-modal>
    </div>
  </template>
  <script>
  export default {
    data() {
      return {
        testForm: this.$form.createForm(this),
        previewVisible: false,
        previewImage: '',
        fileList: [],
        fileUrl: [],
        batchFileList: [],
        uploadingFile: false,
      }
    },
    methods: {
      handleCancel() {
        this.previewVisible = false;
      },
      handlePreview(file) {
        this.previewImage = file.url || file.thumbUrl;
        this.previewVisible = true;
      },
      normFiles(e) {
        if (e.file.status === "uploading") {
          this.uploadingFile = true;
        }
        if (e.file.status === "removed") {
          this.fileList = [];
          this.uploadingFile = false;
          return {} && [];
        }
        if (e.file.status === "done") {
          this.fileList.push(e.file.response);
          this.uploadingFile = false;
        }
        return e && e.fileList
      },
      normBatchFiles(e) {
        if (e.file.status === "removed") {
          let deleteUid = e.file.uid;
          this.batchFileList = this.batchFileList.filter(function(item){
            return item.uid != deleteUid
          });
          if (e.fileList.length == 0) {
            return {} && [];
          }
        }
        if (e.file.status === "done") {
          this.batchFileList.push(e.file.response);
        }
        return e && e.fileList;
      },
      submitFunc() {
        this.testForm.validateFields((err, values) => {
          console.log(values, 'values');
        });
      }
    },
    mounted() {
      this.fileList.push({
        uid: '-1',
        name: 'xxx.png',
        status: 'done',
        url: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png',
      });
      this.batchFileList.push({
        uid: '-1',
        name: 'xxx.png',
        status: 'done',
        url: 'https://zos.alipayobjects.com/rmsportal/jkjgkEfvpUPVyRjUImniVslZfWPnJuuZ.png',
      });
    },
  }
  </script>