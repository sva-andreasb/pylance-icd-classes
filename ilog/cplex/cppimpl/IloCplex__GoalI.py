def ():
    '''returns BranchType\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def getEnv():
    '''returns IloEnv\n\n
    getEnv()\n
    '''
def execute():
    '''returns IloCplex__Goal\n\n
    execute()\n
    '''
def duplicateGoal():
    '''returns IloCplex__Goal\n\n
    duplicateGoal()\n
    '''
def abort():
    '''returns None\n\n
    abort()\n
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
def getBestObjValue():
    '''returns double\n\n
    getBestObjValue()\n
    '''
def getMIPRelativeGap():
    '''returns double\n\n
    getMIPRelativeGap()\n
    '''
def getCutoff():
    '''returns double\n\n
    getCutoff()\n
    '''
def getDirection():
    '''returns SWIGTYPE_p_IloCplex__BranchDirection\n\n
    getDirection(final IloNumVar var)\n
    getDirection(final IloIntVar var)\n
    '''
def getIncumbentObjValue():
    '''returns double\n\n
    getIncumbentObjValue()\n
    '''
def getIncumbentValue():
    '''returns double\n\n
    getIncumbentValue(final IloNumVar var)\n
    getIncumbentValue(final IloIntVar var)\n
    getIncumbentValue(final SWIGTYPE_p_IloExprArg expr)\n
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
def getUserThreads():
    '''returns int\n\n
    getUserThreads()\n
    '''
def getNcuts():
    '''returns int\n\n
    getNcuts(final SWIGTYPE_p_IloCplex__CutType which)\n
    '''
def getNiterations64():
    '''returns long\n\n
    getNiterations64()\n
    '''
def getNiterations():
    '''returns int\n\n
    getNiterations()\n
    '''
def getNnodes64():
    '''returns long\n\n
    getNnodes64()\n
    '''
def getNnodes():
    '''returns int\n\n
    getNnodes()\n
    '''
def getNremainingNodes64():
    '''returns long\n\n
    getNremainingNodes64()\n
    '''
def getNremainingNodes():
    '''returns int\n\n
    getNremainingNodes()\n
    '''
def getPriority():
    '''returns double\n\n
    getPriority(final IloNumVar var)\n
    getPriority(final IloIntVar var)\n
    '''
def isIntegerFeasible():
    '''returns boolean\n\n
    isIntegerFeasible()\n
    '''
def hasIncumbent():
    '''returns boolean\n\n
    hasIncumbent()\n
    '''
def getBranch():
    '''returns double\n\n
    getBranch(final IloNumVarArray vars, final IloNumArray bounds, final IloCplex__BranchDirectionArray dirs, final int i)\n
    '''
def getBranchType():
    '''returns BranchType\n\n
    getBranchType()\n
    '''
def getNbranches():
    '''returns int\n\n
    getNbranches()\n
    '''
def getDownPseudoCost():
    '''returns double\n\n
    getDownPseudoCost(final IloNumVar var)\n
    getDownPseudoCost(final IloIntVar var)\n
    '''
def getFeasibility():
    '''returns IntegerFeasibility\n\n
    getFeasibility(final IloNumVar var)\n
    getFeasibility(final IloIntVar var)\n
    getFeasibility(final IloSOS1 sos)\n
    getFeasibility(final IloSOS2 sos)\n
    '''
def getFeasibilities():
    '''returns None\n\n
    getFeasibilities(final IloCplex__GoalI__IntegerFeasibilityArray stats, final IloNumVarArray vars)\n
    getFeasibilities(final IloCplex__GoalI__IntegerFeasibilityArray stats, final IloIntVarArray vars)\n
    '''
def getLB():
    '''returns double\n\n
    getLB(final IloNumVar var)\n
    getLB(final IloIntVar var)\n
    '''
def getLBs():
    '''returns None\n\n
    getLBs(final IloNumArray vals, final IloNumVarArray vars)\n
    getLBs(final IloNumArray vals, final IloIntVarArray vars)\n
    '''
def getObjCoef():
    '''returns double\n\n
    getObjCoef(final IloNumVar var)\n
    getObjCoef(final IloIntVar var)\n
    '''
def getObjCoefs():
    '''returns None\n\n
    getObjCoefs(final IloNumArray vals, final IloNumVarArray vars)\n
    getObjCoefs(final IloNumArray vals, final IloIntVarArray vars)\n
    '''
def getObjValue():
    '''returns double\n\n
    getObjValue()\n
    '''
def getSlack():
    '''returns double\n\n
    getSlack(final IloRange rng)\n
    '''
def getSlacks():
    '''returns None\n\n
    getSlacks(final IloNumArray vals, final IloRangeArray rngs)\n
    '''
def getUB():
    '''returns double\n\n
    getUB(final IloNumVar var)\n
    getUB(final IloIntVar var)\n
    '''
def getUBs():
    '''returns None\n\n
    getUBs(final IloNumArray vals, final IloNumVarArray vars)\n
    getUBs(final IloNumArray vals, final IloIntVarArray vars)\n
    '''
def getUpPseudoCost():
    '''returns double\n\n
    getUpPseudoCost(final IloNumVar var)\n
    getUpPseudoCost(final IloIntVar var)\n
    '''
def getValue():
    '''returns double\n\n
    getValue(final SWIGTYPE_p_IloExprArg expr)\n
    getValue(final IloNumVar var)\n
    getValue(final IloIntVar var)\n
    getValue(final IloNumExpr expr)\n
    '''
def getValues():
    '''returns None\n\n
    getValues(final IloNumArray vals, final IloNumVarArray vars)\n
    getValues(final IloNumArray vals, final IloIntVarArray vars)\n
    '''
def isSOSFeasible():
    '''returns boolean\n\n
    isSOSFeasible(final IloSOS1 sos1)\n
    isSOSFeasible(final IloSOS2 sos2)\n
    '''
def mySwigValue():
    '''returns int\n\n
    mySwigValue()\n
    mySwigValue()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
