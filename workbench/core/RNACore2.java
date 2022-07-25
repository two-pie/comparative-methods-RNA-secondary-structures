package it.unicam.cs.bdslab.aspralign;

import java.util.*;


public class RNACore2 {
    private final RNASecondaryStructure secondaryStructure;
    private final List<List<WeakBond>> core;

    public RNACore2(RNASecondaryStructure secondaryStructure) {
        this.secondaryStructure = Objects.requireNonNull(secondaryStructure);
        this.core = new ArrayList<>();
        this.createStacks(this.p(secondaryStructure));

    }

    // recreate the array p of the secondary structure because there is no public method to access it
    private int[] p(RNASecondaryStructure s) {
        var p = new int[s.getSize() + 1];
        for (WeakBond b : s.getBonds()) {
            p[b.getLeft()] = b.getRight();
            p[b.getRight()] = b.getLeft();
        }
        return p;
    }

    private void createStacks(int[] p) {
        var bonds = secondaryStructure.getBonds();
        if (bonds.size() > 0) {
            // initialize stack
            var stack = new ArrayList<WeakBond>();
            core.add(stack);
            // last bound encountered
            var lastBond = bonds.get(0);
            // the goal is to group all the parallel bonds after eliminating the unpaired nucleotides,
            // in this case we use two simple conditions that solve this problem
            for (var b : bonds) {
                if (!this.isWithin(b, lastBond) || this.isThereBond(b, lastBond, p)) {
                    stack = new ArrayList<>();
                    core.add(stack);
                }
                stack.add(b);
                // update the last bond
                lastBond = b;
            }
        }

    }

    // determine if the second bond is contained within the first bond
    private boolean isWithin(WeakBond wb1, WeakBond wb2) {
        return wb2.getLeft() >= wb1.getLeft() || wb2.getRight() <= wb1.getRight();
    }

    // determine if there is another bond between the first and second bond (the second bond must be contained in the first bond)
    private boolean isThereBond(WeakBond wb1, WeakBond wb2, int[] p) {
        boolean isThereBond = false;
        for (int i = wb1.getLeft() + 1; i < wb2.getLeft(); i++)
            if (p[i] != 0) {
                isThereBond = true;
                break;
            }
        if (!isThereBond)
            for (int i = wb2.getRight() + 1; i < wb1.getRight(); i++)
                if (p[i] != 0) {
                    isThereBond = true;
                    break;
                }
        return isThereBond;
    }

    public RNASecondaryStructure getSecondaryStructure() {
        return this.secondaryStructure;
    }

    public List<List<WeakBond>> getCore() {
        return this.core;
    }

}
