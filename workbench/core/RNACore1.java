package it.unicam.cs.bdslab.aspralign;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class RNACore1 {

    private final RNASecondaryStructure secondaryStructure;
    private final List<List<WeakBond>> core;

    public RNACore1(RNASecondaryStructure secondaryStructure) {
        this.secondaryStructure = Objects.requireNonNull(secondaryStructure);
        this.core = new ArrayList<>();
        this.createStacks();
    }

    private void createStacks() {
        var bonds = secondaryStructure.getBonds();
        if (bonds.size() > 0) {
            // initialize stack
            var stack = new ArrayList<WeakBond>();
            this.core.add(stack);
            // expected distance between the members of a weak bond to be defined as parallel
            var distance = bonds.get(0).getRight() - bonds.get(0).getLeft();
            // group all parallel bonds in the same stack
            for (var b : bonds) {
                if (b.getRight() - b.getLeft() != distance) {
                    stack = new ArrayList<>();
                    core.add(stack);
                }
                stack.add(b);
                // update the distance for the next bond
                distance = b.getRight() - b.getLeft() + 2;
            }
        }
    }

    public RNASecondaryStructure getSecondaryStructure() {
        return this.secondaryStructure;
    }

    public List<List<WeakBond>> getCore() {
        return this.core;
    }
}