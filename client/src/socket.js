/* eslint-disable no-undef */
import lol from './lol.json'
import { reactive } from "vue";
import { io } from "socket.io-client";

export const state = reactive({
    connected: false,
    currentSong: null,
    messages: []
});

const URL = process.env.NODE_ENV === "production" ? undefined : "http://untitlednam.tplinkdns.com:3000/";

export const socket = io(URL);

socket.on("connect", () => {
  state.connected = true;
  lol.forEach((el) => {
    state.messages.push(el)
  })
});

socket.on('chat message', (message) => {
  state.messages.push(message);
})

socket.on("disconnect", () => {
  state.connected = false;
});