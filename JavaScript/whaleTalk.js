let input = 'Corruption is the greatest evil in Kenya';
//declaring an array to store vowels
const vowels = ['a', 'e', 'i', 'o', 'u'];
//declaring an array to store the final result of whaleTalk
let resultArray = [];
//looping through input
for(let i=0;i<input.length;i++){
//logging each character of input to the console with its index
  //console.log(`${input[i]} is ${i}`);
//looping through the vowels while looping through input
  for(let j = 0;j<vowels.length;j++){
  //comparing input and vowels
    if(input[i] === vowels[j]){
      resultArray.push(input[i]);
    }
    //checking for e's and doubling them
    if(input[i]==='e'){
      resultArray.push(input[i]);
    }
    //checking for u's and doubling them
    if(input[i]==='u'){
      resultArray.push(input[i]);
    }
  }
}
//logging resusltArray to the console
console.log(resultArray);
//joining elements in resultArray and capitalizing them
const resultString = resultArray.join('').toUpperCase()
console.log(resultString)
