//creating an object to store team information
const team = {
  _players: [
  // creating an object to store info on players
    player1 = {
      firstName: '', lastName: '', age: 0
    },
    player2 = {
      firstName: '', lastName: '', age: 0
    },
    player3 = {
      firstName: '', lastName: '', age: 0
    }
  ],
  //creating an object to store info on games
  _games: [
    game1 = {
      opponent: '', teamPoints: '', opponentPoints: ''
    },
    game2 = {
      opponent: '', teamPoints: '', opponentPoints: ''
    },
    game3 = {
      opponent:'', teamPoints:'', opponentPoints: ''
    }    
  ],
  //creating a getter to read _players
  get players(){
    return this._players
  },
  //creating a getter to read _games
  get games(){
    return this._games
  },
  //creating a method to add data to _players
  addPlayer(newFirstName, newLastName, newAge){
    const player = {
      firstName: newFirstName, lastName: newLastName, age: newAge
    }
    this._players.push(player);
  },
    //creating a method to add data to _game
  addGame(newOpponent, newTeamPoints,newOpponentPoints){
    const game = {
      opponent: newOpponent, teamPoints: newTeamPoints, opponentPoints: newOpponentPoints
    }
    this._games.push(game);
  }
};
//adding a player to _players using addPlayer method
team.addPlayer('Bugs', 'Bunny', 76);
//adding a player to _games using addGames method
team.addGame('Titans', 100, 98);
console.log(team.players);
console.log(team.games);

