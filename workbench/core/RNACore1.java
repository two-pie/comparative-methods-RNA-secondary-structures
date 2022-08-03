package it.unicam.cs.bdslab.aspralign;

import java.util.*;

public class RNACore1 {

    private final RNASecondaryStructure secondaryStructure;
    private final List<WeakBond> core;

    public RNACore1(RNASecondaryStructure secondaryStructure) {
        this.secondaryStructure = Objects.requireNonNull(secondaryStructure);
        this.core = new ArrayList<>();
        this.createStacks();
    }

    private void createStacks() {//TODO cambiare nome metodo
        var bonds = secondaryStructure.getBonds();
        for (int i = 0; i < bonds.size(); i++)
            if (i == 0 || !this.isParallel(bonds.get(i), bonds.get(i - 1)))
                this.addBond(bonds.get(i));
    }


    private void addBond(WeakBond newBond) {
        var leftNewBond = this.core.size() * 2 + 1;
        var rightNewBond = leftNewBond + 1;
        var bounds = this.secondaryStructure.getBonds();
        for (int i = this.core.size() - 1; i >= 0; i--) {
            var bond = bounds.get(i);
            if (bond.getLeft() > newBond.getLeft()) {
                leftNewBond = Math.min(leftNewBond, this.core.get(i).getLeft());
                this.core.set(i, new WeakBond(this.core.get(i).getLeft() + 1, this.core.get(i).getRight() + 1));
            } else if (bond.getRight() > newBond.getLeft()) {
                leftNewBond = this.core.get(i).getRight();
                this.core.set(i, new WeakBond(this.core.get(i).getLeft(), this.core.get(i).getRight() + 1));
            } else
                break;
        }
        this.core.add(new WeakBond(leftNewBond, rightNewBond));
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
}