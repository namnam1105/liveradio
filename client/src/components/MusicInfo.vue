<template>
    <div class="songContainer">
        <div class="songWrapper">
            <div id="volume">
                <input @input="updateVolume" type="range" id="volumeSlider" min="0" max="100" value="50" v-model="volume">
            </div>
            <img id="songCover" src=""/>
            <div id="songInfo">
                <h2 id="songName">{{state.songName}}</h2>
                <p id="songAuthor">{{state.author}}</p>
            </div>
            <div id="length">
            </div>
            <p id="lengthP">{{formatSeconds(state.elapsedTime)}}</p>
            <p id="lengthEnd">{{formatSeconds(state.duration)}}</p>
        </div>
    </div>
</template>

<script setup>
import { state } from '@/socket';
import { ref , watch} from 'vue';
const volume = ref(50)
console.log(state)
function formatSeconds(seconds) {
    const minutes = Math.floor(seconds / 60);
    const remainingSeconds = seconds % 60;
    return `${minutes}:${remainingSeconds.toString().padStart(2, '0')}`;
}

function updateVolume() {
    state.volume = volume.value;
}
watch(state, (newState)=>{
    document.getElementById('songCover').src = "http://untitlednam.tplinkdns.com:3000/jpgs/"+newState.currentSong+".jpg"
    document.getElementById('lengthP').innerHTML = formatSeconds(newState.elapsedTime)
    document.getElementById('lengthEnd').innerHTML = formatSeconds(Math.floor(newState.duration))
    const percentage = newState.elapsedTime / newState.duration * 100;
    document.documentElement.style.setProperty('--before-width', `${percentage}%`) 
})



</script>

<style>
    :root {
        --before-width: 0%;
    }

    .songContainer {
        position: absolute;
        right: 30em;
        top: 10em;
        height: 33em;
        width: 30em;
        display: inline-block;
    }
    .songWrapper {
        position: absolute;
        width: 1;
        display: inline-block;
    }

    #songInfo {
        position: absolute;
        right: 0;
        bottom: 0.17em;
        padding: 10px;
        background-color: rgba(0, 0, 0, 0.5);
        color: white;
        border-radius: 0 0 20px 20px;
        box-sizing: inherit;
        width: 100%;
        text-align: center;
        z-index: 1;
    }

    #songCover {
        border-radius: 3%;
        box-sizing: border-box;
        width: 450px;
    }
    #length {
        box-sizing: inherit;
        border-radius: 10px;
        transition: transform 500ms ease-in-out;
        position: absolute;
        overflow: hidden;
        height: 5px;
        width: 30em;
        top: 31em;
        background-color: rgba(255,255,255,0.2);
    }

    #length::before{
        box-sizing: inherit;
        position: absolute;
        left: 0;
        content: "";
        background-color: white;
        border-radius: 10px;
        height: 5px;
        transition: all 300ms ease-in-out;
        width: var(--before-width);
        display: flex;
        align-items: center;
        justify-content: center;
        color: black;
    }


    #lengthP {
        box-sizing: inherit;
        position: absolute;
        top: 100%;
        left: 50%;
        transform: translate(-760%, 50%);
        margin: 0;
        padding: 0;
        font-size: 1em;
    }
    #lengthEnd {
        box-sizing: inherit;
        position: absolute;
        top: 100%;
        left: 50%;
        transform: translate(660%, 50%);
        margin: 0;
        padding: 0;
        font-size: 1em;
    }

    #volume {
        box-sizing: inherit;
        border-radius: 10px;
        transition: transform 500ms ease-in-out;
        position: absolute;
        overflow: hidden;
        height: 5px;
        width: 30em;
        top: -1em;
        background-color: rgba(255,255,255,0.2);
    }

    #volumeSlider {
        position: absolute;
        z-index: 1;
        width: 100%;
        -webkit-appearance: none;
        appearance: none;
        height: 5px;
        background: rgba(255,255,255,0.2);
        outline: none;
        opacity: 0.7;
        transition: opacity .2s;
    }


    #volumeSlider::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 15px;
        height: 15px;
        background: white;
        cursor: pointer;
        border-radius: 50%;
    }

    #volumeSlider::-moz-range-thumb {
        width: 15px;
        height: 15px;
        background: white;
        cursor: pointer;
        border-radius: 50%;
    }

    @media (max-width: 1400px) {
        .songContainer {
            right: 10em;
            top: 10em;
        }

        #length {
            top: 31em;
        }

    }
    @media (min-width: 601px) and (max-width: 1024px) {
        .songContainer {
            position: absolute;
            width: 30em;
            top: 55em;
            left: 25%;
        }
        #length {
            width: 30em;
            top: 31em;
        }
        #lengthP {
            transform: translate(-760%, 50%);
        }
        #lengthEnd {
            transform: translate(650%, 50%);
        }
        #volume {
            width: 30em;
        }
    }
    @media (max-width: 600px) {
        .songContainer {
            position: absolute;
            width: 20em;
            top: 80em;
            left: 25%;
        }
        #length {
            width: 20em;
            top: 21em;
        }
        #lengthP {
            transform: translate(-500%, 50%);
        }
        #lengthEnd {
            transform: translate(400%, 50%);
        }
        #volume {
            width: 20em;
        }
    }
    @media (max-width: 500px) {
        .songContainer {
            position: absolute;
            width: 20em;
            top: 90em;
            left: 15%;
        }
        #length {
            width: 20em;
            top: 21em;
        }
        #lengthP {
            transform: translate(-500%, 50%);
        }
        #lengthEnd {
            transform: translate(400%, 50%);
        }
        #volume {
            width: 20em;
        }
    }
    @media (max-width: 400px) {
        .songContainer {
            position: absolute;
            width: 20em;
            top: 110em;
            left: 0;
        }
        #length {
            width: 20em;
            top: 21em;
        }
        #lengthP {
            transform: translate(-500%, 50%);
        }
        #lengthEnd {
            transform: translate(400%, 50%);
        }
        #volume {
            width: 20em;
        }
    }

    #volumeSlider::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 15px;
    height: 15px;
    background: white;
    cursor: pointer;
    border-radius: 50%;
    box-shadow: 0 0 2px rgba(0, 0, 0, 0.5);
}

#volumeSlider::-moz-range-thumb {
    width: 15px;
    height: 15px;
    background: white;
    cursor: pointer;
    border-radius: 50%;
    box-shadow: 0 0 2px rgba(0, 0, 0, 0.5);
}

</style>