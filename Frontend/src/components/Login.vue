<template>
    <el-container>
      <el-header align="center">
        ZALOGUJ SIĘ
      </el-header>
      <el-main>
        <el-col :span="12">
          <el-input placeholder="Login" v-model="login"></el-input>
        </el-col>
        <el-col :span="12">
          <el-input placeholder="Password" v-model="name"></el-input>
          <el-button v-on:click="greet">Log In</el-button>
        </el-col>
      </el-main>
    </el-container>

</template>

<script>
  import Vue from 'vue'
  import ElInput from "../../node_modules/element-ui/packages/input/src/input.vue";
  import ElCol from "element-ui/packages/col/src/col";
  import ElContainer from "../../node_modules/element-ui/packages/container/src/main.vue";
  import ElHeader from "../../node_modules/element-ui/packages/header/src/main.vue";
  import $ from "../../node_modules/jquery";
  import ElButton from "../../node_modules/element-ui/packages/button/src/button.vue";
  import VeeValidate from '../../node_modules/vee-validate';

  export default {
    components: {
      ElButton,
      ElHeader,
      ElContainer,
      ElCol,
      ElInput},
    data() {
      const item = {
        carBrand: 'mercedes',
        price: '100$',
        location: 'No. 189, Grove St, Los Angeles'
      };
      return {
        tableData: Array(20).fill(item),
        input: ''
      }
    },
   methods: {
    greet: function (event) {
      var url = 'http://jsonplaceholder.typicode.com/posts';
      $.getJSON(url, function (data) {
      var lastPost = 2;

        for (var i = lastPost; i < lastPost + 2; i++){
          if(i< data.length) {
            self.items.push(data[i]);


          }
          else {
            break;
          }
        }
        if(data.length > lastPost) {
          lastPost += 2;
          console.log(lastPost);
          console.log(self.items());
        }
      });
    }

    }

  }
</script>
