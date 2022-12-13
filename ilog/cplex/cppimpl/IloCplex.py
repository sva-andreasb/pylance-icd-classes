def IloCplex():
'''public IloCplex(final long cPtr, final boolean cMemoryOwn)
public IloCplex(final IloEnv env)
public IloCplex(final IloModel model)
'''
pass
def getCPtr():
'''public static long getCPtr(final IloCplex obj)
'''
pass
def delete():
'''public void delete()
'''
pass
def getIncumbentId():
'''public static int getIncumbentId()
'''
pass
def setBendersAnnotation():
'''public static void setBendersAnnotation(final String value)
'''
pass
def getBendersAnnotation():
'''public static String getBendersAnnotation()
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
def clearModel():
'''public void clearModel()
'''
pass
def deleteNames():
'''public void deleteNames()
'''
pass
def addUserCut():
'''public IloConstraint addUserCut(final IloConstraint con)
'''
pass
def addUserCuts():
'''public IloConstraintArray addUserCuts(final IloConstraintArray con)
'''
pass
def clearUserCuts():
'''public void clearUserCuts()
'''
pass
def addCut():
'''public IloConstraint addCut(final IloConstraint con)
'''
pass
def addCuts():
'''public IloConstraintArray addCuts(final IloConstraintArray con)
'''
pass
def clearCuts():
'''public void clearCuts()
'''
pass
def addLazyConstraint():
'''public IloConstraint addLazyConstraint(final IloConstraint con)
'''
pass
def addLazyConstraints():
'''public IloConstraintArray addLazyConstraints(final IloConstraintArray con)
'''
pass
def clearLazyConstraints():
'''public void clearLazyConstraints()
'''
pass
def importModel():
'''public void importModel(final IloModel model, final String filename, final IloObjective obj, final IloNumVarArray vars, final IloRangeArray rngs, final IloSOS1Array sos1, final IloSOS2Array sos2, final IloRangeArray lazy, final IloRangeArray cuts)
public void importModel(final IloModel model, final String filename, final IloObjective obj, final IloNumVarArray vars, final IloRangeArray rngs, final IloSOS1Array sos1, final IloSOS2Array sos2, final IloRangeArray lazy)
public void importModel(final IloModel model, final String filename, final IloObjective obj, final IloNumVarArray vars, final IloRangeArray rngs, final IloSOS1Array sos1, final IloSOS2Array sos2)
public void importModel(final IloModel m, final String filename, final IloObjective obj, final IloNumVarArray vars, final IloRangeArray rngs, final IloRangeArray lazy, final IloRangeArray cuts)
public void importModel(final IloModel m, final String filename, final IloObjective obj, final IloNumVarArray vars, final IloRangeArray rngs, final IloRangeArray lazy)
public void importModel(final IloModel m, final String filename, final IloObjective obj, final IloNumVarArray vars, final IloRangeArray rngs)
public void importModel(final IloModel m, final String filename)
'''
pass
def exportModel():
'''public void exportModel(final String filename)
'''
pass
def writeOrder():
'''public void writeOrder(final String filename)
'''
pass
def writeConflict():
'''public void writeConflict(final String filename)
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
'''public void writeSolution(final String name, final int soln)
public void writeSolution(final String name)
'''
pass
def writeSolutions():
'''public void writeSolutions(final String name)
'''
pass
def writeMIPStarts():
'''public void writeMIPStarts(final String name, final int first, final int num)
public void writeMIPStarts(final String name, final int first)
public void writeMIPStarts(final String name)
'''
pass
def readOrder():
'''public void readOrder(final String filename)
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
def writeBendersAnnotation():
'''public void writeBendersAnnotation(final String name)
'''
pass
def readAnnotations():
'''public void readAnnotations(final String name)
'''
pass
def writeAnnotations():
'''public void writeAnnotations(final String name)
'''
pass
def numLongAnnotations():
'''public int numLongAnnotations()
'''
pass
def delAnnotation():
'''public void delAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation anno)
public void delAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation anno)
'''
pass
def getName():
'''public String getName(final SWIGTYPE_p_IloCplex__LongAnnotation annotation)
public String getName(final SWIGTYPE_p_IloCplex__NumAnnotation annotation)
'''
pass
def newLongAnnotation():
'''public SWIGTYPE_p_IloCplex__LongAnnotation newLongAnnotation(final String name, final long defval)
public SWIGTYPE_p_IloCplex__LongAnnotation newLongAnnotation(final String name)
'''
pass
def findLongAnnotation():
'''public SWIGTYPE_p_IloCplex__LongAnnotation findLongAnnotation(final String name)
public SWIGTYPE_p_IloCplex__LongAnnotation findLongAnnotation(final int num)
'''
pass
def hasLongAnnotation():
'''public boolean hasLongAnnotation(final String name)
'''
pass
def getDefaultValue():
'''public long getDefaultValue(final SWIGTYPE_p_IloCplex__LongAnnotation annotation)
public double getDefaultValue(final SWIGTYPE_p_IloCplex__NumAnnotation annotation)
'''
pass
def getAnnotation():
'''public long getAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloNumVar var)
public long getAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloIntVar var)
public long getAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloObjective obj)
public long getAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloConstraint ctr)
public void getAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloNumVarArray var, final IloIntArrayBase value)
public void getAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloIntVarArray var, final IloIntArrayBase value)
public void getAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloConstraintArray ctr, final IloIntArrayBase value)
public double getAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloNumVar var)
public double getAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloIntVar var)
public double getAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloObjective obj)
public double getAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloConstraint ctr)
public void getAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloNumVarArray var, final IloNumArray value)
public void getAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloIntVarArray var, final IloNumArray value)
public void getAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloConstraintArray ctr, final IloNumArray value)
'''
pass
def setAnnotation():
'''public void setAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloNumVar var, final long value)
public void setAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloIntVar var, final long value)
public void setAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloObjective obj, final long value)
public void setAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloConstraint ctr, final long value)
public void setAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloNumVarArray var, final IloIntArrayBase value)
public void setAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloIntVarArray var, final IloIntArrayBase value)
public void setAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloConstraintArray ctr, final IloIntArrayBase value)
public void setAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloNumVar var, final double value)
public void setAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloIntVar var, final double value)
public void setAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloObjective obj, final double value)
public void setAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloConstraint ctr, final double value)
public void setAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloNumVarArray var, final IloNumArray value)
public void setAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloIntVarArray var, final IloNumArray value)
public void setAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation annotation, final IloConstraintArray ctr, final IloNumArray value)
'''
pass
def numNumAnnotations():
'''public int numNumAnnotations()
'''
pass
def newNumAnnotation():
'''public SWIGTYPE_p_IloCplex__NumAnnotation newNumAnnotation(final String name, final double defval)
public SWIGTYPE_p_IloCplex__NumAnnotation newNumAnnotation(final String name)
'''
pass
def findNumAnnotation():
'''public SWIGTYPE_p_IloCplex__NumAnnotation findNumAnnotation(final String name)
public SWIGTYPE_p_IloCplex__NumAnnotation findNumAnnotation(final int num)
'''
pass
def hasNumAnnotation():
'''public boolean hasNumAnnotation(final String name)
'''
pass
def getObjective():
'''public IloObjective getObjective()
'''
pass
def getVersion():
'''public String getVersion()
'''
pass
def getVersionNumber():
'''public int getVersionNumber()
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
def getNbarrierIterations64():
'''public long getNbarrierIterations64()
'''
pass
def getNbarrierIterations():
'''public int getNbarrierIterations()
'''
pass
def getNsiftingIterations64():
'''public long getNsiftingIterations64()
'''
pass
def getNsiftingIterations():
'''public int getNsiftingIterations()
'''
pass
def getNsiftingPhaseOneIterations64():
'''public long getNsiftingPhaseOneIterations64()
'''
pass
def getNsiftingPhaseOneIterations():
'''public int getNsiftingPhaseOneIterations()
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
def getNSOSs():
'''public int getNSOSs()
'''
pass
def getNindicators():
'''public int getNindicators()
'''
pass
def getNLCs():
'''public int getNLCs()
'''
pass
def getNUCs():
'''public int getNUCs()
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
def solveFixed():
'''public boolean solveFixed(final int soln)
public boolean solveFixed()
'''
pass
def isMIP():
'''public boolean isMIP()
'''
pass
def isQC():
'''public boolean isQC()
'''
pass
def isQO():
'''public boolean isQO()
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
def getIncumbentNode64():
'''public long getIncumbentNode64()
'''
pass
def getIncumbentNode():
'''public int getIncumbentNode()
'''
pass
def getNprimalSuperbasics():
'''public int getNprimalSuperbasics()
'''
pass
def getNdualSuperbasics():
'''public int getNdualSuperbasics()
'''
pass
def getNphaseOneIterations64():
'''public long getNphaseOneIterations64()
'''
pass
def getNphaseOneIterations():
'''public int getNphaseOneIterations()
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
def getNnodesLeft64():
'''public long getNnodesLeft64()
'''
pass
def getNnodesLeft():
'''public int getNnodesLeft()
'''
pass
def getNcuts():
'''public int getNcuts(final CutType which)
'''
pass
def getNcrossPPush64():
'''public long getNcrossPPush64()
'''
pass
def getNcrossPPush():
'''public int getNcrossPPush()
'''
pass
def getNcrossPExch64():
'''public long getNcrossPExch64()
'''
pass
def getNcrossPExch():
'''public int getNcrossPExch()
'''
pass
def getNcrossDPush64():
'''public long getNcrossDPush64()
'''
pass
def getNcrossDPush():
'''public int getNcrossDPush()
'''
pass
def getNcrossDExch64():
'''public long getNcrossDExch64()
'''
pass
def getNcrossDExch():
'''public int getNcrossDExch()
'''
pass
def getValues():
'''public void getValues(final IloNumArray val, final IloNumVarArray var)
public void getValues(final IloNumVarArray var, final IloNumArray val)
public void getValues(final IloNumArray val, final IloIntVarArray var)
public void getValues(final IloIntVarArray var, final IloNumArray val)
public void getValues(final IloNumArray val, final IloNumVarArray var, final int soln)
public void getValues(final IloNumVarArray var, final IloNumArray val, final int soln)
public void getValues(final IloNumArray val, final IloIntVarArray var, final int soln)
public void getValues(final IloIntVarArray var, final IloNumArray val, final int soln)
'''
pass
def getValue():
'''public double getValue(final IloNumVar var, final int soln)
public double getValue(final IloIntVar var, final int soln)
public double getValue(final IloNumExprArg expr, final int soln)
public double getValue(final IloObjective ob, final int soln)
'''
pass
def getObjValue():
'''public double getObjValue(final int soln)
'''
pass
def getDual():
'''public double getDual(final IloRange range)
public double getDual(final IloForAllRange range)
'''
pass
def getSlack():
'''public double getSlack(final IloRange range, final int soln)
public double getSlack(final IloRange range)
public double getSlack(final IloForAllRange range, final int soln)
public double getSlack(final IloForAllRange range)
'''
pass
def getInfeasibility():
'''public double getInfeasibility(final IloConstraint con)
public double getInfeasibility(final IloNumVar var)
public double getInfeasibility(final IloIntVar var)
'''
pass
def getAX():
'''public double getAX(final IloRange range)
public void getAX(final IloNumArray val, final IloRangeArray con)
public double getAX(final IloForAllRange range)
public void getAX(final IloNumArray val, final IloForAllRangeArray con)
'''
pass
def getReducedCost():
'''public double getReducedCost(final IloNumVar var)
public double getReducedCost(final IloIntVar var)
'''
pass
def getQCDSlack():
'''public void getQCDSlack(final IloRange range, final IloNumArray vals, final IloNumVarArray vars)
public void getQCDSlack(final IloForAllRange range, final IloNumArray vals, final IloNumVarArray vars)
'''
pass
def getBasisStatus():
'''public BasisStatus getBasisStatus(final IloNumVar var)
public BasisStatus getBasisStatus(final IloIntVar var)
public BasisStatus getBasisStatus(final IloConstraint con)
'''
pass
def getDuals():
'''public void getDuals(final IloNumArray val, final IloRangeArray con)
public void getDuals(final IloNumArray val, final IloForAllRangeArray con)
'''
pass
def getSlacks():
'''public void getSlacks(final IloNumArray val, final IloRangeArray con, final int soln)
public void getSlacks(final IloNumArray val, final IloRangeArray con)
public void getSlacks(final IloNumArray val, final IloForAllRangeArray con, final int soln)
public void getSlacks(final IloNumArray val, final IloForAllRangeArray con)
'''
pass
def getInfeasibilities():
'''public double getInfeasibilities(final IloNumArray infeas, final IloConstraintArray con)
public double getInfeasibilities(final IloNumArray infeas, final IloNumVarArray var)
public double getInfeasibilities(final IloNumArray infeas, final IloIntVarArray var)
'''
pass
def getReducedCosts():
'''public void getReducedCosts(final IloNumArray val, final IloNumVarArray var)
public void getReducedCosts(final IloNumArray val, final IloIntVarArray var)
'''
pass
def getBasisStatuses():
'''public void getBasisStatuses(final IloCplex__BasisStatusArray stat, final IloNumVarArray var)
public void getBasisStatuses(final IloCplex__BasisStatusArray stat, final IloIntVarArray var)
public void getBasisStatuses(final IloCplex__BasisStatusArray stat, final IloConstraintArray con)
public void getBasisStatuses(final IloCplex__BasisStatusArray cstat, final IloNumVarArray var, final IloCplex__BasisStatusArray rstat, final IloConstraintArray con)
public void getBasisStatuses(final IloCplex__BasisStatusArray cstat, final IloIntVarArray var, final IloCplex__BasisStatusArray rstat, final IloConstraintArray con)
'''
pass
def getBoundSA():
'''public void getBoundSA(final IloNumArray lblower, final IloNumArray lbupper, final IloNumArray ublower, final IloNumArray ubupper, final IloNumVarArray vars)
public void getBoundSA(final IloNumArray lblower, final IloNumArray lbupper, final IloNumArray ublower, final IloNumArray ubupper, final IloIntVarArray vars)
'''
pass
def getRangeSA():
'''public void getRangeSA(final IloNumArray lblower, final IloNumArray lbupper, final IloNumArray ublower, final IloNumArray ubupper, final IloRangeArray con)
'''
pass
def getRHSSA():
'''public void getRHSSA(final IloNumArray lower, final IloNumArray upper, final IloRangeArray cons)
'''
pass
def getObjSA():
'''public void getObjSA(final IloNumArray lower, final IloNumArray upper, final IloNumVarArray vars)
public void getObjSA(final IloNumArray lower, final IloNumArray upper, final IloIntVarArray cols)
'''
pass
def getForAllRanges():
'''public void getForAllRanges(final IloForAllRangeArray rows, final IloConstraint forall)
'''
pass
def getLB():
'''public double getLB(final IloForAllRange range)
'''
pass
def getUB():
'''public double getUB(final IloForAllRange range)
'''
pass
def feasOpt():
'''public boolean feasOpt(final IloRangeArray rngs, final IloNumArray rnglb, final IloNumArray rngub, final IloForAllRangeArray rngf, final IloNumArray frnglb, final IloNumArray frngub, final IloNumVarArray vars, final IloNumArray varlb, final IloNumArray varub)
public boolean feasOpt(final IloRangeArray rngs, final IloNumArray rnglb, final IloNumArray rngub, final IloNumVarArray vars, final IloNumArray varlb, final IloNumArray varub)
public boolean feasOpt(final IloRangeArray rngs, final IloNumArray rnglb, final IloNumArray rngub, final IloIntVarArray vars, final IloNumArray varlb, final IloNumArray varub)
public boolean feasOpt(final IloNumVarArray vars, final IloNumArray varlb, final IloNumArray varub)
public boolean feasOpt(final IloIntVarArray vars, final IloNumArray varlb, final IloNumArray varub)
public boolean feasOpt(final IloRangeArray rngs, final IloNumArray rnglb, final IloNumArray rngub)
public boolean feasOpt(final IloConstraintArray cts, final IloNumArray prefs)
'''
pass
def setBasisStatuses():
'''public void setBasisStatuses(final IloCplex__BasisStatusArray cstat, final IloNumVarArray var, final IloCplex__BasisStatusArray rstat, final IloConstraintArray con)
public void setBasisStatuses(final IloCplex__BasisStatusArray cstat, final IloIntVarArray var, final IloCplex__BasisStatusArray rstat, final IloConstraintArray con)
'''
pass
def setStart():
'''public void setStart(final IloNumArray x, final IloNumArray dj, final IloNumVarArray var, final IloNumArray slack, final IloNumArray pi, final IloRangeArray rng)
public void setStart(final IloNumArray x, final IloNumArray dj, final IloIntVarArray var, final IloNumArray slack, final IloNumArray pi, final IloRangeArray rng)
'''
pass
def getNMIPStarts():
'''public int getNMIPStarts()
'''
pass
def addMIPStart():
'''public int addMIPStart(final IloNumVarArray vars, final IloNumArray values, final MIPStartEffort effort, final String name)
public int addMIPStart(final IloNumVarArray vars, final IloNumArray values, final MIPStartEffort effort)
public int addMIPStart(final IloNumVarArray vars, final IloNumArray values)
public int addMIPStart(final IloNumVarArray vars)
public int addMIPStart()
'''
pass
def changeMIPStart():
'''public void changeMIPStart(final int mipstartindex, final IloNumVarArray vars, final IloNumArray values)
public void changeMIPStart(final int mipstartindex, final IloNumVarArray vars, final IloNumArray values, final MIPStartEffort effortlevel)
'''
pass
def deleteMIPStarts():
'''public void deleteMIPStarts(final int first, final int num)
public void deleteMIPStarts(final int first)
'''
pass
def getMIPStart():
'''public MIPStartEffort getMIPStart(final int mipstartindex, final IloNumVarArray vars, final IloNumArray vals, final SWIGTYPE_p_IloBoolArray isset)
'''
pass
def getMIPStartName():
'''public String getMIPStartName(final int mipstartindex)
'''
pass
def getMIPStartIndex():
'''public int getMIPStartIndex(final String lname_str)
'''
pass
def setDefaults():
'''public void setDefaults()
'''
pass
def setIntParam():
'''public void setIntParam(final IntParam parameter, final int value)
'''
pass
def setLongParam():
'''public void setLongParam(final LongParam parameter, final long value)
'''
pass
def setBoolParam():
'''public void setBoolParam(final BoolParam parameter, final boolean value)
'''
pass
def setNumParam():
'''public void setNumParam(final NumParam parameter, final double value)
'''
pass
def setStringParam():
'''public void setStringParam(final StringParam parameter, final String value)
'''
pass
def getIntParam():
'''public int getIntParam(final IntParam parameter)
'''
pass
def getLongParam():
'''public long getLongParam(final LongParam parameter)
'''
pass
def getBoolParam():
'''public boolean getBoolParam(final BoolParam parameter)
'''
pass
def getNumParam():
'''public double getNumParam(final NumParam parameter)
'''
pass
def getStringParam():
'''public String getStringParam(final StringParam parameter)
'''
pass
def getDefaultBoolParam():
'''public boolean getDefaultBoolParam(final BoolParam parameter)
'''
pass
def getDefaultIntParam():
'''public int getDefaultIntParam(final IntParam parameter)
'''
pass
def getDefaultLongParam():
'''public long getDefaultLongParam(final LongParam parameter)
'''
pass
def getDefaultNumParam():
'''public double getDefaultNumParam(final NumParam parameter)
'''
pass
def getDefaultStringParam():
'''public String getDefaultStringParam(final StringParam parameter)
'''
pass
def getMinIntParam():
'''public int getMinIntParam(final IntParam parameter)
'''
pass
def getMinLongParam():
'''public long getMinLongParam(final LongParam parameter)
'''
pass
def getMinNumParam():
'''public double getMinNumParam(final NumParam parameter)
'''
pass
def getMaxIntParam():
'''public int getMaxIntParam(final IntParam parameter)
'''
pass
def getMaxLongParam():
'''public long getMaxLongParam(final LongParam parameter)
'''
pass
def getMaxNumParam():
'''public double getMaxNumParam(final NumParam parameter)
'''
pass
def getParameterSet():
'''public IloCplex__ParameterSet getParameterSet()
'''
pass
def setParameterSet():
'''public void setParameterSet(final IloCplex__ParameterSet set)
'''
pass
def getStatus():
'''public Status getStatus()
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
def isPrimalFeasible():
'''public boolean isPrimalFeasible()
'''
pass
def isDualFeasible():
'''public boolean isDualFeasible()
'''
pass
def getAlgorithm():
'''public Algorithm getAlgorithm()
'''
pass
def getSubAlgorithm():
'''public Algorithm getSubAlgorithm()
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
def populate():
'''public boolean populate()
'''
pass
def tuneParam():
'''public int tuneParam(final IloStringArrayBase filename, final IloCplex__ParameterSet fixedset)
public int tuneParam()
public int tuneParam(final IloCplex__ParameterSet fixedset)
public int tuneParam(final IloStringArrayBase filename)
'''
pass
def refineConflict():
'''public boolean refineConflict(final IloConstraintArray cons, final IloNumArray prefs)
'''
pass
def refineMIPStartConflict():
'''public boolean refineMIPStartConflict(final int mipstartindex, final IloConstraintArray cons, final IloNumArray prefs)
'''
pass
def getConflict():
'''public IloCplex__ConflictStatusArray getConflict(final IloConstraintArray cons)
public ConflictStatus getConflict(final IloConstraint con)
'''
pass
def getQuality():
'''public double getQuality(final Quality q, final IloNumVar var, final IloConstraint rng)
public double getQuality(final Quality q, final IloNumVar var)
public double getQuality(final Quality q)
public double getQuality(final Quality q, final IloConstraint rng, final IloNumVar var)
public double getQuality(final Quality q, final IloConstraint rng)
public double getQuality(final Quality q, final int soln, final IloConstraint rng, final IloNumVar var)
public double getQuality(final Quality q, final int soln, final IloConstraint rng)
public double getQuality(final Quality q, final int soln, final IloNumVar var, final IloConstraint rng)
public double getQuality(final Quality q, final int soln, final IloNumVar var)
public double getQuality(final Quality q, final int soln)
'''
pass
def setPriority():
'''public void setPriority(final IloNumVar var, final double pri)
public void setPriority(final IloIntVar var, final double pri)
'''
pass
def setPriorities():
'''public void setPriorities(final IloNumVarArray var, final IloNumArray pri)
public void setPriorities(final IloIntVarArray var, final IloNumArray pri)
'''
pass
def setDirection():
'''public void setDirection(final IloNumVar var, final BranchDirection dir)
public void setDirection(final IloIntVar var, final BranchDirection dir)
'''
pass
def setDirections():
'''public void setDirections(final IloNumVarArray var, final IloCplex__BranchDirectionArray dir)
public void setDirections(final IloIntVarArray var, final IloCplex__BranchDirectionArray dir)
'''
pass
def delPriority():
'''public void delPriority(final IloNumVar var)
public void delPriority(final IloIntVar var)
'''
pass
def delPriorities():
'''public void delPriorities(final IloNumVarArray var)
public void delPriorities(final IloIntVarArray var)
'''
pass
def delDirection():
'''public void delDirection(final IloNumVar var)
public void delDirection(final IloIntVar var)
'''
pass
def delDirections():
'''public void delDirections(final IloNumVarArray var)
public void delDirections(final IloIntVarArray var)
'''
pass
def getPriority():
'''public double getPriority(final IloNumVar var)
public double getPriority(final IloIntVar var)
'''
pass
def getDirection():
'''public BranchDirection getDirection(final IloNumVar var)
public BranchDirection getDirection(final IloIntVar var)
'''
pass
def getPriorities():
'''public void getPriorities(final IloNumArray pri, final IloNumVarArray var)
public void getPriorities(final IloNumArray pri, final IloIntVarArray var)
'''
pass
def getDirections():
'''public void getDirections(final IloCplex__BranchDirectionArray dir, final IloNumVarArray var)
public void getDirections(final IloCplex__BranchDirectionArray dir, final IloIntVarArray var)
'''
pass
def basicPresolve():
'''public void basicPresolve(final IloNumVarArray vars, final IloNumArray redlb, final IloNumArray redub, final IloRangeArray rngs, final SWIGTYPE_p_IloBoolArray redundant)
public void basicPresolve(final IloNumVarArray vars, final IloNumArray redlb, final IloNumArray redub, final IloRangeArray rngs)
public void basicPresolve(final IloNumVarArray vars, final IloNumArray redlb, final IloNumArray redub)
public void basicPresolve(final IloNumVarArray vars, final IloNumArray redlb)
public void basicPresolve(final IloNumVarArray vars)
public void basicPresolve(final IloIntVarArray vars, final IloNumArray redlb, final IloNumArray redub, final IloRangeArray rngs, final SWIGTYPE_p_IloBoolArray redundant)
public void basicPresolve(final IloIntVarArray vars, final IloNumArray redlb, final IloNumArray redub, final IloRangeArray rngs)
public void basicPresolve(final IloIntVarArray vars, final IloNumArray redlb, final IloNumArray redub)
public void basicPresolve(final IloIntVarArray vars, final IloNumArray redlb)
public void basicPresolve(final IloIntVarArray vars)
'''
pass
def freePresolve():
'''public void freePresolve()
'''
pass
def presolve():
'''public void presolve(final SWIGTYPE_p_IloCplex__Algorithm alg)
'''
pass
def getDiverging():
'''public IloExtractable getDiverging()
'''
pass
def getRay():
'''public void getRay(final IloNumArray vals, final IloNumVarArray vars)
'''
pass
def dualFarkas():
'''public double dualFarkas(final IloConstraintArray rng, final IloNumArray y)
'''
pass
def qpIndefCertificate():
'''public void qpIndefCertificate(final IloNumVarArray var, final IloNumArray x)
public void qpIndefCertificate(final IloIntVarArray var, final IloNumArray x)
'''
pass
def protectVariables():
'''public void protectVariables(final IloNumVarArray var)
public void protectVariables(final IloIntVarArray var)
'''
pass
def use():
'''public IloCplex__Aborter use(final IloCplex__Aborter abort)
public IloCplex__Callback use(final IloCplex__Callback cb)
'''
pass
def getAborter():
'''public IloCplex__Aborter getAborter()
'''
pass
def remove():
'''public void remove(final IloCplex__Aborter abort)
public void remove(final IloCplex__Callback cb)
'''
pass
def solve():
'''public boolean solve()
public boolean solve(final IloCplex__Goal goal)
'''
pass
def setFormulationEpsValue():
'''public void setFormulationEpsValue(final double eps)
'''
pass
def getFormulationEpsValue():
'''public double getFormulationEpsValue()
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
def getCplexTime():
'''public double getCplexTime()
'''
pass
def getDetTime():
'''public double getDetTime()
'''
pass
def getNumCores():
'''public int getNumCores()
'''
pass
def GetVersion():
'''public static void GetVersion(final String buffer, final int len)
'''
pass
def GetAcademicMsg():
'''public static void GetAcademicMsg(final String buffer, final int len)
'''
pass
def GetPreviewMsg():
'''public static void GetPreviewMsg(final String buffer, final int len)
'''
pass
def Apply():
'''public static IloCplex__Goal Apply(final IloCplex cplex, final IloCplex__Goal goal, final IloCplex__NodeEvaluator eval)
'''
pass
def LimitSearch():
'''public static IloCplex__Goal LimitSearch(final IloCplex cplex, final IloCplex__Goal goal, final SWIGTYPE_p_SearchLimit limit)
'''
pass
def add():
'''public IloCplex__Callback add(final IloCplex__Callback cb)
'''
pass
def inUse():
'''public boolean inUse(final IloCplex__Callback cb)
'''
pass
def _readVMConfig():
'''public void _readVMConfig(final String f)
'''
pass
def _copyVMConfig():
'''public void _copyVMConfig(final String f)
'''
pass
def mySwigValue():
'''public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
public int mySwigValue()
'''
pass
def swigValue():
'''public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
public final int swigValue()
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
'''
pass
def swigToEnum():
'''public static WriteLevelType swigToEnum(final int swigValue)
public static BasisStatus swigToEnum(final int swigValue)
public static CutType swigToEnum(final int swigValue)
public static MIPStartEffort swigToEnum(final int swigValue)
public static NumParam swigToEnum(final int swigValue)
public static BoolParam swigToEnum(final int swigValue)
public static IntParam swigToEnum(final int swigValue)
public static LongParam swigToEnum(final int swigValue)
public static StringParam swigToEnum(final int swigValue)
public static MIPEmphasisType swigToEnum(final int swigValue)
public static OptimalityTargetType swigToEnum(final int swigValue)
public static VariableSelect swigToEnum(final int swigValue)
public static NodeSelect swigToEnum(final int swigValue)
public static DistMIPRampupDuration swigToEnum(final int swigValue)
public static PrimalPricing swigToEnum(final int swigValue)
public static ConflictAlgorithm swigToEnum(final int swigValue)
public static Parallel_Mode swigToEnum(final int swigValue)
public static MIPsearch swigToEnum(final int swigValue)
public static DataCheckType swigToEnum(final int swigValue)
public static DualPricing swigToEnum(final int swigValue)
public static BranchDirection swigToEnum(final int swigValue)
public static Algorithm swigToEnum(final int swigValue)
public static Relaxation swigToEnum(final int swigValue)
public static BendersStrategyType swigToEnum(final int swigValue)
public static CplexStatus swigToEnum(final int swigValue)
public static DeleteMode swigToEnum(final int swigValue)
public static TuningStatus swigToEnum(final int swigValue)
public static ConflictStatus swigToEnum(final int swigValue)
public static Quality swigToEnum(final int swigValue)
public static CutManagement swigToEnum(final int swigValue)
public static FilterType swigToEnum(final int swigValue)
'''
pass
def WriteLevelType():
'''public WriteLevelType(final String swigName, final int swigValue)
'''
pass
def BasisStatus():
'''public BasisStatus(final String swigName, final int swigValue)
'''
pass
def CutType():
'''public CutType(final String swigName, final int swigValue)
'''
pass
def MIPStartEffort():
'''public MIPStartEffort(final String swigName, final int swigValue)
'''
pass
def NumParam():
'''public NumParam(final String swigName, final int swigValue)
'''
pass
def BoolParam():
'''public BoolParam(final String swigName, final int swigValue)
'''
pass
def IntParam():
'''public IntParam(final String swigName, final int swigValue)
'''
pass
def LongParam():
'''public LongParam(final String swigName, final int swigValue)
'''
pass
def StringParam():
'''public StringParam(final String swigName, final int swigValue)
'''
pass
def MIPEmphasisType():
'''public MIPEmphasisType(final String swigName, final int swigValue)
'''
pass
def OptimalityTargetType():
'''public OptimalityTargetType(final String swigName, final int swigValue)
'''
pass
def VariableSelect():
'''public VariableSelect(final String swigName, final int swigValue)
'''
pass
def NodeSelect():
'''public NodeSelect(final String swigName, final int swigValue)
'''
pass
def DistMIPRampupDuration():
'''public DistMIPRampupDuration(final String swigName, final int swigValue)
'''
pass
def PrimalPricing():
'''public PrimalPricing(final String swigName, final int swigValue)
'''
pass
def ConflictAlgorithm():
'''public ConflictAlgorithm(final String swigName, final int swigValue)
'''
pass
def Parallel_Mode():
'''public Parallel_Mode(final String swigName, final int swigValue)
'''
pass
def MIPsearch():
'''public MIPsearch(final String swigName, final int swigValue)
'''
pass
def DataCheckType():
'''public DataCheckType(final String swigName, final int swigValue)
'''
pass
def DualPricing():
'''public DualPricing(final String swigName, final int swigValue)
'''
pass
def BranchDirection():
'''public BranchDirection(final String swigName, final int swigValue)
'''
pass
def Algorithm():
'''public Algorithm(final String swigName, final int swigValue)
'''
pass
def Relaxation():
'''public Relaxation(final String swigName, final int swigValue)
'''
pass
def BendersStrategyType():
'''public BendersStrategyType(final String swigName, final int swigValue)
'''
pass
def CplexStatus():
'''public CplexStatus(final String swigName, final int swigValue)
'''
pass
def DeleteMode():
'''public DeleteMode(final String swigName, final int swigValue)
'''
pass
def TuningStatus():
'''public TuningStatus(final String swigName, final int swigValue)
'''
pass
def ConflictStatus():
'''public ConflictStatus(final String swigName, final int swigValue)
'''
pass
def Quality():
'''public Quality(final String swigName, final int swigValue)
'''
pass
def CutManagement():
'''public CutManagement(final String swigName, final int swigValue)
'''
pass
def FilterType():
'''public FilterType(final String swigName, final int swigValue)
'''
pass
