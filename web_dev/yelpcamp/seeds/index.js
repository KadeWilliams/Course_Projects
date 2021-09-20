const mongoose = require('mongoose');
const cities = require('./cities')
const Campground = require('../models/campground');
const { places, descriptors } = require('./seedHelpers')

main()
    .then(() => console.log("CONNECTED"))
    .catch(err => console.log(err))

async function main() {
    await mongoose.connect('mongodb://localhost:27017/yelp-camp')
}

const sample = arr => arr[Math.floor(Math.random() * arr.length)]

const seedDB = async () => {
    await Campground.deleteMany({})
    for (let i = 0; i < 50; i++) {
        const random1000 = Math.floor(Math.random() * 1000)
        const price = Math.floor(Math.random() * 20) + 10
        const camp = new Campground({
            location: `${cities[random1000].city}, ${cities[random1000].state}`,
            title: `${sample(descriptors)} ${sample(places)}`,
            image: 'https://images.unsplash.com/photo-1518602164578-cd0074062767?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1000&q=80',
            description: 'Lorem ipsum dolor sit amet consectetur, adipisicing elit. Laborum, beatae dolor excepturi quidem asperiores neque qui necessitatibus sed quia magnam saepe soluta non a eveniet velit. Provident quidem soluta nostrum.',
            price
        })
        await camp.save()
    }
}

seedDB().then(() => {
    mongoose.connection.close()
})