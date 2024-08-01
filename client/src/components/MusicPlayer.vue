<template>
    <audio id="aud"></audio>
</template>

<script lang="ts" setup>
import { onMounted, watch } from 'vue';
import { state } from '@/socket';

watch(state, (newsatae) => {
    if (newsatae.elapsedTime > 5) {return}
    let newVolume = newsatae.volume;
    const audio = document.getElementById('aud') as HTMLAudioElement;
    audio.volume = newVolume/100;
    audio.loop = true;
    audio.currentTime = newsatae.elapsedTime;
    audio.src = `http://untitlednam.tplinkdns.com:3000/music/${newsatae.currentSong}.mp3`;
    if (newsatae.elapsedTime < 5){audio.play()}

})

    onMounted(() => {
        const audio = document.getElementById('aud') as HTMLAudioElement;
        audio.src = `http://untitlednam.tplinkdns.com:3000/music/${state.currentSong}.mp3`;
        audio.loop = true;
        audio.volume = state.volume/100;
        audio.currentTime = state.elapsedTime
        audio.play()
    })
</script>

<script>
</script>

<style>

</style>