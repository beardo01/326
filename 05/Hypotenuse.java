strictfp class Hypotenuse {
    public static void main(String[] args) {
        float x = 3.0f;
        float y = 4.0f;
        float z = 5.0f;
        
        for(int i = 0; i < 25; i++) {
            float e = Math.abs(hyp(x, y) - z)/z;
            System.out.println(i + " " + e);
            x /= 10.0f;
            y /= 10.0f;
            z /= 10.0f;
        }
    }
    
    public static float hyp(float x, float y) {
        float a = Math.abs(x);
        float b = Math.abs(y); 
        if (a > b) {
            b = b/a;
            return (float) Math.sqrt(1.0f + b*b)*a; 
        } else if (a < b) { 
            a = a/b;
            return (float) Math.sqrt(1.0f + a*a)*b;
        } else { 
            return (float) Math.sqrt(2.0f)*a; 
        }
    }
}
