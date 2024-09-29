import java.util.*;
class bintodec{
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the number:");
        int n=sc.nextInt();
    //     System.out.println(bintodec1(n));

    // }
    // public static int bintodec1(int num)
    // {
    //     int pow=0;
    //     int dec=0;
    //     while(num>0)
    //     {
    //         int dig=num%10;
    //         dec+=(dig*(Math.pow(2,pow)));
    //         pow++;
    //         num=num/10;

    //     }
    //     return dec;
    // }
        int arr[]=new int[n];
        for(int i=0;i<n;i++)
        {
            arr[i]=sc.nextInt();
        }
        System.out.println(equilibirium(arr, n));

    }
    public static int equilibirium(int arr[],int n)
    {
        for(int i=0;i<n;i++)
        {
            int leftsum=0;
            for(int j=0;j<i;j++)
            {
                leftsum+=arr[j];
            }
            int rightsum=0;
            for(int j=i+1;j<n;j++)
            {
                rightsum+=arr[j];
            }
            if(leftsum==rightsum)
            {
                return arr[i];
            }
        }
        return -1;
    }
}