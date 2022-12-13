def NodeCallbackWrapper():
    '''    public NodeCallbackWrapper(final long cPtr, final boolean cMemoryOwn)
    public NodeCallbackWrapper(final IloEnv env)
    '''
def getCPtr():
    '''    public static long getCPtr(final NodeCallbackWrapper obj)
    '''
def delete():
    '''    public void delete()
    '''
def main_cpp():
    '''    public void main_cpp()
    '''
def duplicateCallback():
    '''    public IloCplex__CallbackI duplicateCallback()
    '''
def callbackImpl():
    '''    public void callbackImpl()
    '''
def abort():
    '''    public void abort()
    '''
def getEnv():
    '''    public IloEnv getEnv()
    '''
def getModel():
    '''    public IloModel getModel()
    '''
def getNcols():
    '''    public int getNcols()
    '''
def getNrows():
    '''    public int getNrows()
    '''
def getNQCs():
    '''    public int getNQCs()
    '''
def getBestObjValue():
    '''    public double getBestObjValue()
    '''
def getIncumbentObjValue():
    '''    public double getIncumbentObjValue()
    '''
def getIncumbentValue():
    '''    public double getIncumbentValue(final IloNumVar var)
    public double getIncumbentValue(final IloIntVar var)
    public double getIncumbentValue(final IloNumExprArg ex)
    '''
def getIncumbentValues():
    '''    public void getIncumbentValues(final IloNumArray val, final IloNumVarArray vars)
    public void getIncumbentValues(final IloNumArray val, final IloIntVarArray vars)
    '''
def getMyThreadNum():
    '''    public int getMyThreadNum()
    '''
def hasIncumbent():
    '''    public boolean hasIncumbent()
    '''
def getNnodes():
    '''    public int getNnodes()
    '''
def getNremainingNodes():
    '''    public int getNremainingNodes()
    '''
def getNiterations():
    '''    public int getNiterations()
    '''
def getCutoff():
    '''    public double getCutoff()
    '''
def getPriority():
    '''    public double getPriority(final IloNumVar sos)
    public double getPriority(final IloIntVar sos)
    '''
def getUserThreads():
    '''    public int getUserThreads()
    '''
def getObjCoef():
    '''    public double getObjCoef(final IloNumVar var)
    public double getObjCoef(final IloIntVar var)
    '''
def getObjCoefs():
    '''    public void getObjCoefs(final IloNumArray val, final IloNumVarArray vars)
    public void getObjCoefs(final IloNumArray val, final IloIntVarArray vars)
    '''
def getNodeId():
    '''    public NodeId getNodeId(final long node)
    '''
def getObjValue():
    '''    public double getObjValue(final long node)
    public double getObjValue(final NodeId nodeid)
    '''
def getEstimatedObjValue():
    '''    public double getEstimatedObjValue(final long node)
    public double getEstimatedObjValue(final NodeId nodeid)
    '''
def getDepth():
    '''    public int getDepth(final long node)
    public int getDepth(final NodeId nodeid)
    '''
def getInfeasibilitySum():
    '''    public double getInfeasibilitySum(final long node)
    public double getInfeasibilitySum(final NodeId nodeid)
    '''
def getNinfeasibilities():
    '''    public int getNinfeasibilities(final long node)
    public int getNinfeasibilities(final NodeId nodeid)
    '''
def getNodeData():
    '''    public SWIGTYPE_p_NodeData getNodeData(final long node)
    public SWIGTYPE_p_NodeData getNodeData(final NodeId nodeid)
    '''
def selectNode():
    '''    public void selectNode(final long node)
    public void selectNode(final NodeId nodeid)
    '''
def getBranchVar():
    '''    public IloNumVar getBranchVar(final long node)
    public IloNumVar getBranchVar(final NodeId nodeid)
    '''
def getNodeNumber64():
    '''    public long getNodeNumber64(final NodeId nodeid)
    '''
def setNodeData():
    '''    public SWIGTYPE_p_NodeData setNodeData(final long node, final SWIGTYPE_p_NodeData data)
    '''
