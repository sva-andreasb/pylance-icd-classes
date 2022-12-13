def NodeCallbackWrapper():
'''public NodeCallbackWrapper(final long cPtr, final boolean cMemoryOwn)
public NodeCallbackWrapper(final IloEnv env)
'''
pass
def getCPtr():
'''public static long getCPtr(final NodeCallbackWrapper obj)
'''
pass
def delete():
'''public void delete()
'''
pass
def main_cpp():
'''public void main_cpp()
'''
pass
def duplicateCallback():
'''public IloCplex__CallbackI duplicateCallback()
'''
pass
def callbackImpl():
'''public void callbackImpl()
'''
pass
def abort():
'''public void abort()
'''
pass
def getEnv():
'''public IloEnv getEnv()
'''
pass
def getModel():
'''public IloModel getModel()
'''
pass
def getNcols():
'''public int getNcols()
'''
pass
def getNrows():
'''public int getNrows()
'''
pass
def getNQCs():
'''public int getNQCs()
'''
pass
def getBestObjValue():
'''public double getBestObjValue()
'''
pass
def getIncumbentObjValue():
'''public double getIncumbentObjValue()
'''
pass
def getIncumbentValue():
'''public double getIncumbentValue(final IloNumVar var)
public double getIncumbentValue(final IloIntVar var)
public double getIncumbentValue(final IloNumExprArg ex)
'''
pass
def getIncumbentValues():
'''public void getIncumbentValues(final IloNumArray val, final IloNumVarArray vars)
public void getIncumbentValues(final IloNumArray val, final IloIntVarArray vars)
'''
pass
def getMyThreadNum():
'''public int getMyThreadNum()
'''
pass
def hasIncumbent():
'''public boolean hasIncumbent()
'''
pass
def getNnodes():
'''public int getNnodes()
'''
pass
def getNremainingNodes():
'''public int getNremainingNodes()
'''
pass
def getNiterations():
'''public int getNiterations()
'''
pass
def getCutoff():
'''public double getCutoff()
'''
pass
def getPriority():
'''public double getPriority(final IloNumVar sos)
public double getPriority(final IloIntVar sos)
'''
pass
def getUserThreads():
'''public int getUserThreads()
'''
pass
def getObjCoef():
'''public double getObjCoef(final IloNumVar var)
public double getObjCoef(final IloIntVar var)
'''
pass
def getObjCoefs():
'''public void getObjCoefs(final IloNumArray val, final IloNumVarArray vars)
public void getObjCoefs(final IloNumArray val, final IloIntVarArray vars)
'''
pass
def getNodeId():
'''public NodeId getNodeId(final long node)
'''
pass
def getObjValue():
'''public double getObjValue(final long node)
public double getObjValue(final NodeId nodeid)
'''
pass
def getEstimatedObjValue():
'''public double getEstimatedObjValue(final long node)
public double getEstimatedObjValue(final NodeId nodeid)
'''
pass
def getDepth():
'''public int getDepth(final long node)
public int getDepth(final NodeId nodeid)
'''
pass
def getInfeasibilitySum():
'''public double getInfeasibilitySum(final long node)
public double getInfeasibilitySum(final NodeId nodeid)
'''
pass
def getNinfeasibilities():
'''public int getNinfeasibilities(final long node)
public int getNinfeasibilities(final NodeId nodeid)
'''
pass
def getNodeData():
'''public SWIGTYPE_p_NodeData getNodeData(final long node)
public SWIGTYPE_p_NodeData getNodeData(final NodeId nodeid)
'''
pass
def selectNode():
'''public void selectNode(final long node)
public void selectNode(final NodeId nodeid)
'''
pass
def getBranchVar():
'''public IloNumVar getBranchVar(final long node)
public IloNumVar getBranchVar(final NodeId nodeid)
'''
pass
def getNodeNumber64():
'''public long getNodeNumber64(final NodeId nodeid)
'''
pass
def setNodeData():
'''public SWIGTYPE_p_NodeData setNodeData(final long node, final SWIGTYPE_p_NodeData data)
'''
pass
