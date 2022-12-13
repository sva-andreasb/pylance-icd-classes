def ControlCallbackWrapper():
'''public ControlCallbackWrapper(final long cPtr, final boolean cMemoryOwn)
public ControlCallbackWrapper(final IloEnv env)
'''
pass
def getCPtr():
'''public static long getCPtr(final ControlCallbackWrapper obj)
'''
pass
def delete():
'''public void delete()
'''
pass
def main_cpp():
'''public void main_cpp()
'''
pass
def duplicateCallback():
'''public IloCplex__CallbackI duplicateCallback()
'''
pass
def callbackImpl():
'''public void callbackImpl()
'''
pass
def abort():
'''public void abort()
'''
pass
def getEnv():
'''public IloEnv getEnv()
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
def getNQCs():
'''public int getNQCs()
'''
pass
def getBestObjValue():
'''public double getBestObjValue()
'''
pass
def getIncumbentObjValue():
'''public double getIncumbentObjValue()
'''
pass
def getIncumbentValue():
'''public double getIncumbentValue(final IloNumVar var)
public double getIncumbentValue(final IloIntVar var)
public double getIncumbentValue(final IloNumExprArg ex)
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
def hasIncumbent():
'''public boolean hasIncumbent()
'''
pass
def getNnodes():
'''public int getNnodes()
'''
pass
def getNremainingNodes():
'''public int getNremainingNodes()
'''
pass
def getNiterations():
'''public int getNiterations()
'''
pass
def getCutoff():
'''public double getCutoff()
'''
pass
def getPriority():
'''public double getPriority(final IloNumVar sos)
public double getPriority(final IloIntVar sos)
'''
pass
def getUserThreads():
'''public int getUserThreads()
'''
pass
def getObjCoef():
'''public double getObjCoef(final IloNumVar var)
public double getObjCoef(final IloIntVar var)
'''
pass
def getObjCoefs():
'''public void getObjCoefs(final IloNumArray val, final IloNumVarArray vars)
public void getObjCoefs(final IloNumArray val, final IloIntVarArray vars)
'''
pass
def getFeasibility():
'''public IntegerFeasibility getFeasibility(final IloSOS1 sos)
public IntegerFeasibility getFeasibility(final IloSOS2 sos)
public IntegerFeasibility getFeasibility(final IloNumVar var)
public IntegerFeasibility getFeasibility(final IloIntVar var)
'''
pass
def getFeasibilities():
'''public void getFeasibilities(final IloCplex__ControlCallbackI__IntegerFeasibilityArray stat, final IloNumVarArray var)
public void getFeasibilities(final IloCplex__ControlCallbackI__IntegerFeasibilityArray stat, final IloIntVarArray var)
'''
pass
def isSOSFeasible():
'''public boolean isSOSFeasible(final IloSOS1 sos1)
public boolean isSOSFeasible(final IloSOS2 sos2)
'''
pass
def getLB():
'''public double getLB(final IloNumVar var)
public double getLB(final IloIntVar var)
'''
pass
def getUB():
'''public double getUB(final IloNumVar var)
public double getUB(final IloIntVar var)
'''
pass
def getLBs():
'''public void getLBs(final IloNumArray val, final IloNumVarArray vars)
public void getLBs(final IloNumArray val, final IloIntVarArray vars)
'''
pass
def getUBs():
'''public void getUBs(final IloNumArray val, final IloNumVarArray vars)
public void getUBs(final IloNumArray val, final IloIntVarArray vars)
'''
pass
def getObjValue():
'''public double getObjValue()
'''
pass
def getValue():
'''public double getValue(final IloNumExprArg expr)
public double getValue(final IloNumVar var)
public double getValue(final IloIntVar var)
'''
pass
def getSlack():
'''public double getSlack(final IloRange rng)
'''
pass
def getValues():
'''public void getValues(final IloNumArray val, final IloNumVarArray vars)
public void getValues(final IloNumArray val, final IloIntVarArray vars)
'''
pass
def getSlacks():
'''public void getSlacks(final IloNumArray val, final IloRangeArray con)
'''
pass
def getDownPseudoCost():
'''public double getDownPseudoCost(final IloNumVar var)
public double getDownPseudoCost(final IloIntVar var)
'''
pass
def getUpPseudoCost():
'''public double getUpPseudoCost(final IloNumVar var)
public double getUpPseudoCost(final IloIntVar var)
'''
pass
def getNodeData():
'''public SWIGTYPE_p_NodeData getNodeData()
'''
pass
def setNodeData():
'''public SWIGTYPE_p_NodeData setNodeData(final SWIGTYPE_p_NodeData data)
'''
pass
