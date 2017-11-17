<template>
  <el-container>
    <el-header align="center">
      Wybierz dane do obserwacji
    </el-header>
    <el-main class="form">
      <el-row>
        <el-col class="textCol" :span="12">
          Wybierz walute
        </el-col>
        <el-col :span="12">
          <input type="text" id="datepicker">
        </el-col>
      </el-row>
      <el-row>
        <el-col class="textCol" :span="12">
          Wybierz do kiedy chcesz obserwować
        </el-col>
        <el-col :span="12">
          <input type="date">
        </el-col>
      </el-row>
      <el-row>
        <el-col class="textCol" :span="12">
          Wyslać powiadomienie sms?</el-col>
        <el-col class="textCol" :span="12">
        <el-checkbox>
        </el-checkbox></el-col>
      </el-row>
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
  import ElRow from "element-ui/packages/row/src/row";
  import ElCheckbox from "../../node_modules/element-ui/packages/checkbox/src/checkbox.vue";

  export default {
    components: {
      ElCheckbox,
      ElRow,
      ElButton,
      ElHeader,
      ElContainer,
      ElCol,
      ElInput
    },
    data() {
      return {
        options: [{
          label: 'California',
          cities: []
        }, {
          label: 'Florida',
          cities: []
        }],
        props: {
          value: 'label',
          children: 'cities'
        }
      }
    },
  }
</script>

<style scoped>
  .form {

  }

  textCol {
    text-align: right;

  }
</style>
