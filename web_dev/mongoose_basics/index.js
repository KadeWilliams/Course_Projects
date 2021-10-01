const mongoose = require('mongoose')

main()
    .then(() => console.log("CONNECTED"))
    .catch(err => console.log(err))

async function main() {
    await mongoose.connect('mongodb://localhost:27017/movieApp')

}

const movieSchema = new mongoose.Schema({
    title: String,
    year: Number,
    score: Number,
    rating: String
});

const Movie = mongoose.model('Movie', movieSchema)

// const parasite = new Movie({ title: 'Parasite', year: 2019, score: 10, rating: 'R' })
