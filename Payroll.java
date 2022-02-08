import java.util.Scanner;

/**
 * Tyler Mears
 * 2/2/2022
 * Programming Assignment #3: Caclulate Payroll
 * The program Calculate Payroll will request information from the user
 * And then calculate payrate weekly
 */
public class Payroll {
   public static void main(String[] args) {
      String name;
      int hours;
      double rate;
      double fedTax;
      double stateTax;

      try (Scanner input = new Scanner(System.in)) {
         System.out.print("Enter employee name: "); // obtaining user name
         name = input.next();

         System.out.print("Enter number of hours worked in a week: "); // obtaining hours worked
         hours = input.nextInt();

         System.out.print("Enter hourly pay rate: "); // pay rate
         rate = input.nextDouble();

         System.out.print("Enter federal tax withholding rate: "); // federal tax
         fedTax = input.nextDouble();

         System.out.print("Enter state tax withholding rate: "); // state tax
         stateTax = input.nextDouble();
      }

      double grossPay;
      grossPay = rate * hours;

      double fedwithHolding;
      fedwithHolding = (fedTax / 100) * grossPay;

      double statewithHolding;
      statewithHolding = (stateTax / 100) * grossPay;

      double deduction;
      deduction = fedwithHolding + statewithHolding;

      double netPay;
      netPay = (grossPay) - deduction;

      System.out.println("The grosspay is $" + grossPay);
      System.out.println("The netpay is $" + netPay);
      System.out.println("Employee's name: " + name);// Employee's name (e.g., Smith)
      System.out.println("Number of hours worked in a week: " + hours);
      System.out.println("Hourly pay rate: $" + rate);
      System.out.println("Federal tax withholding rate: " + fedTax + "%");
      System.out.println("State tax withholding rate: " + stateTax + "%");
   }
}