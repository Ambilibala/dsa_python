import java.io.*;
import java.util.Scanner;

class sum{
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);

        int a, b;
        System.out.println("Enter the numbers");
        a = s.nextInt();
        b = s.nextInt();
        void sum(int a,int b){
            int sum;
            sum = a + b;
            System.out.println(sum);}

        sum s1 = new sum();
        s1.sum(a, b);
    }
}