const {readFile} = require('fs');
const { reject } = require('lodash');
const { resolve } = require('path');

const getText = (path) => {
    return new Promise((resolve,reject)=>{
        readFile(path,'utf8',(err,data)=>{
        if(err){
            reject(err)
        }
        else{
            resolve(data)
        }
    })
})
}


// readFile('./content/first.txt','utf8',(err,data)=>{
    //     if(err){
        //         return;
        //     }
        //     else{
            //         console.log(data)
            //     }
            // })
            
            const start =async()=>{
                try{

                }
                catch(error){
                    
                }
                const first = await getText('./content/first.txt');
                console.log(first)
            }
            start()
            // getText('./content/first.txt')
            // .then(result => console.log(result))
            // .catch((err)=>console.log(err))
