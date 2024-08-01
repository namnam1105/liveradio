# Vue and Flask app for playing music in realtime Version 1.0

To use it you have to open two servers. `5173` and `3000`.

Clone the github repo
```shell
git clone https://github.com/Noname110678/liveradio.git
cd liveradio
```

Refer to the project root as either `root` or `/`

Frontend (Client) server `(5173)`


```shell
cd client # change working directory to the client project
yarn # install dependencies
yarn format # format the project using prettier
yarn lint # lint the project using ESLint
yarn dev --host # run client server
```

Backend Server `(3000)`
```shell
# MUST BE IN THE ROOT DIRECTORY OF THE PROJECT (/)
python3 -m venv venv
# UNIX activate env
source ./venv/bin/activate
# WINDOWS activate env (POWERSHELL)
./venv/scripts/activate
pip install -r req.txt
python3 main.py
```

# Adding songs

1. Download the song in `.mp3` format and put it inside /music folder.
2. Download the song cover in `.jpg` format and put it inside /jpgs folder.
3. Edit the song table to display song names properly

`/client/src/socket.js`

```js
const songTable = {
  "songName (as a file without extension)": ["Author(s)", "Song name"],
  "cats": ["The Living Tombstone", "Cats"] // example
}
```

# Fixing bugs.

I am hoping that someone will be able to fix the bugs of Chat component updating the whole page instead of just one component and I will be thankful if someone decides to contribute.

# Contact

- Telegram: @n4n4m
- Discord: @nn4m