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

    // recreate the array p of the structure because there is no public method to access it
    private int[] p(RNASecondaryStructure s) {
        var p = new int[s.getSize() + 1];
        for (WeakBond b : s.getBonds()) {
            p[b.getLeft()] = b.getRight();
            p[b.getRight()] = b.getLeft();
        }
        return p;
    }

    private void createStacks(int[] p) {
        // initialize stack
        var stack = new ArrayList<WeakBond>();
        // store all weak bonds in the secondary structure
        var bonds = secondaryStructure.getBonds();
        // last bound encountered
        WeakBond lastBond = bonds.size() > 0 ? bonds.get(0) : null;
        // iterate over all bonds and add them to the respective stack
        for (var b : bonds) {
            // determine whether a new stack is needed after eliminating all unpaired nucleotides
            if (!this.isWithin(b, lastBond) || this.isThereNucleotide(b, lastBond,p)) {
                core.add(stack);
                stack = new ArrayList<>();
            }
            stack.add(b);
            // update the last bond
            lastBond = b;
        }
        // the last stack is not added inside the loop, so it is added here
        core.add(stack);
    }

    // determine if the second bond is contained within the first bond
    private boolean isWithin(WeakBond wb1, WeakBond wb2) {
        return wb2.getLeft() >= wb1.getLeft() || wb2.getRight() <= wb1.getRight();
    }

    // determine if there is another nucleotide between the first and second bond (the second bond must be contained in the first bond)
    private boolean isThereNucleotide(WeakBond wb1, WeakBond wb2, int[] p) {
        boolean isThereNucleotide = false;
        for (int i = wb1.getLeft()+1; i < wb2.getLeft(); i++) {
            if (p[i] !=0) {
                isThereNucleotide = true;
                break;
            }
        }
        if (!isThereNucleotide)
            for (int i = wb2.getRight()+1; i < wb1.getRight(); i++) {
                if (p[i] !=0) {
                    isThereNucleotide = true;
                    break;
                }
            }
        return isThereNucleotide;
    }

    public RNASecondaryStructure getSecondaryStructure() {
        return this.secondaryStructure;
    }

    public List<List<WeakBond>> getCore() {
        return this.core;
    }

}
