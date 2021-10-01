const express = require('express')
const app = express()

app.get('/', (req, res) => {
    res.send('<h1>Hello</h1>')
})

// app.get('/contact', (req, res) => {
//     res.send('Contact at kade@gmail.com')
// })

// app.get('/about', (req, res) => {
//     res.send("I'm kade williams")
// })

app.listen(3000, () => {
    console.log("Listening on port 3000")
})