package at.htlhl;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;

public class Part2 {
    private static int i = 0;

    public static void main(String[] args) throws IOException {
        var content = Files.readString(Paths.get("target/classes/input.txt"));
        long sum = 0;
        for (String line : content.split("\n")) {
            var chars = line.toCharArray();

            i = 0;
            long _1 = getLargest(chars, 1) * 100000000000L;
            long _2 = getLargest(chars, 2) * 10000000000L;
            long _3 = getLargest(chars, 3) * 1000000000L;
            long _4 = getLargest(chars, 4) * 100000000L;
            long _5 = getLargest(chars, 5) * 10000000L;
            long _6 = getLargest(chars, 6) * 1000000L;
            long _7 = getLargest(chars, 7) * 100000L;
            long _8 = getLargest(chars, 8) * 10000L;
            long _9 = getLargest(chars, 9) * 1000L;
            long _10 = getLargest(chars, 10) * 100L;
            long _11 = getLargest(chars, 11) * 10L;
            long _12 = getLargest(chars, 12);

            var n = _1 + _2 + _3 + _4 + _5 + _6 + _7 + _8 + _9 + _10 + _11 + _12;
            sum = Math.addExact(sum, n);
        }
        System.out.println(sum);
    }

    private static int getLargest(char[] chars, int elementN) {
        var largest_j = Integer.parseInt("" + chars[i]);
        var largest = 0;
        for (int j = i; j < chars.length; j++) {
            if (Integer.parseInt("" + chars[j]) > largest) {
                if (j >= chars.length - 12 + elementN) continue;
                largest_j = j;
                largest = Integer.parseInt("" + chars[j]);
            }
        }
        i = largest_j + 1;
        return largest;
    }
}
