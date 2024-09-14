// typedefs(type definitons) are used to define a new name/alias of a type

typedef IntList = List<int>;
IntList integerList = [1, 2, 3];

// typedef with parameters
typedef ListMapper<X> = Map<X, List<X>>;
ListMapper<String> m2 = {};
Map<String, List<String>> m1 = {};
// m1 and m2 above are of the same type

// Dart Type System
void printsInts(List<int> a) => print(a);

class Animal {
  void makeSound(Animal animal) {
    print('Animal makes a sound');
  }
}

class Dog extends Animal {
  @override
  void makeSound(Animal animal) {
    //can also be (Object animal) - must be a the same type or a supertype of the parent method
    print('Dog barks');
  }
}

void main() {
  final list = <int>[];
  // if I don't explicitly specify list = <int>[] above, the following error will be thrown: The argument type 'List<dynamic>' can't be assigned to the parameter type 'List<int>'.
  // the initializing declaration without specifying <int> does not provide the analyzer with enough info hence list will be assigned to dynamic
  list.add(1);
  list.add(2);
  // Now if I attemt to annotate any other data type to the list, the following error is thrown: The argument type 'data_type' can't be assigned to the parameter type 'int'.
  printsInts(list);

  // The analyser can infer types except for when it does not have enough information. In this case it infers dynamic.

  // In type substitution, you can replace a consumer's type with a supertype and a producer's type with a subtype.
  /*
   Animal
   Cat
   Lion*/
  // In the above heirarchy, we may have Animal c = Cat(); but we can't have Lion c = Cat();
  // x c - consumer
  // Cat() - producer
}
