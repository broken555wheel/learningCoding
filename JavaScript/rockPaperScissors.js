//getting user choice
const getUserChoice = userInput => {
    userInput.toLowerCase();
  //validating user choice
    if (userInput === 'rock'){
      return 'rock';
    }else if (userInput === 'paper'){
      return 'paper';
    }else if (userInput === 'scissors'){
      return 'scissors';
    }else if (userInput === 'bomb'){//secret cheatcode(always wins)
      return 'bomb';
    }else{
      console.log('Please enter a valid option among rock, paper or scissors');
    }
  } 
  //getting computer choice
  function getComputerChoice(){
  //using pseudo-random numbers to generate the computer choice
    let choice = Math.trunc(Math.random()*3)+1;
    switch (choice){
      case 1:
      return 'rock';
      break;
      case 2:
      return 'paper';
      break;
      case 3:
      return 'scissors';
      break;
    }
  }
  
  //determining the winner
  function determineWinner(userInput, computerChoice){
    //checking for the winner
    if(userInput === computerChoice){
      return('It\'s a tie!');
    } else if(userInput === 'rock'){
        if(computerChoice === 'paper'){
         return('You lose!');
        }else{
          return('You win!');
        }
      }else if(userInput === 'paper'){
        if(computerChoice === 'scissors'){
          return('You lose!');
        }else{
          return('You win')
        }
      }else if (userInput === 'bomb'){
        return('You win!');
      }else{
        if(computerChoice === 'rock'){
          return('You lose!');
        }else{
          return('You win');
        }
      }
  }
  
  //playing the game
  function playGame(userInput,computerChoice){
    userInput = getUserChoice('bomb');
    computerChoice=getComputerChoice();
    console.log(determineWinner(userInput,computerChoice));
  }
  playGame();
  