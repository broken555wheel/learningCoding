let userName = 'David';
//check if userName is blank and print a greeting accordingly
userName ? console.log(`Hello ${userName}!`):console.log('Hello!');
//user question
let userQuestion = 'Is it going to rain?';
//check if userName is blank and print the question accordingly
if(userName){
  console.log(`${userName} asks, "${userQuestion}"`);
}else{
  console.log(`${userQuestion}`);
}
//generating pseudo-random integers from 1-8
let randomNumber = Math.trunc((Math.random()*8)+1);
//declaring a variable to store the response
let eightBall = '';
//using a switch statement to get a pseudo-random response
switch (randomNumber){
  case 1:
  eightBall = 'It is certain';
  break;
  case 2:
  eightBall = 'It is decidedly so';
  break;
  case 3:
  eightBall = 'Reply hazy try again';
  break;
  case 4:
  eightBall = 'Cannot predict now';
  break;
  case 5:
  eightBall = 'Do not count on it';
  break;
  case 6:
  eightBall = 'My sources say no';
  case 7:
  eightBall = 'Outlook not good';
  default:
  eightBall = 'Signs point to yes';
  break;
}
//print the response
console.log(eightBall);