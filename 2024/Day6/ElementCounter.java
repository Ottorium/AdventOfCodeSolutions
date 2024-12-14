import java.util.ArrayList;
import java.util.Collections;

public class ElementCounter {
    public static int countOccurrences(ArrayList<Integer> arr, int target) {
        int firstIndex = findFirstOccurrence(arr, target);

        if (firstIndex == -1) {
            return 0;
        }

        int lastIndex = findLastOccurrence(arr, target);

        return lastIndex - firstIndex + 1;
    }

    private static int findFirstOccurrence(ArrayList<Integer> arr, int target) {
        int left = 0;
        int right = arr.size() - 1;
        int result = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (arr.get(mid) == target) {
                result = mid;
                right = mid - 1;
            } else if (arr.get(mid) < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return result;
    }

    private static int findLastOccurrence(ArrayList<Integer> arr, int target) {
        int left = 0;
        int right = arr.size() - 1;
        int result = -1;

        while (left <= right) {
            int mid = left + (right - left) / 2;

            if (arr.get(mid) == target) {
                result = mid;
                left = mid + 1;
            } else if (arr.get(mid) < target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        return result;
    }
}