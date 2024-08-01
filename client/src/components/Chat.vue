<template>
    <div id="chatComp" 	>
        <ul id="messages">
            <li id="li" v-for="(msg, index) in state.messages" :key="index">{{msg}}</li>
        </ul>
    </div>
</template>

<script lang="js" setup>
import { onMounted, watch, getCurrentInstance } from 'vue';
import { state } from "@/socket";
import eventBus from "@/eventBus";

// Import the EventEmitter type from Node.js or a similar library


// Cast eventBus to the correct type


const chatDiv = document.getElementById('chatComp')
const needUpdate = () => {
  getCurrentInstance().proxy.$forceUpdate();
    if (chatDiv.value) {
        chatDiv.value.scrollTop = chatDiv.value.scrollHeight;
    }
}


onMounted(() => {
    try {
        eventBus.on('update-chat', needUpdate);
    } catch (error) {
        console.warn('Failed to listen to update-chat event:', error);
    }
    if (chatDiv.value) {
        chatDiv.value.scrollTop = chatDiv.value.scrollHeight;
    }
});

watch(() => state.messages, ()=>{
    needUpdate();
})
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