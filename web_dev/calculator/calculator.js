const express = require('express')
const app = express()
app.use(express.urlencoded({ extended: true }))

// const path = require('path')
// app.set('views', path.join(__dirname, 'views'))
// app.set('view engine', 'html')

app.get('/', (req, res) => {
    // let number1 = document.getElementById('number1').textContent
    // let number2 = document.getElementById('number2').textContent
    res.sendFile(__dirname + '/index.html')
})

app.post('/', (req, res) => {
    let { num1, num2 } = req.body
    num1 = Number(num1)
    num2 = Number(num2)
    console.log(num1 + num2)
    res.redirect('/')
})

app.get('/bmicalculator', (req, res) => {
    res.sendFile(__dirname + '/bmiCalculator.html')
})

app.post('/bmicalculator', (req, res) => {
    let { height, weight } = req.body
    height = Number(height)
    weight = Number(weight)
    res.send(`YOUR BMI IS ${(weight / (height * height)) * 10000}`)
})
app.listen(3000, () => {
    console.log("Listening on port 3000")
})