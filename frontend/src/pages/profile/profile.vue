<template>
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
                <a-button type="primary" @click="edit">编辑</a-button>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    data() {
        return {
            username: "heshan",
            signature: "fuck,you"
        }
    },
    methods:{
        edit(){
            alert('success!')
        }
    }
}
</script>

<style>
.profileTop {
    width: 1000px;
    height: 140px;
    padding-top: 20px;
    background-color: white;
    margin-top: 30px;
    position: absolute;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    border-radius: 5px;
}

.avatar {
    width: 120px;
    height: 120px;
    background-color: #8c939d;
    margin-right: 24px;
    margin-left: 20px;
    overflow: hidden;
    border-radius: 50%;

}

.userText {
    width: 60%;
    height: 100%;
    line-height: 30px;
}

.userName {
    font-weight: bold;
    font-size: 20px;
}

.signature {
    font-size: 14px;
    color: #999;
}
</style>