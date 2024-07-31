<template>
    <p id="state">{{ connected ? "Connected" : "Not connected" }}</p>
  </template>
  
  <script setup>
  import { state } from "@/socket";
    import { computed } from "vue";
    const connected = computed(() => state.connected);
  function checkForConnect(){
    if (!state.connected) {
      document.querySelectorAll('li').forEach((li) => {
        li.remove();
    })
  }
  setTimeout(()=>{
    checkForConnect()
  }, 1000)
  }
  checkForConnect()

</script>


<style>
#state {
    position: absolute;
    top: 5px;
    right: 5px
}
</style>