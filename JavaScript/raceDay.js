let raceNumber = Math.floor(Math.random() * 1000);
let earlyRegister = false;
let runnerAge = 15;
if(earlyRegister && runnerAge>18){
  raceNumber+=1000;
}
if (earlyRegister && runnerAge>18){
  console.log(`Racer no.${raceNumber}, your race will begin at 9:30 am!`);
}else if(!earlyRegister && runnerAge>18){
  console.log(`Racer no.${raceNumber}, your race will begin at 11:00 am!`);
}else if (runnerAge < 18){
  console.log(`Racer no.${raceNumber}, your race begins at 12:30 pm!`);
}else{
  console.log('See the registration desk!');
}