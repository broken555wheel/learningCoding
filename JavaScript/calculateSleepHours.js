//function to get number of hourse slept each day
function getSleepHours (day){
    day.toLowerCase();
    switch (day){
      case 'monday':
      return 6;
      break;
      case 'tuesday':
      return 6;
      break;
      case 'wednesday':
      return 7;
      break;
      case 'thursday':
      return 8;
      break;
      case 'friday':
      return 3;
      break;
      case 'saturday':
      return 5;
      break;
      case 'sunday':
      return 10;
      break;
      default:
      console.log('please enter a valid day of the week');
      break;
    }
  }
  //getting actual sleep hours for the week
  const getActualSleepHours = () =>  getSleepHours('monday')+getSleepHours('tuesday')+getSleepHours('wednesday')+getSleepHours('thursday')+getSleepHours('friday')+getSleepHours('saturday')+getSleepHours('sunday');
  //getting ideal hours of sleep for the week
  function getIdealSleepHours(idealSleepHours){
    return idealSleepHours*7;
  }
  //calculating sleep debt
  function calculateSleepDebt(){
    let actualSleepHours = getActualSleepHours();
    let idealSleepHours = getIdealSleepHours(6);
    if(actualSleepHours === idealSleepHours){
      return('You got enough sleep');
    }else if(actualSleepHours>idealSleepHours){
      return(`You got more sleep than needed by ${actualSleepHours-idealSleepHours} hours`);
    }else{
      return(`You got less sleep hours than requrired by ${idealSleepHours-actualSleepHours} hours`);
    }
  }
  console.log(calculateSleepDebt());
  