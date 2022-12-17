IntMin = "int  -2147483647"
IntMax = "int  Integer.MAX_VALUE"
Infinity = "double  Double.POSITIVE_INFINITY"
IntervalMin = "int  -1073741822"
IntervalMax = "int  1073741822"
NoState = "int  -1"
def ():
    '''returns ParamIterator\n\n
    ()\n
    (final IloEnv env)\n
    (final IloCP cp)\n
    (final ilog.cp.cppimpl.IloCP cp)\n
    (final ilog.cp.cppimpl.IloCP cp, final boolean noStreams)\n
    (final ilog.cp.cppimpl.IloCP cp, final boolean noStreams, final boolean noModel)\n
    (final IloCP cp, final ilog.concert.cppimpl.IloIntVar var)\n
    (final ilog.cp.cppimpl.IloCP cp, final ilog.concert.cppimpl.IloIntVar var)\n
    (final IloCP cp, final ilog.concert.cppimpl.IloNumVar var)\n
    (final ilog.cp.cppimpl.IloCP cp, final ilog.concert.cppimpl.IloNumVar var)\n
    (final ilog.cp.cppimpl.IloCP cp)\n
    (final IloCP cp)\n
    (final ilog.cp.cppimpl.IloCP cp)\n
    (final IloCP cp)\n
    '''
def model():
    '''returns IloModel\n\n
    model()\n
    '''
def setParameter():
    '''returns None\n\n
    setParameter(final IntParam param, final ParameterValues value)\n
    setParameter(final IntParam param, final int value)\n
    setParameter(final DoubleParam param, final ParameterValues value)\n
    setParameter(final DoubleParam param, final double value)\n
    setParameter(final String name, final String value)\n
    setParameter(final String name, final double value)\n
    '''
def getParameter():
    '''returns double\n\n
    getParameter(final IntParam param)\n
    getParameter(final DoubleParam param)\n
    getParameter(final String param)\n
    '''
def getParameterDefault():
    '''returns double\n\n
    getParameterDefault(final IntParam param)\n
    getParameterDefault(final DoubleParam param)\n
    '''
def getInfo():
    '''returns double\n\n
    getInfo(final IntInfo which)\n
    getInfo(final DoubleInfo which)\n
    '''
def solution():
    '''returns IloSolution\n\n
    solution()\n
    '''
def store():
    '''returns None\n\n
    store(final IloSolution solution)\n
    '''
def restore():
    '''returns boolean\n\n
    restore(final IloSolution solution)\n
    '''
def setSearchPhases():
    '''returns None\n\n
    setSearchPhases()\n
    setSearchPhases(final IloSearchPhase phase)\n
    setSearchPhases(final IloSearchPhase[] phases)\n
    setSearchPhases(final ilog.cp.IloSearchPhaseArray phases)\n
    '''
def clearExplanations():
    '''returns None\n\n
    clearExplanations()\n
    '''
def explainFailure():
    '''returns None\n\n
    explainFailure(final int failTag)\n
    explainFailure(final int[] failTagArray)\n
    '''
def setStartingPoint():
    '''returns None\n\n
    setStartingPoint(final IloSolution sp)\n
    '''
def clearStartingPoint():
    '''returns None\n\n
    clearStartingPoint()\n
    '''
def solve():
    '''returns boolean\n\n
    solve()\n
    solve(final IloSearchPhase phase)\n
    solve(final IloSearchPhase[] phases)\n
    solve(final ilog.cp.IloSearchPhaseArray phases)\n
    '''
def startNewSearch():
    '''returns None\n\n
    startNewSearch()\n
    startNewSearch(final IloSearchPhase phase)\n
    startNewSearch(final IloSearchPhase[] phases)\n
    startNewSearch(final ilog.cp.IloSearchPhaseArray phases)\n
    '''
def endSearch():
    '''returns None\n\n
    endSearch()\n
    '''
def next():
    '''returns Object\n\n
    next()\n
    next()\n
    next()\n
    next()\n
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
def printInformation():
    '''returns None\n\n
    printInformation(final OutputStream s)\n
    printInformation()\n
    '''
def trueConstraint():
    '''returns IloConstraint\n\n
    trueConstraint()\n
    '''
def falseConstraint():
    '''returns IloConstraint\n\n
    falseConstraint()\n
    '''
def allDiff():
    '''returns IloConstraint\n\n
    allDiff(final IloIntExpr[] exps)\n
    allDiff(final ilog.concert.IloIntExprArray exps)\n
    '''
def allMinDistance():
    '''returns IloConstraint\n\n
    allMinDistance(final IloIntVar[] vars, final int k)\n
    allMinDistance(final ilog.concert.IloIntVarArray vars, final int k)\n
    '''
def distribute():
    '''returns IloConstraint\n\n
    distribute(final IloIntExpr[] cards, final int[] values, final IloIntExpr[] vars)\n
    distribute(final IloIntExpr[] cards, final IloIntExpr[] vars)\n
    distribute(final ilog.concert.IloIntVarArray cards, final ilog.concert.IloIntVarArray vars)\n
    '''
def element():
    '''returns IloNumExpr\n\n
    element(final IloIntExpr var, final IloIntExpr index, final int[] values)\n
    element(final IloNumExpr var, final IloIntExpr index, final double[] values)\n
    element(final IloIntExpr[] exprs, final IloIntExpr index)\n
    element(final ilog.concert.IloIntExprArray exprs, final IloIntExpr index)\n
    element(final int[] values, final IloIntExpr index)\n
    element(final double[] values, final IloIntExpr index)\n
    '''
def eq():
    '''returns IloConstraint\n\n
    eq(final IloIntExpr e, final int v)\n
    eq(final IloIntExpr e1, final IloIntExpr e2)\n
    eq(final int v, final IloIntExpr e)\n
    '''
def ge():
    '''returns IloConstraint\n\n
    ge(final IloIntExpr e, final int v)\n
    ge(final IloIntExpr e1, final IloIntExpr e2)\n
    ge(final int v, final IloIntExpr e)\n
    ge(final int vmax, final IloCumulFunctionExpr f)\n
    ge(final IloIntExpr vmax, final IloCumulFunctionExpr f)\n
    ge(final IloCumulFunctionExpr f, final int vmin)\n
    ge(final IloCumulFunctionExpr f, final IloIntExpr vmin)\n
    '''
def gt():
    '''returns IloConstraint\n\n
    gt(final IloIntExpr e, final int v)\n
    gt(final IloIntExpr e1, final IloIntExpr e2)\n
    gt(final int v, final IloIntExpr e)\n
    '''
def inverse():
    '''returns IloConstraint\n\n
    inverse(final IloIntExpr[] f, final IloIntExpr[] invf)\n
    inverse(final ilog.concert.IloIntVarArray f, final ilog.concert.IloIntVarArray invf)\n
    '''
def le():
    '''returns IloConstraint\n\n
    le(final IloIntExpr e, final int v)\n
    le(final IloIntExpr e1, final IloIntExpr e2)\n
    le(final int v, final IloIntExpr e)\n
    le(final IloCumulFunctionExpr f, final int vmax)\n
    le(final IloCumulFunctionExpr f, final IloIntExpr vmax)\n
    le(final int vmin, final IloCumulFunctionExpr f)\n
    le(final IloIntExpr vmin, final IloCumulFunctionExpr f)\n
    '''
def lexicographic():
    '''returns IloConstraint\n\n
    lexicographic(final IloIntExpr[] arg1, final IloIntExpr[] arg2)\n
    lexicographic(final ilog.concert.IloIntExprArray arg1, final ilog.concert.IloIntExprArray arg2)\n
    '''
def lt():
    '''returns IloConstraint\n\n
    lt(final IloIntExpr e, final int v)\n
    lt(final IloIntExpr e1, final IloIntExpr e2)\n
    lt(final int v, final IloIntExpr e)\n
    '''
def member():
    '''returns IloConstraint\n\n
    member(final IloIntExpr exp, final int[] values)\n
    '''
def neq():
    '''returns IloConstraint\n\n
    neq(final IloIntExpr e, final int v)\n
    neq(final IloIntExpr e1, final IloIntExpr e2)\n
    neq(final int v, final IloIntExpr e)\n
    neq(final IloConstraint c1, final IloConstraint c2)\n
    '''
def pack():
    '''returns IloConstraint\n\n
    pack(final IloIntExpr[] load, final IloIntExpr[] where, final int[] weight)\n
    pack(final IloIntExpr[] load, final IloIntExpr[] where, final int[] weight, final IloIntExpr used)\n
    '''
def allowedAssignments():
    '''returns IloConstraint\n\n
    allowedAssignments(final IloIntVar[] exps, final IloIntTupleSet table)\n
    allowedAssignments(final IloIntExpr exp, final int[] values)\n
    allowedAssignments(final ilog.concert.IloIntVarArray exps, final IloIntTupleSet table)\n
    '''
def forbiddenAssignments():
    '''returns IloConstraint\n\n
    forbiddenAssignments(final IloIntVar[] exps, final IloIntTupleSet table)\n
    forbiddenAssignments(final IloIntExpr exp, final int[] values)\n
    forbiddenAssignments(final ilog.concert.IloIntVarArray exps, final IloIntTupleSet table)\n
    '''
def strong():
    '''returns IloConstraint\n\n
    strong(final ilog.concert.IloIntVarArray vars)\n
    strong(final IloIntVar[] vars)\n
    '''
def equiv():
    '''returns IloConstraint\n\n
    equiv(final IloConstraint c1, final IloConstraint c2)\n
    '''
def ifThenElse():
    '''returns IloConstraint\n\n
    ifThenElse(final IloConstraint c1, final IloConstraint c2, final IloConstraint c3)\n
    '''
def imply():
    '''returns IloConstraint\n\n
    imply(final IloConstraint c1, final IloConstraint c2)\n
    '''
def intExpr():
    '''returns IloIntExpr\n\n
    intExpr(final IloConstraint ct)\n
    '''
def intExprArray():
    '''returns IloIntExpr[]\n\n
    intExprArray(final int n)\n
    '''
def numExprArray():
    '''returns IloNumExpr[]\n\n
    numExprArray(final int n)\n
    '''
def ceil():
    '''returns IloNumExpr\n\n
    ceil(final IloNumExpr arg)\n
    '''
def constant():
    '''returns IloNumExpr\n\n
    constant(final int value, final String name)\n
    constant(final double value, final String name)\n
    '''
def count():
    '''returns IloIntExpr\n\n
    count(final IloIntExpr[] exprs, final int v)\n
    count(final ilog.concert.IloIntExprArray exprs, final int v)\n
    '''
def countDifferent():
    '''returns IloIntExpr\n\n
    countDifferent(final IloIntExpr[] exprs)\n
    countDifferent(final ilog.concert.IloIntExprArray exprs)\n
    '''
def distToInt():
    '''returns IloNumExpr\n\n
    distToInt(final IloNumExpr arg)\n
    '''
def div():
    '''returns IloIntExpr\n\n
    div(final IloIntExpr e1, final IloIntExpr e2)\n
    div(final int e1, final IloIntExpr e2)\n
    div(final IloIntExpr e1, final int e2)\n
    '''
def exponent():
    '''returns IloNumExpr\n\n
    exponent(final IloNumExpr e)\n
    '''
def floor():
    '''returns IloNumExpr\n\n
    floor(final IloNumExpr arg)\n
    '''
def fract():
    '''returns IloNumExpr\n\n
    fract(final IloNumExpr arg)\n
    '''
def log():
    '''returns IloNumExpr\n\n
    log(final IloNumExpr e)\n
    '''
def max():
    '''returns IloNumExpr\n\n
    max(final ilog.concert.IloIntExprArray expr)\n
    max(final IloIntExpr[] exprs)\n
    max(final Collection<IloIntExpr> exprs)\n
    max(final IloNumExprArray expr)\n
    max(final IloNumExpr[] exprs)\n
    '''
def min():
    '''returns IloNumExpr\n\n
    min(final ilog.concert.IloIntExprArray expr)\n
    min(final IloIntExpr[] exprs)\n
    min(final IloNumExprArray expr)\n
    min(final IloNumExpr[] exprs)\n
    '''
def modulo():
    '''returns IloIntExpr\n\n
    modulo(final IloIntExpr e, final int r)\n
    '''
def power():
    '''returns IloNumExpr\n\n
    power(final IloNumExpr e1, final IloNumExpr e2)\n
    power(final IloNumExpr e1, final int e2)\n
    power(final double e1, final IloNumExpr e2)\n
    '''
def prod():
    '''returns IloNumExpr\n\n
    prod(final int[] values, final IloIntExpr[] exps)\n
    prod(final IloIntExpr[] exps1, final IloIntExpr[] exps2)\n
    prod(final ilog.concert.IloIntExprArray exps1, final ilog.concert.IloIntExprArray exps2)\n
    prod(final IloIntExpr[] exps, final int[] values)\n
    prod(final double[] values, final IloNumExpr[] exps)\n
    prod(final IloNumExpr[] exps, final double[] values)\n
    prod(final IloNumExpr[] exps1, final IloNumExpr[] exps2)\n
    prod(final IloNumExprArray exps1, final IloNumExprArray exps2)\n
    '''
def quot():
    '''returns IloNumExpr\n\n
    quot(final IloNumExpr e1, final IloNumExpr e2)\n
    quot(final double e1, final IloNumExpr e2)\n
    quot(final IloNumExpr e1, final double e2)\n
    '''
def scalProd():
    '''returns IloNumExpr\n\n
    scalProd(final ilog.concert.IloIntVarArray vars1, final ilog.concert.IloIntVarArray vars2)\n
    scalProd(final ilog.concert.IloNumVarArray vars1, final ilog.concert.IloNumVarArray vars2)\n
    '''
def sum():
    '''returns IloCumulFunctionExpr\n\n
    sum(final ilog.concert.IloIntExprArray expr)\n
    sum(final IloIntExpr[] exprs)\n
    sum(final IloNumExprArray expr)\n
    sum(final IloNumExpr[] exprs)\n
    sum(final IloCumulFunctionExpr f1, final IloCumulFunctionExpr f2)\n
    '''
def sgn():
    '''returns IloIntExpr\n\n
    sgn(final IloNumExpr e)\n
    '''
def standardDeviation():
    '''returns IloNumExpr\n\n
    standardDeviation(final IloIntExpr[] exprs)\n
    standardDeviation(final IloIntExpr[] exprs, final double meanLB, final double meanUB)\n
    standardDeviation(final ilog.concert.IloIntExprArray exprs)\n
    standardDeviation(final ilog.concert.IloIntExprArray exprs, final double meanLB, final double meanUB)\n
    '''
def piecewiseLinear():
    '''returns IloNumExpr\n\n
    piecewiseLinear(final IloNumExpr e, final double[] point, final double[] slope, final double a, final double fa)\n
    piecewiseLinear(final IloNumExpr e, final double firstSlope, final double[] point, final double[] value, final double lastSlope)\n
    '''
def trunc():
    '''returns IloNumExpr\n\n
    trunc(final IloNumExpr arg)\n
    '''
def numToInt():
    '''returns IloIntExpr\n\n
    numToInt(final IloNumExpr arg)\n
    '''
def round():
    '''returns IloNumExpr\n\n
    round(final IloNumExpr arg)\n
    '''
def intSet():
    '''returns IloIntSet\n\n
    intSet(final int[] values)\n
    intSet(final int min, final int max)\n
    '''
def startBeforeStart():
    '''returns IloConstraint\n\n
    startBeforeStart(final IloIntervalVar a, final IloIntervalVar b)\n
    startBeforeStart(final IloIntervalVar a, final IloIntervalVar b, final int z)\n
    startBeforeStart(final IloIntervalVar a, final IloIntervalVar b, final IloIntExpr z)\n
    '''
def startBeforeEnd():
    '''returns IloConstraint\n\n
    startBeforeEnd(final IloIntervalVar a, final IloIntervalVar b)\n
    startBeforeEnd(final IloIntervalVar a, final IloIntervalVar b, final int z)\n
    startBeforeEnd(final IloIntervalVar a, final IloIntervalVar b, final IloIntExpr z)\n
    '''
def endBeforeStart():
    '''returns IloConstraint\n\n
    endBeforeStart(final IloIntervalVar a, final IloIntervalVar b)\n
    endBeforeStart(final IloIntervalVar a, final IloIntervalVar b, final int z)\n
    endBeforeStart(final IloIntervalVar a, final IloIntervalVar b, final IloIntExpr z)\n
    '''
def endBeforeEnd():
    '''returns IloConstraint\n\n
    endBeforeEnd(final IloIntervalVar a, final IloIntervalVar b)\n
    endBeforeEnd(final IloIntervalVar a, final IloIntervalVar b, final int z)\n
    endBeforeEnd(final IloIntervalVar a, final IloIntervalVar b, final IloIntExpr z)\n
    '''
def startAtStart():
    '''returns IloConstraint\n\n
    startAtStart(final IloIntervalVar a, final IloIntervalVar b)\n
    startAtStart(final IloIntervalVar a, final IloIntervalVar b, final int z)\n
    startAtStart(final IloIntervalVar a, final IloIntervalVar b, final IloIntExpr z)\n
    '''
def startAtEnd():
    '''returns IloConstraint\n\n
    startAtEnd(final IloIntervalVar a, final IloIntervalVar b)\n
    startAtEnd(final IloIntervalVar a, final IloIntervalVar b, final int z)\n
    startAtEnd(final IloIntervalVar a, final IloIntervalVar b, final IloIntExpr z)\n
    '''
def endAtStart():
    '''returns IloConstraint\n\n
    endAtStart(final IloIntervalVar a, final IloIntervalVar b)\n
    endAtStart(final IloIntervalVar a, final IloIntervalVar b, final int z)\n
    endAtStart(final IloIntervalVar a, final IloIntervalVar b, final IloIntExpr z)\n
    '''
def endAtEnd():
    '''returns IloConstraint\n\n
    endAtEnd(final IloIntervalVar a, final IloIntervalVar b)\n
    endAtEnd(final IloIntervalVar a, final IloIntervalVar b, final int z)\n
    endAtEnd(final IloIntervalVar a, final IloIntervalVar b, final IloIntExpr z)\n
    '''
def presenceOf():
    '''returns IloConstraint\n\n
    presenceOf(final IloIntervalVar a)\n
    '''
def implies():
    '''returns IloConstraint\n\n
    implies(final IloIntervalVar a, final IloIntervalVar b)\n
    '''
def impliesNot():
    '''returns IloConstraint\n\n
    impliesNot(final IloIntervalVar a, final IloIntervalVar b)\n
    '''
def orWith():
    '''returns IloConstraint\n\n
    orWith(final IloIntervalVar a, final IloIntervalVar b)\n
    '''
def equivalent():
    '''returns IloConstraint\n\n
    equivalent(final IloIntervalVar a, final IloIntervalVar b)\n
    '''
def opposite():
    '''returns IloConstraint\n\n
    opposite(final IloIntervalVar a, final IloIntervalVar b)\n
    '''
def forbidStart():
    '''returns IloConstraint\n\n
    forbidStart(final IloIntervalVar a, final IloNumToNumStepFunction f)\n
    '''
def forbidEnd():
    '''returns IloConstraint\n\n
    forbidEnd(final IloIntervalVar a, final IloNumToNumStepFunction f)\n
    '''
def forbidExtent():
    '''returns IloConstraint\n\n
    forbidExtent(final IloIntervalVar a, final IloNumToNumStepFunction f)\n
    '''
def previous():
    '''returns IloConstraint\n\n
    previous(final IloIntervalSequenceVar seq, final IloIntervalVar prev, final IloIntervalVar next)\n
    '''
def first():
    '''returns IloConstraint\n\n
    first(final IloIntervalSequenceVar seq, final IloIntervalVar a)\n
    '''
def last():
    '''returns IloConstraint\n\n
    last(final IloIntervalSequenceVar seq, final IloIntervalVar a)\n
    '''
def before():
    '''returns IloConstraint\n\n
    before(final IloIntervalSequenceVar seq, final IloIntervalVar pred, final IloIntervalVar succ)\n
    '''
def sameSequence():
    '''returns IloConstraint\n\n
    sameSequence(final IloIntervalSequenceVar seq1, final IloIntervalSequenceVar seq2)\n
    sameSequence(final IloIntervalSequenceVar seq1, final IloIntervalSequenceVar seq2, final String name)\n
    sameSequence(final IloIntervalSequenceVar seq1, final IloIntervalSequenceVar seq2, final IloIntervalVar[] a1, final IloIntervalVar[] a2)\n
    sameSequence(final IloIntervalSequenceVar seq1, final IloIntervalSequenceVar seq2, final IloIntervalVar[] a1, final IloIntervalVar[] a2, final String name)\n
    '''
def sameCommonSubsequence():
    '''returns IloConstraint\n\n
    sameCommonSubsequence(final IloIntervalSequenceVar seq1, final IloIntervalSequenceVar seq2)\n
    sameCommonSubsequence(final IloIntervalSequenceVar seq1, final IloIntervalSequenceVar seq2, final String name)\n
    sameCommonSubsequence(final IloIntervalSequenceVar seq1, final IloIntervalSequenceVar seq2, final IloIntervalVar[] a1, final IloIntervalVar[] a2)\n
    sameCommonSubsequence(final IloIntervalSequenceVar seq1, final IloIntervalSequenceVar seq2, final IloIntervalVar[] a1, final IloIntervalVar[] a2, final String name)\n
    '''
def alwaysIn():
    '''returns IloConstraint\n\n
    alwaysIn(final IloCumulFunctionExpr f, final int start, final int end, final int vmin, final int vmax)\n
    alwaysIn(final IloCumulFunctionExpr f, final IloIntervalVar a, final int vmin, final int vmax)\n
    alwaysIn(final IloStateFunction f, final int start, final int end, final int vmin, final int vmax)\n
    alwaysIn(final IloStateFunction f, final IloIntervalVar a, final int vmin, final int vmax)\n
    '''
def alwaysEqual():
    '''returns IloConstraint\n\n
    alwaysEqual(final IloCumulFunctionExpr f, final int start, final int end, final int v)\n
    alwaysEqual(final IloCumulFunctionExpr f, final IloIntervalVar a, final int v)\n
    alwaysEqual(final IloStateFunction f, final int start, final int end, final int v, final boolean startAlign, final boolean endAlign)\n
    alwaysEqual(final IloStateFunction f, final int start, final int end, final int v)\n
    alwaysEqual(final IloStateFunction f, final IloIntervalVar a, final int v, final boolean startAlign, final boolean endAlign)\n
    alwaysEqual(final IloStateFunction f, final IloIntervalVar a, final int v)\n
    '''
def alwaysNoState():
    '''returns IloConstraint\n\n
    alwaysNoState(final IloStateFunction f, final int start, final int end)\n
    alwaysNoState(final IloStateFunction f, final IloIntervalVar a)\n
    '''
def alwaysConstant():
    '''returns IloConstraint\n\n
    alwaysConstant(final IloStateFunction f, final int start, final int end, final boolean startAlign, final boolean endAlign)\n
    alwaysConstant(final IloStateFunction f, final int start, final int end)\n
    alwaysConstant(final IloStateFunction f, final IloIntervalVar a, final boolean startAlign, final boolean endAlign)\n
    alwaysConstant(final IloStateFunction f, final IloIntervalVar a)\n
    '''
def intVar():
    '''returns IloIntVar\n\n
    intVar(final int lb, final int ub, final String name)\n
    intVar(final int[] values, final String name)\n
    intVar(final int[] values)\n
    '''
def intVarArray():
    '''returns IloIntVar[]\n\n
    intVarArray(final int n)\n
    intVarArray(final int n, final int[] values, final String name)\n
    intVarArray(final int n, final int min, final int max, final String name)\n
    '''
def arrayEltName():
    '''returns String\n\n
    arrayEltName(final String name, final int index)\n
    '''
def numVarArray():
    '''returns IloNumVar[]\n\n
    numVarArray(final int n)\n
    numVarArray(final int n, final double min, final double max, final String name)\n
    '''
def intTable():
    '''returns IloIntTupleSet\n\n
    intTable(final int dimension)\n
    '''
def addTuple():
    '''returns None\n\n
    addTuple(final IloIntTupleSet ts, final int[] array)\n
    '''
def intervalVar():
    '''returns IloIntervalVar\n\n
    intervalVar()\n
    intervalVar(final String name)\n
    intervalVar(final int sz)\n
    intervalVar(final int sz, final String name)\n
    intervalVar(final int szmin, final int szmax)\n
    intervalVar(final int szmin, final int szmax, final boolean opt, final IloNumToNumStepFunction intensity, final int granularity)\n
    '''
def intervalSequenceVar():
    '''returns IloIntervalSequenceVar\n\n
    intervalSequenceVar(final IloIntervalVar[] a, final String name)\n
    intervalSequenceVar(final IloIntervalVar[] a)\n
    intervalSequenceVar(final IloIntervalVar[] a, final int[] types, final String name)\n
    intervalSequenceVar(final IloIntervalVar[] a, final int[] types)\n
    intervalSequenceVar(final Collection<IloIntervalVar> a, final int[] types, final String name)\n
    '''
def staticLex():
    '''returns IloMultiCriterionExpr\n\n
    staticLex(final IloNumExprArray criteria, final String name)\n
    staticLex(final IloNumExprArray criteria)\n
    staticLex(final IloNumExpr[] criteria, final String name)\n
    staticLex(final IloNumExpr[] criteria)\n
    staticLex(final IloNumExpr c1)\n
    staticLex(final IloNumExpr c1, final IloNumExpr c2)\n
    staticLex(final IloNumExpr c1, final IloNumExpr c2, final IloNumExpr c3)\n
    staticLex(final IloNumExpr c1, final IloNumExpr c2, final IloNumExpr c3, final IloNumExpr c4)\n
    '''
def maximize():
    '''returns IloObjective\n\n
    maximize(final IloIntExpr e)\n
    maximize(final IloMultiCriterionExpr e)\n
    '''
def minimize():
    '''returns IloObjective\n\n
    minimize(final IloIntExpr e)\n
    minimize(final IloMultiCriterionExpr e)\n
    '''
def getObjValue():
    '''returns double\n\n
    getObjValue()\n
    getObjValue(final int i)\n
    '''
def getNumberOfCriteria():
    '''returns int\n\n
    getNumberOfCriteria()\n
    '''
def getObjValues():
    '''returns double[]\n\n
    getObjValues()\n
    '''
def hasObjective():
    '''returns boolean\n\n
    hasObjective()\n
    '''
def range():
    '''returns IloRange\n\n
    range(final IloNumExpr expr, final double b)\n
    '''
def propagate():
    '''returns boolean\n\n
    propagate()\n
    propagate(final IloConstraint ct)\n
    '''
def dumpModel():
    '''returns None\n\n
    dumpModel(final String filename)\n
    dumpModel(final OutputStream s)\n
    '''
def exportModel():
    '''returns None\n\n
    exportModel(final String filename)\n
    exportModel(final OutputStream s)\n
    '''
def importModel():
    '''returns None\n\n
    importModel(final String filename)\n
    importModel(final InputStream s)\n
    '''
def getAllIloIntVars():
    '''returns IloIntVar[]\n\n
    getAllIloIntVars()\n
    '''
def getAllIloIntervalVars():
    '''returns IloIntervalVar[]\n\n
    getAllIloIntervalVars()\n
    '''
def getAllIloIntervalSequenceVars():
    '''returns IloIntervalSequenceVar[]\n\n
    getAllIloIntervalSequenceVars()\n
    '''
def getAllIloStateFunctions():
    '''returns IloStateFunction[]\n\n
    getAllIloStateFunctions()\n
    '''
def getAllConstrainedIloCumulFunctionExprs():
    '''returns IloCumulFunctionExpr[]\n\n
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
    '''returns double\n\n
    getValue(final String intVarName)\n
    getValue(final IloIntVar i)\n
    getValue(final IloIntExpr i)\n
    getValue(final IloNumVar num)\n
    getValue(final IloNumExpr num)\n
    getValue(final IloCumulFunctionExpr f, final int t)\n
    getValue(final IloStateFunction f, final int t)\n
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
def getValues():
    '''returns None\n\n
    getValues(final IloIntVar[] vars, final double[] vals)\n
    getValues(final ilog.concert.IloIntVarArray varArray, final double[] numArray)\n
    getValues(final IloNumVar[] varArray, final double[] numArray)\n
    '''
def getIntValue():
    '''returns int\n\n
    getIntValue(final IloIntVar var)\n
    '''
def getMin():
    '''returns double\n\n
    getMin(final IloNumVar var)\n
    '''
def getMax():
    '''returns double\n\n
    getMax(final IloNumVar var)\n
    '''
def isInDomain():
    '''returns boolean\n\n
    isInDomain(final IloNumVar var, final int value)\n
    '''
def getDomainSize():
    '''returns int\n\n
    getDomainSize(final IloNumVar var)\n
    '''
def isFixed():
    '''returns boolean\n\n
    isFixed(final IloNumVar var)\n
    isFixed(final IloIntervalVar a)\n
    isFixed(final IloIntervalSequenceVar seq)\n
    isFixed(final IloCumulFunctionExpr f)\n
    isFixed(final IloStateFunction f)\n
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
def getDomain():
    '''returns String\n\n
    getDomain(final IloIntervalVar var)\n
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
    '''
def getSegmentStart():
    '''returns int\n\n
    getSegmentStart(final IloCumulFunctionExpr f, final int i)\n
    getSegmentStart(final IloStateFunction f, final int i)\n
    '''
def getSegmentEnd():
    '''returns int\n\n
    getSegmentEnd(final IloCumulFunctionExpr f, final int i)\n
    getSegmentEnd(final IloStateFunction f, final int i)\n
    '''
def getSegmentValue():
    '''returns int\n\n
    getSegmentValue(final IloCumulFunctionExpr f, final int i)\n
    getSegmentValue(final IloStateFunction f, final int i)\n
    '''
def searchPhase():
    '''returns IloSearchPhase\n\n
    searchPhase(final IloIntVar[] vars)\n
    searchPhase(final ilog.concert.IloIntVarArray vars)\n
    searchPhase(final IloIntVar[] vars, final IloIntVarChooser varChooser, final IloIntValueChooser valueChooser)\n
    searchPhase(final ilog.concert.IloIntVarArray vars, final IloIntVarChooser varChooser, final IloIntValueChooser valueChooser)\n
    searchPhase(final IloIntVarChooser varChooser, final IloIntValueChooser valueChooser)\n
    searchPhase(final IloIntervalVar[] intervalVars)\n
    searchPhase(final IloIntervalSequenceVar[] sequenceVars)\n
    '''
def intVarChooser():
    '''returns IloIntVarChooser\n\n
    intVarChooser(final IloVarSelector varSel)\n
    intVarChooser(final IloVarSelector[] varSels)\n
    '''
def intValueChooser():
    '''returns IloIntValueChooser\n\n
    intValueChooser(final IloValueSelector valueSel)\n
    intValueChooser(final IloValueSelector[] valueSels)\n
    '''
def selectSmallest():
    '''returns IloValueSelector\n\n
    selectSmallest(final double minNumber, final IloIntVarEval e)\n
    selectSmallest(final IloIntVarEval e)\n
    selectSmallest(final IloIntVarEval e, final double tol)\n
    selectSmallest(final double minNumber, final IloIntValueEval e)\n
    selectSmallest(final IloIntValueEval e)\n
    selectSmallest(final IloIntValueEval e, final double tol)\n
    '''
def selectLargest():
    '''returns IloValueSelector\n\n
    selectLargest(final double minNumber, final IloIntVarEval e)\n
    selectLargest(final IloIntVarEval e)\n
    selectLargest(final IloIntVarEval e, final double tol)\n
    selectLargest(final double minNumber, final IloIntValueEval e)\n
    selectLargest(final IloIntValueEval e)\n
    selectLargest(final IloIntValueEval e, final double tol)\n
    '''
def selectRandomVar():
    '''returns IloVarSelector\n\n
    selectRandomVar()\n
    '''
def selectRandomValue():
    '''returns IloValueSelector\n\n
    selectRandomValue()\n
    '''
def explicitValueEval():
    '''returns IloIntValueEval\n\n
    explicitValueEval(final int[] vals, final int[] evaluation, final double defautEval)\n
    explicitValueEval(final int[] vals, final int[] evaluation)\n
    explicitValueEval(final int[] vals, final double[] evaluation, final double defautEval)\n
    explicitValueEval(final int[] vals, final double[] evaluation)\n
    '''
def valueIndex():
    '''returns IloIntValueEval\n\n
    valueIndex(final int[] vals, final int defautEval)\n
    valueIndex(final int[] vals)\n
    '''
def value():
    '''returns IloIntValueEval\n\n
    value()\n
    '''
def valueImpact():
    '''returns IloIntValueEval\n\n
    valueImpact()\n
    '''
def valueSuccessRate():
    '''returns IloIntValueEval\n\n
    valueSuccessRate()\n
    '''
def valueLocalImpact():
    '''returns IloIntValueEval\n\n
    valueLocalImpact()\n
    '''
def valueLowerObjVariation():
    '''returns IloIntValueEval\n\n
    valueLowerObjVariation()\n
    '''
def valueUpperObjVariation():
    '''returns IloIntValueEval\n\n
    valueUpperObjVariation()\n
    '''
def varIndex():
    '''returns IloIntVarEval\n\n
    varIndex(final ilog.concert.IloIntVarArray vars, final int defaultIndex)\n
    varIndex(final IloIntVar[] vars)\n
    varIndex(final IloIntVar[] vars, final int defaultIndex)\n
    varIndex(final ilog.concert.IloIntVarArray vars)\n
    '''
def explicitVarEval():
    '''returns IloIntVarEval\n\n
    explicitVarEval(final IloIntVar[] vars, final int[] vals, final double defautEval)\n
    explicitVarEval(final IloIntVar[] vars, final int[] vals)\n
    explicitVarEval(final IloIntVar[] vars, final double[] vals, final double defautEval)\n
    explicitVarEval(final IloIntVar[] vars, final double[] vals)\n
    '''
def domainMin():
    '''returns IloIntVarEval\n\n
    domainMin()\n
    '''
def domainMax():
    '''returns IloIntVarEval\n\n
    domainMax()\n
    '''
def domainSize():
    '''returns IloIntVarEval\n\n
    domainSize()\n
    '''
def regretOnMin():
    '''returns IloIntVarEval\n\n
    regretOnMin()\n
    '''
def regretOnMax():
    '''returns IloIntVarEval\n\n
    regretOnMax()\n
    '''
def varSuccessRate():
    '''returns IloIntVarEval\n\n
    varSuccessRate()\n
    '''
def varImpact():
    '''returns IloIntVarEval\n\n
    varImpact()\n
    '''
def varLocalImpact():
    '''returns IloIntVarEval\n\n
    varLocalImpact(final int effort)\n
    varLocalImpact()\n
    '''
def impactOfLastBranch():
    '''returns IloIntVarEval\n\n
    impactOfLastBranch()\n
    '''
def varLowerObjVariation():
    '''returns IloIntVarEval\n\n
    varLowerObjVariation()\n
    '''
def varUpperObjVariation():
    '''returns IloIntVarEval\n\n
    varUpperObjVariation()\n
    '''
def add():
    '''returns IloAddable\n\n
    add(final IloAddable object)\n
    '''
def remove():
    '''returns None\n\n
    remove(final IloAddable object)\n
    remove()\n
    remove()\n
    remove()\n
    '''
def startOf():
    '''returns IloIntExpr\n\n
    startOf(final IloIntervalVar a)\n
    startOf(final IloIntervalVar a, final int absVal)\n
    '''
def endOf():
    '''returns IloIntExpr\n\n
    endOf(final IloIntervalVar a)\n
    endOf(final IloIntervalVar a, final int absVal)\n
    '''
def lengthOf():
    '''returns IloIntExpr\n\n
    lengthOf(final IloIntervalVar a)\n
    lengthOf(final IloIntervalVar a, final int absVal)\n
    '''
def sizeOf():
    '''returns IloIntExpr\n\n
    sizeOf(final IloIntervalVar a)\n
    sizeOf(final IloIntervalVar a, final int absVal)\n
    '''
def typeOfNext():
    '''returns IloIntExpr\n\n
    typeOfNext(final IloIntervalSequenceVar seq, final IloIntervalVar a, final int lastVal)\n
    typeOfNext(final IloIntervalSequenceVar seq, final IloIntervalVar a, final int lastVal, final int absVal)\n
    '''
def typeOfPrevious():
    '''returns IloIntExpr\n\n
    typeOfPrevious(final IloIntervalSequenceVar seq, final IloIntervalVar a, final int firstVal)\n
    typeOfPrevious(final IloIntervalSequenceVar seq, final IloIntervalVar a, final int firstVal, final int absVal)\n
    '''
def startOfNext():
    '''returns IloIntExpr\n\n
    startOfNext(final IloIntervalSequenceVar seq, final IloIntervalVar a, final int lastVal)\n
    startOfNext(final IloIntervalSequenceVar seq, final IloIntervalVar a, final int lastVal, final int absVal)\n
    '''
def startOfPrevious():
    '''returns IloIntExpr\n\n
    startOfPrevious(final IloIntervalSequenceVar seq, final IloIntervalVar a, final int firstVal)\n
    startOfPrevious(final IloIntervalSequenceVar seq, final IloIntervalVar a, final int firstVal, final int absVal)\n
    '''
def endOfNext():
    '''returns IloIntExpr\n\n
    endOfNext(final IloIntervalSequenceVar seq, final IloIntervalVar a, final int lastVal)\n
    endOfNext(final IloIntervalSequenceVar seq, final IloIntervalVar a, final int lastVal, final int absVal)\n
    '''
def endOfPrevious():
    '''returns IloIntExpr\n\n
    endOfPrevious(final IloIntervalSequenceVar seq, final IloIntervalVar a, final int firstVal)\n
    endOfPrevious(final IloIntervalSequenceVar seq, final IloIntervalVar a, final int firstVal, final int absVal)\n
    '''
def sizeOfNext():
    '''returns IloIntExpr\n\n
    sizeOfNext(final IloIntervalSequenceVar seq, final IloIntervalVar a, final int lastVal)\n
    sizeOfNext(final IloIntervalSequenceVar seq, final IloIntervalVar a, final int lastVal, final int absVal)\n
    '''
def sizeOfPrevious():
    '''returns IloIntExpr\n\n
    sizeOfPrevious(final IloIntervalSequenceVar seq, final IloIntervalVar a, final int firstVal)\n
    sizeOfPrevious(final IloIntervalSequenceVar seq, final IloIntervalVar a, final int firstVal, final int absVal)\n
    '''
def lengthOfNext():
    '''returns IloIntExpr\n\n
    lengthOfNext(final IloIntervalSequenceVar seq, final IloIntervalVar a, final int lastVal)\n
    lengthOfNext(final IloIntervalSequenceVar seq, final IloIntervalVar a, final int lastVal, final int absVal)\n
    '''
def lengthOfPrevious():
    '''returns IloIntExpr\n\n
    lengthOfPrevious(final IloIntervalSequenceVar seq, final IloIntervalVar a, final int firstVal)\n
    lengthOfPrevious(final IloIntervalSequenceVar seq, final IloIntervalVar a, final int firstVal, final int absVal)\n
    '''
def overlapLength():
    '''returns IloIntExpr\n\n
    overlapLength(final IloIntervalVar a1, final IloIntervalVar a2, final int absVal)\n
    overlapLength(final IloIntervalVar a1, final IloIntervalVar a2)\n
    overlapLength(final IloIntervalVar a, final int start, final int end, final int absVal)\n
    overlapLength(final IloIntervalVar a, final int start, final int end)\n
    '''
def startEval():
    '''returns IloNumExpr\n\n
    startEval(final IloIntervalVar a, final IloNumToNumSegmentFunction f)\n
    startEval(final IloIntervalVar a, final IloNumToNumSegmentFunction f, final double absVal)\n
    '''
def endEval():
    '''returns IloNumExpr\n\n
    endEval(final IloIntervalVar a, final IloNumToNumSegmentFunction f)\n
    endEval(final IloIntervalVar a, final IloNumToNumSegmentFunction f, final double absVal)\n
    '''
def lengthEval():
    '''returns IloNumExpr\n\n
    lengthEval(final IloIntervalVar a, final IloNumToNumSegmentFunction f)\n
    lengthEval(final IloIntervalVar a, final IloNumToNumSegmentFunction f, final double absVal)\n
    '''
def sizeEval():
    '''returns IloNumExpr\n\n
    sizeEval(final IloIntervalVar a, final IloNumToNumSegmentFunction f)\n
    sizeEval(final IloIntervalVar a, final IloNumToNumSegmentFunction f, final double absVal)\n
    '''
def noOverlap():
    '''returns IloNoOverlap\n\n
    noOverlap(final IloIntervalVar[] a, final String name)\n
    noOverlap(final IloIntervalVar[] a)\n
    noOverlap(final Collection<IloIntervalVar> a)\n
    noOverlap(final IloIntervalSequenceVar seq, final IloTransitionDistance tdist, final String name)\n
    noOverlap(final IloIntervalSequenceVar seq, final IloTransitionDistance tdist)\n
    noOverlap(final IloIntervalSequenceVar seq)\n
    noOverlap(final IloIntervalSequenceVar seq, final IloTransitionDistance tdist, final boolean direct, final String name)\n
    noOverlap(final IloIntervalSequenceVar seq, final IloTransitionDistance tdist, final boolean direct)\n
    '''
def span():
    '''returns IloSpan\n\n
    span(final IloIntervalVar a, final IloIntervalVar[] bs, final String name)\n
    span(final IloIntervalVar a, final IloIntervalVar[] bs)\n
    '''
def alternative():
    '''returns IloAlternative\n\n
    alternative(final IloIntervalVar a, final IloIntervalVar[] bs)\n
    alternative(final IloIntervalVar a, final IloIntervalVar[] bs, final String name)\n
    alternative(final IloIntervalVar a, final IloIntervalVar[] bs, final int c)\n
    alternative(final IloIntervalVar a, final IloIntervalVar[] bs, final int c, final String name)\n
    alternative(final IloIntervalVar a, final IloIntervalVar[] bs, final IloIntExpr c)\n
    alternative(final IloIntervalVar a, final IloIntervalVar[] bs, final IloIntExpr c, final String name)\n
    alternative(final IloIntervalVar a, final Collection<IloIntervalVar> bs)\n
    '''
def synchronize():
    '''returns IloSynchronize\n\n
    synchronize(final IloIntervalVar a, final IloIntervalVar[] bs, final String name)\n
    synchronize(final IloIntervalVar a, final IloIntervalVar[] bs)\n
    '''
def isomorphism():
    '''returns IloIsomorphism\n\n
    isomorphism(final IloIntervalVar[] domain, final IloIntervalVar[] intervals)\n
    isomorphism(final IloIntervalVar[] domain, final IloIntervalVar[] intervals, final String name)\n
    isomorphism(final IloIntervalVar[] domain, final IloIntervalVar[] intervals, final IloIntExpr[] map, final int absVal)\n
    isomorphism(final IloIntervalVar[] domain, final IloIntervalVar[] intervals, final IloIntExpr[] map, final int absVal, final String name)\n
    '''
def cumulFunctionExpr():
    '''returns IloCumulFunctionExpr\n\n
    cumulFunctionExpr()\n
    cumulFunctionExpr(final String name)\n
    '''
def heightAtStart():
    '''returns IloIntExpr\n\n
    heightAtStart(final IloIntervalVar a, final IloCumulFunctionExpr f)\n
    heightAtStart(final IloIntervalVar a, final IloCumulFunctionExpr f, final int absVal)\n
    '''
def heightAtEnd():
    '''returns IloIntExpr\n\n
    heightAtEnd(final IloIntervalVar a, final IloCumulFunctionExpr f)\n
    heightAtEnd(final IloIntervalVar a, final IloCumulFunctionExpr f, final int absVal)\n
    '''
def step():
    '''returns IloCumulFunctionExpr\n\n
    step(final int t, final int v)\n
    '''
def pulse():
    '''returns IloCumulFunctionExpr\n\n
    pulse(final int start, final int end, final int v)\n
    pulse(final IloIntervalVar a, final int v)\n
    pulse(final IloIntervalVar a, final int vmin, final int vmax)\n
    '''
def stepAtStart():
    '''returns IloCumulFunctionExpr\n\n
    stepAtStart(final IloIntervalVar a, final int v)\n
    stepAtStart(final IloIntervalVar a, final int vmin, final int vmax)\n
    '''
def stepAtEnd():
    '''returns IloCumulFunctionExpr\n\n
    stepAtEnd(final IloIntervalVar a, final int v)\n
    stepAtEnd(final IloIntervalVar a, final int vmin, final int vmax)\n
    '''
def diff():
    '''returns IloCumulFunctionExpr\n\n
    diff(final IloCumulFunctionExpr f1, final IloCumulFunctionExpr f2)\n
    '''
def transitionDistance():
    '''returns IloTransitionDistance\n\n
    transitionDistance(final int i, final String name)\n
    transitionDistance(final int i)\n
    transitionDistance(final int[][] dtable, final String name)\n
    transitionDistance(final int[][] dtable)\n
    '''
def stateFunction():
    '''returns IloStateFunction\n\n
    stateFunction()\n
    stateFunction(final String name)\n
    stateFunction(final IloTransitionDistance t)\n
    stateFunction(final IloTransitionDistance t, final String name)\n
    '''
def numToNumSegmentFunction():
    '''returns IloNumToNumSegmentFunction\n\n
    numToNumSegmentFunction(final double xmin, final double xmax, final double dval, final String name)\n
    numToNumSegmentFunction(final double xmin, final double xmax, final double dval)\n
    numToNumSegmentFunction(final double xmin, final double xmax)\n
    numToNumSegmentFunction(final double xmin)\n
    numToNumSegmentFunction()\n
    numToNumSegmentFunction(final double[] x, final double[] v, final double xmin, final double xmax, final String name)\n
    numToNumSegmentFunction(final double[] x, final double[] v, final double xmin, final double xmax)\n
    numToNumSegmentFunction(final double[] x, final double[] v, final double xmin)\n
    numToNumSegmentFunction(final double[] x, final double[] v)\n
    '''
def piecewiseLinearFunction():
    '''returns IloNumToNumSegmentFunction\n\n
    piecewiseLinearFunction(final double[] point, final double[] slope, final double a, final double fa, final String name)\n
    piecewiseLinearFunction(final double[] point, final double[] slope, final double a, final double fa)\n
    '''
def numToNumSegmentFunctionCursor():
    '''returns IloNumToNumSegmentFunctionCursor\n\n
    numToNumSegmentFunctionCursor(final IloNumToNumSegmentFunction f, final double x)\n
    '''
def numToNumStepFunction():
    '''returns IloNumToNumStepFunction\n\n
    numToNumStepFunction(final double xmin, final double xmax, final double dval, final String name)\n
    numToNumStepFunction(final double xmin, final double xmax, final double dval)\n
    numToNumStepFunction(final double xmin, final double xmax)\n
    numToNumStepFunction(final double xmin)\n
    numToNumStepFunction()\n
    '''
def numToNumStepFunctionCursor():
    '''returns IloNumToNumStepFunctionCursor\n\n
    numToNumStepFunctionCursor(final IloNumToNumStepFunction f, final double x)\n
    '''
def iterator():
    '''returns Iterator\n\n
    iterator(final IloIntVar var)\n
    '''
def refineConflict():
    '''returns boolean\n\n
    refineConflict()\n
    refineConflict(final IloConstraint[] csts)\n
    refineConflict(final IloConstraint[] csts, final double[] prefs)\n
    refineConflict(final IloSolution sol)\n
    refineConflict(final IloConstraintArray csts)\n
    refineConflict(final IloConstraintArray csts, final ilog.concert.IloNumArray prefs)\n
    '''
def getConflict():
    '''returns ConflictStatus\n\n
    getConflict(final IloConstraint cst)\n
    getConflict(final IloNumVar var)\n
    getConflict(final IloIntervalVar var)\n
    '''
def writeConflict():
    '''returns None\n\n
    writeConflict(final OutputStream s)\n
    '''
def exportConflict():
    '''returns None\n\n
    exportConflict(final OutputStream s)\n
    '''
def registerXML():
    '''returns None\n\n
    registerXML()\n
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
def end():
    '''returns None\n\n
    end()\n
    '''
def getInfoIterator():
    '''returns InfoIterator\n\n
    getInfoIterator()\n
    '''
def getParamIterator():
    '''returns ParamIterator\n\n
    getParamIterator()\n
    '''
def getStatusString():
    '''returns String\n\n
    getStatusString()\n
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
def hasNext():
    '''returns boolean\n\n
    hasNext()\n
    hasNext()\n
    hasNext()\n
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
def getId():
    '''returns int\n\n
    getId()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    getName()\n
    '''
def isInt():
    '''returns boolean\n\n
    isInt()\n
    isInt()\n
    '''
def isNum():
    '''returns boolean\n\n
    isNum()\n
    isNum()\n
    '''
def isSymbolic():
    '''returns boolean\n\n
    isSymbolic()\n
    '''
def getSymbolicValueString():
    '''returns String\n\n
    getSymbolicValueString()\n
    '''
