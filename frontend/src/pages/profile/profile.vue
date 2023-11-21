<template>
    <!-- <a-card hoverable style="width: 300px">
    <img
      slot="cover"
      alt="example"
      src="https://gw.alipayobjects.com/zos/rmsportal/JiqGstEfoWAOHiTxclqi.png"
    />
    <template slot="actions" class="ant-card-actions">
      <a-icon key="setting" type="setting" />
      <a-icon key="edit" type="edit" />
      <a-icon key="ellipsis" type="ellipsis" />
    </template>
    <a-card-meta title="Card title" description="This is the description">
      <a-avatar
        slot="avatar"
        src="https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png"
      />
    </a-card-meta>
  </a-card> -->
    <div class="fullPage">
        <div class="profileTop">
            <img class="avatar" src="@/assets/img/avatar.jpg" />
            <div class="userText">
                <div class="userName">
                    <span>{{ username }}</span>
                </div>
                <div class="signature">
                    <span>个性签名：{{ signature }}</span>
                </div>
                <div>
                    <a-button type="primary" :loading="loading" @click="edit">编辑</a-button>
                </div>
            </div>
        </div>

        <div class="profileStatistic">
            <div class="profileStatisticItem">
                <div class="profileStatisticItemTitle">关注</div>
                <div class="profileStatisticItemNum">0</div>
            </div>
            <div class="profileStatisticItem">
                <div class="profileStatisticItemTitle">粉丝</div>
                <div class="profileStatisticItemNum">0</div>
            </div>
            <div class="profileStatisticItem">
                <div class="profileStatisticItemTitle">发布量</div>
                <div class="profileStatisticItemNum">0</div>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            username: "heshan",
            signature: "fuck,you",
            loading: false
        }
    },
    methods: {
        // test() {
        //     alert('just for test')
        // },
        edit() {
            this.loading = true
            // TODO: 添加向后端发送数据的函数并得到返回值
            setTimeout(() => {
                alert('success!')
                this.loading = false
            }, 500)
        }
    }
}
</script>

<style>
.fullPage {
    background-color: #adb2b9;
}

.profileTop {
    width: 1000px;
    height: 250px;
    padding-top: 20px;
    /* background-color: white; */
    background-image: url("../../assets/img/background.jpg");
    margin-top: auto;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    border-radius: 5px;
}

.avatar {
    width: 60px;
    height: 60px;
    background-color: #707884;
    margin-top: auto;
    overflow: hidden;
    border-radius: 50%;
}

.userText {
    margin-top: auto;
    width: 60%;
    height: 60%;
    line-height: 30px;
}

.userName {
    font-weight: bold;
    font-size: 20px;
    color: #ffffff;
}

.signature {
    font-size: 14px;
    color: #999;
}

.profileStatistic {
    width: 1000px;
    height: 100px;
    background-color: white;
    margin-top: auto;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    border-radius: 5px;
}

.profileStatisticItem {
    width: 33%;
    height: 100%;
    display: flex;
    flex-direction: column;
    margin-right: 20px;
    margin-left: 20px;
    align-items: center;
    justify-content: center;
}
</style>