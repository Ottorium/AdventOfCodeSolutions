package at.htlhl;

import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Comparator;

public class Main {
    public static void main(String[] args) throws IOException {
        var content = Files.readString(Paths.get("target/classes/input.txt"));
        var sum = 0;
        for (String line : content.split("\n")) {
            var chars = line.toCharArray();


            var largest_i = 0;
            var largest = 0;
            for (int i = 0; i < chars.length; i++) {
                if (Integer.parseInt("" + chars[i]) > largest
                        && i != chars.length - 1) {
                    largest_i = i;
                    largest = Integer.parseInt("" + chars[i]);
                }
            }

            var largest_j = Integer.parseInt("" + chars[largest_i + 1]);
            var largest2 = 0;
            for (int j = largest_i + 1; j < chars.length; j++) {
                if (Integer.parseInt("" + chars[j]) > largest2) {
                    largest_j = j;
                    largest2 = Integer.parseInt("" + chars[j]);
                }

            }


            var n = Integer.parseInt("" + chars[largest_i]) * 10 + Integer.parseInt("" + chars[largest_j]);
            System.out.println(line + " -> " + n);
            sum += n;
        }
        System.out.println(sum);
    }
}