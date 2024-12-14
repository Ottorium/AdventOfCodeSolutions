import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        final String[] file = readFileToStringArray("5.txt");
        int sum = 0;
        int wrongSum = 0;
        ArrayList<String> correctSequences = new ArrayList<>();
        for (String line : file) {
            if (line.contains("|")){
                String[] arr = line.split("\\|");
                int n1 = Integer.parseInt(arr[0]);
                int n2 = Integer.parseInt(arr[1]);
                Rules.rules.add(new int[]{n1, n2});
            }
            else {
                String[] arr = line.split(",");
                if (arr.length < 3) {
                    continue;
                }

                int[] narr = new int[arr.length];
                for (int i = 0; i < arr.length; i++) {
                    narr[i] = Integer.parseInt(arr[i]);
                }


                if (Rules.IsCorrectSequence(false, narr)){
                    correctSequences.add(line);
                    sum += narr[narr.length / 2];
                }
                else {
                    int[] corrected = Rules.CorrectSequence(narr);
                    wrongSum += corrected[corrected.length / 2];
                }
            }
        }
        System.out.println("Part 1:" + sum);
        System.out.println("Part 2:" + wrongSum);
    }

    public static String[] readFileToStringArray(String filePath) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get(filePath));
        return lines.toArray(new String[0]);
    }
}