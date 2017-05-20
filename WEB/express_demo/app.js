const app = require("express")()
const sqlite3 = require("sqlite3").verbose()
const db = new sqlite3.Database('./fifty_sound.db')


app.get('/api/chars', (req, res) => {
  db.all('SELECT * FROM FIFTY_SOUND;', (err, all)=> {
    res.send(all)
  })
})


app.listen(3000)
