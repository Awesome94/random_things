public class Test{

    public static void main(String args[]) {
        int [] numbers = {1, 3, 4, 5, 6 };
        for(int number: numbers){
            System.out.println(Integer.toString(number));
            System.out.println(",");
        }
        System.out.println("\n");
        String [] names = {"james", "peter", "Leonard"};
        for(String name: names){
            System.out.println(name);
            System.out.println(",");
        }
    }
}