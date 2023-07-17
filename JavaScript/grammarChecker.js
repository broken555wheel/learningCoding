let story = 'Last weekend, I took literally the most beautifull bike ride of my life. The route is called "The 9W to Nyack" and it stretches all the way from Riverside Park in Manhattan to South Nyack, New Jersey. It\'s really an adventure from beginning to end! It is a 48 mile loop and it literally took me an entire day. I stopped at Riverbank State Park to take some artsy photos. It was a short stop, though, because I had a freaking long way to go. After a quick photo op at the very popular Little Red Lighthouse I began my trek across the George Washington Bridge into New Jersey. The GW is a breathtaking 4,760 feet long! I was already very tired by the time I got to the other side. An hour later, I reached Greenbrook Nature Sanctuary, an extremely beautifull park along the coast of the Hudson. Something that was very surprising to me was that near the end of the route you literally cross back into New York! At this point, you are very close to the end.';
//splitting the string to an array
let storyWords = story.split(' ');
//console.log(storyWords);

let unnecessaryWord = 'literally';
let misspelledWord = 'beautifull';
let badWord = 'freaking';
let count = 0;

//counting the number of words in the array using forEach()
storyWords.forEach(word => count++);
//logging the number of words to the console
console.log(count);

//removing the word 'literally' from storyWords
storyWords = storyWords.filter((word) => word !== unnecessaryWord);

//removing the word 'freaking' from storyWords using its index
let badWordIndex = storyWords.findIndex((word) => word === badWord);
storyWords[badWordIndex] = 'really';
//checking if every word in the paragraph is less than 10 characters long
const lengthCheck = storyWords.every((word) => word.length<=10);
console.log(lengthCheck);

//replacing the word with more than 10 characters
const longWord = storyWords.findIndex(word => word.length>10);
storyWords[longWord] = 'glorious';

//replacing the misspelled word
for(let i = 0; i<count; i++){
  if(storyWords[i] === misspelledWord){
    storyWords[i] = 'beautiful';
  }
}

//logging the elements of storyWords to the console as a string
console.log(storyWords.join(' '));
