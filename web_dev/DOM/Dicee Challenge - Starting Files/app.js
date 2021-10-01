const rand1 = Math.floor(Math.random() * 6) + 1
const rand2 = Math.floor(Math.random() * 6) + 1

let img1 = document.querySelector('div img.img1')
let img2 = document.querySelector('div img.img2')

img1.setAttribute('src', `images/dice${rand1}.png`)
img2.setAttribute('src', `images/dice${rand2}.png`)

let title = document.querySelector('h1')

if (rand1 > rand2) {
    title.textContent = 'Player 1 Wins'
} else if (rand2 > rand1) {
    title.textContent = 'Player 2 Wins'
} else {
    title.textContent = 'Draw'
}
