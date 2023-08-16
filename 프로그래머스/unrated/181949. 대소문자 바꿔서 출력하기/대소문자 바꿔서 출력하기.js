const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let input = [];

rl.on('line', function (line) {
    input = [line];
}).on('close',function(){
    str = input[0];
    const newInput = [...str].map(alp => {
        if(alp.toUpperCase() === alp){
            return alp.toLowerCase()
        }else{
            return alp.toUpperCase()
        }
    })
    console.log(newInput.join(""))
});