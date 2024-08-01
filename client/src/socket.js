/* eslint-disable no-undef */
import lol from './lol.json'
import { reactive } from "vue";
import { io } from "socket.io-client";

export const state = reactive({
    connected: false,
    currentSong: "",
    messages: [],
    volume: 50,
    clientElapsed: 0,
    elapsedTime: 0,
    duration: 0,
    songName: "",
    author: ""
});

const songTable = {
  "cats": ["The Living Tombstone", "Cats"]
}

const URL = process.env.NODE_ENV === "production" ? undefined : "http://untitlednam.tplinkdns.com:3000/";

export const socket = io(URL);

socket.on("connect", () => {
  state.connected = true;
  lol.forEach((el) => {
    state.messages.push(el)
  })
});


socket.on('new_music', (music) => {
  if (!state.elapsedTime == 0) {
    state.elapsedTime = (music.timestamp)
    return}
  state.duration = (music.length)
  state.currentSong = (music.filename).slice(0, -4)
  state.duration = (music.length)
  state.elapsedTime = (music.timestamp)
  state.songName = songTable[state.currentSong][1]
  state.author = songTable[state.currentSong][0]
})

socket.on('chat message', (message) => {
  state.messages.push(message);
})

socket.on("disconnect", () => {
  state.connected = false;
});