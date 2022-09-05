package it.unicam.cs.bsdlab.aspralign;

import java.util.*;
import java.util.stream.Collectors;

public class RNACore1 {

    private final RNASecondaryStructure secondaryStructure;
    private final List<WeakBond> core;

    public RNACore1(RNASecondaryStructure secondaryStructure) {
        this.secondaryStructure = Objects.requireNonNull(secondaryStructure);
        this.core = new ArrayList<>();
        this.createCore();
    }

    private void createCore() {
        var bonds = secondaryStructure.getBonds();
        for (int i = 0; i < bonds.size(); i++)
            if (i == 0 || !this.isParallel(bonds.get(i), bonds.get(i - 1)))
                this.core.add(bonds.get(i));
    }

    private boolean isParallel(WeakBond wb1, WeakBond wb2) {
        return wb1.getLeft() + 1 == wb2.getLeft() && wb1.getRight() - 1 == wb2.getRight();
    }

    public RNASecondaryStructure getSecondaryStructure() {
        return this.secondaryStructure;
    }

    public List<WeakBond> getCore() {
        return this.core;
    }

    public String getBrackets() {
        SortedMap<Integer, Character> left = new TreeMap<>();
        this.core.forEach(b -> left.put(b.getLeft(), '('));
        SortedMap<Integer, Character> right = new TreeMap<>();
        this.core.forEach(b -> right.put(b.getRight(), ')'));
        SortedMap<Integer, Character> all = new TreeMap<>();
        all.putAll(left);
        all.putAll(right);
        StringBuilder sb = new StringBuilder();
        all.values().forEach(sb::append);
        return sb.toString();
    }

}