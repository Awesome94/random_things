import java.util.Arrays;

public class MyClass {
    public static void main(String args[]) {
      int x=10;
      int y=25;
      int z=x+y;
      
      int[] a = {1,3,2,4, 4};
      hasSingleMaximum(a);
      chunkArray(a, 2);
    }
    
    static int hasSingleMaximum(int[] a) {
        Arrays.sort(a);
        int max = a[a.length-1];

        int count = 0;
        for (int i=0; i<a.length; i++) {
            if (a[i] == max) {
                count++;
            }
        }
        
        return count == 1 ?  1 : 0;
    }

public static int[][] chunkArray(int[] array, int chunkSize) {
    int numOfChunks = (int)Math.ceil((double)array.length / chunkSize);
    int[][] output = new int[numOfChunks][];

    for(int i = 0; i < numOfChunks; ++i) {
        int start = i * chunkSize;
        int length = Math.min(array.length - start, chunkSize);

        int[] temp = new int[length];
        System.arraycopy(array, start, temp, 0, length);
        output[i] = temp;
    }
    System.out.print(output.toString());
    return output;
    }
}