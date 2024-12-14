import java.util.ArrayList;
import java.util.Arrays;
import java.util.stream.Collectors;

public class Rules {
    public static ArrayList<int[]> rules = new ArrayList<>();

    public static boolean IsCorrectSequence(boolean thowIfWrong, int... sequence) {
        ArrayList<Integer> sequenceList = new ArrayList<>(Arrays.stream(sequence).boxed().collect(Collectors.toList()));

        for (int i = 0; i < sequence.length - 1; i++) {
            ArrayList<Integer> rulesIdxs = findAllRulesWithElement(sequenceList.get(i));
            for (int j = i + 1; j < sequence.length; j++) {
                Integer n1 = sequenceList.get(i);
                Integer n2 = sequenceList.get(j);
                if (Conflicts(rulesIdxs, n1, n2)) {
                    if (thowIfWrong) {
                        throw new IllegalArgumentException(i + "," + j + " conflict with rules");
                    }
                    return false;
                }
            }
        }
        return true;
    }

    public static int[] CorrectSequence(int... sequence) {
        while (true) {
            int[] idxs = new int[2];
            try{
                if (IsCorrectSequence(true, sequence)) return sequence;
            } catch (IllegalArgumentException e){
                String[] splitMsg = e.getMessage().split(",");
                idxs[0] = Integer.parseInt(splitMsg[0]);
                idxs[1] = Integer.parseInt(splitMsg[1].split(" ")[0]);
            }
            swap(sequence, idxs[0], idxs[1]);
        }
    }

    private static void swap(int[] sequence, int n1, int n2) {
        int temp = sequence[n1];
        sequence[n1] = sequence[n2];
        sequence[n2] = temp;
    }

    private static boolean Conflicts(ArrayList<Integer> rulesIdxs, int n1, int n2) {
        for (int i = 0; i < rulesIdxs.size(); i++) {
            int[] rule = rules.get(rulesIdxs.get(i));
            if (rule[0] ==n2 && rule[1] == n1)
                return true;
        }
        return false;
    }


    private static ArrayList<Integer> findAllRulesWithElement(int n) {
        ArrayList<Integer> elements = new ArrayList<>();

        for (int i = 0; i < rules.size(); i++) {
            int[] rule = rules.get(i);
            for (int j = 0; j < rule.length; j++) {
                if (rule[j] == n)
                    elements.add(i);
            }
        }

        return elements;
    }
}
