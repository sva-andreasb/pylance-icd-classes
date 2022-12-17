def ():
    '''returns IloOplModel\n\n
    (final long cPtr, final boolean cMemoryOwn)\n
    (final IloOplModelDefinition definition, final ilog.cplex.cppimpl.IloCplex cplex)\n
    (final IloEnv env, final IloOplModelDefinition definition, final ilog.cplex.cppimpl.IloCplex cplex)\n
    (final IloOplSettings settings, final IloOplModelDefinition definition, final ilog.cplex.cppimpl.IloCplex cplex)\n
    (final IloEnv env, final IloOplSettings settings, final IloOplModelDefinition definition, final ilog.cplex.cppimpl.IloCplex cplex)\n
    (final IloOplModelDefinition definition, final ilog.cp.cppimpl.IloCP cp)\n
    (final IloEnv env, final IloOplModelDefinition definition, final ilog.cp.cppimpl.IloCP cp)\n
    (final IloOplSettings settings, final IloOplModelDefinition definition, final ilog.cp.cppimpl.IloCP cp)\n
    (final IloEnv env, final IloOplSettings settings, final IloOplModelDefinition definition, final ilog.cp.cppimpl.IloCP cp)\n
    '''
def setOwn():
    '''returns None\n\n
    setOwn(final boolean cMemoryOwn)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def setCplex():
    '''returns None\n\n
    setCplex(final IloCplex cplex)\n
    '''
def getCplex():
    '''returns IloCplex\n\n
    getCplex()\n
    '''
def setCP():
    '''returns None\n\n
    setCP(final IloCP cp)\n
    '''
def getCP():
    '''returns IloCP\n\n
    getCP()\n
    '''
def generate():
    '''returns None\n\n
    generate()\n
    generate(final IloOplLabelCallback cb)\n
    '''
def getObjective():
    '''returns IloObjective\n\n
    getObjective()\n
    '''
def printData():
    '''returns None\n\n
    printData(final OutputStream outs)\n
    '''
def printCalculatedData():
    '''returns None\n\n
    printCalculatedData(final OutputStream outs)\n
    '''
def printExternalData():
    '''returns None\n\n
    printExternalData(final OutputStream outs)\n
    '''
def printInternalData():
    '''returns None\n\n
    printInternalData(final OutputStream outs)\n
    '''
def printSolution():
    '''returns None\n\n
    printSolution(final OutputStream outs)\n
    '''
def printConflict():
    '''returns int\n\n
    printConflict(final OutputStream outs)\n
    '''
def printRelaxation():
    '''returns int\n\n
    printRelaxation(final OutputStream outs)\n
    '''
def getElementIterator():
    '''returns Iterator\n\n
    getElementIterator()\n
    getElementIterator(final boolean ownElements)\n
    '''
def hasCplex():
    '''returns boolean\n\n
    hasCplex()\n
    '''
def hasCP():
    '''returns boolean\n\n
    hasCP()\n
    '''
def end():
    '''returns None\n\n
    end()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getSourceName():
    '''returns String\n\n
    getSourceName()\n
    '''
def applyOpsSettings():
    '''returns None\n\n
    applyOpsSettings(final String baseDir, final String opsFile)\n
    '''
def resolvePath():
    '''returns String\n\n
    resolvePath(final String name)\n
    '''
def resolveStream():
    '''returns istream\n\n
    resolveStream(final String name)\n
    '''
def getSettings():
    '''returns IloOplSettings\n\n
    getSettings()\n
    '''
def setSettings():
    '''returns None\n\n
    setSettings(final IloOplSettings settings)\n
    '''
def getModelDefinition():
    '''returns IloOplModelDefinition\n\n
    getModelDefinition()\n
    '''
def addDataSource():
    '''returns None\n\n
    addDataSource(final IloOplDataSource source)\n
    '''
def addSettings():
    '''returns None\n\n
    addSettings(final IloOplSettings settings)\n
    '''
def registerPostProcessListener():
    '''returns None\n\n
    registerPostProcessListener(final IloOplPostProcessListener d)\n
    '''
def unregisterPostProcessListener():
    '''returns None\n\n
    unregisterPostProcessListener(final IloOplPostProcessListener d)\n
    '''
def internalSolve():
    '''returns boolean\n\n
    internalSolve()\n
    '''
def getElement():
    '''returns IloOplElement\n\n
    getElement(final String name)\n
    '''
def hasElement():
    '''returns boolean\n\n
    hasElement(final String name)\n
    '''
def getElementNamesInPostProcessing():
    '''returns IloStringArray\n\n
    getElementNamesInPostProcessing()\n
    '''
def setZeroSolutionGetter():
    '''returns None\n\n
    setZeroSolutionGetter()\n
    '''
def setStatusSolutionGetter():
    '''returns None\n\n
    setStatusSolutionGetter(final boolean status)\n
    setStatusSolutionGetter(final boolean status, final boolean warnObsolete)\n
    '''
def setMIPInfoSolutionGetter():
    '''returns None\n\n
    setMIPInfoSolutionGetter(final IloCplex__Callback cb)\n
    '''
def setZeroDataSource():
    '''returns None\n\n
    setZeroDataSource()\n
    '''
def getSolutionGetter():
    '''returns IloOplSolutionGetter\n\n
    getSolutionGetter()\n
    '''
def resetSolutionGetter():
    '''returns None\n\n
    resetSolutionGetter()\n
    '''
def hasPublishers():
    '''returns boolean\n\n
    hasPublishers()\n
    '''
def registerCustomDataHandler():
    '''returns None\n\n
    registerCustomDataHandler(final String customId, final IloOplCustomDataHandler handler)\n
    '''
def unregisterCustomDataHandler():
    '''returns None\n\n
    unregisterCustomDataHandler(final String customId)\n
    '''
def makeScriptExpression():
    '''returns IloOplScriptExpression\n\n
    makeScriptExpression(final String name, final IloStringArray paramNames, final String code)\n
    '''
def getConstraintElementItem():
    '''returns IloConstraint\n\n
    getConstraintElementItem(final String name, final IloOplDataElements indices)\n
    '''
def getModel():
    '''returns IloModel\n\n
    getModel()\n
    '''
def getOuterModel():
    '''returns IloModel\n\n
    getOuterModel()\n
    '''
def convertAllIntVars():
    '''returns None\n\n
    convertAllIntVars()\n
    '''
def unconvertAllIntVars():
    '''returns None\n\n
    unconvertAllIntVars()\n
    '''
def cppHasCP():
    '''returns boolean\n\n
    cppHasCP()\n
    '''
def isUsingCplex():
    '''returns boolean\n\n
    isUsingCplex()\n
    '''
def isUsingCP():
    '''returns boolean\n\n
    isUsingCP()\n
    '''
def isGenerated():
    '''returns boolean\n\n
    isGenerated()\n
    '''
def loadDataOnly():
    '''returns None\n\n
    loadDataOnly()\n
    '''
def processDecisionExpr():
    '''returns None\n\n
    processDecisionExpr(final IloNumExprArg expr, final IloOplDecisionExprCallback callback)\n
    '''
def processDecisionExprSolution():
    '''returns None\n\n
    processDecisionExprSolution(final String name, final IloOplDecisionExprSolutionCallback callback)\n
    '''
def evaluateConstraintLeft():
    '''returns double\n\n
    evaluateConstraintLeft(final IloMapIndexArray indexArray, final IloMapIndexArray valueArray, final IloConstraint ct)\n
    '''
def evaluateConstraintMid():
    '''returns double\n\n
    evaluateConstraintMid(final IloMapIndexArray indexArray, final IloMapIndexArray valueArray, final IloConstraint ct)\n
    '''
def evaluateConstraintRight():
    '''returns double\n\n
    evaluateConstraintRight(final IloMapIndexArray indexArray, final IloMapIndexArray valueArray, final IloConstraint ct)\n
    '''
def postProcess():
    '''returns None\n\n
    postProcess()\n
    '''
def warnNeverUsedElements():
    '''returns None\n\n
    warnNeverUsedElements()\n
    '''
def main():
    '''returns int\n\n
    main()\n
    '''
def makeDataElements():
    '''returns IloOplDataElements\n\n
    makeDataElements()\n
    '''
def getConflictIterator():
    '''returns IloOplConflictIterator\n\n
    getConflictIterator()\n
    '''
def getRelaxationIterator():
    '''returns IloOplRelaxationIterator\n\n
    getRelaxationIterator()\n
    '''
def setPoolSolution():
    '''returns boolean\n\n
    setPoolSolution(final int solId)\n
    '''
def tuneParam():
    '''returns boolean\n\n
    tuneParam(final IloCplex__ParameterSet fixedSet)\n
    tuneParam(final IloCplex__ParameterSet fixedSet, final IloCplex__ParameterSet resultSet)\n
    '''
def registerDisposeListener():
    '''returns None\n\n
    registerDisposeListener(final IloOplDisposeListener d)\n
    '''
def unregisterDisposeListener():
    '''returns None\n\n
    unregisterDisposeListener(final IloOplDisposeListener d)\n
    '''
def setProgressListener():
    '''returns None\n\n
    setProgressListener(final IloOplProgressListener l)\n
    '''
def removeProgressListener():
    '''returns None\n\n
    removeProgressListener(final IloOplProgressListener l)\n
    '''
def getProgressListener():
    '''returns IloOplProgressListener\n\n
    getProgressListener()\n
    '''
def saveResultsInText():
    '''returns None\n\n
    saveResultsInText(final String filePath)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getModelID():
    '''returns int\n\n
    getModelID()\n
    '''
