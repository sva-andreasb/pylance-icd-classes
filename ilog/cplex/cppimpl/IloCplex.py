def IloCplex():
    '''    public IloCplex(final long cPtr, final boolean cMemoryOwn)
    public IloCplex(final IloEnv env)
    public IloCplex(final IloModel model)
    '''
def getCPtr():
    '''    public static long getCPtr(final IloCplex obj)
    '''
def delete():
    '''    public void delete()
    '''
def getIncumbentId():
    '''    public static int getIncumbentId()
    '''
def setBendersAnnotation():
    '''    public static void setBendersAnnotation(final String value)
    '''
def getBendersAnnotation():
    '''    public static String getBendersAnnotation()
    '''
def hasVMConfig():
    '''    public boolean hasVMConfig()
    '''
def delVMConfig():
    '''    public void delVMConfig()
    '''
def clearModel():
    '''    public void clearModel()
    '''
def deleteNames():
    '''    public void deleteNames()
    '''
def addUserCut():
    '''    public IloConstraint addUserCut(final IloConstraint con)
    '''
def addUserCuts():
    '''    public IloConstraintArray addUserCuts(final IloConstraintArray con)
    '''
def clearUserCuts():
    '''    public void clearUserCuts()
    '''
def addCut():
    '''    public IloConstraint addCut(final IloConstraint con)
    '''
def addCuts():
    '''    public IloConstraintArray addCuts(final IloConstraintArray con)
    '''
def clearCuts():
    '''    public void clearCuts()
    '''
def addLazyConstraint():
    '''    public IloConstraint addLazyConstraint(final IloConstraint con)
    '''
def addLazyConstraints():
    '''    public IloConstraintArray addLazyConstraints(final IloConstraintArray con)
    '''
def clearLazyConstraints():
    '''    public void clearLazyConstraints()
    '''
def importModel():
    '''    public void importModel(final IloModel model, final String filename, final IloObjective obj, final IloNumVarArray vars, final IloRangeArray rngs, final IloSOS1Array sos1, final IloSOS2Array sos2, final IloRangeArray lazy, final IloRangeArray cuts)
    public void importModel(final IloModel model, final String filename, final IloObjective obj, final IloNumVarArray vars, final IloRangeArray rngs, final IloSOS1Array sos1, final IloSOS2Array sos2, final IloRangeArray lazy)
    public void importModel(final IloModel model, final String filename, final IloObjective obj, final IloNumVarArray vars, final IloRangeArray rngs, final IloSOS1Array sos1, final IloSOS2Array sos2)
    public void importModel(final IloModel m, final String filename, final IloObjective obj, final IloNumVarArray vars, final IloRangeArray rngs, final IloRangeArray lazy, final IloRangeArray cuts)
    public void importModel(final IloModel m, final String filename, final IloObjective obj, final IloNumVarArray vars, final IloRangeArray rngs, final IloRangeArray lazy)
    public void importModel(final IloModel m, final String filename, final IloObjective obj, final IloNumVarArray vars, final IloRangeArray rngs)
    public void importModel(final IloModel m, final String filename)
    '''
def exportModel():
    '''    public void exportModel(final String filename)
    '''
def writeOrder():
    '''    public void writeOrder(final String filename)
    '''
def writeConflict():
    '''    public void writeConflict(final String filename)
    '''
def writeParam():
    '''    public void writeParam(final String name)
    '''
def writeBasis():
    '''    public void writeBasis(final String name)
    '''
def writeSolution():
    '''    public void writeSolution(final String name, final int soln)
    public void writeSolution(final String name)
    '''
def writeSolutions():
    '''    public void writeSolutions(final String name)
    '''
def writeMIPStarts():
    '''    public void writeMIPStarts(final String name, final int first, final int num)
    public void writeMIPStarts(final String name, final int first)
    public void writeMIPStarts(final String name)
    '''
def readOrder():
    '''    public void readOrder(final String filename)
    '''
def readParam():
    '''    public void readParam(final String name)
    '''
def readBasis():
    '''    public void readBasis(final String name)
    '''
def readSolution():
    '''    public void readSolution(final String name)
    '''
def readMIPStarts():
    '''    public void readMIPStarts(final String name)
    '''
def writeBendersAnnotation():
    '''    public void writeBendersAnnotation(final String name)
    '''
def readAnnotations():
    '''    public void readAnnotations(final String name)
    '''
def writeAnnotations():
    '''    public void writeAnnotations(final String name)
    '''
def numLongAnnotations():
    '''    public int numLongAnnotations()
    '''
def delAnnotation():
    '''    public void delAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation anno)
    public void delAnnotation(final SWIGTYPE_p_IloCplex__NumAnnotation anno)
    '''
def getName():
    '''    public String getName(final SWIGTYPE_p_IloCplex__LongAnnotation annotation)
    public String getName(final SWIGTYPE_p_IloCplex__NumAnnotation annotation)
    '''
def newLongAnnotation():
    '''    public SWIGTYPE_p_IloCplex__LongAnnotation newLongAnnotation(final String name, final long defval)
    public SWIGTYPE_p_IloCplex__LongAnnotation newLongAnnotation(final String name)
    '''
def findLongAnnotation():
    '''    public SWIGTYPE_p_IloCplex__LongAnnotation findLongAnnotation(final String name)
    public SWIGTYPE_p_IloCplex__LongAnnotation findLongAnnotation(final int num)
    '''
def hasLongAnnotation():
    '''    public boolean hasLongAnnotation(final String name)
    '''
def getDefaultValue():
    '''    public long getDefaultValue(final SWIGTYPE_p_IloCplex__LongAnnotation annotation)
    public double getDefaultValue(final SWIGTYPE_p_IloCplex__NumAnnotation annotation)
    '''
def getAnnotation():
    '''    public long getAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloNumVar var)
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
def setAnnotation():
    '''    public void setAnnotation(final SWIGTYPE_p_IloCplex__LongAnnotation annotation, final IloNumVar var, final long value)
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
def numNumAnnotations():
    '''    public int numNumAnnotations()
    '''
def newNumAnnotation():
    '''    public SWIGTYPE_p_IloCplex__NumAnnotation newNumAnnotation(final String name, final double defval)
    public SWIGTYPE_p_IloCplex__NumAnnotation newNumAnnotation(final String name)
    '''
def findNumAnnotation():
    '''    public SWIGTYPE_p_IloCplex__NumAnnotation findNumAnnotation(final String name)
    public SWIGTYPE_p_IloCplex__NumAnnotation findNumAnnotation(final int num)
    '''
def hasNumAnnotation():
    '''    public boolean hasNumAnnotation(final String name)
    '''
def getObjective():
    '''    public IloObjective getObjective()
    '''
def getVersion():
    '''    public String getVersion()
    '''
def getVersionNumber():
    '''    public int getVersionNumber()
    '''
def getNiterations64():
    '''    public long getNiterations64()
    '''
def getNiterations():
    '''    public int getNiterations()
    '''
def getNbarrierIterations64():
    '''    public long getNbarrierIterations64()
    '''
def getNbarrierIterations():
    '''    public int getNbarrierIterations()
    '''
def getNsiftingIterations64():
    '''    public long getNsiftingIterations64()
    '''
def getNsiftingIterations():
    '''    public int getNsiftingIterations()
    '''
def getNsiftingPhaseOneIterations64():
    '''    public long getNsiftingPhaseOneIterations64()
    '''
def getNsiftingPhaseOneIterations():
    '''    public int getNsiftingPhaseOneIterations()
    '''
def getNcols():
    '''    public int getNcols()
    '''
def getNrows():
    '''    public int getNrows()
    '''
def getNQCs():
    '''    public int getNQCs()
    '''
def getNSOSs():
    '''    public int getNSOSs()
    '''
def getNindicators():
    '''    public int getNindicators()
    '''
def getNLCs():
    '''    public int getNLCs()
    '''
def getNUCs():
    '''    public int getNUCs()
    '''
def getNNZs():
    '''    public int getNNZs()
    '''
def getNNZs64():
    '''    public long getNNZs64()
    '''
def getNintVars():
    '''    public int getNintVars()
    '''
def getNbinVars():
    '''    public int getNbinVars()
    '''
def getNsemiContVars():
    '''    public int getNsemiContVars()
    '''
def getNsemiIntVars():
    '''    public int getNsemiIntVars()
    '''
def solveFixed():
    '''    public boolean solveFixed(final int soln)
    public boolean solveFixed()
    '''
def isMIP():
    '''    public boolean isMIP()
    '''
def isQC():
    '''    public boolean isQC()
    '''
def isQO():
    '''    public boolean isQO()
    '''
def getBestObjValue():
    '''    public double getBestObjValue()
    '''
def getMIPRelativeGap():
    '''    public double getMIPRelativeGap()
    '''
def getCutoff():
    '''    public double getCutoff()
    '''
def getIncumbentNode64():
    '''    public long getIncumbentNode64()
    '''
def getIncumbentNode():
    '''    public int getIncumbentNode()
    '''
def getNprimalSuperbasics():
    '''    public int getNprimalSuperbasics()
    '''
def getNdualSuperbasics():
    '''    public int getNdualSuperbasics()
    '''
def getNphaseOneIterations64():
    '''    public long getNphaseOneIterations64()
    '''
def getNphaseOneIterations():
    '''    public int getNphaseOneIterations()
    '''
def getNnodes64():
    '''    public long getNnodes64()
    '''
def getNnodes():
    '''    public int getNnodes()
    '''
def getNnodesLeft64():
    '''    public long getNnodesLeft64()
    '''
def getNnodesLeft():
    '''    public int getNnodesLeft()
    '''
def getNcuts():
    '''    public int getNcuts(final CutType which)
    '''
def getNcrossPPush64():
    '''    public long getNcrossPPush64()
    '''
def getNcrossPPush():
    '''    public int getNcrossPPush()
    '''
def getNcrossPExch64():
    '''    public long getNcrossPExch64()
    '''
def getNcrossPExch():
    '''    public int getNcrossPExch()
    '''
def getNcrossDPush64():
    '''    public long getNcrossDPush64()
    '''
def getNcrossDPush():
    '''    public int getNcrossDPush()
    '''
def getNcrossDExch64():
    '''    public long getNcrossDExch64()
    '''
def getNcrossDExch():
    '''    public int getNcrossDExch()
    '''
def getValues():
    '''    public void getValues(final IloNumArray val, final IloNumVarArray var)
    public void getValues(final IloNumVarArray var, final IloNumArray val)
    public void getValues(final IloNumArray val, final IloIntVarArray var)
    public void getValues(final IloIntVarArray var, final IloNumArray val)
    public void getValues(final IloNumArray val, final IloNumVarArray var, final int soln)
    public void getValues(final IloNumVarArray var, final IloNumArray val, final int soln)
    public void getValues(final IloNumArray val, final IloIntVarArray var, final int soln)
    public void getValues(final IloIntVarArray var, final IloNumArray val, final int soln)
    '''
def getValue():
    '''    public double getValue(final IloNumVar var, final int soln)
    public double getValue(final IloIntVar var, final int soln)
    public double getValue(final IloNumExprArg expr, final int soln)
    public double getValue(final IloObjective ob, final int soln)
    '''
def getObjValue():
    '''    public double getObjValue(final int soln)
    '''
def getDual():
    '''    public double getDual(final IloRange range)
    public double getDual(final IloForAllRange range)
    '''
def getSlack():
    '''    public double getSlack(final IloRange range, final int soln)
    public double getSlack(final IloRange range)
    public double getSlack(final IloForAllRange range, final int soln)
    public double getSlack(final IloForAllRange range)
    '''
def getInfeasibility():
    '''    public double getInfeasibility(final IloConstraint con)
    public double getInfeasibility(final IloNumVar var)
    public double getInfeasibility(final IloIntVar var)
    '''
def getAX():
    '''    public double getAX(final IloRange range)
    public void getAX(final IloNumArray val, final IloRangeArray con)
    public double getAX(final IloForAllRange range)
    public void getAX(final IloNumArray val, final IloForAllRangeArray con)
    '''
def getReducedCost():
    '''    public double getReducedCost(final IloNumVar var)
    public double getReducedCost(final IloIntVar var)
    '''
def getQCDSlack():
    '''    public void getQCDSlack(final IloRange range, final IloNumArray vals, final IloNumVarArray vars)
    public void getQCDSlack(final IloForAllRange range, final IloNumArray vals, final IloNumVarArray vars)
    '''
def getBasisStatus():
    '''    public BasisStatus getBasisStatus(final IloNumVar var)
    public BasisStatus getBasisStatus(final IloIntVar var)
    public BasisStatus getBasisStatus(final IloConstraint con)
    '''
def getDuals():
    '''    public void getDuals(final IloNumArray val, final IloRangeArray con)
    public void getDuals(final IloNumArray val, final IloForAllRangeArray con)
    '''
def getSlacks():
    '''    public void getSlacks(final IloNumArray val, final IloRangeArray con, final int soln)
    public void getSlacks(final IloNumArray val, final IloRangeArray con)
    public void getSlacks(final IloNumArray val, final IloForAllRangeArray con, final int soln)
    public void getSlacks(final IloNumArray val, final IloForAllRangeArray con)
    '''
def getInfeasibilities():
    '''    public double getInfeasibilities(final IloNumArray infeas, final IloConstraintArray con)
    public double getInfeasibilities(final IloNumArray infeas, final IloNumVarArray var)
    public double getInfeasibilities(final IloNumArray infeas, final IloIntVarArray var)
    '''
def getReducedCosts():
    '''    public void getReducedCosts(final IloNumArray val, final IloNumVarArray var)
    public void getReducedCosts(final IloNumArray val, final IloIntVarArray var)
    '''
def getBasisStatuses():
    '''    public void getBasisStatuses(final IloCplex__BasisStatusArray stat, final IloNumVarArray var)
    public void getBasisStatuses(final IloCplex__BasisStatusArray stat, final IloIntVarArray var)
    public void getBasisStatuses(final IloCplex__BasisStatusArray stat, final IloConstraintArray con)
    public void getBasisStatuses(final IloCplex__BasisStatusArray cstat, final IloNumVarArray var, final IloCplex__BasisStatusArray rstat, final IloConstraintArray con)
    public void getBasisStatuses(final IloCplex__BasisStatusArray cstat, final IloIntVarArray var, final IloCplex__BasisStatusArray rstat, final IloConstraintArray con)
    '''
def getBoundSA():
    '''    public void getBoundSA(final IloNumArray lblower, final IloNumArray lbupper, final IloNumArray ublower, final IloNumArray ubupper, final IloNumVarArray vars)
    public void getBoundSA(final IloNumArray lblower, final IloNumArray lbupper, final IloNumArray ublower, final IloNumArray ubupper, final IloIntVarArray vars)
    '''
def getRangeSA():
    '''    public void getRangeSA(final IloNumArray lblower, final IloNumArray lbupper, final IloNumArray ublower, final IloNumArray ubupper, final IloRangeArray con)
    '''
def getRHSSA():
    '''    public void getRHSSA(final IloNumArray lower, final IloNumArray upper, final IloRangeArray cons)
    '''
def getObjSA():
    '''    public void getObjSA(final IloNumArray lower, final IloNumArray upper, final IloNumVarArray vars)
    public void getObjSA(final IloNumArray lower, final IloNumArray upper, final IloIntVarArray cols)
    '''
def getForAllRanges():
    '''    public void getForAllRanges(final IloForAllRangeArray rows, final IloConstraint forall)
    '''
def getLB():
    '''    public double getLB(final IloForAllRange range)
    '''
def getUB():
    '''    public double getUB(final IloForAllRange range)
    '''
def feasOpt():
    '''    public boolean feasOpt(final IloRangeArray rngs, final IloNumArray rnglb, final IloNumArray rngub, final IloForAllRangeArray rngf, final IloNumArray frnglb, final IloNumArray frngub, final IloNumVarArray vars, final IloNumArray varlb, final IloNumArray varub)
    public boolean feasOpt(final IloRangeArray rngs, final IloNumArray rnglb, final IloNumArray rngub, final IloNumVarArray vars, final IloNumArray varlb, final IloNumArray varub)
    public boolean feasOpt(final IloRangeArray rngs, final IloNumArray rnglb, final IloNumArray rngub, final IloIntVarArray vars, final IloNumArray varlb, final IloNumArray varub)
    public boolean feasOpt(final IloNumVarArray vars, final IloNumArray varlb, final IloNumArray varub)
    public boolean feasOpt(final IloIntVarArray vars, final IloNumArray varlb, final IloNumArray varub)
    public boolean feasOpt(final IloRangeArray rngs, final IloNumArray rnglb, final IloNumArray rngub)
    public boolean feasOpt(final IloConstraintArray cts, final IloNumArray prefs)
    '''
def setBasisStatuses():
    '''    public void setBasisStatuses(final IloCplex__BasisStatusArray cstat, final IloNumVarArray var, final IloCplex__BasisStatusArray rstat, final IloConstraintArray con)
    public void setBasisStatuses(final IloCplex__BasisStatusArray cstat, final IloIntVarArray var, final IloCplex__BasisStatusArray rstat, final IloConstraintArray con)
    '''
def setStart():
    '''    public void setStart(final IloNumArray x, final IloNumArray dj, final IloNumVarArray var, final IloNumArray slack, final IloNumArray pi, final IloRangeArray rng)
    public void setStart(final IloNumArray x, final IloNumArray dj, final IloIntVarArray var, final IloNumArray slack, final IloNumArray pi, final IloRangeArray rng)
    '''
def getNMIPStarts():
    '''    public int getNMIPStarts()
    '''
def addMIPStart():
    '''    public int addMIPStart(final IloNumVarArray vars, final IloNumArray values, final MIPStartEffort effort, final String name)
    public int addMIPStart(final IloNumVarArray vars, final IloNumArray values, final MIPStartEffort effort)
    public int addMIPStart(final IloNumVarArray vars, final IloNumArray values)
    public int addMIPStart(final IloNumVarArray vars)
    public int addMIPStart()
    '''
def changeMIPStart():
    '''    public void changeMIPStart(final int mipstartindex, final IloNumVarArray vars, final IloNumArray values)
    public void changeMIPStart(final int mipstartindex, final IloNumVarArray vars, final IloNumArray values, final MIPStartEffort effortlevel)
    '''
def deleteMIPStarts():
    '''    public void deleteMIPStarts(final int first, final int num)
    public void deleteMIPStarts(final int first)
    '''
def getMIPStart():
    '''    public MIPStartEffort getMIPStart(final int mipstartindex, final IloNumVarArray vars, final IloNumArray vals, final SWIGTYPE_p_IloBoolArray isset)
    '''
def getMIPStartName():
    '''    public String getMIPStartName(final int mipstartindex)
    '''
def getMIPStartIndex():
    '''    public int getMIPStartIndex(final String lname_str)
    '''
def setDefaults():
    '''    public void setDefaults()
    '''
def setIntParam():
    '''    public void setIntParam(final IntParam parameter, final int value)
    '''
def setLongParam():
    '''    public void setLongParam(final LongParam parameter, final long value)
    '''
def setBoolParam():
    '''    public void setBoolParam(final BoolParam parameter, final boolean value)
    '''
def setNumParam():
    '''    public void setNumParam(final NumParam parameter, final double value)
    '''
def setStringParam():
    '''    public void setStringParam(final StringParam parameter, final String value)
    '''
def getIntParam():
    '''    public int getIntParam(final IntParam parameter)
    '''
def getLongParam():
    '''    public long getLongParam(final LongParam parameter)
    '''
def getBoolParam():
    '''    public boolean getBoolParam(final BoolParam parameter)
    '''
def getNumParam():
    '''    public double getNumParam(final NumParam parameter)
    '''
def getStringParam():
    '''    public String getStringParam(final StringParam parameter)
    '''
def getDefaultBoolParam():
    '''    public boolean getDefaultBoolParam(final BoolParam parameter)
    '''
def getDefaultIntParam():
    '''    public int getDefaultIntParam(final IntParam parameter)
    '''
def getDefaultLongParam():
    '''    public long getDefaultLongParam(final LongParam parameter)
    '''
def getDefaultNumParam():
    '''    public double getDefaultNumParam(final NumParam parameter)
    '''
def getDefaultStringParam():
    '''    public String getDefaultStringParam(final StringParam parameter)
    '''
def getMinIntParam():
    '''    public int getMinIntParam(final IntParam parameter)
    '''
def getMinLongParam():
    '''    public long getMinLongParam(final LongParam parameter)
    '''
def getMinNumParam():
    '''    public double getMinNumParam(final NumParam parameter)
    '''
def getMaxIntParam():
    '''    public int getMaxIntParam(final IntParam parameter)
    '''
def getMaxLongParam():
    '''    public long getMaxLongParam(final LongParam parameter)
    '''
def getMaxNumParam():
    '''    public double getMaxNumParam(final NumParam parameter)
    '''
def getParameterSet():
    '''    public IloCplex__ParameterSet getParameterSet()
    '''
def setParameterSet():
    '''    public void setParameterSet(final IloCplex__ParameterSet set)
    '''
def getStatus():
    '''    public Status getStatus()
    '''
def getCplexStatus():
    '''    public CplexStatus getCplexStatus()
    '''
def getCplexSubStatus():
    '''    public CplexStatus getCplexSubStatus()
    '''
def isPrimalFeasible():
    '''    public boolean isPrimalFeasible()
    '''
def isDualFeasible():
    '''    public boolean isDualFeasible()
    '''
def getAlgorithm():
    '''    public Algorithm getAlgorithm()
    '''
def getSubAlgorithm():
    '''    public Algorithm getSubAlgorithm()
    '''
def setDeleteMode():
    '''    public void setDeleteMode(final DeleteMode mode)
    '''
def getDeleteMode():
    '''    public DeleteMode getDeleteMode()
    '''
def populate():
    '''    public boolean populate()
    '''
def tuneParam():
    '''    public int tuneParam(final IloStringArrayBase filename, final IloCplex__ParameterSet fixedset)
    public int tuneParam()
    public int tuneParam(final IloCplex__ParameterSet fixedset)
    public int tuneParam(final IloStringArrayBase filename)
    '''
def refineConflict():
    '''    public boolean refineConflict(final IloConstraintArray cons, final IloNumArray prefs)
    '''
def refineMIPStartConflict():
    '''    public boolean refineMIPStartConflict(final int mipstartindex, final IloConstraintArray cons, final IloNumArray prefs)
    '''
def getConflict():
    '''    public IloCplex__ConflictStatusArray getConflict(final IloConstraintArray cons)
    public ConflictStatus getConflict(final IloConstraint con)
    '''
def getQuality():
    '''    public double getQuality(final Quality q, final IloNumVar var, final IloConstraint rng)
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
def setPriority():
    '''    public void setPriority(final IloNumVar var, final double pri)
    public void setPriority(final IloIntVar var, final double pri)
    '''
def setPriorities():
    '''    public void setPriorities(final IloNumVarArray var, final IloNumArray pri)
    public void setPriorities(final IloIntVarArray var, final IloNumArray pri)
    '''
def setDirection():
    '''    public void setDirection(final IloNumVar var, final BranchDirection dir)
    public void setDirection(final IloIntVar var, final BranchDirection dir)
    '''
def setDirections():
    '''    public void setDirections(final IloNumVarArray var, final IloCplex__BranchDirectionArray dir)
    public void setDirections(final IloIntVarArray var, final IloCplex__BranchDirectionArray dir)
    '''
def delPriority():
    '''    public void delPriority(final IloNumVar var)
    public void delPriority(final IloIntVar var)
    '''
def delPriorities():
    '''    public void delPriorities(final IloNumVarArray var)
    public void delPriorities(final IloIntVarArray var)
    '''
def delDirection():
    '''    public void delDirection(final IloNumVar var)
    public void delDirection(final IloIntVar var)
    '''
def delDirections():
    '''    public void delDirections(final IloNumVarArray var)
    public void delDirections(final IloIntVarArray var)
    '''
def getPriority():
    '''    public double getPriority(final IloNumVar var)
    public double getPriority(final IloIntVar var)
    '''
def getDirection():
    '''    public BranchDirection getDirection(final IloNumVar var)
    public BranchDirection getDirection(final IloIntVar var)
    '''
def getPriorities():
    '''    public void getPriorities(final IloNumArray pri, final IloNumVarArray var)
    public void getPriorities(final IloNumArray pri, final IloIntVarArray var)
    '''
def getDirections():
    '''    public void getDirections(final IloCplex__BranchDirectionArray dir, final IloNumVarArray var)
    public void getDirections(final IloCplex__BranchDirectionArray dir, final IloIntVarArray var)
    '''
def basicPresolve():
    '''    public void basicPresolve(final IloNumVarArray vars, final IloNumArray redlb, final IloNumArray redub, final IloRangeArray rngs, final SWIGTYPE_p_IloBoolArray redundant)
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
def freePresolve():
    '''    public void freePresolve()
    '''
def presolve():
    '''    public void presolve(final SWIGTYPE_p_IloCplex__Algorithm alg)
    '''
def getDiverging():
    '''    public IloExtractable getDiverging()
    '''
def getRay():
    '''    public void getRay(final IloNumArray vals, final IloNumVarArray vars)
    '''
def dualFarkas():
    '''    public double dualFarkas(final IloConstraintArray rng, final IloNumArray y)
    '''
def qpIndefCertificate():
    '''    public void qpIndefCertificate(final IloNumVarArray var, final IloNumArray x)
    public void qpIndefCertificate(final IloIntVarArray var, final IloNumArray x)
    '''
def protectVariables():
    '''    public void protectVariables(final IloNumVarArray var)
    public void protectVariables(final IloIntVarArray var)
    '''
def use():
    '''    public IloCplex__Aborter use(final IloCplex__Aborter abort)
    public IloCplex__Callback use(final IloCplex__Callback cb)
    '''
def getAborter():
    '''    public IloCplex__Aborter getAborter()
    '''
def remove():
    '''    public void remove(final IloCplex__Aborter abort)
    public void remove(final IloCplex__Callback cb)
    '''
def solve():
    '''    public boolean solve()
    public boolean solve(final IloCplex__Goal goal)
    '''
def setFormulationEpsValue():
    '''    public void setFormulationEpsValue(final double eps)
    '''
def getFormulationEpsValue():
    '''    public double getFormulationEpsValue()
    '''
def getSolnPoolMeanObjValue():
    '''    public double getSolnPoolMeanObjValue()
    '''
def getSolnPoolNsolns():
    '''    public int getSolnPoolNsolns()
    '''
def getSolnPoolNreplaced():
    '''    public int getSolnPoolNreplaced()
    '''
def delSolnPoolSoln():
    '''    public void delSolnPoolSoln(final int which)
    '''
def delSolnPoolSolns():
    '''    public void delSolnPoolSolns(final int begin, final int end)
    '''
def getCplexTime():
    '''    public double getCplexTime()
    '''
def getDetTime():
    '''    public double getDetTime()
    '''
def getNumCores():
    '''    public int getNumCores()
    '''
def GetVersion():
    '''    public static void GetVersion(final String buffer, final int len)
    '''
def GetAcademicMsg():
    '''    public static void GetAcademicMsg(final String buffer, final int len)
    '''
def GetPreviewMsg():
    '''    public static void GetPreviewMsg(final String buffer, final int len)
    '''
def Apply():
    '''    public static IloCplex__Goal Apply(final IloCplex cplex, final IloCplex__Goal goal, final IloCplex__NodeEvaluator eval)
    '''
def LimitSearch():
    '''    public static IloCplex__Goal LimitSearch(final IloCplex cplex, final IloCplex__Goal goal, final SWIGTYPE_p_SearchLimit limit)
    '''
def add():
    '''    public IloCplex__Callback add(final IloCplex__Callback cb)
    '''
def inUse():
    '''    public boolean inUse(final IloCplex__Callback cb)
    '''
def _readVMConfig():
    '''    public void _readVMConfig(final String f)
    '''
def _copyVMConfig():
    '''    public void _copyVMConfig(final String f)
    '''
def mySwigValue():
    '''    public int mySwigValue()
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
def swigValue():
    '''    public final int swigValue()
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
def toString():
    '''    public String toString()
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
def swigToEnum():
    '''    public static WriteLevelType swigToEnum(final int swigValue)
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
def WriteLevelType():
    '''    public WriteLevelType(final String swigName, final int swigValue)
    '''
def BasisStatus():
    '''    public BasisStatus(final String swigName, final int swigValue)
    '''
def CutType():
    '''    public CutType(final String swigName, final int swigValue)
    '''
def MIPStartEffort():
    '''    public MIPStartEffort(final String swigName, final int swigValue)
    '''
def NumParam():
    '''    public NumParam(final String swigName, final int swigValue)
    '''
def BoolParam():
    '''    public BoolParam(final String swigName, final int swigValue)
    '''
def IntParam():
    '''    public IntParam(final String swigName, final int swigValue)
    '''
def LongParam():
    '''    public LongParam(final String swigName, final int swigValue)
    '''
def StringParam():
    '''    public StringParam(final String swigName, final int swigValue)
    '''
def MIPEmphasisType():
    '''    public MIPEmphasisType(final String swigName, final int swigValue)
    '''
def OptimalityTargetType():
    '''    public OptimalityTargetType(final String swigName, final int swigValue)
    '''
def VariableSelect():
    '''    public VariableSelect(final String swigName, final int swigValue)
    '''
def NodeSelect():
    '''    public NodeSelect(final String swigName, final int swigValue)
    '''
def DistMIPRampupDuration():
    '''    public DistMIPRampupDuration(final String swigName, final int swigValue)
    '''
def PrimalPricing():
    '''    public PrimalPricing(final String swigName, final int swigValue)
    '''
def ConflictAlgorithm():
    '''    public ConflictAlgorithm(final String swigName, final int swigValue)
    '''
def Parallel_Mode():
    '''    public Parallel_Mode(final String swigName, final int swigValue)
    '''
def MIPsearch():
    '''    public MIPsearch(final String swigName, final int swigValue)
    '''
def DataCheckType():
    '''    public DataCheckType(final String swigName, final int swigValue)
    '''
def DualPricing():
    '''    public DualPricing(final String swigName, final int swigValue)
    '''
def BranchDirection():
    '''    public BranchDirection(final String swigName, final int swigValue)
    '''
def Algorithm():
    '''    public Algorithm(final String swigName, final int swigValue)
    '''
def Relaxation():
    '''    public Relaxation(final String swigName, final int swigValue)
    '''
def BendersStrategyType():
    '''    public BendersStrategyType(final String swigName, final int swigValue)
    '''
def CplexStatus():
    '''    public CplexStatus(final String swigName, final int swigValue)
    '''
def DeleteMode():
    '''    public DeleteMode(final String swigName, final int swigValue)
    '''
def TuningStatus():
    '''    public TuningStatus(final String swigName, final int swigValue)
    '''
def ConflictStatus():
    '''    public ConflictStatus(final String swigName, final int swigValue)
    '''
def Quality():
    '''    public Quality(final String swigName, final int swigValue)
    '''
def CutManagement():
    '''    public CutManagement(final String swigName, final int swigValue)
    '''
def FilterType():
    '''    public FilterType(final String swigName, final int swigValue)
    '''
