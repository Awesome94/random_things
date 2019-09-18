public class Random{
    public static void PrintNumbers(int n){
        for (int i=0; i<n; i++){
            System.out.println("this is I" +i);
        }
    }

    public static void PrintArray(String[] x){
        for(String i: x){
            System.out.println(i);
        }
    }
    public static void main(String[] args){
        String [] x = {"this", "is", "awesome"};
        PrintNumbers(9);
        PrintArray(x);

    }
};