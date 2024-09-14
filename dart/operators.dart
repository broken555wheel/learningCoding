/* 
Arithmetic Operators
+ => add
- => subtract
-expr => negation
* => multiply
/ => divide
~/ => int division
% => modullus
++var/ --var => pre increment i.e. the value used for var will be var+/-1
var++/var-- => post increment i.e var will be used as is then incremented
*/

/* 
Equality and relational operators
==	Equal
!=	Not equal
>	Greater than
<	Less than
>=	Greater than or equal to
<=	Less than or equal to
 */

//  identical() - used to check whether two objects are identical

/* 
Type test operators
as => used for type casting i.e. it attempts to cast an object to a specific type, if not it throws an error
is => used to check if an object is of a specific type
is! => negation of is */
class Person {
  String name = '';
  int age = 0;

  void setName(String name) {
    this.name = name;
  }

  void setAge(int age) {
    this.age = age;
  }

  void printInfo() {
    print('Name: $name, Age: $age');
  }
}

main() {
  var number = 42;
  // var text = number as String; error as int is not a subtype of string
  print(number is String); // returns false

  /* Conditional Expressions
  condition ? expr1 : expr2;
  checks if condition is true, if so exaluatest to expr1 otherwise expr2 */
  var isPublic = false;
  var visibility = isPublic ? 'public' : 'private';
  print(visibility);

  //if null operator/ null-coalescing

  Object? name;
  var firstName = 'David';
  var identification = name ??
      firstName; // checks if expression one is null, if it iss, it returns expression two
  print(identification);

  // Cascade notation
  var person = Person()
    ..setName('Alice')
    ..setAge(30)
    ..printInfo();
  // we need not call person every time we are accessing the object's methods or attributes

  // Null aware spread operator
  var list = [1, 2, 3, 4.5];
  var second_list = [
    0,
    ...?list
  ]; // Used like the spread operator but used when the iterable object may be null

  // Collection if and collection for
  var promoActive = false;
  var nav = ['Home', 'Furniture', 'Plants', if(promoActive) 'Outlet'];  //Conditionally creates a list 

  // if case
  var navBar = ['Home', 'Furniture', 'Plants', if(promoActive case true) 'Outlet'];
}
