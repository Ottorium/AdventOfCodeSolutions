import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        String[] lines = readFileToStringArray("2.txt");

        int sum = 0;
        int sumPart1 = 0;
        for (String line : lines) {
            ArrayList<Integer> intList = convertToIntList(line.split(" "));
            writeAppend("DebugOutput.txt", Arrays.toString(intList.toArray()));
            if (isSafe(intList)) {
                sumPart1++;
                sum++;
                writeAppend("DebugOutput.txt", " : true\n");
            }
            else {
                for (int i = 0; i < intList.size(); i++) {
                    ArrayList<Integer> copy = new ArrayList<>(intList);
                    copy.remove(i);
                    if (isSafe(copy)) {
                        sum++;
                        break;
                    }
                }
            }
        }
        System.out.println("Part 1: " + sumPart1);
        System.out.println("Part 2: " + sum);
    }

    private static boolean isSafe(ArrayList<Integer> intList) {
        final boolean isPlus = Math.abs(intList.get(1) - intList.get(0)) == intList.get(1) - intList.get(0);
        for (int i = 0; i < intList.size() - 1; i++) {
            int diff = intList.get(i + 1) - intList.get(i);

            if (diff == 0) {
                //intList.remove(i + 1);
                return false;
            }

            if (diff > 0 && !isPlus || (diff < 0 && isPlus)) {
                //intList.remove(i + 1);
                return false;
            }
            if (Math.abs(diff) > 3) {
                //intList.remove(i + 1);
                return false;
            }
        }
        return true;
    }

    private static void writeAppend(String path, String content) throws IOException {
        try (BufferedWriter writer = new BufferedWriter(new FileWriter(path, true))) {
            writer.write(content);
        }
    }

    private static ArrayList<Integer> convertToIntList(String[] strArr) {
        ArrayList<Integer> intList = new ArrayList<>();
        for (String str : strArr) {
            intList.add(Integer.parseInt(str));
        }
        return intList;
    }


    private static int[] convertToIntArr(String[] arr) {
        int[] intArr = new int[arr.length];
        for (int i = 0; i < arr.length; i++) {
            intArr[i] = Integer.parseInt(arr[i]);
        }
        return intArr;
    }

    public static String[] readFileToStringArray(String filePath) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get(filePath));
        return lines.toArray(new String[0]);
    }
}