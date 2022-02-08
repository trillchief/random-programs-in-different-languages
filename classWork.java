import java.util.Scanner; //Imports the Scanner class
public class classWork {
    // defining method in which asks user for 2 numbers and calculates what the 
    // area
    // and perimeter would be
    public static double area_perimeter() {
        try (Scanner myObj = new Scanner(System.in)) {
            System.out.println("Please enter two numbers you would like used to calculate the area and perimeter of a rectangle: ");
            double width = myObj.nextDouble();
            double height = myObj.nextDouble();
            double calculate_area = width * height;
            double calculate_perimeter = 2 * width + 2 * height;
            System.out.println("Area: " + calculate_area);
            System.out.println("Perimeter: " + calculate_perimeter);
        } catch (Exception e) {
            System.out.println("You made an error, please run program again");
        }
        return 0;
    }
    // defining my main
    public static void main(String[] args) {
        // calling my previously created method
        area_perimeter();
    }
}
/*
 * Tyler Mears
 * Programming Assignment #1: Display Information
 * Due: Wed Jan 26, 2022 11:59pm
 * This program excepts to numbers provided by the user and then calculates the
 * area and perimeter for the user
 */