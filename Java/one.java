import java.util.Scanner;

class Shape {
    void draw() {
        System.out.println("Drawing a generic shape");
    }

    double calculateArea() {
        System.out.println("Calculating area of a generic shape");
        return 0.0;
    }
}

class Circle extends Shape {
    double radius;

    Circle(double radius) {
        this.radius = radius;
    }

    @Override
    void draw() {
        System.out.println("Drawing a circle with radius " + radius);
    }

    @Override
    double calculateArea() {
        System.out.println("Calculating area of a circle");
        return Math.PI * radius * radius;
    }
}

class Cylinder extends Circle {
    double height;

    Cylinder(double radius, double height) {
        super(radius);
        this.height = height;
    }

    @Override
    void draw() {
        System.out.println("Drawing a cylinder with radius " + radius + " and height " + height);
    }

    @Override
    double calculateArea() {
        System.out.println("Calculating total surface area of a cylinder");
        // The formula for the total surface area of a cylinder is 2πr^2 + 2πrh
        return 2 * super.calculateArea() + 2 * Math.PI * radius * height;
    }
}

public class one {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter the radius of the circle: ");
        double circleRadius = input.nextDouble();
        Circle circle = new Circle(circleRadius);

        System.out.print("Enter the radius of the cylinder: ");
        double cylinderRadius = input.nextDouble();
        System.out.print("Enter the height of the cylinder: ");
        double cylinderHeight = input.nextDouble();
        Cylinder cylinder = new Cylinder(cylinderRadius, cylinderHeight);

        
        circle.draw();
        System.out.println("Area of the circle: " + circle.calculateArea());

        
        cylinder.draw();
        System.out.println("Total surface area of the cylinder: " + cylinder.calculateArea());
    }
}
 
    
