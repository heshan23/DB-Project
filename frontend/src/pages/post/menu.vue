<template>
    <div>
            <a-radio-group default-value="a" button-style="solid" v-model="value" @change="onChange">
                <a-radio-button value="a">
                    休闲娱乐
                </a-radio-button>
                <a-radio-button value="b">
                    信息科技
                </a-radio-button>
                <a-radio-button value="c">
                    生活时尚
                </a-radio-button>
                <a-radio-button value="d" onclick="click">
                    课程交流
                </a-radio-button>
            </a-radio-group>
    </div>
</template>
<script>
export default {
    data(){
        return {
            value:'a',
        }
    },
    methods:{
        onChange(e){
            console.log(e.target.value)
        },
    }
}
</script>
  