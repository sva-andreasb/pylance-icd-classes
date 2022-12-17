def ():
    '''returns NodeCallbackWrapper\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def main_cpp():
    '''returns None\n\n
    main_cpp()\n
    '''
def duplicateCallback():
    '''returns IloCplex__CallbackI\n\n
    duplicateCallback()\n
    '''
def callbackImpl():
    '''returns None\n\n
    callbackImpl()\n
    '''
def abort():
    '''returns None\n\n
    abort()\n
    '''
def getEnv():
    '''returns IloEnv\n\n
    getEnv()\n
    '''
def getModel():
    '''returns IloModel\n\n
    getModel()\n
    '''
def getNcols():
    '''returns int\n\n
    getNcols()\n
    '''
def getNrows():
    '''returns int\n\n
    getNrows()\n
    '''
def getNQCs():
    '''returns int\n\n
    getNQCs()\n
    '''
def getBestObjValue():
    '''returns double\n\n
    getBestObjValue()\n
    '''
def getIncumbentObjValue():
    '''returns double\n\n
    getIncumbentObjValue()\n
    '''
def getIncumbentValue():
    '''returns double\n\n
    getIncumbentValue(final IloNumVar var)\n
    getIncumbentValue(final IloIntVar var)\n
    getIncumbentValue(final IloNumExprArg ex)\n
    '''
def getIncumbentValues():
    '''returns None\n\n
    getIncumbentValues(final IloNumArray val, final IloNumVarArray vars)\n
    getIncumbentValues(final IloNumArray val, final IloIntVarArray vars)\n
    '''
def getMyThreadNum():
    '''returns int\n\n
    getMyThreadNum()\n
    '''
def hasIncumbent():
    '''returns boolean\n\n
    hasIncumbent()\n
    '''
def getNnodes():
    '''returns int\n\n
    getNnodes()\n
    '''
def getNremainingNodes():
    '''returns int\n\n
    getNremainingNodes()\n
    '''
def getNiterations():
    '''returns int\n\n
    getNiterations()\n
    '''
def getCutoff():
    '''returns double\n\n
    getCutoff()\n
    '''
def getPriority():
    '''returns double\n\n
    getPriority(final IloNumVar sos)\n
    getPriority(final IloIntVar sos)\n
    '''
def getUserThreads():
    '''returns int\n\n
    getUserThreads()\n
    '''
def getObjCoef():
    '''returns double\n\n
    getObjCoef(final IloNumVar var)\n
    getObjCoef(final IloIntVar var)\n
    '''
def getObjCoefs():
    '''returns None\n\n
    getObjCoefs(final IloNumArray val, final IloNumVarArray vars)\n
    getObjCoefs(final IloNumArray val, final IloIntVarArray vars)\n
    '''
def getNodeId():
    '''returns NodeId\n\n
    getNodeId(final long node)\n
    '''
def getObjValue():
    '''returns double\n\n
    getObjValue(final long node)\n
    getObjValue(final NodeId nodeid)\n
    '''
def getEstimatedObjValue():
    '''returns double\n\n
    getEstimatedObjValue(final long node)\n
    getEstimatedObjValue(final NodeId nodeid)\n
    '''
def getDepth():
    '''returns int\n\n
    getDepth(final long node)\n
    getDepth(final NodeId nodeid)\n
    '''
def getInfeasibilitySum():
    '''returns double\n\n
    getInfeasibilitySum(final long node)\n
    getInfeasibilitySum(final NodeId nodeid)\n
    '''
def getNinfeasibilities():
    '''returns int\n\n
    getNinfeasibilities(final long node)\n
    getNinfeasibilities(final NodeId nodeid)\n
    '''
def getNodeData():
    '''returns SWIGTYPE_p_NodeData\n\n
    getNodeData(final long node)\n
    getNodeData(final NodeId nodeid)\n
    '''
def selectNode():
    '''returns None\n\n
    selectNode(final long node)\n
    selectNode(final NodeId nodeid)\n
    '''
def getBranchVar():
    '''returns IloNumVar\n\n
    getBranchVar(final long node)\n
    getBranchVar(final NodeId nodeid)\n
    '''
def getNodeNumber64():
    '''returns long\n\n
    getNodeNumber64(final NodeId nodeid)\n
    '''
def setNodeData():
    '''returns SWIGTYPE_p_NodeData\n\n
    setNodeData(final long node, final SWIGTYPE_p_NodeData data)\n
    '''
