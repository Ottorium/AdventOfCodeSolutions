import java.io.IOException;
import java.util.ArrayList;

public class Level2 {
    public static void run(char[][] inputArr, ArrayList<int[]> squaresVisited) throws IOException {
        int sum = 0;
        for (int i = 0; i < squaresVisited.size(); i++) {
            int[] square = squaresVisited.get(i);
            if (inputArr[square[0]][square[1]] == Main.GO_UP || inputArr[square[0]][square[1]] == Main.GO_DOWN || inputArr[square[0]][square[1]] == Main.GO_LEFT || inputArr[square[0]][square[1]] == Main.GO_RIGHT) {
                continue;
            }
            var temp = Main.cloneCharArray(inputArr);

            inputArr[square[0]][square[1]] = '#';
            try {
                Main.paintVisitedSquaresX(inputArr);
            } catch (InfiniteLoopException e) {
                //System.out.println("progress:" + i + " out of " + squaresVisited.size());
                sum++;
            }
            inputArr = temp;
        }
        System.out.println("Part 2:" + sum);
    }
}
