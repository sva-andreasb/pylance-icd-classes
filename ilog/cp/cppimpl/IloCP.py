def ():
    '''returns FunctionValues\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloEnv env)\n
    (final IloModel model)\n
    ()\n
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
def setIntParameter():
    '''returns None\n\n
    setIntParameter(final IntParam param, final double value)\n
    '''
def getIntParameter():
    '''returns double\n\n
    getIntParameter(final IntParam param)\n
    '''
def getIntParameterDefault():
    '''returns double\n\n
    getIntParameterDefault(final IntParam param)\n
    '''
def getIntInfo():
    '''returns double\n\n
    getIntInfo(final IntInfo info)\n
    '''
def setParameter():
    '''returns None\n\n
    setParameter(final IntParam param, final int value)\n
    setParameter(final NumParam param, final double value)\n
    setParameter(final String name, final double value)\n
    setParameter(final String name, final String value)\n
    '''
def getParameter():
    '''returns double\n\n
    getParameter(final IntParam param)\n
    getParameter(final String name)\n
    '''
def getParameterDefault():
    '''returns int\n\n
    getParameterDefault(final IntParam param)\n
    '''
def getNumParameter():
    '''returns double\n\n
    getNumParameter(final NumParam param)\n
    '''
def getNumParameterDefault():
    '''returns double\n\n
    getNumParameterDefault(final NumParam param)\n
    '''
def getInfo():
    '''returns int\n\n
    getInfo(final IntInfo info)\n
    '''
def getNumInfo():
    '''returns double\n\n
    getNumInfo(final NumInfo info)\n
    '''
def hasObjective():
    '''returns boolean\n\n
    hasObjective()\n
    '''
def setSearchPhases():
    '''returns None\n\n
    setSearchPhases()\n
    setSearchPhases(final IloSearchPhase phase)\n
    setSearchPhases(final IloSearchPhaseArray phaseArray)\n
    '''
def setStartingPoint():
    '''returns None\n\n
    setStartingPoint(final IloSolution sp)\n
    '''
def clearStartingPoint():
    '''returns None\n\n
    clearStartingPoint()\n
    '''
def clearExplanations():
    '''returns None\n\n
    clearExplanations()\n
    '''
def explainFailure():
    '''returns None\n\n
    explainFailure(final int failIndex)\n
    explainFailure(final IloIntArray failIndexArray)\n
    '''
def solve():
    '''returns boolean\n\n
    solve()\n
    solve(final IloSearchPhaseArray phaseArray)\n
    solve(final IloSearchPhase phase)\n
    '''
def startNewSearch():
    '''returns None\n\n
    startNewSearch()\n
    startNewSearch(final IloSearchPhaseArray phaseArray)\n
    startNewSearch(final IloSearchPhase phase)\n
    '''
def next():
    '''returns boolean\n\n
    next()\n
    '''
def endSearch():
    '''returns None\n\n
    endSearch()\n
    '''
def dumpModel():
    '''returns None\n\n
    dumpModel(final String filename)\n
    dumpModel(final ostream s)\n
    '''
def exportModel():
    '''returns None\n\n
    exportModel(final String filename)\n
    exportModel(final ostream s)\n
    '''
def importModel():
    '''returns None\n\n
    importModel(final String filename)\n
    importModel(final istream s)\n
    '''
def getAllIloIntVars():
    '''returns IloIntVarArray\n\n
    getAllIloIntVars()\n
    '''
def getAllIloIntervalVars():
    '''returns IloIntervalVarArray\n\n
    getAllIloIntervalVars()\n
    '''
def getAllIloStateFunctions():
    '''returns IloStateFunctionArray\n\n
    getAllIloStateFunctions()\n
    '''
def getAllIloIntervalSequenceVars():
    '''returns IloIntervalSequenceVarArray\n\n
    getAllIloIntervalSequenceVars()\n
    '''
def getAllConstrainedIloCumulFunctionExprs():
    '''returns IloCumulFunctionExprArray\n\n
    getAllConstrainedIloCumulFunctionExprs()\n
    '''
def getIloIntVar():
    '''returns IloIntVar\n\n
    getIloIntVar(final String name)\n
    '''
def getIloIntervalVar():
    '''returns IloIntervalVar\n\n
    getIloIntervalVar(final String name)\n
    '''
def getIloIntervalSequenceVar():
    '''returns IloIntervalSequenceVar\n\n
    getIloIntervalSequenceVar(final String name)\n
    '''
def getIloStateFunction():
    '''returns IloStateFunction\n\n
    getIloStateFunction(final String name)\n
    '''
def getIloCumulFunctionExpr():
    '''returns IloCumulFunctionExpr\n\n
    getIloCumulFunctionExpr(final String name)\n
    '''
def getValue():
    '''returns int\n\n
    getValue(final String intVarName)\n
    getValue(final IloObjective obj)\n
    getValue(final IloNumExprArg expr)\n
    getValue(final IloNumVar v)\n
    getValue(final IloCumulFunctionExpr f, final int t)\n
    getValue(final IloStateFunction f, final int t)\n
    getValue(final IloStateFunctionExpr expr, final int t)\n
    '''
def isPresent():
    '''returns boolean\n\n
    isPresent(final String intervalVarName)\n
    isPresent(final IloIntervalVar a)\n
    '''
def isAbsent():
    '''returns boolean\n\n
    isAbsent(final String intervalVarName)\n
    isAbsent(final IloIntervalVar a)\n
    '''
def getStart():
    '''returns int\n\n
    getStart(final String intervalVarName)\n
    getStart(final IloIntervalVar a)\n
    '''
def getEnd():
    '''returns int\n\n
    getEnd(final String intervalVarName)\n
    getEnd(final IloIntervalVar a)\n
    '''
def getSize():
    '''returns int\n\n
    getSize(final String intervalVarName)\n
    getSize(final IloIntervalVar a)\n
    '''
def getLength():
    '''returns int\n\n
    getLength(final String intervalVarName)\n
    getLength(final IloIntervalVar a)\n
    '''
def createDummyConcertModel():
    '''returns IloModel\n\n
    createDummyConcertModel()\n
    '''
def setLocation():
    '''returns None\n\n
    setLocation(final IloExtractable e, final String fileName, final int lineNumber)\n
    '''
def refineConflict():
    '''returns boolean\n\n
    refineConflict()\n
    refineConflict(final IloConstraintArray csts)\n
    refineConflict(final IloConstraintArray csts, final IloNumArray prefs)\n
    refineConflict(final IloSolution sol)\n
    '''
def getConflict():
    '''returns ConflictStatus\n\n
    getConflict(final IloConstraint cst)\n
    getConflict(final IloNumVar var)\n
    getConflict(final IloIntervalVar var)\n
    '''
def getIntConflict():
    '''returns int\n\n
    getIntConflict(final IloConstraint cst)\n
    getIntConflict(final IloNumVar var)\n
    getIntConflict(final IloIntervalVar var)\n
    '''
def writeConflict():
    '''returns None\n\n
    writeConflict(final ostream str)\n
    '''
def exportConflict():
    '''returns None\n\n
    exportConflict(final ostream str)\n
    '''
def propagate():
    '''returns boolean\n\n
    propagate(final IloConstraint constraint)\n
    propagate()\n
    '''
def store():
    '''returns None\n\n
    store(final IloSolution solution)\n
    '''
def restore():
    '''returns boolean\n\n
    restore(final IloSolution solution)\n
    '''
def printInformation():
    '''returns None\n\n
    printInformation()\n
    printInformation(final ostream stream)\n
    '''
def getObjValues():
    '''returns None\n\n
    getObjValues(final IloNumArray values)\n
    '''
def getNumberOfCriteria():
    '''returns int\n\n
    getNumberOfCriteria()\n
    '''
def getObjValue():
    '''returns double\n\n
    getObjValue(final int i)\n
    '''
def getMin():
    '''returns int\n\n
    getMin(final IloNumVar v)\n
    getMin(final IloIntVar var)\n
    '''
def getMax():
    '''returns int\n\n
    getMax(final IloNumVar v)\n
    getMax(final IloIntVar var)\n
    '''
def isInDomain():
    '''returns boolean\n\n
    isInDomain(final IloNumVar var, final int value)\n
    isInDomain(final IloIntVar var, final int value)\n
    '''
def getDomainSize():
    '''returns int\n\n
    getDomainSize(final IloNumVar var)\n
    '''
def isFixed():
    '''returns boolean\n\n
    isFixed(final IloNumVar var)\n
    isFixed(final IloIntVar var)\n
    isFixed(final IloIntervalVar a)\n
    isFixed(final IloIntervalSequenceVar seq)\n
    isFixed(final IloCumulFunctionExpr f)\n
    isFixed(final IloStateFunction f)\n
    '''
def getReduction():
    '''returns int\n\n
    getReduction(final IloIntVar x)\n
    '''
def getImpactOfLastAssignment():
    '''returns double\n\n
    getImpactOfLastAssignment(final IloIntVar x)\n
    '''
def getImpact():
    '''returns double\n\n
    getImpact(final IloIntVar x)\n
    getImpact(final IloIntVar x, final int value)\n
    '''
def getSuccessRate():
    '''returns double\n\n
    getSuccessRate(final IloIntVar x)\n
    getSuccessRate(final IloIntVar x, final int value)\n
    '''
def getRandomInt():
    '''returns int\n\n
    getRandomInt(final int n)\n
    '''
def getRandomNum():
    '''returns double\n\n
    getRandomNum()\n
    '''
def getVersion():
    '''returns String\n\n
    getVersion()\n
    '''
def abortSearch():
    '''returns None\n\n
    abortSearch()\n
    '''
def clearAbort():
    '''returns None\n\n
    clearAbort()\n
    '''
def clearLimit():
    '''returns None\n\n
    clearLimit()\n
    '''
def getStartMin():
    '''returns int\n\n
    getStartMin(final IloIntervalVar a)\n
    '''
def getStartMax():
    '''returns int\n\n
    getStartMax(final IloIntervalVar a)\n
    '''
def getEndMin():
    '''returns int\n\n
    getEndMin(final IloIntervalVar a)\n
    '''
def getEndMax():
    '''returns int\n\n
    getEndMax(final IloIntervalVar a)\n
    '''
def getSizeMin():
    '''returns int\n\n
    getSizeMin(final IloIntervalVar a)\n
    '''
def getSizeMax():
    '''returns int\n\n
    getSizeMax(final IloIntervalVar a)\n
    '''
def getLengthMin():
    '''returns int\n\n
    getLengthMin(final IloIntervalVar a)\n
    '''
def getLengthMax():
    '''returns int\n\n
    getLengthMax(final IloIntervalVar a)\n
    '''
def getFirst():
    '''returns IloIntervalVar\n\n
    getFirst(final IloIntervalSequenceVar seq)\n
    '''
def getLast():
    '''returns IloIntervalVar\n\n
    getLast(final IloIntervalSequenceVar seq)\n
    '''
def getNext():
    '''returns IloIntervalVar\n\n
    getNext(final IloIntervalSequenceVar seq, final IloIntervalVar a)\n
    '''
def getPrev():
    '''returns IloIntervalVar\n\n
    getPrev(final IloIntervalSequenceVar seq, final IloIntervalVar a)\n
    '''
def getNumberOfSegments():
    '''returns int\n\n
    getNumberOfSegments(final IloCumulFunctionExpr f)\n
    getNumberOfSegments(final IloStateFunction f)\n
    getNumberOfSegments(final IloStateFunctionExpr expr)\n
    '''
def getNumberOfSegmentsAsNum():
    '''returns double\n\n
    getNumberOfSegmentsAsNum(final IloCumulFunctionExpr f)\n
    '''
def getSegmentStart():
    '''returns int\n\n
    getSegmentStart(final IloCumulFunctionExpr f, final int i)\n
    getSegmentStart(final IloStateFunction f, final int s)\n
    getSegmentStart(final IloStateFunctionExpr expr, final int i)\n
    '''
def getSegmentStartAsNum():
    '''returns double\n\n
    getSegmentStartAsNum(final IloCumulFunctionExpr f, final int i)\n
    getSegmentStartAsNum(final IloStateFunction f, final int s)\n
    '''
def getSegmentEnd():
    '''returns int\n\n
    getSegmentEnd(final IloCumulFunctionExpr f, final int i)\n
    getSegmentEnd(final IloStateFunction f, final int s)\n
    getSegmentEnd(final IloStateFunctionExpr expr, final int i)\n
    '''
def getSegmentEndAsNum():
    '''returns double\n\n
    getSegmentEndAsNum(final IloCumulFunctionExpr f, final int i)\n
    getSegmentEndAsNum(final IloStateFunction f, final int s)\n
    '''
def getSegmentValue():
    '''returns int\n\n
    getSegmentValue(final IloCumulFunctionExpr f, final int i)\n
    getSegmentValue(final IloStateFunction f, final int s)\n
    getSegmentValue(final IloStateFunctionExpr expr, final int i)\n
    '''
def getSegmentValueAsNum():
    '''returns double\n\n
    getSegmentValueAsNum(final IloCumulFunctionExpr f, final int i)\n
    getSegmentValueAsNum(final IloStateFunction f, final int s)\n
    '''
def getHeightAtStart():
    '''returns int\n\n
    getHeightAtStart(final IloIntervalVar var, final IloCumulFunctionExpr f)\n
    '''
def getHeightAtEnd():
    '''returns int\n\n
    getHeightAtEnd(final IloIntervalVar var, final IloCumulFunctionExpr f)\n
    '''
def getValueAsNum():
    '''returns double\n\n
    getValueAsNum(final IloCumulFunctionExpr f, final int t)\n
    getValueAsNum(final IloStateFunction f, final int t)\n
    '''
def storeWarningsInternally():
    '''returns None\n\n
    storeWarningsInternally(final boolean store)\n
    storeWarningsInternally()\n
    '''
def iterator_IntVarIterator():
    '''returns IloCP_IntVarIterator\n\n
    iterator_IntVarIterator(final IloIntVar var)\n
    iterator_IntVarIterator(final IloNumVar var)\n
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
    '''
