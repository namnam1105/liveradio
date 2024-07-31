<!-- eslint-disable vue/multi-word-component-names -->
<!-- eslint-disable vue/require-v-for-key -->
<template>
    <div id="chatComp">
        <ul id="messages">
            <li id="li" v-for="(msg, index) in state.messages" :key="index">{{msg}}</li>
        </ul>
    </div>
</template>

<script lang="js" setup>
import { getCurrentInstance, onMounted, watch } from 'vue';
import { state } from "@/socket";
import eventBus from "@/eventBus";

const needUpdate = () => {
    const instance = getCurrentInstance();
    instance.proxy.$forceUpdate();
}

onMounted(() => {
  eventBus.on('update-chat', needUpdate);
});

watch(() => state.messages, ()=>{
    needUpdate();
})
/*

       /\         nam@fedoralinux
      /  \        os     Arch Linux
     /\   \       host   B550M AORUS ELITE -CF
    /      \      kernel 6.10.1-arch1-1
   /   ,,   \     uptime 4h 44m
  /   |  |  -\    pkgs   1163
 /_-''    ''-_\   memory 10167M / 32019M


*/


</script>




<style scoped>
#chatComp{
    overflow: scroll;
    width: 100%;
    height: 50rem; /* Adjust the height for better visibility */
    background-color: #44444444;
    position: relative;
    left: 0; /* Position at the left edge */
    top: 0; /* Position at the top edge */
}
#messages { list-style-type: none; margin: 0; padding: 0;}
#messages > li {padding: 0.5rem 1 rem; font-size: 32px;} /* Adjust the font size for better readability */
#messages > li:nth-child(odd) {background-color: #353535;}

/* Media queries for different screen sizes */

/* Small screens (mobile devices) */
@media (max-width: 600px) {
  #chatComp {
    height: auto; /* Adjust the height to fit the content */
  }
  #messages {
    font-size: 24px; /* Adjust the font size for better readability */
  }
}

/* Medium screens (tablets) */
@media (min-width: 601px) and (max-width: 1024px) {
  #chatComp {
    height: 40rem; /* Adjust the height for better visibility */
  }
  #messages {
    font-size: 28px; /* Adjust the font size for better readability */
  }
}

/* Large screens (desktops) */
@media (min-width: 1025px) {
  #chatComp {
    position: absolute;
    left: 1rem;
    top: 1rem;
    width: 40%;
    height: 35%; /* Adjust the height for better visibility */
  }
  #messages #li {
    font-size: 1.35vw; /* Adjust the font size for better readability */
  }
}

</style>