public class Searcher {

    public static int searchHorizontal(char[][] input, int[] x) {
        return searchHorizontalRight(input, x) + searchHorizontalLeft(input, x);
    }

    public static int searchVertical(char[][] input, int[] x) {
        return searchVerticalUp(input, x) + searchVerticalDown(input, x);
    }

    public static int searchDiagonal(char[][] input, int[] x) {
        return searchDiagonalUpRight(input, x) + searchDiagonalDownRight(input, x) + searchDiagonalDownLeft(input, x) + searchDiagonalUpLeft(input, x);
    }


    private static int searchHorizontalLeft(char[][] input, int[] x) {
        try {
            if (input[x[0]][x[1] - 1] == 'M'
                    && input[x[0]][x[1] - 2] == 'A'
                    && input[x[0]][x[1] - 3] == 'S'
            )
                return 1;
        } catch (Exception e) {
            return 0;
        }
        return 0;
    }

    private static int searchHorizontalRight(char[][] input, int[] x) {
        try {
            if (input[x[0]][x[1] + 1] == 'M'
                    && input[x[0]][x[1] + 2] == 'A'
                    && input[x[0]][x[1] + 3] == 'S'
            )
                return 1;
        } catch (Exception e) {
            return 0;
        }
        return 0;
    }

    private static int searchVerticalDown(char[][] input, int[] x) {
        try {
            if (input[x[0] + 1][x[1]] == 'M'
                    && input[x[0] + 2][x[1]] == 'A'
                    && input[x[0] + 3][x[1]] == 'S'
            )
                return 1;
        } catch (Exception e) {
            return 0;
        }
        return 0;
    }

    private static int searchVerticalUp(char[][] input, int[] x) {
        try {
            if (input[x[0] - 1][x[1]] == 'M'
                    && input[x[0] - 2][x[1]] == 'A'
                    && input[x[0] - 3][x[1]] == 'S'
            )
                return 1;
        } catch (Exception e) {
            return 0;
        }
        return 0;
    }

    private static int searchDiagonalUpLeft(char[][] input, int[] x) {
        try {
            if (input[x[0] - 1][x[1] - 1] == 'M'
                    && input[x[0] - 2][x[1] - 2] == 'A'
                    && input[x[0] - 3][x[1] - 3] == 'S'
            )
                return 1;
        } catch (Exception e) {
            return 0;
        }
        return 0;
    }

    private static int searchDiagonalDownLeft(char[][] input, int[] x) {
        try {
            if (input[x[0] + 1][x[1] - 1] == 'M'
                    && input[x[0] + 2][x[1] - 2] == 'A'
                    && input[x[0] + 3][x[1] - 3] == 'S'
            )
                return 1;
        } catch (Exception e) {
            return 0;
        }
        return 0;
    }

    private static int searchDiagonalDownRight(char[][] input, int[] x) {
        try {
            if (input[x[0] + 1][x[1] + 1] == 'M'
                    && input[x[0] + 2][x[1] + 2] == 'A'
                    && input[x[0] + 3][x[1] + 3] == 'S'
            )
                return 1;
        } catch (Exception e) {
            return 0;
        }
        return 0;
    }

    private static int searchDiagonalUpRight(char[][] input, int[] x) {
        try {
            if (input[x[0] - 1][x[1] + 1] == 'M'
                    && input[x[0] - 2][x[1] + 2] == 'A'
                    && input[x[0] - 3][x[1] + 3] == 'S'
            )
                return 1;
        } catch (Exception e) {
            return 0;
        }
        return 0;
    }

    public static int checkA(char[][] input, int[] a) {
        if (a[0] == 0 || a[1] == 0 || a[0] == input.length - 1 || a[1] == input[0].length - 1)
            return 0;
        int sum = 0;
        if (isMasRightDown(input, a) && isMasRightUp(input, a))
            sum++;
        return sum;
    }

    private static boolean isMasRightUp(char[][] input, int[] a) {
        if (input[a[0] - 1][a[1] + 1] == 'M') {
            if (input[a[0] + 1][a[1] - 1] == 'S')
                return true;
        }
        if (input[a[0] - 1][a[1] + 1] == 'S') {
            if (input[a[0] + 1][a[1] - 1] == 'M')
                return true;
        }
        return false;
    }

    private static boolean isMasRightDown(char[][] input, int[] a) {
        if (input[a[0] - 1][a[1] - 1] == 'M') {
            if (input[a[0] + 1][a[1] + 1] == 'S')
                return true;
        }
        if (input[a[0] - 1][a[1] - 1] == 'S') {
            if (input[a[0] + 1][a[1] + 1] == 'M')
                return true;
        }
        return false;
    }
}
