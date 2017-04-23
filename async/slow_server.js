const http = require('http');

var count = 0

http.createServer((req, res) => {
  setTimeout(() => {
    // print connection count to stdout
    console.log('connection count: ',++count)
    res.writeHead(200, { "Content-Type": "text/plain" });
    res.end("hello!");
  }, 1000);
}).listen(3000);
