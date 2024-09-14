class Foo {
  final String one;
  final int two;
  Foo({required this.one, required this.two});
}

String asciiCharType(int char) {
  const space = 32;
  const zero = 48;
  const nine = 57;

  return switch (char) {
    < space => 'control',
    == space => 'space',
    > space && < zero => 'punctuation',
    >= zero && <= nine => 'digit',
    _ => ''
  };
}

// Patters represents the shape of a set of values that it may match against actual values
// Patterns may match a value, destructure a value or both

// Destructing
void main() {
  var numList = [1, 2, 3];
  var [a, b, c] = numList;
  print(a + b + c);

  // Pattern use in varialble declaration
  var (d, [e, f]) = ('str', [1, 2]);
  print('$d, $e $f');

  // Logiacal patterns with switch expression
  var color = 'pink';
  var isPrimary = switch (color) {
    'red' || 'yellow' || 'blue' => true, // Logical-or pattern
    _ => false
  }; // Refutable pattern
  print(isPrimary);

  // variable assignment
  var (y, z) = ('left', 'right'); // Irrefutable pattern
  (z, y) = (y, z);
  print('$y $z');

  // Refutable patterns - patterns that can fail to match a value
  // Irrefutable patterns - patterns that will always succeed in matching a value

  // Guard clauses - evaluate an arbitrary condition as part of the case without exiting the switch if the else condition is false
  var pair = (12, 10);
  switch (pair) {
    // case (int a, int b):
    //   if (a > b) print('First element is greater');  => if the if is false, nothing will be printed and the switch will be exited
    case (int a, int b) when a > b: //guard clause  // Variable pattern check
      print('First element greater');
    case (int a, int b):
      print('First element not grater');
  }

  // For and for-in loops
  Map<String, int> hist = {
    'a': 100,
    'b': 23,
  };

  for (var MapEntry(key: key, value: count) in hist // Map pattern match
      .entries) //hist.entries: Returns an iterable of key-value pairs as MapEntry objects.
  {
    // MapEntry(key: key, value: count) is a destructuring pattern - it extracts the key and value for easier access in the loop.
    // the deconstructing pattern can also be written as (var MapEntry(:key, value : count)) because object patterns can infer the getter name for the variable subpattern (for same names)

    print('$key occured $count times');
  }

  //Destructing class instances
  final Foo myFoo = Foo(one: 'one', two: 2);
  var Foo(:one, :two) =
      myFoo; //destructuring to extract the values of the one and two fields from the myFoo instance.
  // The shorthand :one and :two automatically assigns the extracted values to local variables with the same names as the fields (one and two).
  print('one $one, two $two');

  // JSON validation - patterns are used for Json validation allowing us to write fewer lines of code

  // PATTERN TYPES
  // Paranthesized patterns - since patterns have different precedence, you can use the aforementioned to execute lower precedent patterns first
  /* 
    Pattern precedence
    *Logical-or < Logical-and < Relational
    *Post-fix unary patterns(cast, null-check, null-assert) => same precedence
    *Collection type and object type have highest precedence
   */

  // Relational patterns
  print(asciiCharType(a));

  // Cast pattern - allows you to cast a type to another type during destructing before assingning it to another subpattern
  (num, Object) record = (1, 's');
  var (i as int, s as String) = record;
  print('num: $i and string: $s');

  // Null check
  // String? maybeNull = 'This string may be null';
  String? maybeNull;
  switch (maybeNull) {
    case var p?: // Runs if the value of the variable being checked is not null
      print('maybeNull is not null');
      break;
    case null:
      print('maybeNull is null');
      break;
  }
  //   ? in pattern matching is used to exclude null values and only matched non null ones

  // Null-assert
  List<String?> row = ['user', 'Mwalimu'];
  switch (row) {
    case ['user', var name!]:
      print('username: $name');
      break;
    // if name is null, Error because of the null and the ! operator ensures that a non-null is used
  }
  // Eliminating null values from declaration patterns
  (int?, int?) position = (2, 3);
  var (m!, n!) = position;
  print(m + n);

  // Constant patterns - pattern check where a variable's value is checked to match a value

  // Paranthesizes patterns - pattern matching where the matching conditions are placed in parethesis

  // List pattern matching
  const g = 'a';
  const h = 'b';
  const obj = ['a', 'b'];
  switch (obj) {
    case [g, h]:
      print('$g, $h');
      break;
    default:
      print('Pattern match not found');
      break;
  }

  // Rest element - allows for pattern matching with lists of arbitrary lengths
  var [ha, he, ..., hi, ho] = [1, 2, 3, 4, 5, 6, 7, 8, 9];
  print('$ha, $he, $hi, $ho');

  var [la, le, ...li, lo, lu] = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9
  ]; //...li collects elements that don't match the other subpatterns in the list into a new list
  print('$la, $le, $li, $lo, $lu');

  // Record pattern matching
  var (myStr: foo, myNum: bar) = (myStr: 'string', myNum: 12);
  // Record patterns require that the pattern match the entire record. To destructure a record with named fields using a pattern, include the field names in the pattern
  //If the value isn't a record with the same shape as the pattern, the match fails.

  // Wildcard (_) variable or identifier pattern that doesn't bind or assign to any variable
  // Useful as a placeholder in places you need a subpattern in order to deconstruct later values
  var numbers = [1, 2, 3];
  var [_, second, _] = numbers;
  print(second);

  // wildcard with type annotation eg int _ is used to check a values type without binding it to a value
}
