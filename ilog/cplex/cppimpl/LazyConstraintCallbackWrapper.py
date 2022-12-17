def ():
    '''returns LazyConstraintCallbackWrapper\n\n
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
    getValue(final IloNumExprArg expr)\n
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
def add():
    '''returns IloConstraint\n\n
    add(final IloConstraint con)\n
    '''
def addLocal():
    '''returns IloConstraint\n\n
    addLocal(final IloConstraint con)\n
    '''
