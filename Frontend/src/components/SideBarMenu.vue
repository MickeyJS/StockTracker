<template>
  <el-aside style="width:auto">
    <el-menu :default-openeds="['1', '3']">
      <el-submenu index="1">
        <template slot="title"><img class="icon-car" src="../assets/ic_directions_car_black_24dp_1x.png" alt="my icon"/>Car</template>
        <el-menu-item index="1-1">Sedan</el-menu-item>
        <el-menu-item index="1-2">SUV</el-menu-item>
        <el-menu-item index="1-3">Van</el-menu-item>
        <el-menu-item index="1-4">Sports Car</el-menu-item>
        <el-menu-item index="1-5">Luxury Car</el-menu-item>
        <el-menu-item index="1-6">Truck</el-menu-item>
      </el-submenu>
      <el-menu-item index="3">
        <img class="icon-location" src="../assets/ic_location_on_black_24dp_1x.png" alt="my icon"/>
        <span>Locations</span>
      </el-menu-item>
      <el-menu-item index="3">
        <img class="icon-offer" src="../assets/ic_local_offer_black_24dp_1x.png" alt="my icon"/>
        <span>Offers</span>
      </el-menu-item>
      <el-menu-item index="3">
        <img class="icon-assignment" src="../assets/ic_assignment_black_24dp_1x.png" alt="my icon"/>
        <span>Reservations</span>
      </el-menu-item>
    </el-menu>
  </el-aside>
</template>

<script>
</script>

<style scoped>
  .el-aside .icon-car {
    opacity: 0.5;
  }

  .el-aside .icon-assignment {
    opacity: 0.5;
  }

  .el-aside .icon-offer {
    opacity: 0.5;
  }

  .el-aside .icon-location {
    opacity: 0.5;
  }
</style>
