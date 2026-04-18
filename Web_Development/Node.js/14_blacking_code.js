const http = require('http')
// const server = require('json-server')

const server = http.createServer((req,res)=>{
if(req.url==='/')
{
    res.end('Home Page')
}
if(req.url==='/about')
{
    // BLOCKING CODE !!!!
    for (let i=0;i<1000;i++){
        for(let j=0;j<1000;j++){
            console.log(`${i} ${j}`)
        }
    }
    res.end('about Page')
}
else{
    res.end('error Page')
    }
})

server.listen(5000,()=>{
    console.log('Sever Listening on port 5000...')
})