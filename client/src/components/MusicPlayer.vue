<template>
    <audio id="aud"></audio>
</template>

<script lang="ts" setup>
import { onMounted, watch, getCurrentInstance, ref  } from 'vue';
import { state } from '@/socket';



let curSong = '';
// ok so here is the music update to actually sync between clients
watch(state, (newsatae) => {
    let newVolume = newsatae.volume;
    const audio = document.getElementById('aud') as HTMLAudioElement;
    audio.volume = newVolume/100;
    if (curSong != newsatae.currentSong) {
        console.log(`${curSong} != ${newsatae.currentSong}`)
        console.log('new song')
        curSong = newsatae.currentSong;
        audio.src = `http://untitlednam.tplinkdns.com:3000/music/${state.currentSong}.mp3#t=${state.elapsedTime}`;
        audio.play();
    }
    if (audio.paused || audio.ended) {
        console.log('ended and waiting for the next trigger')
        curSong = newsatae.currentSong;
        return
    }
    if (newsatae.clientElapsed > 2) {
        return;
    }
    // audio.currentTime = newsatae.elapsedTime;
    audio.src = `http://untitlednam.tplinkdns.com:3000/music/${state.currentSong}.mp3#t=${state.elapsedTime}`;
    if (audio.paused || audio.ended) { audio.play()}
    
})
// sync on mount
onMounted(() => {
    const audio = document.getElementById('aud') as HTMLAudioElement;
    audio.src = `http://untitlednam.tplinkdns.com:3000/music/${state.currentSong}.mp3#t=${state.elapsedTime}`;

    audio.volume = state.volume/100;
    audio.currentTime = state.elapsedTime
    audio.play()
})
async function clientElapse() {
    state.clientElapsed++;
    await setTimeout(clientElapse, 1000);
} 
clientElapse()
</script>

<script>
</script>

<style>

</style>