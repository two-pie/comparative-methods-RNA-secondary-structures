package it.unicam.cs.hierro.corecalculator;

public class RNACore {

    private final String core;

    public RNACore(String brackets) {
        this.core = new RNACorePlus(new RNACorePlus(brackets).getCorePlus()).getCorePlus();
    }

    public String getCore() {
        return core;
    }

}
