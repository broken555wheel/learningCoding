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

//using the setters to add a meal and price to menu
menu.meal = 'Spaghetti';
menu.price = 15;
//logging menu to the console using its getter
console.log(menu.todaysSpecial);
