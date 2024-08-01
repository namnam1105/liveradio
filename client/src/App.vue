<script setup>
import Chat from './components/Chat.vue';
import ChatInput from './components/ChatInput.vue';
import ConnectionState from './components/ConnectionState.vue';
import ConnectionManager from './components/ConnectionManager.vue';
import MusicInfo from './components/MusicInfo.vue';
import MusicVisualizer from './components/MusicVisualizer.vue';
import MusicPlayer from './components/MusicPlayer.vue';
</script>

<template>
  <Chat />
  <ChatInput/>
  <ConnectionState/>
  <ConnectionManager/>
  <MusicInfo/>
  <MusicVisualizer/>
  <MusicPlayer/>
</template>

<style scoped>
header {
  line-height: 1.5;
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }
}
</style>
