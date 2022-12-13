PROPERTY_FROMACTIVITY = "String  fromActivity""
PROPERTY_TOACTIVITY = "String  toActivity""
PROPERTY_SAVEDCONSTRAINTTYPE = "String  _SAVEDCONSTRAINTTYPE""
PROPERTY_NEWCONSTRAINT = "String  _NEWCONSTRAINT""
PROPERTY_CONSTRAINTCHANGEID = "String  _CONSTRAINTCHANGEID""
PROPERTY_LEADLAGHOURS = "String  LEADLAGHOURS""
PROPERTY_OPTSPLIT = "String  OPTSPLIT""
PROPERTY_OPTIMIZE = "String  OPTIMIZE""
PROPERTY_OPERATION = "String  OPERATION""
OPERATION_CONSTRAINTCHANGED = "String  CONSTRAINTCHANGED""
OPERATION_CONSTRAINTREMOVED = "String  CONSTRAINTREMOVED""
OPERATION_CONSTRAINTINSERTED = "String  CONSTRAINTINSERTED""
PROPERTY_PREDECESSOR_WONUM = "String  PREDWONUM""
PROPERTY_PREDECESSOR_DESCRIPTION = "String  PREDDESC""
PROPERTY_SUCCESSOR_WONUM = "String  SUCCWONUM""
PROPERTY_SUCCESSOR_DESCRIPTION = "String  SUCCDESC""
def MXConstraint():
'''public MXConstraint(final IlvActivity fromActivity, final IlvActivity toActivity, final IlvConstraintType type)
'''
pass
def setProperty():
'''public Object setProperty(final String property, final Object value)
'''
pass
def getModifiedProperties():
'''public Iterator getModifiedProperties()
'''
pass
def isModified():
'''public boolean isModified()
'''
pass
def getObjectName():
'''public String getObjectName()
'''
pass
def getObjectId():
'''public long getObjectId()
'''
pass
def getApplinkObject():
'''public String getApplinkObject(final String propertyName)
'''
pass
def getApplinkAppList():
'''public HashMap<String, String> getApplinkAppList(final String propertyName)
'''
pass
def getFromActivityObject():
'''public IMXActivity getFromActivityObject()
'''
pass
def getToActivityObject():
'''public IMXActivity getToActivityObject()
'''
pass
def setLeadLagHours():
'''public void setLeadLagHours(final Double leadLagHours)
'''
pass
def setOptimize():
'''public void setOptimize(final Boolean optimize)
'''
pass
def setOptsplit():
'''public void setOptsplit(final Boolean optsplit)
'''
pass
def createConstraint():
'''public MXConstraint createConstraint(final MXActivity fromActivity, final MXActivity toActivity, final IlvConstraintType type)
'''
pass
