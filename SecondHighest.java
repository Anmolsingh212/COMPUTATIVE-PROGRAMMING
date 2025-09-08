 import java.util.Scanner;

public class SecondHighest {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Input three numbers
        System.out.print("Enter first number: ");
        int a = scanner.nextInt();

        System.out.print("Enter second number: ");
        int b = scanner.nextInt();

        System.out.print("Enter third number: ");
        int c = scanner.nextInt();

        int second;

        // Logic to find second highest
        if ((a > b && a < c) || (a > c && a < b)) {
            second = a;
        } else if ((b > a && b < c) || (b > c && b < a)) {
            second = b;
        } else {
            second = c;
        }

        System.out.println("Second highest number is: " + second);
        scanner.close();
    }
}
