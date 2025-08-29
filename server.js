// const express = require('express');
// const http = require('http');
// const socketIo = require('socket.io');
// const fs = require('fs');
// const chokidar = require('chokidar');

// const app = express();
// const server = http.createServer(app);
// const io = socketIo(server);

// app.use(express.static('public'));

// const watcher = chokidar.watch('example.txt', {
//     persistent: true,
// });

// watcher.on('change', (path) => {
//     console.log(`File ${path} has been changed`);
//     io.emit('fileChanged');
// });

// io.on('connection', (socket) => {
//     console.log('a user connected');
//     socket.on('disconnect', () => {
//         console.log('user disconnected');
//     });
// });

// const PORT = process.env.PORT || 3000;
// server.listen(PORT, () => {
//     console.log(`Server is running on port ${PORT}`);
// });



const express = require('express');
const http = require('http');
const socketIo = require('socket.io');
const fs = require('fs');
const chokidar = require('chokidar');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = socketIo(server);

app.use(express.static('public'));

// Serve static files from the root directory
app.use(express.static(__dirname));

// Serve example.txt explicitly
app.get('/example.txt', (req, res) => {
    res.sendFile(path.join(__dirname, 'example.txt'));
});

// Watch for file changes
const watcher = chokidar.watch('example.txt', {
    persistent: true,
});

watcher.on('change', (path) => {
    console.log(`File ${path} has been changed`);
    io.emit('fileChanged');
});

io.on('connection', (socket) => {
    console.log('A user connected');
    socket.on('disconnect', () => {
        console.log('User disconnected');
    });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
