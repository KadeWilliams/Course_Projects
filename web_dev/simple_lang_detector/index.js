import { franc, francAll } from 'franc'
import langs from 'langs'
import colors from 'colors'

const inp = process.argv[2]

try {
    const lang = franc(inp)
    console.log(langs.where('3', lang).name.green)
} catch (err) {
    console.log('Could not match a language. Please try again.'.underline.red)
}