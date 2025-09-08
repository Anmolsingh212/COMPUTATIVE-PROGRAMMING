import java.util.Scanner;

class Divide {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

       System.out.println("enter  value of n:");
        int n = sc.nextInt();

        if (n % 10 == 4)
            System.out.println("Yes");
        else
            System.out.println("No");

    }
}
