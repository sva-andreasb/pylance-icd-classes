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
def MXConstraint():
    '''public MXConstraint(final IlvActivity fromActivity, final IlvActivity toActivity, final IlvConstraintType type)
    '''
def setProperty():
    '''public Object setProperty(final String property, final Object value)
    '''
def getModifiedProperties():
    '''public Iterator getModifiedProperties()
    '''
def isModified():
    '''public boolean isModified()
    '''
def getObjectName():
    '''public String getObjectName()
    '''
def getObjectId():
    '''public long getObjectId()
    '''
def getApplinkObject():
    '''public String getApplinkObject(final String propertyName)
    '''
def getApplinkAppList():
    '''public HashMap<String, String> getApplinkAppList(final String propertyName)
    '''
def getFromActivityObject():
    '''public IMXActivity getFromActivityObject()
    '''
def getToActivityObject():
    '''public IMXActivity getToActivityObject()
    '''
def setLeadLagHours():
    '''public void setLeadLagHours(final Double leadLagHours)
    '''
def setOptimize():
    '''public void setOptimize(final Boolean optimize)
    '''
def setOptsplit():
    '''public void setOptsplit(final Boolean optsplit)
    '''
def createConstraint():
    '''public MXConstraint createConstraint(final MXActivity fromActivity, final MXActivity toActivity, final IlvConstraintType type)
    '''
