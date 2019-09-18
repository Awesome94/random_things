public class StringDemo{
    public static void main(String args[]){
        char [] mystring  = {'H', 'E', 'L', 'L', 'O'};
        String hiString = new String(mystring);
        System.out.println(hiString);

        String palindrome = "this is a string";
        int len =  palindrome.length();
        System.out.println("This is lenght of the palindrome:" +palindrome.concat(Integer.toString(len)));
        
        // Stringbuffer and stringbuilder.
        // StringBuilder is faster than StringBug
    }
}
