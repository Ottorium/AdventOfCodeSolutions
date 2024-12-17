public class Level2Personalized {
    public static void main(String[] args) {
        String progString = "2,4,1,5,7,5,1,6,4,3,5,5,0,3,3,0";

        //16: 3
        //15: 24., 25, 29, 31
        //14: 195., 197
        //13: 1563.
        //12: 12504.
        //11: 100036., 100038., 100039
        //10: 800317.,800319
        //9: 6402536.,6402537
        //8: 51220289
        //7: 409762316
        //6: 3278098532,3278098535
        //5: 26224788258
        //4: 209798306068
        //3: 1678386448550
        //2: 13427091588403

        long original = 47792830;
        long min = 8L * 13427091588403L;
        long max = min + 7;
        for (long val = min; val <= max; val++) {
            long a = val;
            long b = 0;
            long c = 0;
            String out = "";
            while (a != 0) {
                b = a % 8 ^ 0b101;
                c = (long) (a / Math.pow(2, b));
                b = b ^ c ^ 0b110;
                out += "," + (b % 8);
                a = a / 8;
            }
            out = out.substring(1);
            if (out.equals(progString)) {
                System.out.println("yay:" + val);
            }
            if (progString.endsWith(out)) System.out.print(val + ",");
        }
    }
}
