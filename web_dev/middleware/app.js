const express = require('express');
const app = express();
const morgan = require('morgan')

const AppError = require('AppError')


app.use(morgan('tiny'))
app.use((req, res, next) => {
    req.requestTime = Date.now()
    console.log(req.method, req.path)
    next()
})

app.use('/dogs', (req, res, next) => {
    console.log('I LOVE DOGS')
    next()
})

app.use((req, res, next) => {
    const { password } = req.query
    if (password === "chickennugget") {
        next()
    }
    res.send('Sorry you need a password')
})

app.get('/', async (req, res) => {
    console.log(req.requestTime)
    res.send('HOW YOU DOING?')
})

app.get('/dogs', async (req, res) => {
    res.send('woof?')
})

app.listen(3000, () => {

})