def ():
    '''returns IloCplex__MIPInfoCallbackI\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def getBestObjValue():
    '''returns double\n\n
    getBestObjValue()\n
    '''
def getMIPRelativeGap():
    '''returns double\n\n
    getMIPRelativeGap()\n
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
def getIncumbentSlack():
    '''returns double\n\n
    getIncumbentSlack(final IloRange rng)\n
    getIncumbentSlack(final IloForAllRange rng)\n
    '''
def getIncumbentSlacks():
    '''returns None\n\n
    getIncumbentSlacks(final IloNumArray vals, final IloRangeArray cons)\n
    getIncumbentSlacks(final IloNumArray vals, final IloForAllRangeArray cons)\n
    '''
def getNcuts():
    '''returns int\n\n
    getNcuts(final SWIGTYPE_p_IloCplex__CutType which)\n
    '''
def getMyThreadNum():
    '''returns int\n\n
    getMyThreadNum()\n
    '''
def hasIncumbent():
    '''returns boolean\n\n
    hasIncumbent()\n
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
def getNiterations64():
    '''returns long\n\n
    getNiterations64()\n
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
def getQuality():
    '''returns double\n\n
    getQuality(final SWIGTYPE_p_IloCplex__Quality q)\n
    '''
