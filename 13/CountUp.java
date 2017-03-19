/**
* The inspiration to use pascals triangle with binomial coefficient equation of 
* addition can be found here: https://goo.gl/AdxH9m
*
* Thomas Youngson - 7444007
* Oliver Reid - 2569385
*/

/**
* Makes pascals triangles which are made from the addition of the two previous
* numbers. The triangles are stored in double arrays of each row holding every 
* column of the triangle.
*/
public class CountUp {
    public static void main(String [] args) {
        int n = Integer.parseInt(args[0]);
        int k = Integer.parseInt(args[1]);
        
        long [][] pascal = new long[n+1][];
        
        /** Stores each pascal triangle */
        for (int i=0; i < pascal.length; i++){
            pascal[i] = new long[i+1];
            pascal[i][0] = 1;
            pascal[i][i] = 1;
            for (int j=1; j<i; j++) {
                pascal[i][j] = pascal[i-1][j]+pascal[i-1][j-1];
            }
        }
        System.out.println(pascal[n][k]);
    }
}
