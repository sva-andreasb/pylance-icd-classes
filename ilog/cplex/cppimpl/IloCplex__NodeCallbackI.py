def IloCplex__NodeCallbackI():
    '''    public IloCplex__NodeCallbackI(final long cPtr, final boolean cMemoryOwn)
    '''
def getCPtr():
    '''    public static long getCPtr(final IloCplex__NodeCallbackI obj)
    '''
def delete():
    '''    public void delete()
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
def setNodeData():
    '''    public SWIGTYPE_p_NodeData setNodeData(final long node, final SWIGTYPE_p_NodeData data)
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
def getNodeNumber():
    '''    public int getNodeNumber(final NodeId nodeid)
    '''
