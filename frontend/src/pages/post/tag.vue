<template>
  <div>
    <span :style="{ marginRight: 8 }">标签:</span>
    <template v-for="tag in tags">
      <a-checkable-tag :key="tag" :checked="selectedTags.indexOf(tag) > -1"
        @change="checked => handleChange(tag, checked)">
        {{ tag }}
      </a-checkable-tag>
    </template>
  </div>
</template>
<script>
export default {
  data() {
    return {
      tags: ['学习交流', '美食分享', '生活经验', '物品交换'],
      selectedTags: [],
    };
  },
  methods: {
    handleChange(tag, checked) {
      const { selectedTags } = this;
      const nextSelectedTags = checked
        ? [...selectedTags, tag]
        : selectedTags.filter(t => t !== tag);
      console.log('You are interested in: ', nextSelectedTags);
      this.selectedTags = nextSelectedTags;
      //返回一个数组
    },
  },
};
</script>
  