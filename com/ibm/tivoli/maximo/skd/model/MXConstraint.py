PROPERTY_FROMACTIVITY = "String  \"fromActivity\""
PROPERTY_TOACTIVITY = "String  \"toActivity\""
PROPERTY_SAVEDCONSTRAINTTYPE = "String  \"_SAVEDCONSTRAINTTYPE\""
PROPERTY_NEWCONSTRAINT = "String  \"_NEWCONSTRAINT\""
PROPERTY_CONSTRAINTCHANGEID = "String  \"_CONSTRAINTCHANGEID\""
PROPERTY_LEADLAGHOURS = "String  \"LEADLAGHOURS\""
PROPERTY_OPTSPLIT = "String  \"OPTSPLIT\""
PROPERTY_OPTIMIZE = "String  \"OPTIMIZE\""
PROPERTY_OPERATION = "String  \"OPERATION\""
OPERATION_CONSTRAINTCHANGED = "String  \"CONSTRAINTCHANGED\""
OPERATION_CONSTRAINTREMOVED = "String  \"CONSTRAINTREMOVED\""
OPERATION_CONSTRAINTINSERTED = "String  \"CONSTRAINTINSERTED\""
PROPERTY_PREDECESSOR_WONUM = "String  \"PREDWONUM\""
PROPERTY_PREDECESSOR_DESCRIPTION = "String  \"PREDDESC\""
PROPERTY_SUCCESSOR_WONUM = "String  \"SUCCWONUM\""
PROPERTY_SUCCESSOR_DESCRIPTION = "String  \"SUCCDESC\""
def ():
    '''returns MXConstraint\n\n
    (final IlvActivity fromActivity, final IlvActivity toActivity, final IlvConstraintType type)\n
    '''
def setProperty():
    '''returns Object\n\n
    setProperty(final String property, final Object value)\n
    '''
def getModifiedProperties():
    '''returns Iterator\n\n
    getModifiedProperties()\n
    '''
def isModified():
    '''returns boolean\n\n
    isModified()\n
    '''
def getObjectName():
    '''returns String\n\n
    getObjectName()\n
    '''
def getObjectId():
    '''returns long\n\n
    getObjectId()\n
    '''
def getApplinkObject():
    '''returns String\n\n
    getApplinkObject(final String propertyName)\n
    '''
def getFromActivityObject():
    '''returns IMXActivity\n\n
    getFromActivityObject()\n
    '''
def getToActivityObject():
    '''returns IMXActivity\n\n
    getToActivityObject()\n
    '''
def setLeadLagHours():
    '''returns None\n\n
    setLeadLagHours(final Double leadLagHours)\n
    '''
def setOptimize():
    '''returns None\n\n
    setOptimize(final Boolean optimize)\n
    '''
def setOptsplit():
    '''returns None\n\n
    setOptsplit(final Boolean optsplit)\n
    '''
def createConstraint():
    '''returns MXConstraint\n\n
    createConstraint(final MXActivity fromActivity, final MXActivity toActivity, final IlvConstraintType type)\n
    '''
