def ():
    '''returns IloCplex__NodeCallbackI\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
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
def setNodeData():
    '''returns SWIGTYPE_p_NodeData\n\n
    setNodeData(final long node, final SWIGTYPE_p_NodeData data)\n
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
def getNodeNumber():
    '''returns int\n\n
    getNodeNumber(final NodeId nodeid)\n
    '''
