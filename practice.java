import java.io.PrintStream;

public class practice {

    public static void main(String[] args) {

        mymethod("hot dogs"); // calls my method

        mysecondmethod(""); // calling my method
        System.out.println(mysecondmethod("my dog")); // printing my method

        Animal a = new Animal(); // making an object
        String dog = a.iamdog();
        System.out.println(dog); //

        String doit = System.input.println("Enter name"); //

        PrintStream System.doit.println("Enter your name");
        

    }

    private static String mysecondmethod(String string2) {
        return string2 + "!"; // what this method returns
    }

    private static void mymethod(String string) { // creating my mymethod
        System.out.println(string + "!"); // defining what my method does - it takes a string and adds an exclamation mark to the end
    }



}
