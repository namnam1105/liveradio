import express from 'express';
import { Server } from 'socket.io';
import { createServer } from 'node:http';
import fs from 'fs';
import { createRequire } from "module";
const require = createRequire(import.meta.url);
const lol = require('./client/src/lol.json');

const app = express();
const server = createServer(app);
const io = new Server(server, {
    cors: {
        origin: '*'
    }
});

app.get("/", (req, res) => {
    res.send("Hello world! This is a backend server so you wont find anything interesting");
})

io.on('connection', (socket) => {
    console.log("A user connected");
    socket.on('disconnect', () => {
        console.log("A user disconnected");
    })
    socket.on('chat message', (msg) => {
        io.emit('chat message', msg);
        console.log(msg)
        lol.push(msg)
        fs.writeFile("./client/src/lol.json", JSON.stringify(lol), (err) => {
            console.log('wrote')
            console.log(err)
        })
    })
});

server.listen(8080, '192.168.0.4', ()=> console.log("Opened for",8080))