import java.util.*;
class tcs_vehical
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the number of vihecle:");
        int v=sc.nextInt();
        System.out.println("enter the wheels:");
        int w=sc.nextInt();
        int arr[]=carAndmot(v, w);
        for(int i=0;i<arr.length;i++)
        {
            System.out.println("number of car and vehicle is:"+arr[i]);
        }
    }
    public static int[] carAndmot(int v,int w)
    {
        int arr[]=new int[2];
        int y=(w/2)-v;
        int x=v-y;
        arr[0]=x;
        arr[1]=y;

        return arr;
    }
}