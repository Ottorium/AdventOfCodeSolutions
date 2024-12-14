public class Mover {
    public static boolean moveLeft(char[][] arr, char[] guard, char guardLetter) {
        char leftOfGuard = 0;
        try {
            leftOfGuard = arr[guard[0]][guard[1] - 1];
        } catch (IndexOutOfBoundsException e) {
            return false;
        }
        if (leftOfGuard == Main.OBSTACLE) {
            arr[guard[0]][guard[1]] = Main.GO_UP;
        } else {
            arr[guard[0]][guard[1]] = 'X';
            arr[guard[0]][guard[1] - 1] = guardLetter;
        }
        return true;
    }


    public static boolean moveDown(char[][] arr, char[] guard, char guardLetter) {
        char belowGuard = 0;
        try {
            belowGuard = arr[guard[0] + 1][guard[1]];
        } catch (IndexOutOfBoundsException e) {
            return false;
        }
        if (belowGuard == Main.OBSTACLE) {
            arr[guard[0]][guard[1]] = Main.GO_LEFT;
        } else {
            arr[guard[0]][guard[1]] = 'X';
            arr[guard[0] + 1][guard[1]] = guardLetter;
        }
        return true;
    }


    public static boolean moveRight(char[][] arr, char[] guard, char guardLetter) {
        char rightOfGuard = 0;
        try {
            rightOfGuard = arr[guard[0]][guard[1] + 1];
        } catch (IndexOutOfBoundsException e) {
            return false;
        }
        if (rightOfGuard == Main.OBSTACLE) {
            arr[guard[0]][guard[1]] = Main.GO_DOWN;
        } else {
            arr[guard[0]][guard[1]] = 'X';
            arr[guard[0]][guard[1] + 1] = guardLetter;
        }
        return true;
    }


    public static boolean moveUp(char[][] arr, char[] guard, char guardLetter) {
        char aboveGuard = 0;
        try {
            aboveGuard = arr[guard[0] - 1][guard[1]];
        } catch (IndexOutOfBoundsException e) {
            return false;
        }
        if (aboveGuard == Main.OBSTACLE) {
            arr[guard[0]][guard[1]] = Main.GO_RIGHT;
        }
        else {
            arr[guard[0]][guard[1]] = 'X';
            arr[guard[0] - 1][guard[1]] = guardLetter;
        }
        return true;
    }
}
