// allows you to create classes, methods, and functions that can work with different types while ensuring type safety.
class Box<T> {
  T value;

  Box(this.value);

  void show() {
    print(value);
  }
}

T getFirst<T>(List<T> items) {
  return items[0];
}

void main() {
  var intBox = Box<int>(10);
  intBox.show();

  var stringBox = Box<String>('Mwalimu');
  stringBox.show();

  var items = ['A', 'B', 'C'];
  print(getFirst(items));

  var nums = [1, 2, 3];
  print(getFirst(nums));
}
