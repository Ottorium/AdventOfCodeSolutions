import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;

public class Main {
    public static void main(String[] args) throws IOException {
        final char[][] input = convertString(String.join("\n", readFileToStringArray("4.txt")));
        ArrayList<int[]> xs = findXs(input);
        int sum = 0;
        for (int[] x : xs) {
            sum += Searcher.searchHorizontal(input, x);
            sum += Searcher.searchVertical(input, x);
            sum += Searcher.searchDiagonal(input, x);

        }
        System.out.println("Part 1: " + sum);

        ArrayList<int[]> as = findAs(input);
        sum = 0;
        for (int[] a : as) {
            sum += Searcher.checkA(input, a);
        }

        System.out.println("Part 2: " + sum);
    }

    public static char[][] convertString(String input) {
        String[] rows = input.split("\n");
        char[][] result = new char[rows.length][];
        for (int i = 0; i < rows.length; i++) {
            result[i] = rows[i].toCharArray();
        }
        return result;
    }

    public static ArrayList<int[]> findAs(char[][] input) {
        ArrayList<int[]> xCoordinates = new ArrayList<>();

        for (int row = 0; row < input.length; row++) {
            for (int col = 0; col < input[row].length; col++) {
                if (input[row][col] == 'A') {
                    xCoordinates.add(new int[]{row, col});
                }
            }
        }

        return xCoordinates;
    }
    public static ArrayList<int[]> findXs(char[][] input) {
        ArrayList<int[]> xCoordinates = new ArrayList<>();

        for (int row = 0; row < input.length; row++) {
            for (int col = 0; col < input[row].length; col++) {
                if (input[row][col] == 'X') {
                    xCoordinates.add(new int[]{row, col});
                }
            }
        }

        return xCoordinates;
    }

    public static String[] readFileToStringArray(String filePath) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get(filePath));
        return lines.toArray(new String[0]);
    }
}