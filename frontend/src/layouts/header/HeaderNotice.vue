<template>
  <a-dropdown :trigger="['click']" v-model="show">
    <div slot="overlay">
      <a-spin :spinning="loading">
        <a-tabs class="dropdown-tabs" :tabBarStyle="{ textAlign: 'center' }" :style="{ width: '297px' }">
          <a-tab-pane tab="公告" key="1">
            <a-list class="tab-pane">
              <a-list-item v-for="(notice, key) in notices" :key="key">
                <a-list-item-meta :title="notice.title" :description="notice.date">
                  <a-avatar style="background-color: white" slot="avatar"
                    src="https://gw.alipayobjects.com/zos/rmsportal/ThXAXghbEsBCCSDihZxY.png" />
                </a-list-item-meta>
              </a-list-item>
            </a-list>
          </a-tab-pane>
          <a-tab-pane tab="评论" key="2">
            <a-list class="tab-pane">
              <a-list-item v-for="(comment, key) in comments" :key="key">
                <a-list-item-meta :title="comment.title" :description="comment.date">
                  <a-avatar style="background-color: white" slot="avatar"
                    src="https://gw.alipayobjects.com/zos/rmsportal/ThXAXghbEsBCCSDihZxY.png" />
                </a-list-item-meta>
              </a-list-item>
            </a-list>
          </a-tab-pane>
          <a-tab-pane tab="私信" key="3">
            <a-list class="tab-pane"></a-list>
          </a-tab-pane>
        </a-tabs>
      </a-spin>
    </div>
    <span @click="fetchNotice" class="header-notice">
      <a-badge class="notice-badge" count="12">
        <a-icon :class="['header-notice-icon']" type="bell" />
      </a-badge>
    </span>
  </a-dropdown>
</template>

<script>
export default {
  name: 'HeaderNotice',
  data() {
    return {
      loading: false,
      show: false,
      notices: [
        { title: "请维护个人资料", date: "1年前" },
        { title: "谨防上当受骗", date: "2年前" }
      ],
      comments: [
        { title: "heshan评论了你的文章second", date: "32s前" },
        { title: "heshan评论了你的文章first", date: "40s前" }
      ],
      letter: [],
    }
  },
  computed: {
  },
  methods: {
    fetchNotice() {
      if (this.loading) {
        this.loading = false
        return
      }
      if (this.show) return
      this.loading = true
      let notice = {
        title: 'xxx',
        date: 'xxx'
      }
      const commenter = 'xxx'
      const article = 'xxx'
      let comment = {
        title: commenter + '评论了你的文章' + article,
        date: 'xxx'
      }
      this.notices.unshift(notice)
      this.comments.unshift(comment)
      setTimeout(() => {
        this.loading = false
      }, 1000)
    }
  }
}
</script>

<style lang="less">
.header-notice {
  display: inline-block;
  transition: all 0.3s;

  span {
    vertical-align: initial;
  }

  .notice-badge {
    color: inherit;

    .header-notice-icon {
      font-size: 16px;
      padding: 4px;
    }
  }
}

.dropdown-tabs {
  background-color: @base-bg-color;
  box-shadow: 0 2px 8px @shadow-color;
  border-radius: 4px;

  .tab-pane {
    padding: 0 24px 12px;
    min-height: 250px;
  }
}
</style>
