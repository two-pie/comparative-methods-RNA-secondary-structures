// Pseudo java code of RNACore1 class

// constructor that creates a core instance from a secondary rna structure (aspralign class)

RNACore1(RNASecondaryStructure s){
	this.core = new ArrayList<ArrayList<WeakBonds>>();
  
  // stack that contains weak bonds in parallel sequence
  List<WeakBond> stack;

  // expected distance between the members of a weak bond to be defined as parallel
  int distance;

  boolean isNewStackNeeded = true;

  foreach(WeakBond wb:  s.getBonds()){
    // initialize a new stack if needed 
    if(isNewStackNeeded){
      stack= new ArrayList<>();
      distance = wb.getRight() - wb.getLeft();
      isNewStackNeeded = false;
    }

    // checks if the members of the weak bond are parallel and then increment the distance
    if (wb.getRight() - wb.getLeft() == distance++)
      // adds the weak bond to the stack and removes it from the list
      stack.add(wb);
    else{
      isNewStackNeeded = true;
      this.core.add(stack);
    }
}
