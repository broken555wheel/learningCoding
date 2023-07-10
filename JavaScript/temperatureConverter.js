//Converting temperature from Kelvin to Celsius.

//Asking for user input

//Declaring a consant value for temperature in Kelvin
const kelvin = 0;

//Converting kelvin to celsius by lessing kelvin by 273
let celsius = kelvin - 273;
//Converting celcius to farenheit
let fahrenheit = celsius * (9/5) + 32;
//Truncating the value of farenheit
Math.trunc(fahrenheit);
console.log(`The temperature is ${fahrenheit} degrees Fahrenheit`)

//Converting Celsius to Newton
let Newton = celsius*(33/100);
Math.floor(Newton);
console.log(Newton);