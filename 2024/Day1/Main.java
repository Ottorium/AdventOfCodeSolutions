import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        String[] lines = readFileToStringArray("1.txt");
        int[] leftArr = new int[lines.length];
        int[] rightArr = new int[lines.length];
        for (int i = 0; i < lines.length; i++) {
            String line = lines[i];
            String[] tokens = line.split(" {3}");
            leftArr[i] = Integer.parseInt(tokens[0]);
            rightArr[i] = Integer.parseInt(tokens[1]);
        }
        Arrays.sort(leftArr);
        Arrays.sort(rightArr);

        assert leftArr.length == rightArr.length;
        ArrayList<Integer> leftList = new ArrayList<>();
        ArrayList<Integer> rightList = new ArrayList<>();
        for (int i = 0; i < leftArr.length; i++) {
            leftList.add(leftArr[i]);
            rightList.add(rightArr[i]);
        }
        var leftCopy =  new ArrayList<>(leftList);;
        var rightCopy = new ArrayList<>(rightList);;
        int sum = getSumOfDifferencesFirstStar(leftList, rightList);
        System.out.println("Part 1: " + sum);
        sum = getSimulatityScoreSecondStar(leftCopy, rightCopy);
        System.out.println("Part 2: " + sum);
    }

    private static int getSumOfDifferencesFirstStar(ArrayList<Integer> leftArr, ArrayList<Integer> rightArr) {
        int sum = 0;
        while (!leftArr.isEmpty() && !rightArr.isEmpty()) {
            int firtElementLeft = leftArr.getFirst();
            int firtElementRight = rightArr.getFirst();
            sum += Math.abs(firtElementLeft - firtElementRight);
            leftArr.removeFirst();
            rightArr.removeFirst();
        }
        return sum;
    }

    private static int getSimulatityScoreSecondStar(ArrayList<Integer> leftList, ArrayList<Integer> rightList) {
        int sum = 0;
        while (!leftList.isEmpty() && !rightList.isEmpty()) {
            int n = leftList.getFirst();
            int result = ElementCounter.countOccurrences(rightList, n);
            sum += result * n;
            leftList.removeFirst();
            for (int i = 0; i < result; i++) {
                rightList.removeFirst();
            }
        }
        return sum;
    }

    public static String[] readFileToStringArray(String filePath) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get(filePath));
        return lines.toArray(new String[0]);
    }
}