// const path = require('path');
// const methodOverride = require('method-override')
// const { v4: uuid } = require('uuid'); //For generating ID's
const express = require('express');
// const { RSA_X931_PADDING } = require('constants');
const app = express();

// app.use(express.urlencoded({ extended: true }))
// app.use(express.json())
// app.use(methodOverride('_method'))

// app.set('views', path.join(__dirname, 'views'))
// app.set('view engine', 'ejs')

// const comments = [
//     {
//         id: uuid(),
//         username: 'Todd',
//         comment: "Lol that's so funny"
//     },
//     {
//         id: uuid(),
//         username: 'Skyler',
//         comment: 'I like to go birdwatching with my dog'
//     },
//     {
//         id: uuid(),
//         username: 'Sk8erBoi',
//         comment: 'Plz delete your account, Todd'
//     },
//     {
//         id: uuid(),
//         username: 'onlysayswoof',
//         comment: 'woof woof woof'
//     }
// ]

// app.get('/comments', (req, res) => {
//     res.render('comments/index', { comments });
// })

// app.get('/comments/new', (req, res) => {
//     res.render('comments/new');
// })

// app.post('/comments', (req, res) => {
//     const { username, comment } = req.body
//     comments.push({ username, comment, id: uuid() })
//     res.redirect('/comments')
// }
// )

// app.get('/comments/:id', (req, res) => {
//     const { id } = req.params
//     const comment = comments.find(c => c.id === id)
//     res.render('comments/show', { comment })
// })

// app.get('/comments/:id/edit', (req, res) => {
//     const { id } = req.params
//     const comment = comments.find(c => c.id === id)
//     res.render('comments/edit', { comment })
// })

// app.patch('/comments/:id', (req, res) => {
//     const { id } = req.params
//     const newCommentText = req.body.comment
//     const foundComment = comments.find(c => c.id === id)
//     foundComment.comment = newCommentText
//     res.redirect('comments')
// })


// ////////////////////////////////////

// app.get('/tacos', (req, res) => {
//     res.send("GET /tacos response")
// })

// app.post('/tacos', (req, res) => {
//     const { meat, qty } = req.body;
//     res.send(`OK, here are your ${qty} ${meat} tacos`)
// })

// app.listen(3000, () => {
//     console.log("ON PORT 3000!")
// })


// GET /comments - list all comments
// POST /comments - Create a new comment 
// GET /comments/:id - Get one comment (using ID)
// PATCH /comments/:id - Update one comment
// DELETE /comments/:id - Destroy one comment

//To parse form data in POST request body:
app.use(express.urlencoded({ extended: true }))
// To parse incoming JSON in POST request body:
app.use(express.json())
// To 'fake' put/patch/delete requests:
app.use(methodOverride('_method'))
// Views folder and EJS setup:
app.set('views', path.join(__dirname, 'views'))
app.set('view engine', 'ejs')

// Our fake database:
let comments = [
    {
        id: uuid(),
        username: 'Todd',
        comment: 'lol that is so funny!'
    },
    {
        id: uuid(),
        username: 'Skyler',
        comment: 'I like to go birdwatching with my dog'
    },
    {
        id: uuid(),
        username: 'Sk8erBoi',
        comment: 'Plz delete your account, Todd'
    },
    {
        id: uuid(),
        username: 'onlysayswoof',
        comment: 'woof woof woof'
    }
]
// **********************************
// INDEX - renders multiple comments
// **********************************
app.get('/comments', (req, res) => {
    res.render('comments/index', { comments });
})
// **********************************
// NEW - renders a form
// **********************************
app.get('/comments/new', (req, res) => {
    res.render('comments/new');
})
// **********************************
// CREATE - creates a new comment
// **********************************
app.post('/comments', (req, res) => {
    const { username, comment } = req.body;
    comments.push({ username, comment, id: uuid() })
    res.redirect('/comments');
})
// *******************************************
// SHOW - details about one particular comment
// *******************************************
app.get('/comments/:id', (req, res) => {
    const { id } = req.params;
    const comment = comments.find(c => c.id === id);
    res.render('comments/show', { comment })
})
// *******************************************
// EDIT - renders a form to edit a comment
// *******************************************
app.get('/comments/:id/edit', (req, res) => {
    const { id } = req.params;
    const comment = comments.find(c => c.id === id);
    res.render('comments/edit', { comment })
})
// *******************************************
// UPDATE - updates a particular comment
// *******************************************
app.patch('/comments/:id', (req, res) => {
    const { id } = req.params;
    const foundComment = comments.find(c => c.id === id);

    //get new text from req.body
    const newCommentText = req.body.comment;
    //update the comment with the data from req.body:
    foundComment.comment = newCommentText;
    //redirect back to index (or wherever you want)
    res.redirect('/comments')
})

// *******************************************
// DELETE/DESTROY- removes a single comment
// *******************************************
app.delete('/comments/:id', (req, res) => {
    const { id } = req.params;
    comments = comments.filter(c => c.id !== id);
    res.redirect('/comments');
})



















