const express = require("express")
const request = require("request")
const path = require("path")
const app = express()


app.use(express.urlencoded({ extended: true }))

const url = "https://api.openweathermap.org/data/2.5/weather"

app.get('/', (req, res) => {
    res.sendFile(path.join(__dirname + '/index.html'))
})

app.get('/weather', (req, res) => {
    const { city } = req.body
    request(url + `?q=${city}&units=imperial&appid=9fd426754b113937b93606a1e7d069e8`, (err, response, body) => {
        console.error(err)
        console.log(response && response.statusCode)
        console.log(body)
        res.send(body)
    })
})


app.listen(3000, () => {
    console.log('Listening on port 3000')
})