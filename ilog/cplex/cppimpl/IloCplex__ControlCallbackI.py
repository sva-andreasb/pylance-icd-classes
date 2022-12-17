def ():
    '''returns IntegerFeasibility\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final String swigName, final int swigValue)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def getNodeId():
    '''returns NodeId\n\n
    getNodeId()\n
    '''
def getFeasibility():
    '''returns IntegerFeasibility\n\n
    getFeasibility(final IloSOS1 sos)\n
    getFeasibility(final IloSOS2 sos)\n
    getFeasibility(final IloNumVar var)\n
    getFeasibility(final IloIntVar var)\n
    '''
def getFeasibilities():
    '''returns None\n\n
    getFeasibilities(final IloCplex__ControlCallbackI__IntegerFeasibilityArray stat, final IloNumVarArray var)\n
    getFeasibilities(final IloCplex__ControlCallbackI__IntegerFeasibilityArray stat, final IloIntVarArray var)\n
    '''
def isSOSFeasible():
    '''returns boolean\n\n
    isSOSFeasible(final IloSOS1 sos1)\n
    isSOSFeasible(final IloSOS2 sos2)\n
    '''
def getLB():
    '''returns double\n\n
    getLB(final IloNumVar var)\n
    getLB(final IloIntVar var)\n
    '''
def getUB():
    '''returns double\n\n
    getUB(final IloNumVar var)\n
    getUB(final IloIntVar var)\n
    '''
def getLBs():
    '''returns None\n\n
    getLBs(final IloNumArray val, final IloNumVarArray vars)\n
    getLBs(final IloNumArray val, final IloIntVarArray vars)\n
    '''
def getUBs():
    '''returns None\n\n
    getUBs(final IloNumArray val, final IloNumVarArray vars)\n
    getUBs(final IloNumArray val, final IloIntVarArray vars)\n
    '''
def getObjValue():
    '''returns double\n\n
    getObjValue()\n
    '''
def getValue():
    '''returns double\n\n
    getValue(final SWIGTYPE_p_IloExprArg expr)\n
    getValue(final IloNumVar var)\n
    getValue(final IloIntVar var)\n
    '''
def getSlack():
    '''returns double\n\n
    getSlack(final IloRange rng)\n
    '''
def getValues():
    '''returns None\n\n
    getValues(final IloNumArray val, final IloNumVarArray vars)\n
    getValues(final IloNumArray val, final IloIntVarArray vars)\n
    '''
def getSlacks():
    '''returns None\n\n
    getSlacks(final IloNumArray val, final IloRangeArray con)\n
    '''
def getDownPseudoCost():
    '''returns double\n\n
    getDownPseudoCost(final IloNumVar var)\n
    getDownPseudoCost(final IloIntVar var)\n
    '''
def getUpPseudoCost():
    '''returns double\n\n
    getUpPseudoCost(final IloNumVar var)\n
    getUpPseudoCost(final IloIntVar var)\n
    '''
def getNodeData():
    '''returns SWIGTYPE_p_NodeData\n\n
    getNodeData()\n
    '''
def setNodeData():
    '''returns SWIGTYPE_p_NodeData\n\n
    setNodeData(final SWIGTYPE_p_NodeData data)\n
    '''
def mySwigValue():
    '''returns int\n\n
    mySwigValue()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
