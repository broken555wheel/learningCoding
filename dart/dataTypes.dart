/*
The main data types in dart are:
-int
-String
-double
-bool
-dynamic => value can change at runtime
-Object => declaring a variable usign Object means you're no restricting it to a particular type. Disadvantage is losss in type safety, type casting and checking is you want to work the value in a type-specific manner
 */

main() {
  int amount1 = 100;
  var amount2 = 200;

  print('Amount 1: $amount1 | Amount 2: $amount2\n');

  // booleans are written in lowercase

  dynamic weakVariable = 100;
  weakVariable = 'Dart Programming';
  print(weakVariable);

  Object myVariable;
  myVariable = 'Hello';
  myVariable = 12.5;
  myVariable = true;

  // null safety
  // raises an error if acces to a non allowed null is attempted
  // declaring a nullable type
  String?
      name; // name can be null. However we can't access non initialized variables in dart

  // Late Variables
  /*
  Use cases
  * Declaring a non-nullable varibale that's initialized after declatation
  * Lazily initializing a variable
   */
  // If you're sure that a variable is set before it's used, but Dart disagrees, you can fix the error by marking the variable as late:

  late String
      description; // I we fail to initialize a late variable a runtime error occurs when the variable is used

  description = 'Ryoiki Tenkai';
  print(description);
  // Lazy initialization
  // if we initialize a variable during declaration having marked it as late, the initializer runs when the variable is first used

  // late String tepmperature = readThermomenter();
  // if the temperature variable is never used, then the expensive readThermometer() function is never called

  // Final and const
  // Used when we never intend to change the value of a variable
  // Instance variables(variables declared within a class) can be fincal but not const
  final age = 20;
  final int years = 20;

  /**
   Initialization Timing:

    final: Can be initialized later, but only once.
    const: Must be initialized at the time of declaration.

  Distinct Instances:
    final: Each instance is distinct, even if they have the same properties.
    const: Instances with the same properties share the same memory location.
   */
}
