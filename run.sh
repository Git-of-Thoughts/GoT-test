npm init -y

npm install http-server --save-dev

{
  "name": "2048-game",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "start": "http-server . -p 8000"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "http-server": "^0.12.3"
  }
}

npm start
