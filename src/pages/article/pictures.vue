<template>
    <div class="my">
        <a-carousel :after-change="onChange">
            <div>
                <img :src="addr1" class="myimg" />
            </div>
            <div>
                <img src="@/assets/img/avatar.jpg" class="myimg" />
            </div>
        </a-carousel>
    </div>
</template>
<script>
export default {
    data() {
        return {
            addr1: 'https://zos.alipayobjects.com/rmsportal/ODTLcjxAfvqbxHnVXCYX.png'
        }
    },
    methods: {
        onChange(a, b, c) {
            console.log(a, b, c);
        },
    },
};
</script>
<style scoped>
/* For demo */
.ant-carousel>>>.slick-slide {
    /* text-align: center; */
    /* height: 700px; */
    /* line-height: 160px; */
    /* background: #364d79; */
    /* overflow: hidden; */
    display: flex;
    justify-content: center;
    /* align-items: center; */
}

.ant-carousel>>>.slick-slide h3 {
    color: #fff;
}

.my {
    height: 100%;
}

.myimg {
    /* max-width: 200%; */
    height: 100%;
}
</style>
  