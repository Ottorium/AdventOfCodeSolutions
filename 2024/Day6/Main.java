import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashSet;
import java.util.List;

public class Main {
    public static final char GO_UP = '^';
    public static final char GO_DOWN = 'v';
    public static final char GO_RIGHT = '>';
    public static final char GO_LEFT = '<';
    public static final char OBSTACLE = '#';

    public static void main(String[] args) throws IOException, InfiniteLoopException {
        final char[][] input = convertString(String.join("\n", readFileToStringArray("6.txt")));
        var cleanInput = cloneCharArray(input);
        int sum = 0;
        ArrayList<int[]> squaresVisited = new ArrayList<>();
        paintVisitedSquaresX(input);
        for (int i = 0; i < input.length; i++) {
            char[] x = input[i];
            for (int j = 0; j < x.length; j++) {
                char y = x[j];
                if (y == 'X') {
                    sum++;
                    squaresVisited.add(new int[]{i, j});
                }
            }
        }

        System.out.println("This will take a while ;)");
        System.out.println("Part 1:" + sum);
        Level2.run(cleanInput, squaresVisited);


    }

    public static void paintVisitedSquaresX(char[][] arr) throws InfiniteLoopException {
        HashSet<String> visitedStates = new HashSet<>();
        char[] guard;
        while (true) {
            guard = findGuard(arr);
            String state = Arrays.toString(guard);
            if (visitedStates.contains(state)) {
                throw new InfiniteLoopException("Infinite loop detected");
            }
            visitedStates.add(state);

            if (!makeMoveOrRotate(arr, guard))
                break;

            //writeDebug(arr);
        }
        arr[guard[0]][guard[1]] = 'X';
    }

    public static char[][] cloneCharArray(char[][] original) {
        char[][] clone = new char[original.length][];
        for (int i = 0; i < original.length; i++) {
            clone[i] = original[i].clone();
        }
        return clone;
    }

    private static void writeDebug(char[][] arr) throws IOException {
        StringBuilder s = new StringBuilder();
        for (char[] c : arr) {
            for (char cc : c) {
                s.append(cc);
            }
            s.append('\n');
        }
        String path = "DebugOutput.txt";

        try (BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(path))) {
            bufferedWriter.write(s.toString());
        }
    }

    private static boolean makeMoveOrRotate(char[][] arr, char[] guard) {
        char guardLetter = guard[2];

        if (guardLetter == GO_UP) {
            if (Mover.moveUp(arr, guard, guardLetter)) {
                //System.out.println("moved up");
                return true;
            }
            return false;
        } else if (guardLetter == GO_DOWN) {
            if (Mover.moveDown(arr, guard, guardLetter)) {
                //System.out.println("moved down");
                return true;
            }
            return false;
        } else if (guardLetter == GO_RIGHT) {
            if (Mover.moveRight(arr, guard, guardLetter)) {
                //System.out.println("moved right");
                return true;
            }
            return false;
        } else if (guardLetter == GO_LEFT) {
            if (Mover.moveLeft(arr, guard, guardLetter)) {
                //System.out.println("moved left");
                return true;
            }
            return false;
        }

        throw new IllegalArgumentException("Unknown guard letter");
    }


    private static char[] findGuard(char[][] arr) { //row, col, guard
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                if (arr[i][j] == GO_UP || arr[i][j] == GO_DOWN || arr[i][j] == GO_RIGHT || arr[i][j] == GO_LEFT)
                    return new char[]{(char) i, (char) j, arr[i][j]};
            }
        }
        throw new IllegalArgumentException("No guard found");
    }

    public static char[][] convertString(String input) {
        String[] rows = input.split("\n");
        char[][] result = new char[rows.length][];
        for (int i = 0; i < rows.length; i++) {
            result[i] = rows[i].toCharArray();
        }
        return result;
    }

    public static String[] readFileToStringArray(String filePath) throws IOException {
        List<String> lines = Files.readAllLines(Paths.get(filePath));
        return lines.toArray(new String[0]);
    }
}