import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.InvalidParameterException;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static long register_A;
    static long register_B;
    static long register_C;
    static int[] program;
    static String programAsString;
    static int currentProgramIndex = 0;
    static String output = "";


    public static void main(String[] args) throws IOException {
        initializeProgram();
        executeProgram();
        System.out.println("Part 1: " + output);
    }

    private static void initializeProgram() throws IOException {
        List<String> lines = Files.readAllLines(Paths.get("17.txt"));
        register_A = Long.parseLong(lines.get(0).split(": ")[1]);
        register_B = Long.parseLong(lines.get(1).split(": ")[1]);
        register_C = Long.parseLong(lines.get(2).split(": ")[1]);
        programAsString = lines.get(4).split(": ")[1];
        ArrayList<Integer> p = new ArrayList<>();
        for(String s : programAsString.split(",")) p.add(Integer.parseInt(s));
        program = p.stream().mapToInt(i -> i).toArray();
        currentProgramIndex = 0;
        output = "";
    }

    private static void executeProgram() {
        while (currentProgramIndex < program.length) {
            long literalOrCombo = program[currentProgramIndex + 1];
            switch (program[currentProgramIndex]) {
                case 0:
                    adv(literalOrCombo);
                    break;
                case 1:
                    bxl(literalOrCombo);
                    break;
                case 2:
                    bst(literalOrCombo);
                    break;
                case 3:
                    jnz(literalOrCombo);
                    break;
                case 4:
                    bxc(literalOrCombo);
                    break;
                case 5:
                    out(literalOrCombo);
                    break;
                case 6:
                    bdv(literalOrCombo);
                    break;
                case 7:
                    cdv(literalOrCombo);
                    break;
            }

            currentProgramIndex += 2;
        }
    }

    private static long convertCombo(long combo) {
        if (combo == 4)
            combo = register_A;
        else if (combo == 5)
            combo = register_B;
        else if (combo == 6)
            combo = register_C;
        else if (combo >= 7 || combo < 0)
            throw new InvalidParameterException("invalid combo");
        return combo;
    }

    private static void adv(long combo) {
        combo = convertCombo(combo);
        register_A = (long) (register_A / Math.pow(2, combo));
    }

    private static void bxl(long literal) {
        register_B = register_B ^ literal;
    }

    private static void bst(long combo) {
        combo = convertCombo(combo);
        register_B = combo % 8;
    }

    private static void jnz(long literal) {
        if (register_A == 0) return;
        currentProgramIndex = (int) literal - 2; // -2 because the index is increased by 2 each step
    }

    private static void bxc(long literal) {
        register_B = register_B ^ register_C;
    }

    private static void out(long combo) {
        combo = convertCombo(combo);
        long r = combo % 8;
        if (!output.isEmpty()) output += ",";
        output += r;
    }

    private static void bdv(long combo) {
        combo = convertCombo(combo);
        register_B = (long) (register_A / Math.pow(2, combo));
    }

    private static void cdv(long combo) {
        combo = convertCombo(combo);
        register_C = (long) (register_A / Math.pow(2, combo));
    }

}