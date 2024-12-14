import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        String input = String.join("\n", readFileToStringArray("3.txt"));
        for (int i = 1; i <= 2; i++) {
            if (i == 2)
                input = trimDonts(input);
            var statements = input.split("mul\\(");
            int sum = 0;
            for (var statement : statements) {
                int n1;
                int n2;
                try {
                    String n = statement.split("\\)")[0];
                    String[] nums = n.split(",");
                    if (nums.length != 2) {
                        continue;
                    }
                    n1 = Integer.parseInt(nums[0]);
                    n2 = Integer.parseInt(nums[1]);
                } catch (Exception e) {
                    continue;
                }
                sum += n1 * n2;
            }
            System.out.println("Part " + i + ": " + sum);
        }
    }

    private static String trimDonts(String input) {
        while(true){
            int startCutout = input.indexOf("don't()");
            if(startCutout == -1){
                break;
            }
            int endCutout = input.indexOf("do()");
            if(endCutout == -1){
                endCutout = Integer.MAX_VALUE;
            }
            if (startCutout > endCutout) {
                input = cutOut(input, endCutout, endCutout + 3);
                continue;
            }
            input = cutOut(input, startCutout, endCutout);
        }
        return input;
    }

    private static String cutOut(String input, int startCutout, int endCutout) {
        if (input == null) {
            return null;
        }
        endCutout = Math.min(endCutout, input.length() - 1);
        if (startCutout < 0 || endCutout < 0 || startCutout > endCutout) {
            throw new IllegalArgumentException("invalid input cutout");
        }
        return input.substring(0, startCutout) + input.substring(endCutout + 1);
    }

    public static String[] readFileToStringArray(String filePath) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get(filePath));
        return lines.toArray(new String[0]);
    }
}