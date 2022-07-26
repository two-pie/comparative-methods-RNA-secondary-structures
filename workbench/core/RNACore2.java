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

    private void createStacks(int[] p) {
        var bonds = secondaryStructure.getBonds();
        // group in the same stack all bonds that are parallel after eliminating unpaired nucleotides
        for (int i = 0; i < bonds.size(); i++) {
            if (i == 0 || !this.isParallelAfterElimination(bonds.get(i), bonds.get(i - 1), p))
                this.core.add(new ArrayList<>());
            // add the bond to the last stack
            core.get(core.size() - 1).add(bonds.get(i));
        }
    }


    private boolean isParallelAfterElimination(WeakBond wb1, WeakBond wb2, int[] p) {
        return this.isWithin(wb1, wb2) && !this.isThereBond(wb1, wb2, p);
    }

    // determine if the second bond is contained within the first bond
    private boolean isWithin(WeakBond wb1, WeakBond wb2) {
        return wb2.getLeft() >= wb1.getLeft() || wb2.getRight() <= wb1.getRight();
    }

    // determine if there is a bond between the first and second bond (the second bond must be contained in the first bond)
    private boolean isThereBond(WeakBond wb1, WeakBond wb2, int[] p) {
        var isThereBond = false;
        for (int i = wb1.getLeft() + 1; i < wb2.getLeft(); i++)
            if (p[i] != 0) {
                isThereBond = true;
                break;
            }
        if (!isThereBond) for (int i = wb2.getRight() + 1; i < wb1.getRight(); i++)
            if (p[i] != 0) {
                isThereBond = true;
                break;
            }
        return isThereBond;
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

    public RNASecondaryStructure getSecondaryStructure() {
        return this.secondaryStructure;
    }

    public List<List<WeakBond>> getCore() {
        return this.core;
    }

}
