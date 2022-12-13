def IloCplex__GoalI():
'''public IloCplex__GoalI(final long cPtr, final boolean cMemoryOwn)
'''
pass
def getCPtr():
'''public static long getCPtr(final IloCplex__GoalI obj)
'''
pass
def delete():
'''public void delete()
'''
pass
def getEnv():
'''public IloEnv getEnv()
'''
pass
def execute():
'''public IloCplex__Goal execute()
'''
pass
def duplicateGoal():
'''public IloCplex__Goal duplicateGoal()
'''
pass
def abort():
'''public void abort()
'''
pass
def getModel():
'''public IloModel getModel()
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
def getBestObjValue():
'''public double getBestObjValue()
'''
pass
def getMIPRelativeGap():
'''public double getMIPRelativeGap()
'''
pass
def getCutoff():
'''public double getCutoff()
'''
pass
def getDirection():
'''public SWIGTYPE_p_IloCplex__BranchDirection getDirection(final IloNumVar var)
public SWIGTYPE_p_IloCplex__BranchDirection getDirection(final IloIntVar var)
'''
pass
def getIncumbentObjValue():
'''public double getIncumbentObjValue()
'''
pass
def getIncumbentValue():
'''public double getIncumbentValue(final IloNumVar var)
public double getIncumbentValue(final IloIntVar var)
public double getIncumbentValue(final SWIGTYPE_p_IloExprArg expr)
'''
pass
def getIncumbentValues():
'''public void getIncumbentValues(final IloNumArray val, final IloNumVarArray vars)
public void getIncumbentValues(final IloNumArray val, final IloIntVarArray vars)
'''
pass
def getMyThreadNum():
'''public int getMyThreadNum()
'''
pass
def getUserThreads():
'''public int getUserThreads()
'''
pass
def getNcuts():
'''public int getNcuts(final SWIGTYPE_p_IloCplex__CutType which)
'''
pass
def getNiterations64():
'''public long getNiterations64()
'''
pass
def getNiterations():
'''public int getNiterations()
'''
pass
def getNnodes64():
'''public long getNnodes64()
'''
pass
def getNnodes():
'''public int getNnodes()
'''
pass
def getNremainingNodes64():
'''public long getNremainingNodes64()
'''
pass
def getNremainingNodes():
'''public int getNremainingNodes()
'''
pass
def getPriority():
'''public double getPriority(final IloNumVar var)
public double getPriority(final IloIntVar var)
'''
pass
def isIntegerFeasible():
'''public boolean isIntegerFeasible()
'''
pass
def hasIncumbent():
'''public boolean hasIncumbent()
'''
pass
def getBranch():
'''public double getBranch(final IloNumVarArray vars, final IloNumArray bounds, final IloCplex__BranchDirectionArray dirs, final int i)
'''
pass
def getBranchType():
'''public BranchType getBranchType()
'''
pass
def getNbranches():
'''public int getNbranches()
'''
pass
def getDownPseudoCost():
'''public double getDownPseudoCost(final IloNumVar var)
public double getDownPseudoCost(final IloIntVar var)
'''
pass
def getFeasibility():
'''public IntegerFeasibility getFeasibility(final IloNumVar var)
public IntegerFeasibility getFeasibility(final IloIntVar var)
public IntegerFeasibility getFeasibility(final IloSOS1 sos)
public IntegerFeasibility getFeasibility(final IloSOS2 sos)
'''
pass
def getFeasibilities():
'''public void getFeasibilities(final IloCplex__GoalI__IntegerFeasibilityArray stats, final IloNumVarArray vars)
public void getFeasibilities(final IloCplex__GoalI__IntegerFeasibilityArray stats, final IloIntVarArray vars)
'''
pass
def getLB():
'''public double getLB(final IloNumVar var)
public double getLB(final IloIntVar var)
'''
pass
def getLBs():
'''public void getLBs(final IloNumArray vals, final IloNumVarArray vars)
public void getLBs(final IloNumArray vals, final IloIntVarArray vars)
'''
pass
def getObjCoef():
'''public double getObjCoef(final IloNumVar var)
public double getObjCoef(final IloIntVar var)
'''
pass
def getObjCoefs():
'''public void getObjCoefs(final IloNumArray vals, final IloNumVarArray vars)
public void getObjCoefs(final IloNumArray vals, final IloIntVarArray vars)
'''
pass
def getObjValue():
'''public double getObjValue()
'''
pass
def getSlack():
'''public double getSlack(final IloRange rng)
'''
pass
def getSlacks():
'''public void getSlacks(final IloNumArray vals, final IloRangeArray rngs)
'''
pass
def getUB():
'''public double getUB(final IloNumVar var)
public double getUB(final IloIntVar var)
'''
pass
def getUBs():
'''public void getUBs(final IloNumArray vals, final IloNumVarArray vars)
public void getUBs(final IloNumArray vals, final IloIntVarArray vars)
'''
pass
def getUpPseudoCost():
'''public double getUpPseudoCost(final IloNumVar var)
public double getUpPseudoCost(final IloIntVar var)
'''
pass
def getValue():
'''public double getValue(final SWIGTYPE_p_IloExprArg expr)
public double getValue(final IloNumVar var)
public double getValue(final IloIntVar var)
public double getValue(final IloNumExpr expr)
'''
pass
def getValues():
'''public void getValues(final IloNumArray vals, final IloNumVarArray vars)
public void getValues(final IloNumArray vals, final IloIntVarArray vars)
'''
pass
def isSOSFeasible():
'''public boolean isSOSFeasible(final IloSOS1 sos1)
public boolean isSOSFeasible(final IloSOS2 sos2)
'''
pass
def BranchAsCplexGoal():
'''public static IloCplex__Goal BranchAsCplexGoal(final IloEnv env)
'''
pass
def OrGoal():
'''public static IloCplex__Goal OrGoal(final IloCplex__Goal goal1, final IloCplex__Goal goal2)
'''
pass
def AndGoal():
'''public static IloCplex__Goal AndGoal(final IloCplex__Goal goal1, final IloCplex__Goal goal2)
'''
pass
def FailGoal():
'''public static IloCplex__Goal FailGoal(final IloEnv env)
'''
pass
def GlobalCutGoal():
'''public static IloCplex__Goal GlobalCutGoal(final IloConstraint con)
public static IloCplex__Goal GlobalCutGoal(final IloConstraintArray con)
'''
pass
def SolutionGoal():
'''public static IloCplex__Goal SolutionGoal(final IloNumVarArray vars, final IloNumArray vals)
'''
pass
def mySwigValue():
'''public int mySwigValue()
public int mySwigValue()
'''
pass
def swigValue():
'''public final int swigValue()
public final int swigValue()
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def swigToEnum():
'''public static IntegerFeasibility swigToEnum(final int swigValue)
public static BranchType swigToEnum(final int swigValue)
'''
pass
def IntegerFeasibility():
'''public IntegerFeasibility(final String swigName, final int swigValue)
'''
pass
def BranchType():
'''public BranchType(final String swigName, final int swigValue)
'''
pass
