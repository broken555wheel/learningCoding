//checking the equality of elements in two different arrays and populating third array with the equal elements
const bobsFollowers = ['Andrew', 'Tom', 'Rose', 'Ian'];
const tinasFollowers = ['Rose', 'Nate', 'Tom'];
const mutualFollowers = []
for(let i = 0;i<bobsFollowers.length;i++){
  for(let j = 0;j<tinasFollowers.length;j++){
    if (bobsFollowers[i]===tinasFollowers[j]){
      mutualFollowers.unshift(bobsFollowers[i]);//or mutualFollowers.push(bobsFollowers[i);
    }
  }
}
console.log(mutualFollowers);
