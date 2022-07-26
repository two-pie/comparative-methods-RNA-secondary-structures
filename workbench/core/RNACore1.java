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
        // group all parallel bonds in the same stack
        for (int i = 0; i < bonds.size(); i++) {
            if (i == 0 || !this.isParallel(bonds.get(i), bonds.get(i - 1)))
                this.core.add(new ArrayList<>());
            // add the bond to the last stack
            core.get(core.size() - 1).add(bonds.get(i));
        }
    }

    private boolean isParallel(WeakBond wb1, WeakBond wb2) {
        return wb1.getLeft() + 1 == wb2.getLeft() && wb1.getRight() - 1 == wb2.getRight();
    }

    public RNASecondaryStructure getSecondaryStructure() {
        return this.secondaryStructure;
    }

    public List<List<WeakBond>> getCore() {
        return this.core;
    }
}