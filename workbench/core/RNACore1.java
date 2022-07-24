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

    private void createStacks(){
        // initialize stack
        var stack = new ArrayList<WeakBond>();
        // store all weak bonds in the secondary structure
        var bonds = secondaryStructure.getBonds();
        // expected distance between the members of a weak bond to be defined as parallel,
        // initialize the distance if there is at least one bond
        var distance = bonds.size() > 0 ? bonds.get(0).getRight() - bonds.get(0).getLeft() : null;
        // iterate over all bonds and add them to the respective stack
        for (var b : bonds) {
            // if the bond is not parallel, add the current stack to the core and create a new one
            if (b.getRight() - b.getLeft() != distance) {
                core.add(stack);
                stack = new ArrayList<>();
            }
            stack.add(b);
            // update the distance for the next bond
            distance = b.getRight() - b.getLeft() + 2;
        }
        // the last stack is not added inside the loop, so it is added here
        core.add(stack);
    }

    public RNASecondaryStructure getSecondaryStructure() {
        return this.secondaryStructure;
    }

    public List<List<WeakBond>> getCore() {
        return this.core;
    }
}
