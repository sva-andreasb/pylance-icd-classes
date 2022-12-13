def BranchCallbackWrapper():
    '''public BranchCallbackWrapper(final long cPtr, final boolean cMemoryOwn)
    public BranchCallbackWrapper(final IloEnv env)
    '''
def getCPtr():
    '''public static long getCPtr(final BranchCallbackWrapper obj)
    '''
def delete():
    '''public void delete()
    '''
def main_cpp():
    '''public void main_cpp()
    '''
def duplicateCallback():
    '''public IloCplex__CallbackI duplicateCallback()
    '''
def callbackImpl():
    '''public void callbackImpl()
    '''
def abort():
    '''public void abort()
    '''
def getEnv():
    '''public IloEnv getEnv()
    '''
def getModel():
    '''public IloModel getModel()
    '''
def getNcols():
    '''public int getNcols()
    '''
def getNrows():
    '''public int getNrows()
    '''
def getNQCs():
    '''public int getNQCs()
    '''
def getBestObjValue():
    '''public double getBestObjValue()
    '''
def getIncumbentObjValue():
    '''public double getIncumbentObjValue()
    '''
def getIncumbentValue():
    '''public double getIncumbentValue(final IloNumVar var)
    public double getIncumbentValue(final IloIntVar var)
    public double getIncumbentValue(final IloNumExprArg ex)
    '''
def getIncumbentValues():
    '''public void getIncumbentValues(final IloNumArray val, final IloNumVarArray vars)
    public void getIncumbentValues(final IloNumArray val, final IloIntVarArray vars)
    '''
def getMyThreadNum():
    '''public int getMyThreadNum()
    '''
def hasIncumbent():
    '''public boolean hasIncumbent()
    '''
def getNnodes():
    '''public int getNnodes()
    '''
def getNremainingNodes():
    '''public int getNremainingNodes()
    '''
def getNiterations():
    '''public int getNiterations()
    '''
def getCutoff():
    '''public double getCutoff()
    '''
def getPriority():
    '''public double getPriority(final IloNumVar sos)
    public double getPriority(final IloIntVar sos)
    '''
def getUserThreads():
    '''public int getUserThreads()
    '''
def getObjCoef():
    '''public double getObjCoef(final IloNumVar var)
    public double getObjCoef(final IloIntVar var)
    '''
def getObjCoefs():
    '''public void getObjCoefs(final IloNumArray val, final IloNumVarArray vars)
    public void getObjCoefs(final IloNumArray val, final IloIntVarArray vars)
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
    '''public double getValue(final IloNumExprArg expr)
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
def getNodeId():
    '''public NodeId getNodeId()
    '''
def getNbranches():
    '''public int getNbranches()
    '''
def getBranchType():
    '''public BranchType getBranchType()
    '''
def getBranch():
    '''public double getBranch(final IloNumVarArray vars, final IloNumArray bounds, final IloCplex__BranchDirectionArray dirs, final int i)
    public double getBranch(final IloRangeArray cuts, final int i)
    '''
def isIntegerFeasible():
    '''public boolean isIntegerFeasible()
    '''
def makeBranch():
    '''public NodeId makeBranch(final IloNumVarArray vars, final IloNumArray bounds, final IloCplex__BranchDirectionArray dirs, final double objestimate, final SWIGTYPE_p_NodeData data)
    public NodeId makeBranch(final IloNumVarArray vars, final IloNumArray bounds, final IloCplex__BranchDirectionArray dirs, final double objestimate)
    public NodeId makeBranch(final IloIntVarArray vars, final IloNumArray bounds, final IloCplex__BranchDirectionArray dirs, final double objestimate, final SWIGTYPE_p_NodeData data)
    public NodeId makeBranch(final IloIntVarArray vars, final IloNumArray bounds, final IloCplex__BranchDirectionArray dirs, final double objestimate)
    public NodeId makeBranch(final IloNumVar var, final double bound, final IloCplex.BranchDirection dir, final double objestimate, final SWIGTYPE_p_NodeData data)
    public NodeId makeBranch(final IloNumVar var, final double bound, final IloCplex.BranchDirection dir, final double objestimate)
    public NodeId makeBranch(final IloIntVar var, final double bound, final IloCplex.BranchDirection dir, final double objestimate, final SWIGTYPE_p_NodeData data)
    public NodeId makeBranch(final IloIntVar var, final double bound, final IloCplex.BranchDirection dir, final double objestimate)
    public NodeId makeBranch(final IloConstraintArray cons, final double objestimate, final SWIGTYPE_p_NodeData data)
    public NodeId makeBranch(final IloConstraintArray cons, final double objestimate)
    public NodeId makeBranch(final IloConstraint con, final double objestimate, final SWIGTYPE_p_NodeData data)
    public NodeId makeBranch(final IloConstraint con, final double objestimate)
    public NodeId makeBranch(final IloConstraintArray cons, final IloNumVarArray vars, final IloNumArray bounds, final IloCplex__BranchDirectionArray dirs, final double objestimate, final SWIGTYPE_p_NodeData data)
    public NodeId makeBranch(final IloConstraintArray cons, final IloNumVarArray vars, final IloNumArray bounds, final IloCplex__BranchDirectionArray dirs, final double objestimate)
    public NodeId makeBranch(final IloConstraintArray cons, final IloIntVarArray vars, final IloNumArray bounds, final IloCplex__BranchDirectionArray dirs, final double objestimate, final SWIGTYPE_p_NodeData data)
    public NodeId makeBranch(final IloConstraintArray cons, final IloIntVarArray vars, final IloNumArray bounds, final IloCplex__BranchDirectionArray dirs, final double objestimate)
    public NodeId makeBranch(final int i, final SWIGTYPE_p_NodeData data)
    '''
def prune():
    '''public void prune()
    '''
