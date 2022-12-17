COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloRelaxedRequirementImpl\n\n
    (final IloProcessingService ps, final IloExecutionScope scope, final IloTaskConfig config)\n
    (final IloGoalBreakdownImpl parent, final IloRow row)\n
    (final IloRow settingsRow)\n
    (final IloRequirementImpl parent, final IloRow row)\n
    (final IloRequirementImpl parent, final IloRow row)\n
    '''
def getObjective():
    '''returns double\n\n
    getObjective()\n
    '''
def hasSolution():
    '''returns boolean\n\n
    hasSolution()\n
    '''
def isOptimal():
    '''returns boolean\n\n
    isOptimal()\n
    '''
def getGoalIds():
    '''returns String[]\n\n
    getGoalIds()\n
    '''
def getGoal():
    '''returns IloGoal\n\n
    getGoal(final String goalId)\n
    '''
def hasRelaxation():
    '''returns boolean\n\n
    hasRelaxation()\n
    '''
def getModifiedRequirements():
    '''returns Collection<IloRequirement>\n\n
    getModifiedRequirements()\n
    '''
def getRelaxedRequirement():
    '''returns IloRequirement\n\n
    getRelaxedRequirement(final String requirementId)\n
    getRelaxedRequirement()\n
    '''
def getRuleCategoryRoot():
    '''returns IloRuleFolder\n\n
    getRuleCategoryRoot(final String ruleCategoryId)\n
    getRuleCategoryRoot()\n
    '''
def getAllowRelaxations():
    '''returns boolean\n\n
    getAllowRelaxations()\n
    '''
def getTimeLimit():
    '''returns long\n\n
    getTimeLimit()\n
    '''
def setAllowRelaxations():
    '''returns None\n\n
    setAllowRelaxations(final boolean allowRelaxations)\n
    '''
def setTimeLimit():
    '''returns None\n\n
    setTimeLimit(final long timeLimit)\n
    '''
def acceptVisitor():
    '''returns None\n\n
    acceptVisitor(final IloJobIOVisitor<?> visitor)\n
    '''
def getDetails():
    '''returns TaskDetails\n\n
    getDetails()\n
    '''
def getParent():
    '''returns IloRequirement\n\n
    getParent()\n
    getParent()\n
    '''
def getExplanation():
    '''returns String\n\n
    getExplanation()\n
    getExplanation()\n
    '''
def getValue():
    '''returns double\n\n
    getValue()\n
    getValue()\n
    '''
def getChildren():
    '''returns Collection<IloRequirement>\n\n
    getChildren()\n
    getChildren()\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    getId()\n
    '''
def getWeight():
    '''returns double\n\n
    getWeight()\n
    '''
def isActive():
    '''returns boolean\n\n
    isActive()\n
    isActive()\n
    '''
def setWeight():
    '''returns None\n\n
    setWeight(final double weight)\n
    '''
def setActive():
    '''returns None\n\n
    setActive(final boolean active)\n
    setActive(final boolean active, final boolean applyToChildren)\n
    '''
def getConstraintMin():
    '''returns double\n\n
    getConstraintMin()\n
    '''
def getConstraintMax():
    '''returns double\n\n
    getConstraintMax()\n
    '''
def setConstraintMin():
    '''returns None\n\n
    setConstraintMin(final double min)\n
    '''
def setConstraintMax():
    '''returns None\n\n
    setConstraintMax(final double max)\n
    '''
def clearConstraintMin():
    '''returns None\n\n
    clearConstraintMin()\n
    '''
def clearConstraintMax():
    '''returns None\n\n
    clearConstraintMax()\n
    '''
def setConstraintPriority():
    '''returns None\n\n
    setConstraintPriority(final IloPriority priority)\n
    '''
def getConstraintPriority():
    '''returns IloPriority\n\n
    getConstraintPriority()\n
    '''
def getRelaxedRequirementForConstraintMin():
    '''returns IloRequirement\n\n
    getRelaxedRequirementForConstraintMin()\n
    '''
def getRelaxedRequirementForConstraintMax():
    '''returns IloRequirement\n\n
    getRelaxedRequirementForConstraintMax()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def getModifiedChildren():
    '''returns Collection<IloRequirement>\n\n
    getModifiedChildren()\n
    '''
def getAssociatedRule():
    '''returns IloRule\n\n
    getAssociatedRule()\n
    getAssociatedRule()\n
    '''
def getModifiedPriority():
    '''returns IloPriority\n\n
    getModifiedPriority()\n
    '''
def getRelaxationMessage():
    '''returns String\n\n
    getRelaxationMessage()\n
    '''
def changePriority():
    '''returns None\n\n
    changePriority(final IloPriority priority, final boolean applyToChildren)\n
    '''
def resetPriority():
    '''returns None\n\n
    resetPriority(final boolean applyToChildren)\n
    '''
def getPriority():
    '''returns IloPriority\n\n
    getPriority()\n
    getPriority()\n
    '''
def getAssociatedGoal():
    '''returns IloGoal\n\n
    getAssociatedGoal()\n
    '''
def getValues():
    '''returns Serializable[]\n\n
    getValues()\n
    '''
def setValues():
    '''returns None\n\n
    setValues(final Serializable[] values)\n
    '''
def delete():
    '''returns None\n\n
    delete()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getParentFolder():
    '''returns IloRuleFolder\n\n
    getParentFolder()\n
    '''
def setPriority():
    '''returns None\n\n
    setPriority(final IloPriority priority, final boolean applyToChildren)\n
    '''
