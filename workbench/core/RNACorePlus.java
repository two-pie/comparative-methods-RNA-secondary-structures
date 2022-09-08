package it.unicam.cs.hierro.corecalculator;

import java.util.*;
import java.util.stream.Collectors;

public class RNACorePlus {

    private final String corePlus;

    public RNACorePlus(String brackets) {
        this.corePlus = createCore(brackets);
    }


    public String getCorePlus() {
        return this.corePlus;
    }

    private String createCore(String brackets) {
        // create bonds from the brackets
        var bonds = getBonds(brackets);
        // collapse all parallel bonds
        var collapsedBonds = new ArrayList<Pair<Integer, Integer>>();
        for (int i = 0; i < bonds.size(); i++)
            if (i == 0 || !this.isParallel(bonds.get(i), bonds.get(i - 1)))
                collapsedBonds.add(bonds.get(i));
        // create a string from the collapsed bonds
        var core = "0".repeat(brackets.length()).toCharArray();
        for (var b : collapsedBonds) {
            core[b.first()] = brackets.charAt(b.first());
            core[b.second()] = brackets.charAt(b.second());
        }
        return new String(core).replaceAll("0", "");
    }

    private boolean isParallel(Pair<Integer, Integer> pair1, Pair<Integer, Integer> pair2) {
        return pair1.first().equals(pair2.first() - 1) && pair1.second().equals(pair2.second() + 1);
    }

    //
    private List<Pair<Integer, Integer>> getBonds(String brackets) {
        // initialize variables
        var bonds = new ArrayList<Pair<Integer, Integer>>();
        var stack = new LinkedList<Integer>();
        // iterate over brackets
        for (int right = 0; right < brackets.length(); right++) {
            var c = brackets.charAt(right);
            if (isOpenedBracket(c))
                stack.add(right);
            if (isClosedBracket(c)){
                var left = findPairIndex(brackets,stack,c);
                bonds.add(new Pair<>(left,right));
            }
        }
        bonds.sort(Comparator.comparingInt(Pair::second));
        return bonds;
    }

    private boolean isOpenedBracket(char c) {
        return c == '<' || c == '(' || c == '{' || c == '[' || (Character.isLetter(c) && Character.isUpperCase(c));
    }

    private boolean isClosedBracket(char c) {
        return c == '>' || c == ')' || c == '}' || c == ']' || (Character.isLetter(c) && Character.isLowerCase(c));
    }

    private int findPairIndex(String brackets ,List<Integer> stack, char closedBracket){
        var openedBracket = getOpenedBracket(closedBracket);
        var tmpList = new LinkedList<>(stack);
        while (!tmpList.isEmpty()){
            var popIndex = tmpList.removeLast();
            var bracketToMatch = brackets.charAt(popIndex);
            if (openedBracket == bracketToMatch){
                stack.remove(popIndex);
                return popIndex;
            }
        }
        throw new IllegalArgumentException("There is not an opened bracket for: "+closedBracket);
    }

    private char getOpenedBracket(char c) {
        return switch (c) {
            case '>' -> '<';
            case ')' -> '(';
            case '}' -> '{';
            case ']' -> '[';
            default -> Character.toUpperCase(c);
        };
    }

}