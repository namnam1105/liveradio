<template>
    <div id="form-container">
        <form id="form" @submit.prevent="onSubmit" @keyup.enter="onSubmit">
            <input type="text" name="name" id="name" maxlength="10" placeholder="Your name..." >
            <input type="text" name="message" id="message" maxlength="140" placeholder="Type a message..." >
            <input type="submit" value="Send" id="send">
        </form>
    </div>
</template>

<script setup>
import { socket } from "@/socket";
import eventBus from '@/eventBus';

const updateChatComponent = () => {
  eventBus.emit('update-chat');
};

function onSubmit() {
    let name = document.getElementById('name')
    let message = document.getElementById('message');
    console.log('Form submitted');
    if (name.value == "") {
        alert('pls dont use empty names okok')
        return
    } else if (message.value == "") {
        alert ('pls dont use empty messages')
        return
    }
    socket.emit("chat message", `${name.value}: ${message.value}`);
    setTimeout(() => updateChatComponent(), 500)
}

</script>

<style lang="css">

#chatComp{
    overflow: scroll;
    width: 100%;
    height: 30rem;
    background-color: #44444444;
    position: relative; /* Change to relative positioning */
}
#messages { list-style-type: none; margin: 0; padding: 0;}
#messages > li {padding: 0.5rem 1 rem; font-size: 30px;}
#messages > li:nth-child(odd) {background-color: #353535;}
#form-container {
    display: flex;
    justify-content: center;
    align-items: center;
    position: relative; /* Change to relative positioning */
    margin-top: 2rem;
}
#form {
    width: 100%;
    max-width: 60rem; /* Set a maximum width for the form */
    display: flex;
    flex-direction: column; /* Change to column direction */
    align-items: flex-start; /* Align items to the start */
}
#form #name {
    width: 20rem;
    max-width: 100%; /* Set a maximum width for the input fields */
    height: 40px;
    background-color: #44444444;
    font-size: 30px;
    border: none;
    color: #fcfffc;
    margin-left: 3px;
    margin-right: 3px;
    margin-top: 5px;
    border-radius: 1px;
}
#form #message {
    width: 60rem;
    max-width: 100%; /* Set a maximum width for the input fields */
    height: 40px;
    background-color: #44444444;
    border: none;
    font-size: 30px;
    color: #fcfffc;
    margin: 5px;
    border-radius: 1px;
}
#form #send {
    width: 7.5rem;
    height: 40px;
    background-color: #44444444;
    border: none;
    font-size: 30px;
    margin-top: 5px;
    color: #fcfffc;
    border-radius: 1px;
}

/* Media queries for different screen sizes */

/* Small screens (mobile devices) */
@media (max-width: 600px) {
  #form {
    flex-direction: column;
  }
  #form #name, #form #message {
    width: 100%;
  }
}

/* Medium screens (tablets) */
@media (min-width: 601px) and (max-width: 1024px) {
  #form {
    flex-direction: row;
  }
  #form #name, #form #message {
    width: 50%;
  }

}

/* Large screens (desktops) */
@media (min-width: 1025px) {
    #form-container {
        position: absolute;
        margin-top: 0px;
        left: 0%;
        top: 40%; /* Adjust the top position */
        width: 45%;
    }
  #form {
    justify-content: flex-start; /* Change to flex-start */
    flex-direction: row;
    align-items: flex-start; /* Align items to the start */
  }

  #form #name {
    margin-left: 1rem;
  }

  #form #name, #form #message {
    margin-right: 3%; /* Add some margin to the right */
    width: 35%; /* Adjust the width to 45% */
    height: fit-content;
  }
  #form #send {
    width: 10%; /* Adjust the width to 10% */
    height: fit-content;
  }
  #form #name, #form #message, #form #send {
    font-size: 1.4vw;
  }

}



</style>