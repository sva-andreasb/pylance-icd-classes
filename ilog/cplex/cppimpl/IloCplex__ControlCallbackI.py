def IloCplex__ControlCallbackI():
    '''public IloCplex__ControlCallbackI(final long cPtr, final boolean cMemoryOwn)
    '''
def getCPtr():
    '''public static long getCPtr(final IloCplex__ControlCallbackI obj)
    '''
def delete():
    '''public void delete()
    '''
def getNodeId():
    '''public NodeId getNodeId()
    '''
def getFeasibility():
    '''public IntegerFeasibility getFeasibility(final IloSOS1 sos)
    public IntegerFeasibility getFeasibility(final IloSOS2 sos)
    public IntegerFeasibility getFeasibility(final IloNumVar var)
    public IntegerFeasibility getFeasibility(final IloIntVar var)
    '''
def getFeasibilities():
    '''public void getFeasibilities(final IloCplex__ControlCallbackI__IntegerFeasibilityArray stat, final IloNumVarArray var)
    public void getFeasibilities(final IloCplex__ControlCallbackI__IntegerFeasibilityArray stat, final IloIntVarArray var)
    '''
def isSOSFeasible():
    '''public boolean isSOSFeasible(final IloSOS1 sos1)
    public boolean isSOSFeasible(final IloSOS2 sos2)
    '''
def getLB():
    '''public double getLB(final IloNumVar var)
    public double getLB(final IloIntVar var)
    '''
def getUB():
    '''public double getUB(final IloNumVar var)
    public double getUB(final IloIntVar var)
    '''
def getLBs():
    '''public void getLBs(final IloNumArray val, final IloNumVarArray vars)
    public void getLBs(final IloNumArray val, final IloIntVarArray vars)
    '''
def getUBs():
    '''public void getUBs(final IloNumArray val, final IloNumVarArray vars)
    public void getUBs(final IloNumArray val, final IloIntVarArray vars)
    '''
def getObjValue():
    '''public double getObjValue()
    '''
def getValue():
    '''public double getValue(final SWIGTYPE_p_IloExprArg expr)
    public double getValue(final IloNumVar var)
    public double getValue(final IloIntVar var)
    '''
def getSlack():
    '''public double getSlack(final IloRange rng)
    '''
def getValues():
    '''public void getValues(final IloNumArray val, final IloNumVarArray vars)
    public void getValues(final IloNumArray val, final IloIntVarArray vars)
    '''
def getSlacks():
    '''public void getSlacks(final IloNumArray val, final IloRangeArray con)
    '''
def getDownPseudoCost():
    '''public double getDownPseudoCost(final IloNumVar var)
    public double getDownPseudoCost(final IloIntVar var)
    '''
def getUpPseudoCost():
    '''public double getUpPseudoCost(final IloNumVar var)
    public double getUpPseudoCost(final IloIntVar var)
    '''
def getNodeData():
    '''public SWIGTYPE_p_NodeData getNodeData()
    '''
def setNodeData():
    '''public SWIGTYPE_p_NodeData setNodeData(final SWIGTYPE_p_NodeData data)
    '''
def mySwigValue():
    '''public int mySwigValue()
    '''
def swigValue():
    '''public final int swigValue()
    '''
def toString():
    '''public String toString()
    '''
def swigToEnum():
    '''public static IntegerFeasibility swigToEnum(final int swigValue)
    '''
def IntegerFeasibility():
    '''public IntegerFeasibility(final String swigName, final int swigValue)
    '''
