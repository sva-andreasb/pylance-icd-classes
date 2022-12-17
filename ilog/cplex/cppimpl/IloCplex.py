def ():
    '''returns FilterType\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env)\n
    (final IloModel model)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    (final String swigName, final int swigValue)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def hasVMConfig():
    '''returns boolean\n\n
    hasVMConfig()\n
    '''
def delVMConfig():
    '''returns None\n\n
    delVMConfig()\n
    '''
def clearModel():
    '''returns None\n\n
    clearModel()\n
    '''
def deleteNames():
    '''returns None\n\n
    deleteNames()\n
    '''
def addUserCut():
    '''returns IloConstraint\n\n
    addUserCut(final IloConstraint con)\n
    '''
def addUserCuts():
    '''returns IloConstraintArray\n\n
    addUserCuts(final IloConstraintArray con)\n
    '''
def clearUserCuts():
    '''returns None\n\n
    clearUserCuts()\n
    '''
def addCut():
    '''returns IloConstraint\n\n
    addCut(final IloConstraint con)\n
    '''
def addCuts():
    '''returns IloConstraintArray\n\n
    addCuts(final IloConstraintArray con)\n
    '''
def clearCuts():
    '''returns None\n\n
    clearCuts()\n
    '''
def addLazyConstraint():
    '''returns IloConstraint\n\n
    addLazyConstraint(final IloConstraint con)\n
    '''
def addLazyConstraints():
    '''returns IloConstraintArray\n\n
    addLazyConstraints(final IloConstraintArray con)\n
    '''
def clearLazyConstraints():
    '''returns None\n\n
    clearLazyConstraints()\n
    '''
def importModel():
    '''returns None\n\n
    importModel(final IloModel model, final String filename, final IloObjective obj, final IloNumVarArray vars, final IloRangeArray rngs, final IloSOS1Array sos1, final IloSOS2Array sos2, final IloRangeArray lazy, final IloRangeArray cuts)\n
    importModel(final IloModel model, final String filename, final IloObjective obj, final IloNumVarArray vars, final IloRangeArray rngs, final IloSOS1Array sos1, final IloSOS2Array sos2, final IloRangeArray lazy)\n
    importModel(final IloModel model, final String filename, final IloObjective obj, final IloNumVarArray vars, final IloRangeArray rngs, final IloSOS1Array sos1, final IloSOS2Array sos2)\n
    importModel(final IloModel m, final String filename, final IloObjective obj, final IloNumVarArray vars, final IloRangeArray rngs, final IloRangeArray lazy, final IloRangeArray cuts)\n
    importModel(final IloModel m, final String filename, final IloObjective obj, final IloNumVarArray vars, final IloRangeArray rngs, final IloRangeArray lazy)\n
    importModel(final IloModel m, final String filename, final IloObjective obj, final IloNumVarArray vars, final IloRangeArray rngs)\n
    importModel(final IloModel m, final String filename)\n
    '''
def exportModel():
    '''returns None\n\n
    exportModel(final String filename)\n
    '''
def writeOrder():
    '''returns None\n\n
    writeOrder(final String filename)\n
    '''
def writeConflict():
    '''returns None\n\n
    writeConflict(final String filename)\n
    '''
def writeParam():
    '''returns None\n\n
    writeParam(final String name)\n
    '''
def writeBasis():
    '''returns None\n\n
    writeBasis(final String name)\n
    '''
def writeSolution():
    '''returns None\n\n
    writeSolution(final String name, final int soln)\n
    writeSolution(final String name)\n
    '''
def writeSolutions():
    '''returns None\n\n
    writeSolutions(final String name)\n
    '''
def writeMIPStarts():
    '''returns None\n\n
    writeMIPStarts(final String name, final int first, final int num)\n
    writeMIPStarts(final String name, final int first)\n
    writeMIPStarts(final String name)\n
    '''
def readOrder():
    '''returns None\n\n
    readOrder(final String filename)\n
    '''
def readParam():
    '''returns None\n\n
    readParam(final String name)\n
    '''
def readBasis():
    '''returns None\n\n
    readBasis(final String name)\n
    '''
def readSolution():
    '''returns None\n\n
    readSolution(final String name)\n
    '''
def readMIPStarts():
    '''returns None\n\n
    readMIPStarts(final String name)\n
    '''
def writeBendersAnnotation():
    '''returns None\n\n
    writeBendersAnnotation(final String name)\n
    '''
def readAnnotations():
    '''returns None\n\n
    readAnnotations(final String name)\n
    '''
def writeAnnotations():
    '''returns None\n\n
    writeAnnotations(final String name)\n
    '''
def numLongAnnotations():
    '''returns int\n\n
    numLongAnnotations()\n
    '''
def delAnnotation():
    '''returns None\n\n
    delAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation anno)\n
    delAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation anno)\n
    '''
def getName():
    '''returns String\n\n
    getName(final SWIGTYPE_p_IloCplex__LongAnnotation annotation)\n
    getName(final SWIGTYPE_p_IloCplex__NumAnnotation annotation)\n
    '''
def newLongAnnotation():
    '''returns SWIGTYPE_p_IloCplex__LongAnnotation\n\n
    newLongAnnotation(final String name, final long defval)\n
    newLongAnnotation(final String name)\n
    '''
def findLongAnnotation():
    '''returns SWIGTYPE_p_IloCplex__LongAnnotation\n\n
    findLongAnnotation(final String name)\n
    findLongAnnotation(final int num)\n
    '''
def hasLongAnnotation():
    '''returns boolean\n\n
    hasLongAnnotation(final String name)\n
    '''
def getDefaultValue():
    '''returns double\n\n
    getDefaultValue(final SWIGTYPE_p_IloCplex__LongAnnotation annotation)\n
    getDefaultValue(final SWIGTYPE_p_IloCplex__NumAnnotation annotation)\n
    '''
def getAnnotation():
    '''returns None\n\n
    getAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloNumVar var)\n
    getAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloIntVar var)\n
    getAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloObjective obj)\n
    getAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloConstraint ctr)\n
    getAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloNumVarArray var, final IloIntArrayBase value)\n
    getAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloIntVarArray var, final IloIntArrayBase value)\n
    getAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloConstraintArray ctr, final IloIntArrayBase value)\n
    getAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloNumVar var)\n
    getAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloIntVar var)\n
    getAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloObjective obj)\n
    getAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloConstraint ctr)\n
    getAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloNumVarArray var, final IloNumArray value)\n
    getAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloIntVarArray var, final IloNumArray value)\n
    getAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloConstraintArray ctr, final IloNumArray value)\n
    '''
def setAnnotation():
    '''returns None\n\n
    setAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloNumVar var, final long value)\n
    setAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloIntVar var, final long value)\n
    setAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloObjective obj, final long value)\n
    setAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloConstraint ctr, final long value)\n
    setAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloNumVarArray var, final IloIntArrayBase value)\n
    setAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloIntVarArray var, final IloIntArrayBase value)\n
    setAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloConstraintArray ctr, final IloIntArrayBase value)\n
    setAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloNumVar var, final double value)\n
    setAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloIntVar var, final double value)\n
    setAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloObjective obj, final double value)\n
    setAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloConstraint ctr, final double value)\n
    setAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloNumVarArray var, final IloNumArray value)\n
    setAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloIntVarArray var, final IloNumArray value)\n
    setAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloConstraintArray ctr, final IloNumArray value)\n
    '''
def numNumAnnotations():
    '''returns int\n\n
    numNumAnnotations()\n
    '''
def newNumAnnotation():
    '''returns SWIGTYPE_p_IloCplex__NumAnnotation\n\n
    newNumAnnotation(final String name, final double defval)\n
    newNumAnnotation(final String name)\n
    '''
def findNumAnnotation():
    '''returns SWIGTYPE_p_IloCplex__NumAnnotation\n\n
    findNumAnnotation(final String name)\n
    findNumAnnotation(final int num)\n
    '''
def hasNumAnnotation():
    '''returns boolean\n\n
    hasNumAnnotation(final String name)\n
    '''
def getObjective():
    '''returns IloObjective\n\n
    getObjective()\n
    '''
def getVersion():
    '''returns String\n\n
    getVersion()\n
    '''
def getVersionNumber():
    '''returns int\n\n
    getVersionNumber()\n
    '''
def getNiterations64():
    '''returns long\n\n
    getNiterations64()\n
    '''
def getNiterations():
    '''returns int\n\n
    getNiterations()\n
    '''
def getNbarrierIterations64():
    '''returns long\n\n
    getNbarrierIterations64()\n
    '''
def getNbarrierIterations():
    '''returns int\n\n
    getNbarrierIterations()\n
    '''
def getNsiftingIterations64():
    '''returns long\n\n
    getNsiftingIterations64()\n
    '''
def getNsiftingIterations():
    '''returns int\n\n
    getNsiftingIterations()\n
    '''
def getNsiftingPhaseOneIterations64():
    '''returns long\n\n
    getNsiftingPhaseOneIterations64()\n
    '''
def getNsiftingPhaseOneIterations():
    '''returns int\n\n
    getNsiftingPhaseOneIterations()\n
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
def getNSOSs():
    '''returns int\n\n
    getNSOSs()\n
    '''
def getNindicators():
    '''returns int\n\n
    getNindicators()\n
    '''
def getNLCs():
    '''returns int\n\n
    getNLCs()\n
    '''
def getNUCs():
    '''returns int\n\n
    getNUCs()\n
    '''
def getNNZs():
    '''returns int\n\n
    getNNZs()\n
    '''
def getNNZs64():
    '''returns long\n\n
    getNNZs64()\n
    '''
def getNintVars():
    '''returns int\n\n
    getNintVars()\n
    '''
def getNbinVars():
    '''returns int\n\n
    getNbinVars()\n
    '''
def getNsemiContVars():
    '''returns int\n\n
    getNsemiContVars()\n
    '''
def getNsemiIntVars():
    '''returns int\n\n
    getNsemiIntVars()\n
    '''
def solveFixed():
    '''returns boolean\n\n
    solveFixed(final int soln)\n
    solveFixed()\n
    '''
def isMIP():
    '''returns boolean\n\n
    isMIP()\n
    '''
def isQC():
    '''returns boolean\n\n
    isQC()\n
    '''
def isQO():
    '''returns boolean\n\n
    isQO()\n
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
def getIncumbentNode64():
    '''returns long\n\n
    getIncumbentNode64()\n
    '''
def getIncumbentNode():
    '''returns int\n\n
    getIncumbentNode()\n
    '''
def getNprimalSuperbasics():
    '''returns int\n\n
    getNprimalSuperbasics()\n
    '''
def getNdualSuperbasics():
    '''returns int\n\n
    getNdualSuperbasics()\n
    '''
def getNphaseOneIterations64():
    '''returns long\n\n
    getNphaseOneIterations64()\n
    '''
def getNphaseOneIterations():
    '''returns int\n\n
    getNphaseOneIterations()\n
    '''
def getNnodes64():
    '''returns long\n\n
    getNnodes64()\n
    '''
def getNnodes():
    '''returns int\n\n
    getNnodes()\n
    '''
def getNnodesLeft64():
    '''returns long\n\n
    getNnodesLeft64()\n
    '''
def getNnodesLeft():
    '''returns int\n\n
    getNnodesLeft()\n
    '''
def getNcuts():
    '''returns int\n\n
    getNcuts(final CutType which)\n
    '''
def getNcrossPPush64():
    '''returns long\n\n
    getNcrossPPush64()\n
    '''
def getNcrossPPush():
    '''returns int\n\n
    getNcrossPPush()\n
    '''
def getNcrossPExch64():
    '''returns long\n\n
    getNcrossPExch64()\n
    '''
def getNcrossPExch():
    '''returns int\n\n
    getNcrossPExch()\n
    '''
def getNcrossDPush64():
    '''returns long\n\n
    getNcrossDPush64()\n
    '''
def getNcrossDPush():
    '''returns int\n\n
    getNcrossDPush()\n
    '''
def getNcrossDExch64():
    '''returns long\n\n
    getNcrossDExch64()\n
    '''
def getNcrossDExch():
    '''returns int\n\n
    getNcrossDExch()\n
    '''
def getValues():
    '''returns None\n\n
    getValues(final IloNumArray val, final IloNumVarArray var)\n
    getValues(final IloNumVarArray var, final IloNumArray val)\n
    getValues(final IloNumArray val, final IloIntVarArray var)\n
    getValues(final IloIntVarArray var, final IloNumArray val)\n
    getValues(final IloNumArray val, final IloNumVarArray var, final int soln)\n
    getValues(final IloNumVarArray var, final IloNumArray val, final int soln)\n
    getValues(final IloNumArray val, final IloIntVarArray var, final int soln)\n
    getValues(final IloIntVarArray var, final IloNumArray val, final int soln)\n
    '''
def getValue():
    '''returns double\n\n
    getValue(final IloNumVar var, final int soln)\n
    getValue(final IloIntVar var, final int soln)\n
    getValue(final IloNumExprArg expr, final int soln)\n
    getValue(final IloObjective ob, final int soln)\n
    '''
def getObjValue():
    '''returns double\n\n
    getObjValue(final int soln)\n
    '''
def getDual():
    '''returns double\n\n
    getDual(final IloRange range)\n
    getDual(final IloForAllRange range)\n
    '''
def getSlack():
    '''returns double\n\n
    getSlack(final IloRange range, final int soln)\n
    getSlack(final IloRange range)\n
    getSlack(final IloForAllRange range, final int soln)\n
    getSlack(final IloForAllRange range)\n
    '''
def getInfeasibility():
    '''returns double\n\n
    getInfeasibility(final IloConstraint con)\n
    getInfeasibility(final IloNumVar var)\n
    getInfeasibility(final IloIntVar var)\n
    '''
def getAX():
    '''returns None\n\n
    getAX(final IloRange range)\n
    getAX(final IloNumArray val, final IloRangeArray con)\n
    getAX(final IloForAllRange range)\n
    getAX(final IloNumArray val, final IloForAllRangeArray con)\n
    '''
def getReducedCost():
    '''returns double\n\n
    getReducedCost(final IloNumVar var)\n
    getReducedCost(final IloIntVar var)\n
    '''
def getQCDSlack():
    '''returns None\n\n
    getQCDSlack(final IloRange range, final IloNumArray vals, final IloNumVarArray vars)\n
    getQCDSlack(final IloForAllRange range, final IloNumArray vals, final IloNumVarArray vars)\n
    '''
def getBasisStatus():
    '''returns BasisStatus\n\n
    getBasisStatus(final IloNumVar var)\n
    getBasisStatus(final IloIntVar var)\n
    getBasisStatus(final IloConstraint con)\n
    '''
def getDuals():
    '''returns None\n\n
    getDuals(final IloNumArray val, final IloRangeArray con)\n
    getDuals(final IloNumArray val, final IloForAllRangeArray con)\n
    '''
def getSlacks():
    '''returns None\n\n
    getSlacks(final IloNumArray val, final IloRangeArray con, final int soln)\n
    getSlacks(final IloNumArray val, final IloRangeArray con)\n
    getSlacks(final IloNumArray val, final IloForAllRangeArray con, final int soln)\n
    getSlacks(final IloNumArray val, final IloForAllRangeArray con)\n
    '''
def getInfeasibilities():
    '''returns double\n\n
    getInfeasibilities(final IloNumArray infeas, final IloConstraintArray con)\n
    getInfeasibilities(final IloNumArray infeas, final IloNumVarArray var)\n
    getInfeasibilities(final IloNumArray infeas, final IloIntVarArray var)\n
    '''
def getReducedCosts():
    '''returns None\n\n
    getReducedCosts(final IloNumArray val, final IloNumVarArray var)\n
    getReducedCosts(final IloNumArray val, final IloIntVarArray var)\n
    '''
def getBasisStatuses():
    '''returns None\n\n
    getBasisStatuses(final IloCplex__BasisStatusArray stat, final IloNumVarArray var)\n
    getBasisStatuses(final IloCplex__BasisStatusArray stat, final IloIntVarArray var)\n
    getBasisStatuses(final IloCplex__BasisStatusArray stat, final IloConstraintArray con)\n
    getBasisStatuses(final IloCplex__BasisStatusArray cstat, final IloNumVarArray var, final IloCplex__BasisStatusArray rstat, final IloConstraintArray con)\n
    getBasisStatuses(final IloCplex__BasisStatusArray cstat, final IloIntVarArray var, final IloCplex__BasisStatusArray rstat, final IloConstraintArray con)\n
    '''
def getBoundSA():
    '''returns None\n\n
    getBoundSA(final IloNumArray lblower, final IloNumArray lbupper, final IloNumArray ublower, final IloNumArray ubupper, final IloNumVarArray vars)\n
    getBoundSA(final IloNumArray lblower, final IloNumArray lbupper, final IloNumArray ublower, final IloNumArray ubupper, final IloIntVarArray vars)\n
    '''
def getRangeSA():
    '''returns None\n\n
    getRangeSA(final IloNumArray lblower, final IloNumArray lbupper, final IloNumArray ublower, final IloNumArray ubupper, final IloRangeArray con)\n
    '''
def getRHSSA():
    '''returns None\n\n
    getRHSSA(final IloNumArray lower, final IloNumArray upper, final IloRangeArray cons)\n
    '''
def getObjSA():
    '''returns None\n\n
    getObjSA(final IloNumArray lower, final IloNumArray upper, final IloNumVarArray vars)\n
    getObjSA(final IloNumArray lower, final IloNumArray upper, final IloIntVarArray cols)\n
    '''
def getForAllRanges():
    '''returns None\n\n
    getForAllRanges(final IloForAllRangeArray rows, final IloConstraint forall)\n
    '''
def getLB():
    '''returns double\n\n
    getLB(final IloForAllRange range)\n
    '''
def getUB():
    '''returns double\n\n
    getUB(final IloForAllRange range)\n
    '''
def feasOpt():
    '''returns boolean\n\n
    feasOpt(final IloRangeArray rngs, final IloNumArray rnglb, final IloNumArray rngub, final IloForAllRangeArray rngf, final IloNumArray frnglb, final IloNumArray frngub, final IloNumVarArray vars, final IloNumArray varlb, final IloNumArray varub)\n
    feasOpt(final IloRangeArray rngs, final IloNumArray rnglb, final IloNumArray rngub, final IloNumVarArray vars, final IloNumArray varlb, final IloNumArray varub)\n
    feasOpt(final IloRangeArray rngs, final IloNumArray rnglb, final IloNumArray rngub, final IloIntVarArray vars, final IloNumArray varlb, final IloNumArray varub)\n
    feasOpt(final IloNumVarArray vars, final IloNumArray varlb, final IloNumArray varub)\n
    feasOpt(final IloIntVarArray vars, final IloNumArray varlb, final IloNumArray varub)\n
    feasOpt(final IloRangeArray rngs, final IloNumArray rnglb, final IloNumArray rngub)\n
    feasOpt(final IloConstraintArray cts, final IloNumArray prefs)\n
    '''
def setBasisStatuses():
    '''returns None\n\n
    setBasisStatuses(final IloCplex__BasisStatusArray cstat, final IloNumVarArray var, final IloCplex__BasisStatusArray rstat, final IloConstraintArray con)\n
    setBasisStatuses(final IloCplex__BasisStatusArray cstat, final IloIntVarArray var, final IloCplex__BasisStatusArray rstat, final IloConstraintArray con)\n
    '''
def setStart():
    '''returns None\n\n
    setStart(final IloNumArray x, final IloNumArray dj, final IloNumVarArray var, final IloNumArray slack, final IloNumArray pi, final IloRangeArray rng)\n
    setStart(final IloNumArray x, final IloNumArray dj, final IloIntVarArray var, final IloNumArray slack, final IloNumArray pi, final IloRangeArray rng)\n
    '''
def getNMIPStarts():
    '''returns int\n\n
    getNMIPStarts()\n
    '''
def addMIPStart():
    '''returns int\n\n
    addMIPStart(final IloNumVarArray vars, final IloNumArray values, final MIPStartEffort effort, final String name)\n
    addMIPStart(final IloNumVarArray vars, final IloNumArray values, final MIPStartEffort effort)\n
    addMIPStart(final IloNumVarArray vars, final IloNumArray values)\n
    addMIPStart(final IloNumVarArray vars)\n
    addMIPStart()\n
    '''
def changeMIPStart():
    '''returns None\n\n
    changeMIPStart(final int mipstartindex, final IloNumVarArray vars, final IloNumArray values)\n
    changeMIPStart(final int mipstartindex, final IloNumVarArray vars, final IloNumArray values, final MIPStartEffort effortlevel)\n
    '''
def deleteMIPStarts():
    '''returns None\n\n
    deleteMIPStarts(final int first, final int num)\n
    deleteMIPStarts(final int first)\n
    '''
def getMIPStart():
    '''returns MIPStartEffort\n\n
    getMIPStart(final int mipstartindex, final IloNumVarArray vars, final IloNumArray vals, final SWIGTYPE_p_IloBoolArray isset)\n
    '''
def getMIPStartName():
    '''returns String\n\n
    getMIPStartName(final int mipstartindex)\n
    '''
def getMIPStartIndex():
    '''returns int\n\n
    getMIPStartIndex(final String lname_str)\n
    '''
def setDefaults():
    '''returns None\n\n
    setDefaults()\n
    '''
def setIntParam():
    '''returns None\n\n
    setIntParam(final IntParam parameter, final int value)\n
    '''
def setLongParam():
    '''returns None\n\n
    setLongParam(final LongParam parameter, final long value)\n
    '''
def setBoolParam():
    '''returns None\n\n
    setBoolParam(final BoolParam parameter, final boolean value)\n
    '''
def setNumParam():
    '''returns None\n\n
    setNumParam(final NumParam parameter, final double value)\n
    '''
def setStringParam():
    '''returns None\n\n
    setStringParam(final StringParam parameter, final String value)\n
    '''
def getIntParam():
    '''returns int\n\n
    getIntParam(final IntParam parameter)\n
    '''
def getLongParam():
    '''returns long\n\n
    getLongParam(final LongParam parameter)\n
    '''
def getBoolParam():
    '''returns boolean\n\n
    getBoolParam(final BoolParam parameter)\n
    '''
def getNumParam():
    '''returns double\n\n
    getNumParam(final NumParam parameter)\n
    '''
def getStringParam():
    '''returns String\n\n
    getStringParam(final StringParam parameter)\n
    '''
def getDefaultBoolParam():
    '''returns boolean\n\n
    getDefaultBoolParam(final BoolParam parameter)\n
    '''
def getDefaultIntParam():
    '''returns int\n\n
    getDefaultIntParam(final IntParam parameter)\n
    '''
def getDefaultLongParam():
    '''returns long\n\n
    getDefaultLongParam(final LongParam parameter)\n
    '''
def getDefaultNumParam():
    '''returns double\n\n
    getDefaultNumParam(final NumParam parameter)\n
    '''
def getDefaultStringParam():
    '''returns String\n\n
    getDefaultStringParam(final StringParam parameter)\n
    '''
def getMinIntParam():
    '''returns int\n\n
    getMinIntParam(final IntParam parameter)\n
    '''
def getMinLongParam():
    '''returns long\n\n
    getMinLongParam(final LongParam parameter)\n
    '''
def getMinNumParam():
    '''returns double\n\n
    getMinNumParam(final NumParam parameter)\n
    '''
def getMaxIntParam():
    '''returns int\n\n
    getMaxIntParam(final IntParam parameter)\n
    '''
def getMaxLongParam():
    '''returns long\n\n
    getMaxLongParam(final LongParam parameter)\n
    '''
def getMaxNumParam():
    '''returns double\n\n
    getMaxNumParam(final NumParam parameter)\n
    '''
def getParameterSet():
    '''returns IloCplex__ParameterSet\n\n
    getParameterSet()\n
    '''
def setParameterSet():
    '''returns None\n\n
    setParameterSet(final IloCplex__ParameterSet set)\n
    '''
def getStatus():
    '''returns Status\n\n
    getStatus()\n
    '''
def getCplexStatus():
    '''returns CplexStatus\n\n
    getCplexStatus()\n
    '''
def getCplexSubStatus():
    '''returns CplexStatus\n\n
    getCplexSubStatus()\n
    '''
def isPrimalFeasible():
    '''returns boolean\n\n
    isPrimalFeasible()\n
    '''
def isDualFeasible():
    '''returns boolean\n\n
    isDualFeasible()\n
    '''
def getAlgorithm():
    '''returns Algorithm\n\n
    getAlgorithm()\n
    '''
def getSubAlgorithm():
    '''returns Algorithm\n\n
    getSubAlgorithm()\n
    '''
def setDeleteMode():
    '''returns None\n\n
    setDeleteMode(final DeleteMode mode)\n
    '''
def getDeleteMode():
    '''returns DeleteMode\n\n
    getDeleteMode()\n
    '''
def populate():
    '''returns boolean\n\n
    populate()\n
    '''
def tuneParam():
    '''returns int\n\n
    tuneParam(final IloStringArrayBase filename, final IloCplex__ParameterSet fixedset)\n
    tuneParam()\n
    tuneParam(final IloCplex__ParameterSet fixedset)\n
    tuneParam(final IloStringArrayBase filename)\n
    '''
def refineConflict():
    '''returns boolean\n\n
    refineConflict(final IloConstraintArray cons, final IloNumArray prefs)\n
    '''
def refineMIPStartConflict():
    '''returns boolean\n\n
    refineMIPStartConflict(final int mipstartindex, final IloConstraintArray cons, final IloNumArray prefs)\n
    '''
def getConflict():
    '''returns ConflictStatus\n\n
    getConflict(final IloConstraintArray cons)\n
    getConflict(final IloConstraint con)\n
    '''
def getQuality():
    '''returns double\n\n
    getQuality(final Quality q, final IloNumVar var, final IloConstraint rng)\n
    getQuality(final Quality q, final IloNumVar var)\n
    getQuality(final Quality q)\n
    getQuality(final Quality q, final IloConstraint rng, final IloNumVar var)\n
    getQuality(final Quality q, final IloConstraint rng)\n
    getQuality(final Quality q, final int soln, final IloConstraint rng, final IloNumVar var)\n
    getQuality(final Quality q, final int soln, final IloConstraint rng)\n
    getQuality(final Quality q, final int soln, final IloNumVar var, final IloConstraint rng)\n
    getQuality(final Quality q, final int soln, final IloNumVar var)\n
    getQuality(final Quality q, final int soln)\n
    '''
def setPriority():
    '''returns None\n\n
    setPriority(final IloNumVar var, final double pri)\n
    setPriority(final IloIntVar var, final double pri)\n
    '''
def setPriorities():
    '''returns None\n\n
    setPriorities(final IloNumVarArray var, final IloNumArray pri)\n
    setPriorities(final IloIntVarArray var, final IloNumArray pri)\n
    '''
def setDirection():
    '''returns None\n\n
    setDirection(final IloNumVar var, final BranchDirection dir)\n
    setDirection(final IloIntVar var, final BranchDirection dir)\n
    '''
def setDirections():
    '''returns None\n\n
    setDirections(final IloNumVarArray var, final IloCplex__BranchDirectionArray dir)\n
    setDirections(final IloIntVarArray var, final IloCplex__BranchDirectionArray dir)\n
    '''
def delPriority():
    '''returns None\n\n
    delPriority(final IloNumVar var)\n
    delPriority(final IloIntVar var)\n
    '''
def delPriorities():
    '''returns None\n\n
    delPriorities(final IloNumVarArray var)\n
    delPriorities(final IloIntVarArray var)\n
    '''
def delDirection():
    '''returns None\n\n
    delDirection(final IloNumVar var)\n
    delDirection(final IloIntVar var)\n
    '''
def delDirections():
    '''returns None\n\n
    delDirections(final IloNumVarArray var)\n
    delDirections(final IloIntVarArray var)\n
    '''
def getPriority():
    '''returns double\n\n
    getPriority(final IloNumVar var)\n
    getPriority(final IloIntVar var)\n
    '''
def getDirection():
    '''returns BranchDirection\n\n
    getDirection(final IloNumVar var)\n
    getDirection(final IloIntVar var)\n
    '''
def getPriorities():
    '''returns None\n\n
    getPriorities(final IloNumArray pri, final IloNumVarArray var)\n
    getPriorities(final IloNumArray pri, final IloIntVarArray var)\n
    '''
def getDirections():
    '''returns None\n\n
    getDirections(final IloCplex__BranchDirectionArray dir, final IloNumVarArray var)\n
    getDirections(final IloCplex__BranchDirectionArray dir, final IloIntVarArray var)\n
    '''
def basicPresolve():
    '''returns None\n\n
    basicPresolve(final IloNumVarArray vars, final IloNumArray redlb, final IloNumArray redub, final IloRangeArray rngs, final SWIGTYPE_p_IloBoolArray redundant)\n
    basicPresolve(final IloNumVarArray vars, final IloNumArray redlb, final IloNumArray redub, final IloRangeArray rngs)\n
    basicPresolve(final IloNumVarArray vars, final IloNumArray redlb, final IloNumArray redub)\n
    basicPresolve(final IloNumVarArray vars, final IloNumArray redlb)\n
    basicPresolve(final IloNumVarArray vars)\n
    basicPresolve(final IloIntVarArray vars, final IloNumArray redlb, final IloNumArray redub, final IloRangeArray rngs, final SWIGTYPE_p_IloBoolArray redundant)\n
    basicPresolve(final IloIntVarArray vars, final IloNumArray redlb, final IloNumArray redub, final IloRangeArray rngs)\n
    basicPresolve(final IloIntVarArray vars, final IloNumArray redlb, final IloNumArray redub)\n
    basicPresolve(final IloIntVarArray vars, final IloNumArray redlb)\n
    basicPresolve(final IloIntVarArray vars)\n
    '''
def freePresolve():
    '''returns None\n\n
    freePresolve()\n
    '''
def presolve():
    '''returns None\n\n
    presolve(final SWIGTYPE_p_IloCplex__Algorithm alg)\n
    '''
def getDiverging():
    '''returns IloExtractable\n\n
    getDiverging()\n
    '''
def getRay():
    '''returns None\n\n
    getRay(final IloNumArray vals, final IloNumVarArray vars)\n
    '''
def dualFarkas():
    '''returns double\n\n
    dualFarkas(final IloConstraintArray rng, final IloNumArray y)\n
    '''
def qpIndefCertificate():
    '''returns None\n\n
    qpIndefCertificate(final IloNumVarArray var, final IloNumArray x)\n
    qpIndefCertificate(final IloIntVarArray var, final IloNumArray x)\n
    '''
def protectVariables():
    '''returns None\n\n
    protectVariables(final IloNumVarArray var)\n
    protectVariables(final IloIntVarArray var)\n
    '''
def use():
    '''returns IloCplex__Callback\n\n
    use(final IloCplex__Aborter abort)\n
    use(final IloCplex__Callback cb)\n
    '''
def getAborter():
    '''returns IloCplex__Aborter\n\n
    getAborter()\n
    '''
def remove():
    '''returns None\n\n
    remove(final IloCplex__Aborter abort)\n
    remove(final IloCplex__Callback cb)\n
    '''
def solve():
    '''returns boolean\n\n
    solve()\n
    solve(final IloCplex__Goal goal)\n
    '''
def setFormulationEpsValue():
    '''returns None\n\n
    setFormulationEpsValue(final double eps)\n
    '''
def getFormulationEpsValue():
    '''returns double\n\n
    getFormulationEpsValue()\n
    '''
def getSolnPoolMeanObjValue():
    '''returns double\n\n
    getSolnPoolMeanObjValue()\n
    '''
def getSolnPoolNsolns():
    '''returns int\n\n
    getSolnPoolNsolns()\n
    '''
def getSolnPoolNreplaced():
    '''returns int\n\n
    getSolnPoolNreplaced()\n
    '''
def delSolnPoolSoln():
    '''returns None\n\n
    delSolnPoolSoln(final int which)\n
    '''
def delSolnPoolSolns():
    '''returns None\n\n
    delSolnPoolSolns(final int begin, final int end)\n
    '''
def getCplexTime():
    '''returns double\n\n
    getCplexTime()\n
    '''
def getDetTime():
    '''returns double\n\n
    getDetTime()\n
    '''
def getNumCores():
    '''returns int\n\n
    getNumCores()\n
    '''
def add():
    '''returns IloCplex__Callback\n\n
    add(final IloCplex__Callback cb)\n
    '''
def inUse():
    '''returns boolean\n\n
    inUse(final IloCplex__Callback cb)\n
    '''
def _readVMConfig():
    '''returns None\n\n
    _readVMConfig(final String f)\n
    '''
def _copyVMConfig():
    '''returns None\n\n
    _copyVMConfig(final String f)\n
    '''
def mySwigValue():
    '''returns int\n\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    mySwigValue()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    toString()\n
    '''
