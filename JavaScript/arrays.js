//checking the equality of elements in two different arrays and populating third array with the equal elements
const bobsFollowers = ['Andrew', 'Tom', 'Rose', 'Ian'];
const tinasFollowers = ['Rose', 'Nate', 'Tom'];
const mutualFollowers = []
for(let i = 0;i<bobsFollowers.length;i++){
  for(let j = 0;j<tinasFollowers.length;j++){
    if (bobsFollowers[i]===tinasFollowers[j]){
      mutualFollowers.push(bobsFollowers[i]);//or mutualFollowers.push(bobsFollowers[i);
    }
  }
}
console.log(mutualFollowers);

//alternative methods of iterating through an array
//.forEach() - executes a provided function for each element
bobsFollowers.forEach(bobsFollowers => {
  console.log(`${bobsFollowers} follows Bob on social medial`);
});

//.map() - generates a new array populated by the results of executing a function provided to the elements of the original array
const array = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15];
//using .map() to multiply the elements inside the array by 2, and storing them in s new array called map1
const map1 = array.map(x => x*2);
console.log(map1.join(' '));

//.filter() - generates a new array populated by elements of the array that past a test set by the function passed
const filter1 = array.filter(num => num>5);
console.log(filter1);

//.findIndex() - returns the index of the first element to meet a condition specified in the function and if none of the elements does it returns -1
const index = array.findIndex(num => num >= 12);
console.log(index);

//.reduce() - reduces an array by adding the elements of the array and returing the sum. It adds arrays starting from arr[1]+arr[0] then adding the reulting sum till sum+arr[n-1]. It can take another parameter that specifies where the addition will start i.e x(starting point)+arr[0]
const sum = array.reduce((prev, current) => prev+current,50);//50 becomes the starting point of the addition
console.log(sum); 
//alternatively
const newNumbers = [1, 3, 5, 7];
const newSum = newNumbers.reduce((accumulator, currentValue) => 
  {console.log('The value of accumulator: ', accumulator);
  console.log('The value of currentValue: ', currentValue);
  return accumulator+currentValue;},10//10 becomes the starting point
);
console.log(newSum);

//.some() - tests whether any element in the array meets the condition specified by the function. if so it returns true else it returns false
const tValue = array.some(num => num>sum);
console.log(tValue);


//more from https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array