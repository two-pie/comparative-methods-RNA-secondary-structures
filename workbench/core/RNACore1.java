package it.unicam.cs.bdslab.aspralign;

import java.util.ArrayList;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.IntStream;

public class RNACore1 {

    private final RNASecondaryStructure secondaryStructure;
    private final List<List<WeakBond>> core;

    public RNACore1(RNASecondaryStructure secondaryStructure) {
        this.secondaryStructure = secondaryStructure;
        this.core = new ArrayList<>();


        var weakbounds = secondaryStructure.getBonds();
        var stack = new ArrayList<WeakBond>();
        int distance = -1;
        for(var wb : weakbounds) {
            var isParallel = wb.getRight() - wb.getLeft() == distance;
            if (stack.size() != 0 && !isParallel) {
                core.add(stack);
                stack = new ArrayList<>();
            }
            stack.add(wb);
            distance = wb.getRight() - wb.getLeft();
        }
        core.add(stack);

       /* for (int i = 0, distance = -1; i < weakbounds.size(); i++, distance += 2) {
            var wb = weakbounds.get(i);
            // if the subtraction between the right and left member of a weak bond is equal to the distance then
            // the weak bond is defined as parallel
            var isParallel = wb.getRight() - wb.getLeft() == distance;
            // checks if a new stack is needed
            if (stack.size() != 0 && !isParallel) {
                core.add(stack);
                stack = new ArrayList<>();
            }
            stack.add(wb);
            distance = wb.getRight() - wb.getLeft();
        }
        // the last stack is not added inside the loop, so it is added here
        core.add(stack);*/
    }

    public RNASecondaryStructure getSecondaryStructure() {
        return this.secondaryStructure;
    }

    public List<List<WeakBond>> getCore() {
        return this.core;
    }

    private void createStack() {

    }
}
