//CommonJS every file is module(by default)
// Modules - Enapsulated Code (only share minimum)


const names = require('./4_name')
const sayHi= require('./5_utils')
const data = require('./6_alternative_flavor')
// here we use function so we use require directly without useing variable
require('./7_mind_grenade')
sayHi('susan')
sayHi(names.john)
sayHi(names.peter)

