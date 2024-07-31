<template>
    <button id="connect" @click="connect()">Connect</button>
    <button id="disconnect" @click="disconnect()">Disconnect</button>
  </template>
  
  <script setup>
  import { socket } from "@/socket";

  function connect() {
        socket.connect();
  }
  function disconnect() {
    socket.disconnect()};

    

  </script>

<style>
  #connect {
    position: absolute;
    top: 30px;
    color: #fcfcff;
    background-color: #444444;
    border-radius: 2px;
    border: none;
    right: 5px;
  }
  #disconnect {
    position: absolute;
    top: 30px;
    color: #fcfcff;
    background-color: #444444;
    border-radius: 2px;
    border: none;
    right: 70px;
  }
</style>