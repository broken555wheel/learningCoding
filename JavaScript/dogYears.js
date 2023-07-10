//Converting my age to dog years

//Asking for user input
let myAge = 19;
//Creating a variable to store the first two years for the dog
let earlyYears = 2;
//converting the first two years into dog years
earlyYears*=10.5;
//lessing two from the initial age since it was already converted to dog years
let laterYears = myAge-=2;
//converting the remaining years to dog years
laterYears*=4;
console.log(earlyYears);
console.log(laterYears);
//getting the total for dog years
myAgeInDogYears = earlyYears+laterYears;
//taking users name and converting it to lowercase
myName='David'.toLowerCase();
//printig the output
console.log(`My name is ${myName}. I am ${myAge} years old in human years which is ${myAgeInDogYears} years old in dog years.`);

