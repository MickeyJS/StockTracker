<template>
  <div id="app">
    <el-row class="title">
      <el-col :span="4" >
        <el-header >
          <img src="./assets/bitcoin.png" />
        </el-header>
      </el-col>
      <el-col class="titleFont" :span="20">
        Stock Tracker
      </el-col>
    </el-row>

    <el-row style="width:90%; margin:auto ">
    <el-col class= "sidebar" :span="4" >
      <Login/>
    </el-col>
    <el-col :span="20">
      <Bet/>
    </el-col>
    </el-row>

  </div>
</template>

<script>
import ElHeader from "../node_modules/element-ui/packages/header/src/main.vue";
import SideBarMenu from "./components/SideBarMenu.vue";
import Login from "./components/Login.vue";
import Bet from "./components/Bet.vue";
import DatePicker from "./components/DatePicker.vue";
import ElDatePicker from "../node_modules/element-datepicker"


export default {
  components: {ElHeader, SideBarMenu, Login, Bet, ElDatePicker}
}
</script>

<style scoped>

  #app {
    @import url("//unpkg.com/element-ui@2.0.3/lib/theme-chalk/index.css");
  }
  .el-header img {
    margin-top:1px; height:70px; margin-left: 10%
  }
  .title {
    background-color: #409EFF;
    font-size: 200%;
    text-align: center;
  }
  .titleFont {
    font-size: 200%;
    text-align: center;
  }
  .sidebar {
    background-color: #85c1e9;
  }
</style>
