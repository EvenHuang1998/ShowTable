<template>
  <a-layout id="components-layout-demo-side" style="min-height: 100vh">
    <a-layout-sider v-model="collapsed" collapsible>
      <div class="logo" />
      <a-menu
        theme="dark"
        mode="inline"
        :style="{ position: 'sticky', top: '10px' }"
        :defaultSelectedKeys="['homepage']"
      >
        <a-menu-item key="homepage">
          <a-icon type="home" />
          <router-link to="/frontend" style="display:inline-block">首页</router-link>
        </a-menu-item>
      </a-menu>
    </a-layout-sider>
    <a-layout>
      <a-layout-header
        style="background: #fff; padding: 0; margin-bottom: 20px"
      >
        <h2 class="title">基于P4可编程交换机的意图驱动测量系统</h2>
      </a-layout-header>
      <a-layout-content style="margin: 0 16px">
        <div
          :style="{ padding: '24px', background: '#fff', minHeight: '360px' }"
        >
          <router-view></router-view>
        </div>
      </a-layout-content>
    </a-layout>
  </a-layout>
</template>

<script>

export default {
  name: "App",
  data() {
    return {
      collapsed: false,
    };
  },
  sockets: {
    connect: function () {
      console.log("socket连接成功！");
    },
  },
  methods: {
  },
};
</script>

<style>
#components-layout-demo-side .logo {
  height: 20px;
  background: rgba(0, 21, 41, 0.2);
  margin: 16px;
}

.title {
  color: black;
  padding: 0 20px;
  float: left;
}
</style>