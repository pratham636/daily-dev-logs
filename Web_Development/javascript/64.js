const fs = require("fs");
const text = fs.readFileSync("web_development/javascript/dele.txt","utf-8");
console.log("The content of the file is")
console.log(text);