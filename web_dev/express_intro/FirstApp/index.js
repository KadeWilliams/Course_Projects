const express = require('express');
const app = express();

// app.use((req, res) => {
//     console.log('We got a new request')
//     res.send({ hello: 'world' })
// })

app.get('/', (req, res) => {
    res.send('This is the homepage!!!!!')
})

app.get('/r/:subreddit', (req, res) => {
    const { subreddit } = req.params
    res.send(`<h1> Browsing the ${subreddit} subreddit`)
})

app.post('/cats', (req, res) => {
    res.send("This is different than a get request")
})

app.get('/cats', (req, res) => {
    res.send('Meow!')
})

app.get('/dogs', (req, res) => {
    res.send('Woof!')
})

app.get('/search', (req, res) => {
    const { q } = req.query;
    console.log(q)
    res.send(`<h1>Search results for ${q}</h1>`)
})


app.get('*', (req, res) => {
    res.send("I don't know that path")
})

// /cats => 'meow'
// /dogs => 'woof'
// /home

app.listen(3000, () => {
    console.log("listening on port 3000")
})

