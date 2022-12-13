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
'''public void readVMConfig(final String file)
'''
pass
def hasVMConfig():
'''public boolean hasVMConfig()
'''
pass
def delVMConfig():
'''public void delVMConfig()
'''
pass
def copyVMConfig():
'''public void copyVMConfig(final String xmlString)
'''
pass
def getMIPRelativeGap():
'''public double getMIPRelativeGap()
'''
pass
def remove():
'''public IloAddable remove(final IloAddable object)
public void remove(final Callback cb)
public void remove()
public void remove()
'''
pass
def getModel():
'''public IloModel getModel()
'''
pass
def setModel():
'''public void setModel(final IloModel model)
'''
pass
def le():
'''public IloConstraint le(final IloNumExpr e1, final IloNumExpr e2, final String name)
'''
pass
def ge():
'''public IloConstraint ge(final IloNumExpr e1, final IloNumExpr e2, final String name)
'''
pass
def eq():
'''public IloConstraint eq(final IloNumExpr e1, final IloNumExpr e2, final String name)
'''
pass
def iterator():
'''public Iterator iterator()
'''
pass
def numVar():
'''public IloNumVar numVar(final IloColumn column, final double lb, final double ub, final IloNumVarType type, final String name)
public IloNumVar numVar(final IloColumn column, final double lb, final double ub, final IloNumVarType type)
public IloNumVar numVar(final IloColumn column, final double lb, final double ub, final String name)
public IloNumVar numVar(final IloColumn column, final double lb, final double ub)
'''
pass
def numVarArray():
'''public IloNumVar[] numVarArray(final IloColumnArray cols, final double lb, final double ub, final IloNumVarType type)
public IloNumVar[] numVarArray(final IloColumnArray cols, final double lb, final double ub, final IloNumVarType type, final String[] name)
public IloNumVar[] numVarArray(final IloColumnArray cols, final double[] lb, final double[] ub, final IloNumVarType[] type)
public IloNumVar[] numVarArray(final IloColumnArray cols, final double[] lb, final double[] ub, final IloNumVarType[] type, final String[] name)
public IloNumVar[] numVarArray(final IloColumnArray cols, final double lb, final double ub)
public IloNumVar[] numVarArray(final IloColumnArray cols, final double[] lb, final double[] ub)
public IloNumVar[] numVarArray(final IloColumnArray cols, final double lb, final double ub, final String[] name)
public IloNumVar[] numVarArray(final IloColumnArray cols, final double[] lb, final double[] ub, final String[] name)
'''
pass
def intVar():
'''public IloIntVar intVar(final IloColumn column, final int lb, final int ub)
public IloIntVar intVar(final IloColumn column, final int lb, final int ub, final String name)
'''
pass
def intVarArray():
'''public IloIntVar[] intVarArray(final IloColumnArray cols, final int lb, final int ub, final String[] name)
public IloIntVar[] intVarArray(final IloColumnArray cols, final int[] lb, final int[] ub, final String[] name)
public IloIntVar[] intVarArray(final IloColumnArray cols, final int lb, final int ub)
public IloIntVar[] intVarArray(final IloColumnArray cols, final int[] lb, final int[] ub)
'''
pass
def boolVar():
'''public IloIntVar boolVar(final IloColumn column, final String name)
public IloIntVar boolVar(final IloColumn column)
'''
pass
def boolVarArray():
'''public IloIntVar[] boolVarArray(final IloColumnArray cols)
public IloIntVar[] boolVarArray(final IloColumnArray cols, final String[] name)
'''
pass
def piecewiseLinear():
'''public IloNumExpr piecewiseLinear(final IloNumExpr expr, final double[] points, final double[] slopes, final double a, final double fa)
public IloNumExpr piecewiseLinear(final IloNumExpr expr, final double[] points, final int startPoints, final int num, final double[] slopes, final int startSlopes, final double a, final double fa)
public IloNumExpr piecewiseLinear(final IloNumExpr node, final double firstSlope, final double[] points, final double[] values, final double lastSlope)
'''
pass
def addToExpr():
'''public void addToExpr(final IloObjective obj, final IloNumExpr expr)
public void addToExpr(final IloRange rng, final IloNumExpr expr)
'''
pass
def setLinearCoef():
'''public void setLinearCoef(final IloForAllRange ct, final IloNumVar var, final double val)
public void setLinearCoef(final IloForAllRange ct, final double val, final IloNumVar var)
public void setLinearCoef(final IloObjective obj, final double val, final IloNumVar var)
public void setLinearCoef(final IloObjective obj, final IloNumVar var, final double val)
public void setLinearCoef(final IloRange rng, final double val, final IloNumVar var)
public void setLinearCoef(final IloRange rng, final IloNumVar var, final double val)
'''
pass
def setLinearCoefs():
'''public void setLinearCoefs(final IloForAllRange ct, final double[] val, final IloNumVar[] var)
public void setLinearCoefs(final IloForAllRange ct, final IloNumVar[] var, final double[] val)
public void setLinearCoefs(final IloForAllRange ct, final double[] val, final IloNumVar[] var, final int start, final int num)
public void setLinearCoefs(final IloForAllRange ct, final IloNumVar[] var, final double[] val, final int start, final int num)
public void setLinearCoefs(final IloObjective obj, final double[] val, final IloNumVar[] var)
public void setLinearCoefs(final IloObjective obj, final IloNumVar[] var, final double[] val)
public void setLinearCoefs(final IloObjective obj, final double[] val, final IloNumVar[] var, final int start, final int num)
public void setLinearCoefs(final IloObjective obj, final IloNumVar[] var, final double[] val, final int start, final int num)
public void setLinearCoefs(final IloRange rng, final double[] val, final IloNumVar[] var)
public void setLinearCoefs(final IloRange rng, final IloNumVar[] var, final double[] val)
public void setLinearCoefs(final IloRange rng, final double[] val, final IloNumVar[] var, final int start, final int num)
public void setLinearCoefs(final IloRange rng, final IloNumVar[] var, final double[] val, final int start, final int num)
'''
pass
def semiContVar():
'''public IloSemiContVar semiContVar(final double lb, final double ub, final IloNumVarType type, final String name)
public IloSemiContVar semiContVar(final double lb, final double ub, final IloNumVarType type)
public IloSemiContVar semiContVar(final IloColumn column, final double lb, final double ub, final IloNumVarType type, final String name)
public IloSemiContVar semiContVar(final IloColumn column, final double lb, final double ub, final IloNumVarType type)
'''
pass
def semiContVarArray():
'''public IloSemiContVar[] semiContVarArray(final int n, final double lb, final double ub, final IloNumVarType type)
public IloSemiContVar[] semiContVarArray(final int n, final double[] lb, final double[] ub, final IloNumVarType[] type)
public IloSemiContVar[] semiContVarArray(final int n, final double lb, final double ub, final IloNumVarType type, final String[] name)
public IloSemiContVar[] semiContVarArray(final int n, final double[] lb, final double[] ub, final IloNumVarType[] type, final String[] name)
public IloSemiContVar[] semiContVarArray(final IloColumnArray cols, final double lb, final double ub, final IloNumVarType type)
public IloSemiContVar[] semiContVarArray(final IloColumnArray cols, final double[] lb, final double[] ub, final IloNumVarType[] type)
public IloSemiContVar[] semiContVarArray(final IloColumnArray cols, final double lb, final double ub, final IloNumVarType type, final String[] name)
public IloSemiContVar[] semiContVarArray(final IloColumnArray cols, final double[] lb, final double[] ub, final IloNumVarType[] type, final String[] name)
'''
pass
def minimize():
'''public IloObjective minimize()
public IloObjective minimize(final String name)
'''
pass
def maximize():
'''public IloObjective maximize()
public IloObjective maximize(final String name)
'''
pass
def objective():
'''public IloObjective objective(final IloObjectiveSense sense)
public IloObjective objective(final IloObjectiveSense sense, final String name)
'''
pass
def addMinimize():
'''public IloObjective addMinimize()
public IloObjective addMinimize(final String name)
'''
pass
def addMaximize():
'''public IloObjective addMaximize()
public IloObjective addMaximize(final String name)
'''
pass
def addObjective():
'''public IloObjective addObjective(final IloObjectiveSense sense)
public IloObjective addObjective(final IloObjectiveSense sense, final String name)
'''
pass
def conversion():
'''public IloConversion conversion(final IloNumVar var, final IloNumVarType type, final String name)
public IloConversion conversion(final IloNumVar var, final IloNumVarType type)
public IloConversion conversion(final IloNumVar[] var, final IloNumVarType type, final String name)
public IloConversion conversion(final IloNumVar[] ilovar, final IloNumVarType type)
public IloConversion conversion(final IloNumVar[] var, final IloNumVarType[] type, final String name)
public IloConversion conversion(final IloNumVar[] ilovar, final IloNumVarType[] type)
'''
pass
def addLPMatrix():
'''public IloLPMatrix addLPMatrix(final String name)
public IloLPMatrix addLPMatrix()
'''
pass
def LPMatrix():
'''public IloLPMatrix LPMatrix(final String name)
public IloLPMatrix LPMatrix()
'''
pass
def addRange():
'''public IloRange addRange(final double lb, final double ub, final String name)
public IloRange addRange(final double lb, final double ub)
'''
pass
def range():
'''public IloRange range(final double lb, final double ub, final String name)
public IloRange range(final double lb, final double ub)
'''
pass
def addSOS1():
'''public IloSOS1 addSOS1(final IloNumVar[] var, final double[] val)
public IloSOS1 addSOS1(final IloNumVar[] var, final double[] val, final int start, final int num)
public IloSOS1 addSOS1(final IloNumVar[] var, final double[] val, final String name)
public IloSOS1 addSOS1(final IloNumVar[] var, final double[] val, final int start, final int num, final String name)
'''
pass
def SOS1():
'''public IloSOS1 SOS1(final IloNumVar[] var, final double[] val)
public IloSOS1 SOS1(final IloNumVar[] var, final double[] val, final int start, final int num)
public IloSOS1 SOS1(final IloNumVar[] var, final double[] val, final String name)
public IloSOS1 SOS1(final IloNumVar[] var, final double[] val, final int start, final int num, final String name)
'''
pass
def addSOS2():
'''public IloSOS2 addSOS2(final IloNumVar[] var, final double[] val)
public IloSOS2 addSOS2(final IloNumVar[] var, final double[] val, final int start, final int num)
public IloSOS2 addSOS2(final IloNumVar[] var, final double[] val, final String name)
public IloSOS2 addSOS2(final IloNumVar[] var, final double[] val, final int start, final int num, final String name)
'''
pass
def SOS2():
'''public IloSOS2 SOS2(final IloNumVar[] var, final double[] val)
public IloSOS2 SOS2(final IloNumVar[] var, final double[] val, final int start, final int num)
public IloSOS2 SOS2(final IloNumVar[] var, final double[] val, final String name)
public IloSOS2 SOS2(final IloNumVar[] var, final double[] val, final int start, final int num, final String name)
'''
pass
def column():
'''public IloColumn column(final IloRange rng, final double val)
public IloColumn column(final IloObjective obj, final double val)
public IloColumn column(final IloLPMatrix lp)
public IloColumn column(final IloLPMatrix lp, final int[] ind, final double[] val)
public IloColumn column(final IloLPMatrix lp, final int[] ind, final double[] val, final int start, final int num)
'''
pass
def columnArray():
'''public IloColumnArray columnArray(final IloRange rng, final double[] val)
public IloColumnArray columnArray(final IloRange rng, final double[] val, final int start, final int num)
public IloColumnArray columnArray(final IloObjective obj, final double[] val)
public IloColumnArray columnArray(final IloObjective obj, final double[] val, final int start, final int num)
public IloColumnArray columnArray(final IloLPMatrix lp, final int num, final int[][] ind, final double[][] val)
public IloColumnArray columnArray(final IloLPMatrix lp, final int num)
'''
pass
def delete():
'''public void delete(final IloCopyable obj)
public void delete(final IloCopyable[] obj)
public void delete(final IloCopyable[] objs, final int beg, final int num)
'''
pass
def addUserCut():
'''public IloConstraint addUserCut(final IloConstraint cut)
'''
pass
def addUserCuts():
'''public IloConstraint[] addUserCuts(final IloConstraint[] cuts)
public IloConstraint[] addUserCuts(final IloConstraint[] cuts, final int start, final int num)
'''
pass
def clearUserCuts():
'''public void clearUserCuts()
'''
pass
def addLazyConstraint():
'''public IloConstraint addLazyConstraint(final IloConstraint cut)
'''
pass
def addLazyConstraints():
'''public IloConstraint[] addLazyConstraints(final IloConstraint[] cut)
public IloConstraint[] addLazyConstraints(final IloConstraint[] cut, final int start, final int num)
'''
pass
def clearLazyConstraints():
'''public void clearLazyConstraints()
'''
pass
def addCut():
'''public IloConstraint addCut(final IloConstraint cut)
'''
pass
def addCuts():
'''public IloConstraint[] addCuts(final IloConstraint[] cut)
public IloConstraint[] addCuts(final IloConstraint[] cut, final int start, final int num)
'''
pass
def clearCuts():
'''public void clearCuts()
'''
pass
def exportModel():
'''public void exportModel(final String name)
'''
pass
def importModel():
'''public void importModel(final String name)
'''
pass
def getMatrix():
'''public IloLPMatrixImpl getMatrix()
'''
pass
def clearModel():
'''public void clearModel()
'''
pass
def getNcols():
'''public int getNcols()
'''
pass
def getNrows():
'''public int getNrows()
'''
pass
def getNQCs():
'''public int getNQCs()
'''
pass
def getNSOS1():
'''public int getNSOS1()
'''
pass
def getNSOS2():
'''public int getNSOS2()
'''
pass
def getNSOSs():
'''public int getNSOSs()
'''
pass
def getNNZs():
'''public int getNNZs()
'''
pass
def getNNZs64():
'''public long getNNZs64()
'''
pass
def getNintVars():
'''public int getNintVars()
'''
pass
def getNbinVars():
'''public int getNbinVars()
'''
pass
def getNsemiContVars():
'''public int getNsemiContVars()
'''
pass
def getNsemiIntVars():
'''public int getNsemiIntVars()
'''
pass
def isMIP():
'''public boolean isMIP()
'''
pass
def isQuadratic():
'''public final boolean isQuadratic()
'''
pass
def isQP():
'''public final boolean isQP()
'''
pass
def isQO():
'''public boolean isQO()
'''
pass
def isQC():
'''public boolean isQC()
'''
pass
def LPMatrixIterator():
'''public Iterator LPMatrixIterator()
'''
pass
def rangeIterator():
'''public Iterator rangeIterator()
'''
pass
def conversionIterator():
'''public Iterator conversionIterator()
'''
pass
def SOS1iterator():
'''public Iterator SOS1iterator()
'''
pass
def SOS2iterator():
'''public Iterator SOS2iterator()
'''
pass
def getObjective():
'''public IloObjective getObjective()
'''
pass
def getStatus():
'''public Status getStatus()
public int getStatus()
'''
pass
def isPrimalFeasible():
'''public boolean isPrimalFeasible()
public boolean isPrimalFeasible()
public boolean isPrimalFeasible()
'''
pass
def isDualFeasible():
'''public boolean isDualFeasible()
public boolean isDualFeasible()
public boolean isDualFeasible()
'''
pass
def use():
'''public void use(final Aborter aborter)
public void use(final Callback cb)
'''
pass
def getAborter():
'''public Aborter getAborter()
'''
pass
def setParam():
'''public void setParam(final IntParam which, final int val)
public void setParam(final BooleanParam which, final boolean val)
public void setParam(final LongParam which, final long val)
public void setParam(final DoubleParam which, final double val)
public void setParam(final StringParam which, final String val)
public void setParam(final IntParam which, final int val)
public void setParam(final StringParam which, final String val)
public void setParam(final BooleanParam which, final boolean val)
public void setParam(final DoubleParam which, final double val)
'''
pass
def getParam():
'''public int getParam(final IntParam which)
public boolean getParam(final BooleanParam which)
public long getParam(final LongParam which)
public double getParam(final DoubleParam which)
public String getParam(final StringParam which)
public int getParam(final IntParam which)
public String getParam(final StringParam which)
public boolean getParam(final BooleanParam which)
public double getParam(final DoubleParam which)
'''
pass
def getMin():
'''public int getMin(final IntParam which)
public double getMin(final DoubleParam which)
'''
pass
def getMax():
'''public int getMax(final IntParam which)
public double getMax(final DoubleParam which)
'''
pass
def getDefault():
'''public int getDefault(final IntParam which)
public boolean getDefault(final BooleanParam which)
public long getDefault(final LongParam which)
public double getDefault(final DoubleParam which)
public String getDefault(final StringParam which)
'''
pass
def setDefaults():
'''public void setDefaults()
'''
pass
def getVersion():
'''public String getVersion()
'''
pass
def setDeleteMode():
'''public void setDeleteMode(final DeleteMode mode)
'''
pass
def getDeleteMode():
'''public DeleteMode getDeleteMode()
'''
pass
def getCplexStatus():
'''public CplexStatus getCplexStatus()
'''
pass
def getCplexSubStatus():
'''public CplexStatus getCplexSubStatus()
'''
pass
def getAlgorithm():
'''public int getAlgorithm()
'''
pass
def getSubAlgorithm():
'''public int getSubAlgorithm()
'''
pass
def getObjValue():
'''public double getObjValue()
public double getObjValue(final int soln)
'''
pass
def getBestObjValue():
'''public double getBestObjValue()
'''
pass
def getCutoff():
'''public double getCutoff()
'''
pass
def getValues():
'''public double[] getValues(final IloLPMatrix matrix)
public double[] getValues(final IloLPMatrix matrix, final int soln)
public double[] getValues(final IloLPMatrix matrix, final int start, final int num)
public double[] getValues(final IloLPMatrix matrix, final int start, final int num, final int soln)
public double[] getValues(final IloNumVar[] var)
public double[] getValues(final IloNumVar[] var, final int soln)
public double[] getValues(final IloNumVar[] var, final int start, final int num)
public double[] getValues(final IloNumVar[] var, final int start, final int num, final int soln)
'''
pass
def getValue():
'''public double getValue(final IloNumVar var)
public double getValue(final IloNumVar var, final int soln)
public double getValue(final IloNumExpr expr)
public double getValue(final IloNumExpr expr, final int soln)
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public int getValue()
public long getValue()
public double getValue()
public boolean getValue()
public String getValue()
public double getValue()
'''
pass
def getReducedCosts():
'''public double[] getReducedCosts(final IloLPMatrix matrix)
public double[] getReducedCosts(final IloLPMatrix matrix, final int start, final int num)
public double[] getReducedCosts(final IloNumVar[] var)
public double[] getReducedCosts(final IloNumVar[] var, final int start, final int num)
'''
pass
def getReducedCost():
'''public double getReducedCost(final IloNumVar ivar)
'''
pass
def getDuals():
'''public double[] getDuals(final IloLPMatrix matrix)
public double[] getDuals(final IloLPMatrix matrix, final int start, final int num)
public double[] getDuals(final IloRange[] rng)
public double[] getDuals(final IloRange[] rng, final int start, final int num)
'''
pass
def getDual():
'''public double getDual(final IloRange rng)
public double getDual(final IloForAllRange v)
'''
pass
def getSlacks():
'''public double[] getSlacks(final IloLPMatrix matrix)
public double[] getSlacks(final IloLPMatrix matrix, final int soln)
public double[] getSlacks(final IloLPMatrix matrix, final int start, final int num)
public double[] getSlacks(final IloLPMatrix matrix, final int start, final int num, final int soln)
public double[] getSlacks(final IloRange[] rng)
public double[] getSlacks(final IloRange[] rng, final int soln)
public double[] getSlacks(final IloRange[] rng, final int start, final int num)
public double[] getSlacks(final IloRange[] rng, final int start, final int num, final int soln)
'''
pass
def getSlack():
'''public double getSlack(final IloRange rng)
public double getSlack(final IloRange rng, final int soln)
public double getSlack(final IloForAllRange range)
'''
pass
def getInfeasibilities():
'''public double[] getInfeasibilities(final IloConstraint[] con, final int start, final int num)
public double[] getInfeasibilities(final IloNumVar[] var)
public double[] getInfeasibilities(final IloNumVar[] var, final int start, final int num)
public double[] getInfeasibilities(final IloConstraint[] con)
public double[] getInfeasibilities(final IloLPMatrix matrix)
public double[] getInfeasibilities(final IloLPMatrix matrix, final int start, final int num)
'''
pass
def getInfeasibility():
'''public double getInfeasibility(final IloConstraint con)
public double getInfeasibility(final IloNumVar ivar)
'''
pass
def getAX():
'''public double[] getAX(final IloLPMatrix matrix)
public double[] getAX(final IloLPMatrix matrix, final int start, final int num)
public double getAX(final IloRange rng)
public double[] getAX(final IloRange[] rng)
public double[] getAX(final IloRange[] rng, final int start, final int num)
public double getAX(final IloForAllRange v)
public double[] getAX(final IloForAllRange[] rngs)
'''
pass
def getBasisStatus():
'''public BasisStatus getBasisStatus(final IloNumVar var)
public BasisStatus getBasisStatus(final IloConstraint con)
'''
pass
def getBasisStatuses():
'''public BasisStatus[] getBasisStatuses(final IloNumVar[] var)
public BasisStatus[] getBasisStatuses(final IloNumVar[] var, final int start, final int num)
public BasisStatus[] getBasisStatuses(final IloConstraint[] con)
public BasisStatus[] getBasisStatuses(final IloConstraint[] con, final int start, final int num)
'''
pass
def setBasisStatuses():
'''public void setBasisStatuses(final IloNumVar[] var, final BasisStatus[] cstat, final IloRange[] con, final BasisStatus[] rstat)
public void setBasisStatuses(final IloNumVar[] var, final BasisStatus[] cstat, final int cstart, final int cnum, final IloConstraint[] con, final BasisStatus[] rstat, final int rstart, final int rnum)
'''
pass
def setStart():
'''public void setStart(final double[] x, final double[] dj, final IloNumVar[] var, final double[] slack, final double[] pi, final IloRange[] rng)
public void setStart(final double[] x, final double[] dj, final IloNumVar[] var, final int vstart, final int vnum, final double[] slack, final double[] pi, final IloRange[] rng, final int rstart, final int rnum)
'''
pass
def feasOpt():
'''public boolean feasOpt(final IloConstraint[] cts, final double[] prefs)
public boolean feasOpt(final IloRange[] rngs, final double[] rnglb, final double[] rngub, final IloNumVar[] vars, final double[] varlb, final double[] varub)
public boolean feasOpt(final IloNumVar[] vars, final double[] varlb, final double[] varub)
public boolean feasOpt(final IloRange[] rngs, final double[] rnglb, final double[] rngub)
public boolean feasOpt(final IloRange[] rngs, final double[] rnglb, final double[] rngub, final IloForAllRange[] farngs, final double[] falb, final double[] faub, final IloNumVar[] vars, final double[] varlb, final double[] varub)
'''
pass
def getBoundSA():
'''public void getBoundSA(final double[] lblower, final double[] lbupper, final double[] ublower, final double[] ubupper, final IloLPMatrix matrix)
public void getBoundSA(final double[] lblower, final double[] lbupper, final double[] ublower, final double[] ubupper, final IloLPMatrix matrix, final int start, final int num)
public void getBoundSA(final double[] lblower, final double[] lbupper, final double[] ublower, final double[] ubupper, final IloNumVar[] var)
public void getBoundSA(final double[] lblower, final double[] lbupper, final double[] ublower, final double[] ubupper, final IloNumVar[] var, final int start, final int num)
'''
pass
def getObjSA():
'''public void getObjSA(final double[] lower, final double[] upper, final IloLPMatrix matrix)
public void getObjSA(final double[] lower, final double[] upper, final IloLPMatrix matrix, final int start, final int num)
public void getObjSA(final double[] lower, final double[] upper, final IloNumVar[] var)
public void getObjSA(final double[] lower, final double[] upper, final IloNumVar[] var, final int start, final int num)
'''
pass
def getRangeSA():
'''public void getRangeSA(final double[] lblower, final double[] lbupper, final double[] ublower, final double[] ubupper, final IloRange[] rng)
public void getRangeSA(final double[] lblower, final double[] lbupper, final double[] ublower, final double[] ubupper, final IloRange[] rng, final int start, final int num)
public void getRangeSA(final double[] lblower, final double[] lbupper, final double[] ublower, final double[] ubupper, final IloLPMatrix matrix, final int start, final int num)
public void getRangeSA(final double[] lblower, final double[] lbupper, final double[] ublower, final double[] ubupper, final IloLPMatrix matrix)
'''
pass
def getRHSSA():
'''public void getRHSSA(final double[] lower, final double[] upper, final IloRange[] rng)
public void getRHSSA(final double[] lower, final double[] upper, final IloRange[] rng, final int start, final int num)
public void getRHSSA(final double[] lower, final double[] upper, final IloLPMatrix matrix)
public void getRHSSA(final double[] lower, final double[] upper, final IloLPMatrix matrix, final int start, final int num)
'''
pass
def getQuality():
'''public Quality getQuality(final QualityType which)
public Quality getQuality(final QualityType which, final int soln)
'''
pass
def IloCplex():
'''public IloCplex()
public IloCplex(final IloEnv env)
public IloCplex(final ilog.cplex.cppimpl.IloCplex cplexImpl)
public IloCplex(final ilog.cplex.cppimpl.IloCplex cplexImpl, final boolean noStreams)
'''
pass
def output():
'''public PrintStream output()
'''
pass
def warning():
'''public PrintStream warning()
'''
pass
def error():
'''public PrintStream error()
'''
pass
def setOut():
'''public void setOut(final OutputStream s)
'''
pass
def setWarning():
'''public void setWarning(final OutputStream s)
'''
pass
def setError():
'''public void setError(final OutputStream s)
'''
pass
def solve():
'''public boolean solve()
public final boolean solve(final Goal goal)
'''
pass
def solveFixed():
'''public boolean solveFixed()
public boolean solveFixed(final int soln)
'''
pass
def solveZeroedQP():
'''public boolean solveZeroedQP()
'''
pass
def getNiterations():
'''public int getNiterations()
'''
pass
def getNiterations64():
'''public long getNiterations64()
'''
pass
def getNphaseOneIterations():
'''public int getNphaseOneIterations()
'''
pass
def getNphaseOneIterations64():
'''public long getNphaseOneIterations64()
'''
pass
def getNbarrierIterations():
'''public int getNbarrierIterations()
'''
pass
def getNbarrierIterations64():
'''public long getNbarrierIterations64()
'''
pass
def getNsiftingIterations():
'''public int getNsiftingIterations()
'''
pass
def getNsiftingIterations64():
'''public long getNsiftingIterations64()
'''
pass
def getNsiftingPhaseOneIterations():
'''public int getNsiftingPhaseOneIterations()
'''
pass
def getNsiftingPhaseOneIterations64():
'''public long getNsiftingPhaseOneIterations64()
'''
pass
def getNcrossDExch():
'''public int getNcrossDExch()
'''
pass
def getNcrossDExch64():
'''public long getNcrossDExch64()
'''
pass
def getNcrossDPush():
'''public int getNcrossDPush()
'''
pass
def getNcrossDPush64():
'''public long getNcrossDPush64()
'''
pass
def getNcrossPExch():
'''public int getNcrossPExch()
'''
pass
def getNcrossPExch64():
'''public long getNcrossPExch64()
'''
pass
def getNcrossPPush():
'''public int getNcrossPPush()
'''
pass
def getNcrossPPush64():
'''public long getNcrossPPush64()
'''
pass
def getNdualSuperbasics():
'''public int getNdualSuperbasics()
'''
pass
def getNprimalSuperbasics():
'''public int getNprimalSuperbasics()
'''
pass
def getNnodes():
'''public int getNnodes()
'''
pass
def getNnodes64():
'''public long getNnodes64()
'''
pass
def getNnodesLeft():
'''public int getNnodesLeft()
'''
pass
def getNnodesLeft64():
'''public long getNnodesLeft64()
'''
pass
def getIncumbentNode():
'''public int getIncumbentNode()
'''
pass
def getIncumbentNode64():
'''public long getIncumbentNode64()
'''
pass
def tuneParam():
'''public int tuneParam()
public int tuneParam(final ParameterSet fixedset)
public int tuneParam(final String[] filenames)
public int tuneParam(final String[] filenames, final ParameterSet fixedset)
'''
pass
def setPriority():
'''public void setPriority(final IloNumVar var, final int pri)
'''
pass
def setPriorities():
'''public void setPriorities(final IloNumVar[] var, final int[] pri)
public void setPriorities(final IloNumVar[] var, final int[] pri, final int start, final int num)
'''
pass
def setDirection():
'''public void setDirection(final IloNumVar var, final BranchDirection dir)
'''
pass
def setDirections():
'''public void setDirections(final IloNumVar[] var, final BranchDirection[] brdir)
public void setDirections(final IloNumVar[] var, final BranchDirection[] brdir, final int start, final int num)
'''
pass
def delPriority():
'''public void delPriority(final IloNumVar var)
'''
pass
def delPriorities():
'''public void delPriorities(final IloNumVar[] var)
public void delPriorities(final IloNumVar[] var, final int start, final int num)
'''
pass
def delDirection():
'''public void delDirection(final IloNumVar var)
'''
pass
def delDirections():
'''public void delDirections(final IloNumVar[] var)
public void delDirections(final IloNumVar[] var, final int start, final int num)
'''
pass
def getPriority():
'''public int getPriority(final IloNumVar var)
'''
pass
def getPriorities():
'''public int[] getPriorities(final IloNumVar[] var)
public int[] getPriorities(final IloNumVar[] var, final int start, final int num)
'''
pass
def getDirection():
'''public BranchDirection getDirection(final IloNumVar var)
'''
pass
def getDirections():
'''public BranchDirection[] getDirections(final IloNumVar[] var)
public BranchDirection[] getDirections(final IloNumVar[] var, final int start, final int num)
'''
pass
def writeOrder():
'''public void writeOrder(final String name)
'''
pass
def writeConflict():
'''public void writeConflict(final String name)
'''
pass
def writeParam():
'''public void writeParam(final String name)
'''
pass
def writeBasis():
'''public void writeBasis(final String name)
'''
pass
def writeSolution():
'''public void writeSolution(final String name)
public void writeSolution(final String name, final int soln)
'''
pass
def writeSolutions():
'''public void writeSolutions(final String name)
'''
pass
def writeMIPStarts():
'''public void writeMIPStarts(final String name)
'''
pass
def getCplexTime():
'''public double getCplexTime()
'''
pass
def getDetTime():
'''public double getDetTime()
'''
pass
def readOrder():
'''public void readOrder(final String name)
'''
pass
def readParam():
'''public void readParam(final String name)
'''
pass
def readBasis():
'''public void readBasis(final String name)
'''
pass
def readSolution():
'''public void readSolution(final String name)
'''
pass
def readMIPStarts():
'''public void readMIPStarts(final String name)
'''
pass
def add():
'''public void add(final Callback cb)
'''
pass
def clearCallbacks():
'''public void clearCallbacks()
'''
pass
def addMIPStart():
'''public int addMIPStart(final IloNumVar[] vars, final double[] values, final int vstart, final int vnum, final MIPStartEffort effort, final String name)
public int addMIPStart(final IloNumVar[] vars, final double[] values, final MIPStartEffort effort, final String name)
public int addMIPStart(final MIPStartEffort effort, final String name)
public int addMIPStart(final IloNumVar[] vars, final double[] values, final MIPStartEffort effort)
public int addMIPStart(final IloNumVar[] vars, final double[] values)
public int addMIPStart(final IloNumVar[] vars, final double[] values, final String name)
public int addMIPStart(final MIPStartEffort effort)
public int addMIPStart(final String name)
public int addMIPStart()
'''
pass
def changeMIPStart():
'''public void changeMIPStart(final int mipstartindex, final IloNumVar[] vars, final double[] values, final int vstart, final int vnum, final MIPStartEffort effort)
public void changeMIPStart(final int mipstartindex, final IloNumVar[] vars, final double[] values, final MIPStartEffort effort)
public void changeMIPStart(final int mipstartindex, final MIPStartEffort effort)
public void changeMIPStart(final int mipstartindex, final IloNumVar[] vars, final double[] values)
'''
pass
def deleteMIPStarts():
'''public void deleteMIPStarts(final int first, final int num)
public void deleteMIPStarts(final int first)
'''
pass
def getNMIPStarts():
'''public int getNMIPStarts()
'''
pass
def getMIPStartName():
'''public String getMIPStartName(final int mipstartindex)
'''
pass
def getMIPStartIndex():
'''public int getMIPStartIndex(final String name)
'''
pass
def getMIPStart():
'''public MIPStartEffort getMIPStart(final int mipstartindex, final IloNumVar[] vars, final int begin, final int num, final double[] values, final boolean[] isset)
public MIPStartEffort getMIPStart(final int mipstartindex, final IloNumVar[] vars, final double[] values, final boolean[] isset)
public MIPStartEffort getMIPStart(final int mipstartindex, final IloNumVar[] vars, final int begin, final int num, final double[] values)
public MIPStartEffort getMIPStart(final int mipstartindex, final IloNumVar[] vars, final double[] values)
public MIPStartEffort getMIPStart(final int mipstartindex)
'''
pass
def getRay():
'''public IloLinearNumExpr getRay()
public void getRay(final ilog.concert.IloNumArray vals, final ilog.concert.IloNumVarArray vars)
'''
pass
def getDiverging():
'''public IloCopyable getDiverging()
'''
pass
def dualFarkas():
'''public double dualFarkas(final IloConstraint[] rng, final double[] y)
'''
pass
def qpIndefCertificate():
'''public void qpIndefCertificate(final IloNumVar[] var, final double[] x)
'''
pass
def end():
'''public void end()
public void end()
'''
pass
def and():
'''public final Goal and(final Goal goal1, final Goal goal2)
public final Goal and(final Goal goal1, final Goal goal2, final Goal goal3)
public final Goal and(final Goal goal1, final Goal goal2, final Goal goal3, final Goal goal4)
public final Goal and(final Goal goal1, final Goal goal2, final Goal goal3, final Goal goal4, final Goal goal5)
public final Goal and(final Goal goal1, final Goal goal2, final Goal goal3, final Goal goal4, final Goal goal5, final Goal goal6)
public IloConstraint and(final IloRange[] cts)
'''
pass
def or():
'''public final Goal or(final Goal goal1, final Goal goal2)
public final Goal or(final Goal goal1, final Goal goal2, final Goal goal3)
public final Goal or(final Goal goal1, final Goal goal2, final Goal goal3, final Goal goal4)
public final Goal or(final Goal goal1, final Goal goal2, final Goal goal3, final Goal goal4, final Goal goal5)
public final Goal or(final Goal goal1, final Goal goal2, final Goal goal3, final Goal goal4, final Goal goal5, final Goal goal6)
'''
pass
def branchAsCplex():
'''public final Goal branchAsCplex()
'''
pass
def apply():
'''public final Goal apply(final Goal goal, final NodeEvaluator evaluator)
'''
pass
def limitSearch():
'''public final Goal limitSearch(final Goal goal, final SearchLimit limit)
'''
pass
def failGoal():
'''public final Goal failGoal()
'''
pass
def constraintGoal():
'''public final Goal constraintGoal(final IloConstraint ct)
public final Goal constraintGoal(final IloConstraint[] cut)
'''
pass
def globalCutGoal():
'''public final Goal globalCutGoal(final IloConstraint cut)
public final Goal globalCutGoal(final IloConstraint[] cut)
'''
pass
def solutionGoal():
'''public final Goal solutionGoal(final IloNumVar[] vars, final double[] vals)
'''
pass
def eqGoal():
'''public Goal eqGoal(final IloNumExpr expr, final double rhs)
public Goal eqGoal(final IloNumExpr expr1, final IloNumExpr expr2)
public Goal eqGoal(final double lhs, final IloNumExpr expr)
'''
pass
def geGoal():
'''public Goal geGoal(final IloNumExpr expr, final double rhs)
public Goal geGoal(final IloNumExpr expr1, final IloNumExpr expr2)
public Goal geGoal(final double lhs, final IloNumExpr expr)
'''
pass
def leGoal():
'''public Goal leGoal(final IloNumExpr expr, final double rhs)
public Goal leGoal(final IloNumExpr expr1, final IloNumExpr expr2)
public Goal leGoal(final double lhs, final IloNumExpr expr)
'''
pass
def getEnvImpl():
'''public IloEnv getEnvImpl()
'''
pass
def ToWrParameterSet():
'''public static ParameterSet ToWrParameterSet(final IloCplex__ParameterSet vi)
'''
pass
def ToCppParameterSet():
'''public static IloCplex__ParameterSet ToCppParameterSet(final ParameterSet vi)
'''
pass
def getLB():
'''public double getLB(final IloForAllRange v)
'''
pass
def getUB():
'''public double getUB(final IloForAllRange v)
'''
pass
def lowerBound():
'''public IloNumVarBound lowerBound(final IloNumVar var)
'''
pass
def upperBound():
'''public IloNumVarBound upperBound(final IloNumVar var)
'''
pass
def refineConflict():
'''public boolean refineConflict(final IloConstraint[] cons, final double[] prefs)
public boolean refineConflict(final IloConstraint[] cts, final double[] prefs, final int start, final int num)
'''
pass
def getConflict():
'''public ConflictStatus[] getConflict(final IloConstraint[] cts)
public ConflictStatus getConflict(final IloConstraint ct)
public ConflictStatus[] getConflict(final IloConstraint[] cts, final int start, final int num)
'''
pass
def getForAllRanges():
'''public IloForAllRange[] getForAllRanges(final IloConstraint forAllCt)
'''
pass
def registerLicense():
'''public static void registerLicense(final String ilm_CPLEX_license, final int ilm_CPLEX_license_signature)
'''
pass
def parameterSet():
'''public ParameterSet parameterSet()
'''
pass
def getParameterSet():
'''public ParameterSet getParameterSet()
'''
pass
def setParameterSet():
'''public void setParameterSet(final ParameterSet set)
'''
pass
def populate():
'''public boolean populate()
'''
pass
def getSolnPoolMeanObjValue():
'''public double getSolnPoolMeanObjValue()
'''
pass
def getSolnPoolNsolns():
'''public int getSolnPoolNsolns()
'''
pass
def getSolnPoolNreplaced():
'''public int getSolnPoolNreplaced()
'''
pass
def delSolnPoolSoln():
'''public void delSolnPoolSoln(final int which)
'''
pass
def delSolnPoolSolns():
'''public void delSolnPoolSolns(final int begin, final int end)
'''
pass
def next():
'''public Object next()
public Object next()
'''
pass
def hasNext():
'''public boolean hasNext()
public boolean hasNext()
'''
pass
def FilterIterator():
'''public FilterIterator(final Iterator it)
'''
pass
def isIncluded():
'''public boolean isIncluded(final Object obj)
public boolean isIncluded(final Object obj)
public boolean isIncluded(final Object obj)
public boolean isIncluded(final Object obj)
'''
pass
def toString():
'''public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
public String toString()
'''
pass
def Aborter():
'''public Aborter()
'''
pass
def abort():
'''public void abort()
'''
pass
def isAborted():
'''public boolean isAborted()
'''
pass
def clear():
'''public void clear()
public void clear()
'''
pass
def alsoLong():
'''public boolean alsoLong()
'''
pass
def IntParameter():
'''public IntParameter(final IntParam key, final int value)
'''
pass
def getType():
'''public int getType()
public int getType()
public int getType()
public int getType()
public int getType()
'''
pass
def getKey():
'''public IntParam getKey()
public LongParam getKey()
public DoubleParam getKey()
public BooleanParam getKey()
public StringParam getKey()
'''
pass
def LongParameter():
'''public LongParameter(final LongParam key, final long value)
'''
pass
def DoubleParameter():
'''public DoubleParameter(final DoubleParam key, final double value)
'''
pass
def BooleanParameter():
'''public BooleanParameter(final BooleanParam key, final boolean value)
'''
pass
def StringParameter():
'''public StringParameter(final StringParam key, final String value)
'''
pass
def equals():
'''public boolean equals(final Object obj)
public boolean equals(final Object obj)
public boolean equals(final Object obj)
public boolean equals(final Object obj)
public boolean equals(final Object obj)
public boolean equals(final Object obj)
public boolean equals(final Object obj)
'''
pass
def getNumVar():
'''public IloNumVar getNumVar()
'''
pass
def getConstraint():
'''public IloConstraint getConstraint()
'''
pass
def getQualityType():
'''public QualityType getQualityType()
'''
pass
def close():
'''public void close()
'''
pass
def flush():
'''public void flush()
'''
pass
def write():
'''public void write(final int b)
public void write(final byte[] b)
public void write(final byte[] b, final int off, final int len)
'''
pass
def getCppImpl():
'''public IloCplex__Callback getCppImpl(final IloCplex cplex)
'''
pass
def callbackImpl():
'''public void callbackImpl()
public void callbackImpl()
public void callbackImpl()
public void callbackImpl()
public void callbackImpl()
public void callbackImpl()
public void callbackImpl()
public void callbackImpl()
public void callbackImpl()
public void callbackImpl()
public void callbackImpl()
public void callbackImpl()
public void callbackImpl()
public void callbackImpl()
public void callbackImpl()
public void callbackImpl()
public void callbackImpl()
public void callbackImpl()
public void callbackImpl()
public void callbackImpl()
public void callbackImpl()
public void callbackImpl()
public void callbackImpl()
'''
pass
def IloMyNodeData():
'''public IloMyNodeData(final Object data)
'''
pass
def getObject():
'''public Object getObject()
public Object getObject()
'''
pass
def UnknownObjectException():
'''public UnknownObjectException(final Object obj)
'''
pass
def clone():
'''public Object clone()
'''
pass
def evaluate():
'''public double evaluate()
'''
pass
def init():
'''public void init()
public void init()
'''
pass
def subsume():
'''public boolean subsume(final double evalNode, final double evalCurrent)
'''
pass
def duplicateEvaluator():
'''public IloCplex__NodeEvaluatorI duplicateEvaluator()
'''
pass
def getDepth():
'''public final int getDepth()
'''
pass
def getLeftDepth():
'''public final int getLeftDepth()
'''
pass
def getRightDepth():
'''public final int getRightDepth()
'''
pass
def duplicateGoal():
'''public IloCplex__Goal duplicateGoal()
'''
pass
def execute():
'''public IloCplex__Goal execute()
public Goal execute(final IloCplex cplex)
'''
pass
