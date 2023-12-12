<template>
  <a-dropdown :trigger="['click']" v-model="show">
    <div slot="overlay">
      <a-spin :spinning="loading">
        <a-tabs class="dropdown-tabs" :tabBarStyle="{ textAlign: 'center' }" :style="{ width: '297px' }">
          <!-- <a-tab-pane tab="公告" key="1">
            <a-list class="tab-pane">
              <a-list-item v-for="(notice, key) in notices" :key="key">
                <a-list-item-meta :title="notice.title" :description="notice.date">
                  <a-avatar style="background-color: white" slot="avatar"
                    src="https://gw.alipayobjects.com/zos/rmsportal/ThXAXghbEsBCCSDihZxY.png" />
                </a-list-item-meta>
              </a-list-item>
            </a-list>
          </a-tab-pane> -->
          <a-tab-pane tab="评论" key="2">
            <a-list class="tab-pane">
              <a-list-item v-for="(comment, key) in comments" :key="key" @click="onclick(comment)">
                <a-list-item-meta :title="comment.content" :description="comment.create_date">
                  <a-avatar style="background-color: white" slot="avatar"
                    src="https://gw.alipayobjects.com/zos/rmsportal/ThXAXghbEsBCCSDihZxY.png" />
                </a-list-item-meta>
                <a-badge dot v-if="comment.isUnread" />
              </a-list-item>
            </a-list>
          </a-tab-pane>
          <!-- <a-tab-pane tab="私信" key="3">
            <a-list class="tab-pane"></a-list>
          </a-tab-pane> -->
        </a-tabs>
      </a-spin>
    </div>
    <span @click="fetchNotice" class="header-notice">
      <a-badge class="notice-badge" :count="count">
        <a-icon :class="['header-notice-icon']" type="bell" />
      </a-badge>
    </span>
  </a-dropdown>
</template>

<script>
import { getNowNotice, readNotice } from '../../services/user';
import { mapGetters } from 'vuex';
export default {
  name: 'HeaderNotice',
  data() {
    return {
      loading: false,
      show: false,
      count: 0,
      // notices: [
      //   { title: "请维护个人资料", date: "1年前" },
      //   { title: "谨防上当受骗", date: "2年前" }
      // ],
      comments: [

      ],
      // letter: [],
    }
  },
  computed: {
    ...mapGetters('account', ['user']),
  },
  methods: {
    fetchNotice() {
      if (this.loading) {
        this.loading = false
        return
      }
      if (this.show) return
      this.loading = true
      this.comments = []
      this.count = 0
      getNowNotice(this.user.user_name).then(res => {
        const dataArray = res.data.data
        for (let i = 0, len = dataArray.length; i < len; i++) {
          this.comments.push({
            message_id: dataArray[i].message_id,
            content: dataArray[i].content,
            create_date: dataArray[i].content,
            isUnread: dataArray[i].isUnread,
            post_id: dataArray[i].post_id
          })
          if (dataArray[i].isUnread) {
            this.count = this.count + 1
          }
          console.log(dataArray[i].isUnread)
        }
      }).catch(err => {
        console.log(err)
        this.error("请求失败, 请尝试刷新页面", 1);
      })
      setTimeout(() => {
        this.loading = false
      }, 500)
    },
    onclick(comment) {
      if (!comment.isUnread) {
        return
      }
      comment.isUnread = false
      this.count = this.count - 1
      readNotice(this.user.user_name, comment.message_id).catch(err => {
        console.log(err)
        this.error("请求失败, 请尝试刷新页面", 1);
      })
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
    max-height: 300px;
    overflow: auto;
  }

  .ant-tabs-ink-bar {
    visibility: hidden;
  }
}
</style>
