def IloCplex__GoalI():
    '''public IloCplex__GoalI(final long cPtr, final boolean cMemoryOwn)
    '''
def getCPtr():
    '''public static long getCPtr(final IloCplex__GoalI obj)
    '''
def delete():
    '''public void delete()
    '''
def getEnv():
    '''public IloEnv getEnv()
    '''
def execute():
    '''public IloCplex__Goal execute()
    '''
def duplicateGoal():
    '''public IloCplex__Goal duplicateGoal()
    '''
def abort():
    '''public void abort()
    '''
def getModel():
    '''public IloModel getModel()
    '''
def getNcols():
    '''public int getNcols()
    '''
def getNrows():
    '''public int getNrows()
    '''
def getBestObjValue():
    '''public double getBestObjValue()
    '''
def getMIPRelativeGap():
    '''public double getMIPRelativeGap()
    '''
def getCutoff():
    '''public double getCutoff()
    '''
def getDirection():
    '''public SWIGTYPE_p_IloCplex__BranchDirection getDirection(final IloNumVar var)
    public SWIGTYPE_p_IloCplex__BranchDirection getDirection(final IloIntVar var)
    '''
def getIncumbentObjValue():
    '''public double getIncumbentObjValue()
    '''
def getIncumbentValue():
    '''public double getIncumbentValue(final IloNumVar var)
    public double getIncumbentValue(final IloIntVar var)
    public double getIncumbentValue(final SWIGTYPE_p_IloExprArg expr)
    '''
def getIncumbentValues():
    '''public void getIncumbentValues(final IloNumArray val, final IloNumVarArray vars)
    public void getIncumbentValues(final IloNumArray val, final IloIntVarArray vars)
    '''
def getMyThreadNum():
    '''public int getMyThreadNum()
    '''
def getUserThreads():
    '''public int getUserThreads()
    '''
def getNcuts():
    '''public int getNcuts(final SWIGTYPE_p_IloCplex__CutType which)
    '''
def getNiterations64():
    '''public long getNiterations64()
    '''
def getNiterations():
    '''public int getNiterations()
    '''
def getNnodes64():
    '''public long getNnodes64()
    '''
def getNnodes():
    '''public int getNnodes()
    '''
def getNremainingNodes64():
    '''public long getNremainingNodes64()
    '''
def getNremainingNodes():
    '''public int getNremainingNodes()
    '''
def getPriority():
    '''public double getPriority(final IloNumVar var)
    public double getPriority(final IloIntVar var)
    '''
def isIntegerFeasible():
    '''public boolean isIntegerFeasible()
    '''
def hasIncumbent():
    '''public boolean hasIncumbent()
    '''
def getBranch():
    '''public double getBranch(final IloNumVarArray vars, final IloNumArray bounds, final IloCplex__BranchDirectionArray dirs, final int i)
    '''
def getBranchType():
    '''public BranchType getBranchType()
    '''
def getNbranches():
    '''public int getNbranches()
    '''
def getDownPseudoCost():
    '''public double getDownPseudoCost(final IloNumVar var)
    public double getDownPseudoCost(final IloIntVar var)
    '''
def getFeasibility():
    '''public IntegerFeasibility getFeasibility(final IloNumVar var)
    public IntegerFeasibility getFeasibility(final IloIntVar var)
    public IntegerFeasibility getFeasibility(final IloSOS1 sos)
    public IntegerFeasibility getFeasibility(final IloSOS2 sos)
    '''
def getFeasibilities():
    '''public void getFeasibilities(final IloCplex__GoalI__IntegerFeasibilityArray stats, final IloNumVarArray vars)
    public void getFeasibilities(final IloCplex__GoalI__IntegerFeasibilityArray stats, final IloIntVarArray vars)
    '''
def getLB():
    '''public double getLB(final IloNumVar var)
    public double getLB(final IloIntVar var)
    '''
def getLBs():
    '''public void getLBs(final IloNumArray vals, final IloNumVarArray vars)
    public void getLBs(final IloNumArray vals, final IloIntVarArray vars)
    '''
def getObjCoef():
    '''public double getObjCoef(final IloNumVar var)
    public double getObjCoef(final IloIntVar var)
    '''
def getObjCoefs():
    '''public void getObjCoefs(final IloNumArray vals, final IloNumVarArray vars)
    public void getObjCoefs(final IloNumArray vals, final IloIntVarArray vars)
    '''
def getObjValue():
    '''public double getObjValue()
    '''
def getSlack():
    '''public double getSlack(final IloRange rng)
    '''
def getSlacks():
    '''public void getSlacks(final IloNumArray vals, final IloRangeArray rngs)
    '''
def getUB():
    '''public double getUB(final IloNumVar var)
    public double getUB(final IloIntVar var)
    '''
def getUBs():
    '''public void getUBs(final IloNumArray vals, final IloNumVarArray vars)
    public void getUBs(final IloNumArray vals, final IloIntVarArray vars)
    '''
def getUpPseudoCost():
    '''public double getUpPseudoCost(final IloNumVar var)
    public double getUpPseudoCost(final IloIntVar var)
    '''
def getValue():
    '''public double getValue(final SWIGTYPE_p_IloExprArg expr)
    public double getValue(final IloNumVar var)
    public double getValue(final IloIntVar var)
    public double getValue(final IloNumExpr expr)
    '''
def getValues():
    '''public void getValues(final IloNumArray vals, final IloNumVarArray vars)
    public void getValues(final IloNumArray vals, final IloIntVarArray vars)
    '''
def isSOSFeasible():
    '''public boolean isSOSFeasible(final IloSOS1 sos1)
    public boolean isSOSFeasible(final IloSOS2 sos2)
    '''
def BranchAsCplexGoal():
    '''public static IloCplex__Goal BranchAsCplexGoal(final IloEnv env)
    '''
def OrGoal():
    '''public static IloCplex__Goal OrGoal(final IloCplex__Goal goal1, final IloCplex__Goal goal2)
    '''
def AndGoal():
    '''public static IloCplex__Goal AndGoal(final IloCplex__Goal goal1, final IloCplex__Goal goal2)
    '''
def FailGoal():
    '''public static IloCplex__Goal FailGoal(final IloEnv env)
    '''
def GlobalCutGoal():
    '''public static IloCplex__Goal GlobalCutGoal(final IloConstraint con)
    public static IloCplex__Goal GlobalCutGoal(final IloConstraintArray con)
    '''
def SolutionGoal():
    '''public static IloCplex__Goal SolutionGoal(final IloNumVarArray vars, final IloNumArray vals)
    '''
def mySwigValue():
    '''public int mySwigValue()
    public int mySwigValue()
    '''
def swigValue():
    '''public final int swigValue()
    public final int swigValue()
    '''
def toString():
    '''public String toString()
    public String toString()
    '''
def swigToEnum():
    '''public static IntegerFeasibility swigToEnum(final int swigValue)
    public static BranchType swigToEnum(final int swigValue)
    '''
def IntegerFeasibility():
    '''public IntegerFeasibility(final String swigName, final int swigValue)
    '''
def BranchType():
    '''public BranchType(final String swigName, final int swigValue)
    '''
