import 'dart:io';

main() {
  stdout.writeln('What is your name?'); //line displayed in the terminal 
  var name = stdin.readLineSync(); // Line that waits for user input
  print('My name is $name');  //string interpolation
}


// inline comment
/*
Block comment
 */
///Documentation