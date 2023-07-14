let secretMessage = ['Learning', 'is', 'not', 'about', 'what', 'you', 'get', 'easily', 'the', 'first', 'time,', 'it', 'is', 'about', 'what', 'you', 'can', 'figure', 'out.', '-2015,', 'Chris', 'Pine,', 'Learn', 'JavaScript'];
//removing the last element from the array
secretMessage.pop();
//logging the array length to the console
console.log(secretMessage.length);
//adding 'to' and 'pop' to the array
secretMessage.push('to', 'Program');
//changing easily to right
secretMessage[7] = 'right';
//removing the first element from the array
secretMessage.shift();

//adding 'programming' to the beginning of the array
secretMessage.unshift('Programming');
//replacing some array elements with others
secretMessage.splice(6,5);
secretMessage.splice(6,0,'know');

//joining the elements into one sentence
console.log(secretMessage.join(' '));