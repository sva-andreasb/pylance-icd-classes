Balanced = "int  0"
Feasibility = "int  1"
Optimality = "int  2"
BestBound = "int  1"
HiddenFeas = "int  4"
MinInfeas = "int  -1"
DefaultVarSel = "int  0"
MaxInfeas = "int  1"
Pseudo = "int  2"
Strong = "int  3"
PseudoReduced = "int  4"
DFS = "int  0"
BestEst = "int  2"
BestEstAlt = "int  3"
RampupDisabled = "int  -1"
RampupAuto = "int  0"
RampupDynamic = "int  1"
RampupInfinite = "int  2"
Partial = "int  -1"
Auto = "int  0"
Devex = "int  5"
Steep = "int  2"
SteepQStart = "int  4"
Full = "int  1"
FullSteep = "int  3"
IntType = "int  0"
DoubleType = "int  1"
BooleanType = "int  2"
StringType = "int  3"
LongType = "int  4"
UnknownType = "int  5"
Propagate = "int  1"
Presolve = "int  2"
IIS = "int  3"
Solve = "int  4"
MinSum = "int  0"
OptSum = "int  1"
MinInf = "int  2"
OptInf = "int  3"
MinQuad = "int  4"
OptQuad = "int  5"
def readVMConfig():
    '''returns None\n\n
    readVMConfig(final String file)\n
    '''
def hasVMConfig():
    '''returns boolean\n\n
    hasVMConfig()\n
    '''
def delVMConfig():
    '''returns None\n\n
    delVMConfig()\n
    '''
def copyVMConfig():
    '''returns None\n\n
    copyVMConfig(final String xmlString)\n
    '''
def getMIPRelativeGap():
    '''returns double\n\n
    getMIPRelativeGap()\n
    '''
def remove():
    '''returns None\n\n
    remove(final IloAddable object)\n
    remove(final Callback cb)\n
    remove()\n
    remove()\n
    '''
def getModel():
    '''returns IloModel\n\n
    getModel()\n
    '''
def setModel():
    '''returns None\n\n
    setModel(final IloModel model)\n
    '''
def le():
    '''returns IloConstraint\n\n
    le(final IloNumExpr e1, final IloNumExpr e2, final String name)\n
    '''
def ge():
    '''returns IloConstraint\n\n
    ge(final IloNumExpr e1, final IloNumExpr e2, final String name)\n
    '''
def eq():
    '''returns IloConstraint\n\n
    eq(final IloNumExpr e1, final IloNumExpr e2, final String name)\n
    '''
def iterator():
    '''returns Iterator\n\n
    iterator()\n
    '''
def numVar():
    '''returns IloNumVar\n\n
    numVar(final IloColumn column, final double lb, final double ub, final IloNumVarType type, final String name)\n
    numVar(final IloColumn column, final double lb, final double ub, final IloNumVarType type)\n
    numVar(final IloColumn column, final double lb, final double ub, final String name)\n
    numVar(final IloColumn column, final double lb, final double ub)\n
    '''
def numVarArray():
    '''returns IloNumVar[]\n\n
    numVarArray(final IloColumnArray cols, final double lb, final double ub, final IloNumVarType type)\n
    numVarArray(final IloColumnArray cols, final double lb, final double ub, final IloNumVarType type, final String[] name)\n
    numVarArray(final IloColumnArray cols, final double[] lb, final double[] ub, final IloNumVarType[] type)\n
    numVarArray(final IloColumnArray cols, final double[] lb, final double[] ub, final IloNumVarType[] type, final String[] name)\n
    numVarArray(final IloColumnArray cols, final double lb, final double ub)\n
    numVarArray(final IloColumnArray cols, final double[] lb, final double[] ub)\n
    numVarArray(final IloColumnArray cols, final double lb, final double ub, final String[] name)\n
    numVarArray(final IloColumnArray cols, final double[] lb, final double[] ub, final String[] name)\n
    '''
def intVar():
    '''returns IloIntVar\n\n
    intVar(final IloColumn column, final int lb, final int ub)\n
    intVar(final IloColumn column, final int lb, final int ub, final String name)\n
    '''
def intVarArray():
    '''returns IloIntVar[]\n\n
    intVarArray(final IloColumnArray cols, final int lb, final int ub, final String[] name)\n
    intVarArray(final IloColumnArray cols, final int[] lb, final int[] ub, final String[] name)\n
    intVarArray(final IloColumnArray cols, final int lb, final int ub)\n
    intVarArray(final IloColumnArray cols, final int[] lb, final int[] ub)\n
    '''
def boolVar():
    '''returns IloIntVar\n\n
    boolVar(final IloColumn column, final String name)\n
    boolVar(final IloColumn column)\n
    '''
def boolVarArray():
    '''returns IloIntVar[]\n\n
    boolVarArray(final IloColumnArray cols)\n
    boolVarArray(final IloColumnArray cols, final String[] name)\n
    '''
def piecewiseLinear():
    '''returns IloNumExpr\n\n
    piecewiseLinear(final IloNumExpr expr, final double[] points, final double[] slopes, final double a, final double fa)\n
    piecewiseLinear(final IloNumExpr expr, final double[] points, final int startPoints, final int num, final double[] slopes, final int startSlopes, final double a, final double fa)\n
    piecewiseLinear(final IloNumExpr node, final double firstSlope, final double[] points, final double[] values, final double lastSlope)\n
    '''
def addToExpr():
    '''returns None\n\n
    addToExpr(final IloObjective obj, final IloNumExpr expr)\n
    addToExpr(final IloRange rng, final IloNumExpr expr)\n
    '''
def setLinearCoef():
    '''returns None\n\n
    setLinearCoef(final IloForAllRange ct, final IloNumVar var, final double val)\n
    setLinearCoef(final IloForAllRange ct, final double val, final IloNumVar var)\n
    setLinearCoef(final IloObjective obj, final double val, final IloNumVar var)\n
    setLinearCoef(final IloObjective obj, final IloNumVar var, final double val)\n
    setLinearCoef(final IloRange rng, final double val, final IloNumVar var)\n
    setLinearCoef(final IloRange rng, final IloNumVar var, final double val)\n
    '''
def setLinearCoefs():
    '''returns None\n\n
    setLinearCoefs(final IloForAllRange ct, final double[] val, final IloNumVar[] var)\n
    setLinearCoefs(final IloForAllRange ct, final IloNumVar[] var, final double[] val)\n
    setLinearCoefs(final IloForAllRange ct, final double[] val, final IloNumVar[] var, final int start, final int num)\n
    setLinearCoefs(final IloForAllRange ct, final IloNumVar[] var, final double[] val, final int start, final int num)\n
    setLinearCoefs(final IloObjective obj, final double[] val, final IloNumVar[] var)\n
    setLinearCoefs(final IloObjective obj, final IloNumVar[] var, final double[] val)\n
    setLinearCoefs(final IloObjective obj, final double[] val, final IloNumVar[] var, final int start, final int num)\n
    setLinearCoefs(final IloObjective obj, final IloNumVar[] var, final double[] val, final int start, final int num)\n
    setLinearCoefs(final IloRange rng, final double[] val, final IloNumVar[] var)\n
    setLinearCoefs(final IloRange rng, final IloNumVar[] var, final double[] val)\n
    setLinearCoefs(final IloRange rng, final double[] val, final IloNumVar[] var, final int start, final int num)\n
    setLinearCoefs(final IloRange rng, final IloNumVar[] var, final double[] val, final int start, final int num)\n
    '''
def semiContVar():
    '''returns IloSemiContVar\n\n
    semiContVar(final double lb, final double ub, final IloNumVarType type, final String name)\n
    semiContVar(final double lb, final double ub, final IloNumVarType type)\n
    semiContVar(final IloColumn column, final double lb, final double ub, final IloNumVarType type, final String name)\n
    semiContVar(final IloColumn column, final double lb, final double ub, final IloNumVarType type)\n
    '''
def semiContVarArray():
    '''returns IloSemiContVar[]\n\n
    semiContVarArray(final int n, final double lb, final double ub, final IloNumVarType type)\n
    semiContVarArray(final int n, final double[] lb, final double[] ub, final IloNumVarType[] type)\n
    semiContVarArray(final int n, final double lb, final double ub, final IloNumVarType type, final String[] name)\n
    semiContVarArray(final int n, final double[] lb, final double[] ub, final IloNumVarType[] type, final String[] name)\n
    semiContVarArray(final IloColumnArray cols, final double lb, final double ub, final IloNumVarType type)\n
    semiContVarArray(final IloColumnArray cols, final double[] lb, final double[] ub, final IloNumVarType[] type)\n
    semiContVarArray(final IloColumnArray cols, final double lb, final double ub, final IloNumVarType type, final String[] name)\n
    semiContVarArray(final IloColumnArray cols, final double[] lb, final double[] ub, final IloNumVarType[] type, final String[] name)\n
    '''
def minimize():
    '''returns IloObjective\n\n
    minimize()\n
    minimize(final String name)\n
    '''
def maximize():
    '''returns IloObjective\n\n
    maximize()\n
    maximize(final String name)\n
    '''
def objective():
    '''returns IloObjective\n\n
    objective(final IloObjectiveSense sense)\n
    objective(final IloObjectiveSense sense, final String name)\n
    '''
def addMinimize():
    '''returns IloObjective\n\n
    addMinimize()\n
    addMinimize(final String name)\n
    '''
def addMaximize():
    '''returns IloObjective\n\n
    addMaximize()\n
    addMaximize(final String name)\n
    '''
def addObjective():
    '''returns IloObjective\n\n
    addObjective(final IloObjectiveSense sense)\n
    addObjective(final IloObjectiveSense sense, final String name)\n
    '''
def conversion():
    '''returns IloConversion\n\n
    conversion(final IloNumVar var, final IloNumVarType type, final String name)\n
    conversion(final IloNumVar var, final IloNumVarType type)\n
    conversion(final IloNumVar[] var, final IloNumVarType type, final String name)\n
    conversion(final IloNumVar[] ilovar, final IloNumVarType type)\n
    conversion(final IloNumVar[] var, final IloNumVarType[] type, final String name)\n
    conversion(final IloNumVar[] ilovar, final IloNumVarType[] type)\n
    '''
def addLPMatrix():
    '''returns IloLPMatrix\n\n
    addLPMatrix(final String name)\n
    addLPMatrix()\n
    '''
def LPMatrix():
    '''returns IloLPMatrix\n\n
    LPMatrix(final String name)\n
    LPMatrix()\n
    '''
def addRange():
    '''returns IloRange\n\n
    addRange(final double lb, final double ub, final String name)\n
    addRange(final double lb, final double ub)\n
    '''
def range():
    '''returns IloRange\n\n
    range(final double lb, final double ub, final String name)\n
    range(final double lb, final double ub)\n
    '''
def addSOS1():
    '''returns IloSOS1\n\n
    addSOS1(final IloNumVar[] var, final double[] val)\n
    addSOS1(final IloNumVar[] var, final double[] val, final int start, final int num)\n
    addSOS1(final IloNumVar[] var, final double[] val, final String name)\n
    addSOS1(final IloNumVar[] var, final double[] val, final int start, final int num, final String name)\n
    '''
def SOS1():
    '''returns IloSOS1\n\n
    SOS1(final IloNumVar[] var, final double[] val)\n
    SOS1(final IloNumVar[] var, final double[] val, final int start, final int num)\n
    SOS1(final IloNumVar[] var, final double[] val, final String name)\n
    SOS1(final IloNumVar[] var, final double[] val, final int start, final int num, final String name)\n
    '''
def addSOS2():
    '''returns IloSOS2\n\n
    addSOS2(final IloNumVar[] var, final double[] val)\n
    addSOS2(final IloNumVar[] var, final double[] val, final int start, final int num)\n
    addSOS2(final IloNumVar[] var, final double[] val, final String name)\n
    addSOS2(final IloNumVar[] var, final double[] val, final int start, final int num, final String name)\n
    '''
def SOS2():
    '''returns IloSOS2\n\n
    SOS2(final IloNumVar[] var, final double[] val)\n
    SOS2(final IloNumVar[] var, final double[] val, final int start, final int num)\n
    SOS2(final IloNumVar[] var, final double[] val, final String name)\n
    SOS2(final IloNumVar[] var, final double[] val, final int start, final int num, final String name)\n
    '''
def column():
    '''returns IloColumn\n\n
    column(final IloRange rng, final double val)\n
    column(final IloObjective obj, final double val)\n
    column(final IloLPMatrix lp)\n
    column(final IloLPMatrix lp, final int[] ind, final double[] val)\n
    column(final IloLPMatrix lp, final int[] ind, final double[] val, final int start, final int num)\n
    '''
def columnArray():
    '''returns IloColumnArray\n\n
    columnArray(final IloRange rng, final double[] val)\n
    columnArray(final IloRange rng, final double[] val, final int start, final int num)\n
    columnArray(final IloObjective obj, final double[] val)\n
    columnArray(final IloObjective obj, final double[] val, final int start, final int num)\n
    columnArray(final IloLPMatrix lp, final int num, final int[][] ind, final double[][] val)\n
    columnArray(final IloLPMatrix lp, final int num)\n
    '''
def delete():
    '''returns None\n\n
    delete(final IloCopyable obj)\n
    delete(final IloCopyable[] obj)\n
    delete(final IloCopyable[] objs, final int beg, final int num)\n
    '''
def addUserCut():
    '''returns IloConstraint\n\n
    addUserCut(final IloConstraint cut)\n
    '''
def addUserCuts():
    '''returns IloConstraint[]\n\n
    addUserCuts(final IloConstraint[] cuts)\n
    addUserCuts(final IloConstraint[] cuts, final int start, final int num)\n
    '''
def clearUserCuts():
    '''returns None\n\n
    clearUserCuts()\n
    '''
def addLazyConstraint():
    '''returns IloConstraint\n\n
    addLazyConstraint(final IloConstraint cut)\n
    '''
def addLazyConstraints():
    '''returns IloConstraint[]\n\n
    addLazyConstraints(final IloConstraint[] cut)\n
    addLazyConstraints(final IloConstraint[] cut, final int start, final int num)\n
    '''
def clearLazyConstraints():
    '''returns None\n\n
    clearLazyConstraints()\n
    '''
def addCut():
    '''returns IloConstraint\n\n
    addCut(final IloConstraint cut)\n
    '''
def addCuts():
    '''returns IloConstraint[]\n\n
    addCuts(final IloConstraint[] cut)\n
    addCuts(final IloConstraint[] cut, final int start, final int num)\n
    '''
def clearCuts():
    '''returns None\n\n
    clearCuts()\n
    '''
def exportModel():
    '''returns None\n\n
    exportModel(final String name)\n
    '''
def importModel():
    '''returns None\n\n
    importModel(final String name)\n
    '''
def getMatrix():
    '''returns IloLPMatrixImpl\n\n
    getMatrix()\n
    '''
def clearModel():
    '''returns None\n\n
    clearModel()\n
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
def getNSOS1():
    '''returns int\n\n
    getNSOS1()\n
    '''
def getNSOS2():
    '''returns int\n\n
    getNSOS2()\n
    '''
def getNSOSs():
    '''returns int\n\n
    getNSOSs()\n
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
def isMIP():
    '''returns boolean\n\n
    isMIP()\n
    '''
def isQO():
    '''returns boolean\n\n
    isQO()\n
    '''
def isQC():
    '''returns boolean\n\n
    isQC()\n
    '''
def LPMatrixIterator():
    '''returns Iterator\n\n
    LPMatrixIterator()\n
    '''
def rangeIterator():
    '''returns Iterator\n\n
    rangeIterator()\n
    '''
def conversionIterator():
    '''returns Iterator\n\n
    conversionIterator()\n
    '''
def SOS1iterator():
    '''returns Iterator\n\n
    SOS1iterator()\n
    '''
def SOS2iterator():
    '''returns Iterator\n\n
    SOS2iterator()\n
    '''
def getObjective():
    '''returns IloObjective\n\n
    getObjective()\n
    '''
def getStatus():
    '''returns int\n\n
    getStatus()\n
    getStatus()\n
    '''
def isPrimalFeasible():
    '''returns boolean\n\n
    isPrimalFeasible()\n
    isPrimalFeasible()\n
    isPrimalFeasible()\n
    '''
def isDualFeasible():
    '''returns boolean\n\n
    isDualFeasible()\n
    isDualFeasible()\n
    isDualFeasible()\n
    '''
def use():
    '''returns None\n\n
    use(final Aborter aborter)\n
    use(final Callback cb)\n
    '''
def getAborter():
    '''returns Aborter\n\n
    getAborter()\n
    '''
def setParam():
    '''returns None\n\n
    setParam(final IntParam which, final int val)\n
    setParam(final BooleanParam which, final boolean val)\n
    setParam(final LongParam which, final long val)\n
    setParam(final DoubleParam which, final double val)\n
    setParam(final StringParam which, final String val)\n
    setParam(final IntParam which, final int val)\n
    setParam(final StringParam which, final String val)\n
    setParam(final BooleanParam which, final boolean val)\n
    setParam(final DoubleParam which, final double val)\n
    '''
def getParam():
    '''returns double\n\n
    getParam(final IntParam which)\n
    getParam(final BooleanParam which)\n
    getParam(final LongParam which)\n
    getParam(final DoubleParam which)\n
    getParam(final StringParam which)\n
    getParam(final IntParam which)\n
    getParam(final StringParam which)\n
    getParam(final BooleanParam which)\n
    getParam(final DoubleParam which)\n
    '''
def getMin():
    '''returns double\n\n
    getMin(final IntParam which)\n
    getMin(final DoubleParam which)\n
    '''
def getMax():
    '''returns double\n\n
    getMax(final IntParam which)\n
    getMax(final DoubleParam which)\n
    '''
def getDefault():
    '''returns String\n\n
    getDefault(final IntParam which)\n
    getDefault(final BooleanParam which)\n
    getDefault(final LongParam which)\n
    getDefault(final DoubleParam which)\n
    getDefault(final StringParam which)\n
    '''
def setDefaults():
    '''returns None\n\n
    setDefaults()\n
    '''
def getVersion():
    '''returns String\n\n
    getVersion()\n
    '''
def setDeleteMode():
    '''returns None\n\n
    setDeleteMode(final DeleteMode mode)\n
    '''
def getDeleteMode():
    '''returns DeleteMode\n\n
    getDeleteMode()\n
    '''
def getCplexStatus():
    '''returns CplexStatus\n\n
    getCplexStatus()\n
    '''
def getCplexSubStatus():
    '''returns CplexStatus\n\n
    getCplexSubStatus()\n
    '''
def getAlgorithm():
    '''returns int\n\n
    getAlgorithm()\n
    '''
def getSubAlgorithm():
    '''returns int\n\n
    getSubAlgorithm()\n
    '''
def getObjValue():
    '''returns double\n\n
    getObjValue()\n
    getObjValue(final int soln)\n
    '''
def getBestObjValue():
    '''returns double\n\n
    getBestObjValue()\n
    '''
def getCutoff():
    '''returns double\n\n
    getCutoff()\n
    '''
def getValues():
    '''returns double[]\n\n
    getValues(final IloLPMatrix matrix)\n
    getValues(final IloLPMatrix matrix, final int soln)\n
    getValues(final IloLPMatrix matrix, final int start, final int num)\n
    getValues(final IloLPMatrix matrix, final int start, final int num, final int soln)\n
    getValues(final IloNumVar[] var)\n
    getValues(final IloNumVar[] var, final int soln)\n
    getValues(final IloNumVar[] var, final int start, final int num)\n
    getValues(final IloNumVar[] var, final int start, final int num, final int soln)\n
    '''
def getValue():
    '''returns double\n\n
    getValue(final IloNumVar var)\n
    getValue(final IloNumVar var, final int soln)\n
    getValue(final IloNumExpr expr)\n
    getValue(final IloNumExpr expr, final int soln)\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    getValue()\n
    '''
def getReducedCosts():
    '''returns double[]\n\n
    getReducedCosts(final IloLPMatrix matrix)\n
    getReducedCosts(final IloLPMatrix matrix, final int start, final int num)\n
    getReducedCosts(final IloNumVar[] var)\n
    getReducedCosts(final IloNumVar[] var, final int start, final int num)\n
    '''
def getReducedCost():
    '''returns double\n\n
    getReducedCost(final IloNumVar ivar)\n
    '''
def getDuals():
    '''returns double[]\n\n
    getDuals(final IloLPMatrix matrix)\n
    getDuals(final IloLPMatrix matrix, final int start, final int num)\n
    getDuals(final IloRange[] rng)\n
    getDuals(final IloRange[] rng, final int start, final int num)\n
    '''
def getDual():
    '''returns double\n\n
    getDual(final IloRange rng)\n
    getDual(final IloForAllRange v)\n
    '''
def getSlacks():
    '''returns double[]\n\n
    getSlacks(final IloLPMatrix matrix)\n
    getSlacks(final IloLPMatrix matrix, final int soln)\n
    getSlacks(final IloLPMatrix matrix, final int start, final int num)\n
    getSlacks(final IloLPMatrix matrix, final int start, final int num, final int soln)\n
    getSlacks(final IloRange[] rng)\n
    getSlacks(final IloRange[] rng, final int soln)\n
    getSlacks(final IloRange[] rng, final int start, final int num)\n
    getSlacks(final IloRange[] rng, final int start, final int num, final int soln)\n
    '''
def getSlack():
    '''returns double\n\n
    getSlack(final IloRange rng)\n
    getSlack(final IloRange rng, final int soln)\n
    getSlack(final IloForAllRange range)\n
    '''
def getInfeasibilities():
    '''returns double[]\n\n
    getInfeasibilities(final IloConstraint[] con, final int start, final int num)\n
    getInfeasibilities(final IloNumVar[] var)\n
    getInfeasibilities(final IloNumVar[] var, final int start, final int num)\n
    getInfeasibilities(final IloConstraint[] con)\n
    getInfeasibilities(final IloLPMatrix matrix)\n
    getInfeasibilities(final IloLPMatrix matrix, final int start, final int num)\n
    '''
def getInfeasibility():
    '''returns double\n\n
    getInfeasibility(final IloConstraint con)\n
    getInfeasibility(final IloNumVar ivar)\n
    '''
def getAX():
    '''returns double[]\n\n
    getAX(final IloLPMatrix matrix)\n
    getAX(final IloLPMatrix matrix, final int start, final int num)\n
    getAX(final IloRange rng)\n
    getAX(final IloRange[] rng)\n
    getAX(final IloRange[] rng, final int start, final int num)\n
    getAX(final IloForAllRange v)\n
    getAX(final IloForAllRange[] rngs)\n
    '''
def getBasisStatus():
    '''returns BasisStatus\n\n
    getBasisStatus(final IloNumVar var)\n
    getBasisStatus(final IloConstraint con)\n
    '''
def getBasisStatuses():
    '''returns BasisStatus[]\n\n
    getBasisStatuses(final IloNumVar[] var)\n
    getBasisStatuses(final IloNumVar[] var, final int start, final int num)\n
    getBasisStatuses(final IloConstraint[] con)\n
    getBasisStatuses(final IloConstraint[] con, final int start, final int num)\n
    '''
def setBasisStatuses():
    '''returns None\n\n
    setBasisStatuses(final IloNumVar[] var, final BasisStatus[] cstat, final IloRange[] con, final BasisStatus[] rstat)\n
    setBasisStatuses(final IloNumVar[] var, final BasisStatus[] cstat, final int cstart, final int cnum, final IloConstraint[] con, final BasisStatus[] rstat, final int rstart, final int rnum)\n
    '''
def setStart():
    '''returns None\n\n
    setStart(final double[] x, final double[] dj, final IloNumVar[] var, final double[] slack, final double[] pi, final IloRange[] rng)\n
    setStart(final double[] x, final double[] dj, final IloNumVar[] var, final int vstart, final int vnum, final double[] slack, final double[] pi, final IloRange[] rng, final int rstart, final int rnum)\n
    '''
def feasOpt():
    '''returns boolean\n\n
    feasOpt(final IloConstraint[] cts, final double[] prefs)\n
    feasOpt(final IloRange[] rngs, final double[] rnglb, final double[] rngub, final IloNumVar[] vars, final double[] varlb, final double[] varub)\n
    feasOpt(final IloNumVar[] vars, final double[] varlb, final double[] varub)\n
    feasOpt(final IloRange[] rngs, final double[] rnglb, final double[] rngub)\n
    feasOpt(final IloRange[] rngs, final double[] rnglb, final double[] rngub, final IloForAllRange[] farngs, final double[] falb, final double[] faub, final IloNumVar[] vars, final double[] varlb, final double[] varub)\n
    '''
def getBoundSA():
    '''returns None\n\n
    getBoundSA(final double[] lblower, final double[] lbupper, final double[] ublower, final double[] ubupper, final IloLPMatrix matrix)\n
    getBoundSA(final double[] lblower, final double[] lbupper, final double[] ublower, final double[] ubupper, final IloLPMatrix matrix, final int start, final int num)\n
    getBoundSA(final double[] lblower, final double[] lbupper, final double[] ublower, final double[] ubupper, final IloNumVar[] var)\n
    getBoundSA(final double[] lblower, final double[] lbupper, final double[] ublower, final double[] ubupper, final IloNumVar[] var, final int start, final int num)\n
    '''
def getObjSA():
    '''returns None\n\n
    getObjSA(final double[] lower, final double[] upper, final IloLPMatrix matrix)\n
    getObjSA(final double[] lower, final double[] upper, final IloLPMatrix matrix, final int start, final int num)\n
    getObjSA(final double[] lower, final double[] upper, final IloNumVar[] var)\n
    getObjSA(final double[] lower, final double[] upper, final IloNumVar[] var, final int start, final int num)\n
    '''
def getRangeSA():
    '''returns None\n\n
    getRangeSA(final double[] lblower, final double[] lbupper, final double[] ublower, final double[] ubupper, final IloRange[] rng)\n
    getRangeSA(final double[] lblower, final double[] lbupper, final double[] ublower, final double[] ubupper, final IloRange[] rng, final int start, final int num)\n
    getRangeSA(final double[] lblower, final double[] lbupper, final double[] ublower, final double[] ubupper, final IloLPMatrix matrix, final int start, final int num)\n
    getRangeSA(final double[] lblower, final double[] lbupper, final double[] ublower, final double[] ubupper, final IloLPMatrix matrix)\n
    '''
def getRHSSA():
    '''returns None\n\n
    getRHSSA(final double[] lower, final double[] upper, final IloRange[] rng)\n
    getRHSSA(final double[] lower, final double[] upper, final IloRange[] rng, final int start, final int num)\n
    getRHSSA(final double[] lower, final double[] upper, final IloLPMatrix matrix)\n
    getRHSSA(final double[] lower, final double[] upper, final IloLPMatrix matrix, final int start, final int num)\n
    '''
def getQuality():
    '''returns Quality\n\n
    getQuality(final QualityType which)\n
    getQuality(final QualityType which, final int soln)\n
    '''
def ():
    '''returns UnknownObjectException\n\n
    ()\n
    (final IloEnv env)\n
    (final ilog.cplex.cppimpl.IloCplex cplexImpl)\n
    (final ilog.cplex.cppimpl.IloCplex cplexImpl, final boolean noStreams)\n
    (final Iterator it)\n
    ()\n
    (final IntParam key, final int value)\n
    (final LongParam key, final long value)\n
    (final DoubleParam key, final double value)\n
    (final BooleanParam key, final boolean value)\n
    (final StringParam key, final String value)\n
    (final Object data)\n
    (final Object obj)\n
    '''
def output():
    '''returns PrintStream\n\n
    output()\n
    '''
def warning():
    '''returns PrintStream\n\n
    warning()\n
    '''
def error():
    '''returns PrintStream\n\n
    error()\n
    '''
def setOut():
    '''returns None\n\n
    setOut(final OutputStream s)\n
    '''
def setWarning():
    '''returns None\n\n
    setWarning(final OutputStream s)\n
    '''
def setError():
    '''returns None\n\n
    setError(final OutputStream s)\n
    '''
def solve():
    '''returns boolean\n\n
    solve()\n
    '''
def solveFixed():
    '''returns boolean\n\n
    solveFixed()\n
    solveFixed(final int soln)\n
    '''
def solveZeroedQP():
    '''returns boolean\n\n
    solveZeroedQP()\n
    '''
def getNiterations():
    '''returns int\n\n
    getNiterations()\n
    '''
def getNiterations64():
    '''returns long\n\n
    getNiterations64()\n
    '''
def getNphaseOneIterations():
    '''returns int\n\n
    getNphaseOneIterations()\n
    '''
def getNphaseOneIterations64():
    '''returns long\n\n
    getNphaseOneIterations64()\n
    '''
def getNbarrierIterations():
    '''returns int\n\n
    getNbarrierIterations()\n
    '''
def getNbarrierIterations64():
    '''returns long\n\n
    getNbarrierIterations64()\n
    '''
def getNsiftingIterations():
    '''returns int\n\n
    getNsiftingIterations()\n
    '''
def getNsiftingIterations64():
    '''returns long\n\n
    getNsiftingIterations64()\n
    '''
def getNsiftingPhaseOneIterations():
    '''returns int\n\n
    getNsiftingPhaseOneIterations()\n
    '''
def getNsiftingPhaseOneIterations64():
    '''returns long\n\n
    getNsiftingPhaseOneIterations64()\n
    '''
def getNcrossDExch():
    '''returns int\n\n
    getNcrossDExch()\n
    '''
def getNcrossDExch64():
    '''returns long\n\n
    getNcrossDExch64()\n
    '''
def getNcrossDPush():
    '''returns int\n\n
    getNcrossDPush()\n
    '''
def getNcrossDPush64():
    '''returns long\n\n
    getNcrossDPush64()\n
    '''
def getNcrossPExch():
    '''returns int\n\n
    getNcrossPExch()\n
    '''
def getNcrossPExch64():
    '''returns long\n\n
    getNcrossPExch64()\n
    '''
def getNcrossPPush():
    '''returns int\n\n
    getNcrossPPush()\n
    '''
def getNcrossPPush64():
    '''returns long\n\n
    getNcrossPPush64()\n
    '''
def getNdualSuperbasics():
    '''returns int\n\n
    getNdualSuperbasics()\n
    '''
def getNprimalSuperbasics():
    '''returns int\n\n
    getNprimalSuperbasics()\n
    '''
def getNnodes():
    '''returns int\n\n
    getNnodes()\n
    '''
def getNnodes64():
    '''returns long\n\n
    getNnodes64()\n
    '''
def getNnodesLeft():
    '''returns int\n\n
    getNnodesLeft()\n
    '''
def getNnodesLeft64():
    '''returns long\n\n
    getNnodesLeft64()\n
    '''
def getIncumbentNode():
    '''returns int\n\n
    getIncumbentNode()\n
    '''
def getIncumbentNode64():
    '''returns long\n\n
    getIncumbentNode64()\n
    '''
def tuneParam():
    '''returns int\n\n
    tuneParam()\n
    tuneParam(final ParameterSet fixedset)\n
    tuneParam(final String[] filenames)\n
    tuneParam(final String[] filenames, final ParameterSet fixedset)\n
    '''
def setPriority():
    '''returns None\n\n
    setPriority(final IloNumVar var, final int pri)\n
    '''
def setPriorities():
    '''returns None\n\n
    setPriorities(final IloNumVar[] var, final int[] pri)\n
    setPriorities(final IloNumVar[] var, final int[] pri, final int start, final int num)\n
    '''
def setDirection():
    '''returns None\n\n
    setDirection(final IloNumVar var, final BranchDirection dir)\n
    '''
def setDirections():
    '''returns None\n\n
    setDirections(final IloNumVar[] var, final BranchDirection[] brdir)\n
    setDirections(final IloNumVar[] var, final BranchDirection[] brdir, final int start, final int num)\n
    '''
def delPriority():
    '''returns None\n\n
    delPriority(final IloNumVar var)\n
    '''
def delPriorities():
    '''returns None\n\n
    delPriorities(final IloNumVar[] var)\n
    delPriorities(final IloNumVar[] var, final int start, final int num)\n
    '''
def delDirection():
    '''returns None\n\n
    delDirection(final IloNumVar var)\n
    '''
def delDirections():
    '''returns None\n\n
    delDirections(final IloNumVar[] var)\n
    delDirections(final IloNumVar[] var, final int start, final int num)\n
    '''
def getPriority():
    '''returns int\n\n
    getPriority(final IloNumVar var)\n
    '''
def getPriorities():
    '''returns int[]\n\n
    getPriorities(final IloNumVar[] var)\n
    getPriorities(final IloNumVar[] var, final int start, final int num)\n
    '''
def getDirection():
    '''returns BranchDirection\n\n
    getDirection(final IloNumVar var)\n
    '''
def getDirections():
    '''returns BranchDirection[]\n\n
    getDirections(final IloNumVar[] var)\n
    getDirections(final IloNumVar[] var, final int start, final int num)\n
    '''
def writeOrder():
    '''returns None\n\n
    writeOrder(final String name)\n
    '''
def writeConflict():
    '''returns None\n\n
    writeConflict(final String name)\n
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
    writeSolution(final String name)\n
    writeSolution(final String name, final int soln)\n
    '''
def writeSolutions():
    '''returns None\n\n
    writeSolutions(final String name)\n
    '''
def writeMIPStarts():
    '''returns None\n\n
    writeMIPStarts(final String name)\n
    '''
def getCplexTime():
    '''returns double\n\n
    getCplexTime()\n
    '''
def getDetTime():
    '''returns double\n\n
    getDetTime()\n
    '''
def readOrder():
    '''returns None\n\n
    readOrder(final String name)\n
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
def add():
    '''returns None\n\n
    add(final Callback cb)\n
    '''
def clearCallbacks():
    '''returns None\n\n
    clearCallbacks()\n
    '''
def addMIPStart():
    '''returns int\n\n
    addMIPStart(final IloNumVar[] vars, final double[] values, final int vstart, final int vnum, final MIPStartEffort effort, final String name)\n
    addMIPStart(final IloNumVar[] vars, final double[] values, final MIPStartEffort effort, final String name)\n
    addMIPStart(final MIPStartEffort effort, final String name)\n
    addMIPStart(final IloNumVar[] vars, final double[] values, final MIPStartEffort effort)\n
    addMIPStart(final IloNumVar[] vars, final double[] values)\n
    addMIPStart(final IloNumVar[] vars, final double[] values, final String name)\n
    addMIPStart(final MIPStartEffort effort)\n
    addMIPStart(final String name)\n
    addMIPStart()\n
    '''
def changeMIPStart():
    '''returns None\n\n
    changeMIPStart(final int mipstartindex, final IloNumVar[] vars, final double[] values, final int vstart, final int vnum, final MIPStartEffort effort)\n
    changeMIPStart(final int mipstartindex, final IloNumVar[] vars, final double[] values, final MIPStartEffort effort)\n
    changeMIPStart(final int mipstartindex, final MIPStartEffort effort)\n
    changeMIPStart(final int mipstartindex, final IloNumVar[] vars, final double[] values)\n
    '''
def deleteMIPStarts():
    '''returns None\n\n
    deleteMIPStarts(final int first, final int num)\n
    deleteMIPStarts(final int first)\n
    '''
def getNMIPStarts():
    '''returns int\n\n
    getNMIPStarts()\n
    '''
def getMIPStartName():
    '''returns String\n\n
    getMIPStartName(final int mipstartindex)\n
    '''
def getMIPStartIndex():
    '''returns int\n\n
    getMIPStartIndex(final String name)\n
    '''
def getMIPStart():
    '''returns MIPStartEffort\n\n
    getMIPStart(final int mipstartindex, final IloNumVar[] vars, final int begin, final int num, final double[] values, final boolean[] isset)\n
    getMIPStart(final int mipstartindex, final IloNumVar[] vars, final double[] values, final boolean[] isset)\n
    getMIPStart(final int mipstartindex, final IloNumVar[] vars, final int begin, final int num, final double[] values)\n
    getMIPStart(final int mipstartindex, final IloNumVar[] vars, final double[] values)\n
    getMIPStart(final int mipstartindex)\n
    '''
def getRay():
    '''returns None\n\n
    getRay()\n
    getRay(final ilog.concert.IloNumArray vals, final ilog.concert.IloNumVarArray vars)\n
    '''
def getDiverging():
    '''returns IloCopyable\n\n
    getDiverging()\n
    '''
def dualFarkas():
    '''returns double\n\n
    dualFarkas(final IloConstraint[] rng, final double[] y)\n
    '''
def qpIndefCertificate():
    '''returns None\n\n
    qpIndefCertificate(final IloNumVar[] var, final double[] x)\n
    '''
def end():
    '''returns None\n\n
    end()\n
    end()\n
    '''
def eqGoal():
    '''returns Goal\n\n
    eqGoal(final IloNumExpr expr, final double rhs)\n
    eqGoal(final IloNumExpr expr1, final IloNumExpr expr2)\n
    eqGoal(final double lhs, final IloNumExpr expr)\n
    '''
def geGoal():
    '''returns Goal\n\n
    geGoal(final IloNumExpr expr, final double rhs)\n
    geGoal(final IloNumExpr expr1, final IloNumExpr expr2)\n
    geGoal(final double lhs, final IloNumExpr expr)\n
    '''
def leGoal():
    '''returns Goal\n\n
    leGoal(final IloNumExpr expr, final double rhs)\n
    leGoal(final IloNumExpr expr1, final IloNumExpr expr2)\n
    leGoal(final double lhs, final IloNumExpr expr)\n
    '''
def getEnvImpl():
    '''returns IloEnv\n\n
    getEnvImpl()\n
    '''
def getLB():
    '''returns double\n\n
    getLB(final IloForAllRange v)\n
    '''
def getUB():
    '''returns double\n\n
    getUB(final IloForAllRange v)\n
    '''
def lowerBound():
    '''returns IloNumVarBound\n\n
    lowerBound(final IloNumVar var)\n
    '''
def upperBound():
    '''returns IloNumVarBound\n\n
    upperBound(final IloNumVar var)\n
    '''
def refineConflict():
    '''returns boolean\n\n
    refineConflict(final IloConstraint[] cons, final double[] prefs)\n
    refineConflict(final IloConstraint[] cts, final double[] prefs, final int start, final int num)\n
    '''
def getConflict():
    '''returns ConflictStatus[]\n\n
    getConflict(final IloConstraint[] cts)\n
    getConflict(final IloConstraint ct)\n
    getConflict(final IloConstraint[] cts, final int start, final int num)\n
    '''
def and():
    '''returns IloConstraint\n\n
    and(final IloRange[] cts)\n
    '''
def getForAllRanges():
    '''returns IloForAllRange[]\n\n
    getForAllRanges(final IloConstraint forAllCt)\n
    '''
def parameterSet():
    '''returns ParameterSet\n\n
    parameterSet()\n
    '''
def getParameterSet():
    '''returns ParameterSet\n\n
    getParameterSet()\n
    '''
def setParameterSet():
    '''returns None\n\n
    setParameterSet(final ParameterSet set)\n
    '''
def populate():
    '''returns boolean\n\n
    populate()\n
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
def next():
    '''returns Object\n\n
    next()\n
    next()\n
    '''
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    hasNext()\n
    '''
def isIncluded():
    '''returns boolean\n\n
    isIncluded(final Object obj)\n
    isIncluded(final Object obj)\n
    isIncluded(final Object obj)\n
    isIncluded(final Object obj)\n
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
def abort():
    '''returns None\n\n
    abort()\n
    '''
def isAborted():
    '''returns boolean\n\n
    isAborted()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    clear()\n
    '''
def alsoLong():
    '''returns boolean\n\n
    alsoLong()\n
    '''
def getType():
    '''returns int\n\n
    getType()\n
    getType()\n
    getType()\n
    getType()\n
    getType()\n
    '''
def getKey():
    '''returns StringParam\n\n
    getKey()\n
    getKey()\n
    getKey()\n
    getKey()\n
    getKey()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    equals(final Object obj)\n
    equals(final Object obj)\n
    equals(final Object obj)\n
    equals(final Object obj)\n
    equals(final Object obj)\n
    equals(final Object obj)\n
    '''
def getNumVar():
    '''returns IloNumVar\n\n
    getNumVar()\n
    '''
def getConstraint():
    '''returns IloConstraint\n\n
    getConstraint()\n
    '''
def getQualityType():
    '''returns QualityType\n\n
    getQualityType()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
def write():
    '''returns None\n\n
    write(final int b)\n
    write(final byte[] b)\n
    write(final byte[] b, final int off, final int len)\n
    '''
def getCppImpl():
    '''returns IloCplex__Callback\n\n
    getCppImpl(final IloCplex cplex)\n
    '''
def callbackImpl():
    '''returns None\n\n
    callbackImpl()\n
    callbackImpl()\n
    callbackImpl()\n
    callbackImpl()\n
    callbackImpl()\n
    callbackImpl()\n
    callbackImpl()\n
    callbackImpl()\n
    callbackImpl()\n
    callbackImpl()\n
    callbackImpl()\n
    callbackImpl()\n
    callbackImpl()\n
    callbackImpl()\n
    callbackImpl()\n
    callbackImpl()\n
    callbackImpl()\n
    callbackImpl()\n
    callbackImpl()\n
    callbackImpl()\n
    callbackImpl()\n
    callbackImpl()\n
    callbackImpl()\n
    '''
def getObject():
    '''returns Object\n\n
    getObject()\n
    getObject()\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def evaluate():
    '''returns double\n\n
    evaluate()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    init()\n
    '''
def subsume():
    '''returns boolean\n\n
    subsume(final double evalNode, final double evalCurrent)\n
    '''
def duplicateEvaluator():
    '''returns IloCplex__NodeEvaluatorI\n\n
    duplicateEvaluator()\n
    '''
def duplicateGoal():
    '''returns IloCplex__Goal\n\n
    duplicateGoal()\n
    '''
def execute():
    '''returns Goal\n\n
    execute()\n
    execute(final IloCplex cplex)\n
    '''
