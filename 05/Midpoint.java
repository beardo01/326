import java.util.Random;

strictfp class Midpoint {
    public static void main(String[] args) {
        final Random r = new Random();
        for (int i = 0; i < 1000000; i++) {
            int x = r.nextInt();
            assert midPoint(x, x) == x;
            assert midPoint(x, -x) == 0;
            assert midPoint(x, 0) == x/2;
            int y = r.nextInt();
            assert midPoint(x, y) == midPoint(y, x);
            assert midPoint(x, y) >= Math.min(x, y);
            assert midPoint(x, y) <= Math.max(x, y);
        }
    }
    
    private static int midPoint(int x, int y) {
        if(x == y) {
            return x;
        } else if (x == (y - y*2) || y == (x - x*2)) {
            return 0;
        } else if (x == 0) {
            return y/2;
        } else if(y == 0) {
            return x/2;
        } else {
            int low = Math.min(x, y);
            int high = Math.max(x, y);
            int mid;
            if(low <= 0) {
                if (high < 0) {
                    mid = (Math.abs(high) + low)/2 - Math.abs(high);
                } else {
                    mid = (low + high)/2;
                }
            } else {
                mid = low + (high - low)/2;
            }
            return mid;
        }
    }
}
