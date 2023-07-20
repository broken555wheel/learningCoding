//creating a menu object to store the meal and price
const menu = {
  //declaring properties with an indicator that they should remain private
    _meal:'',
    _price: 0,
    //creating a setter to alter the _meal property
    set meal(mealToCheck){
      if( typeof(mealToCheck) === 'string'){
        this._meal = mealToCheck;
      }
    },
    //creating a setter to alter the _price property
    set price(priceToCheck){
      if( typeof(priceToCheck) === 'number'){
        this._price = priceToCheck;
      }
    },
    get todaysSpecial(){
      if(this._meal && this._price){
        return `Today's special is ${this._meal} for ${this._price}\$`
      }else{
        return `Meal or Price was not set correctly`
      }
    }
  }
  
  //creating an array of meals
  const meals = ['Spaghetti', 'Pizza', 'Mac&Cheese', 'Roasted Potaoes', 'Zukini', 'Vegetable Rice'];
  const prices = [15,10,20,13,10,12];
  
  //randomly selecting a meal an it's price using pseudo-random numbers
  let index;
  do{if(meals.length === prices.length){
    index = Math.trunc(Math.random()*(meals.length));
  }else{
    console.log('Please ensure that each meal is assigned its price')
  }
  }while(meals.length !== prices.length);
  
  
  //using the setters to add a meal and price to menu from their respective arrays
  menu.meal = meals[index];
  menu.price = prices[index];
  
  //logging menu to the console using its getter
  console.log(menu.todaysSpecial);