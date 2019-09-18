
public class Puppy {
    int puppyAge;

    public Puppy(String name){
        System.out.println(name);
    }
    
    public void setage(int age){
        puppyAge = age;
    }

    public int getAge(){
        System.out.println("Puppy age is:" +puppyAge);
        return puppyAge;
    }
    public static void main(String []args){
        Puppy myPuppy = new Puppy("Awesome");
        myPuppy.setage(2);
        myPuppy.getAge();
        System.out.println("Variable value:" +myPuppy.puppyAge);
    }
}