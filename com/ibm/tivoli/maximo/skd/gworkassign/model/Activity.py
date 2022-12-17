PARENT_WOGROUP = "String  \"_PARENT_WONUM\""
PARENT_WONUM = "String  \"WOPARENT\""
ORIGINAL_WONUM = "String  \"_WONUM\""
ISASSIGNMENT = "String  \"ISASSIGNMENT\""
UNPLANNEDWORK = "String  \"UNPLANNEDWORK\""
CREWWORKGROUP = "String  \"CREWWORKGROUP\""
PERSONGROUP = "String  \"PERSONGROUP\""
WORKDAY = "String  \"_WorkDay\""
def ():
    '''returns Activity\n\n
    ()\n
    (final String id)\n
    '''
def setParent():
    '''returns None\n\n
    setParent(final Resource res)\n
    '''
def getParent():
    '''returns Resource\n\n
    getParent()\n
    '''
def setWorkOrderId():
    '''returns None\n\n
    setWorkOrderId(final Long workOrderId)\n
    '''
def getWorkOrderId():
    '''returns Long\n\n
    getWorkOrderId()\n
    '''
def setAssignmentId():
    '''returns None\n\n
    setAssignmentId(final Long assignmentId)\n
    '''
def getAssignmentId():
    '''returns Long\n\n
    getAssignmentId()\n
    '''
def setParentAssignmentId():
    '''returns None\n\n
    setParentAssignmentId(final Long parentassignId)\n
    '''
def getParentAssignmentId():
    '''returns Long\n\n
    getParentAssignmentId()\n
    '''
def isModified():
    '''returns boolean\n\n
    isModified()\n
    '''
def getDuration():
    '''returns Double\n\n
    getDuration()\n
    '''
def setObjectName():
    '''returns None\n\n
    setObjectName(final String objectName)\n
    '''
def setRefObjectName():
    '''returns None\n\n
    setRefObjectName(final String refObjectName)\n
    '''
def setObjectID():
    '''returns None\n\n
    setObjectID(final Long objectID)\n
    '''
def getStartTime():
    '''returns Date\n\n
    getStartTime()\n
    '''
def getEndTime():
    '''returns Date\n\n
    getEndTime()\n
    '''
def getModifiedProperties():
    '''returns Iterator\n\n
    getModifiedProperties()\n
    '''
def getTimeInterval():
    '''returns DateRange\n\n
    getTimeInterval()\n
    '''
def setID():
    '''returns None\n\n
    setID(final String id)\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def setParentID():
    '''returns None\n\n
    setParentID(final String parentId)\n
    '''
def setStartTime():
    '''returns None\n\n
    setStartTime(final Date startTime)\n
    '''
def setEndTime():
    '''returns None\n\n
    setEndTime(final Date endTime)\n
    '''
def setDuration():
    '''returns None\n\n
    setDuration(final Double duration)\n
    '''
def setModified():
    '''returns None\n\n
    setModified(final boolean modified)\n
    '''
def setUncommitted():
    '''returns None\n\n
    setUncommitted(final boolean uncommitted)\n
    '''
def markStartTimeModified():
    '''returns None\n\n
    markStartTimeModified()\n
    '''
def markEndTimeModified():
    '''returns None\n\n
    markEndTimeModified()\n
    '''
def setReadOnly():
    '''returns None\n\n
    setReadOnly(final Boolean readOnly)\n
    '''
def setTimeInterval():
    '''returns None\n\n
    setTimeInterval(final Date activityStart, final Date activityEnd)\n
    '''
def getId():
    '''returns String\n\n
    getId()\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String key)\n
    '''
def getInt():
    '''returns int\n\n
    getInt(final String prop)\n
    '''
def getLong():
    '''returns long\n\n
    getLong(final String prop)\n
    '''
def getFloat():
    '''returns Double\n\n
    getFloat(final String prop)\n
    getFloat()\n
    '''
def getDouble():
    '''returns double\n\n
    getDouble(final String prop)\n
    '''
def getBoolean():
    '''returns boolean\n\n
    getBoolean(final String prop)\n
    '''
def getString():
    '''returns String\n\n
    getString(final String prop)\n
    getString(final String prop, final String defValue)\n
    '''
def getDate():
    '''returns Date\n\n
    getDate(final String prop)\n
    '''
def getObjectName():
    '''returns String\n\n
    getObjectName()\n
    '''
def getObjectId():
    '''returns long\n\n
    getObjectId()\n
    '''
def getID():
    '''returns String\n\n
    getID()\n
    '''
def setProperty():
    '''returns Object\n\n
    setProperty(final String prop, final Object value)\n
    setProperty(final String prop, final Object value, final boolean ignoreChangeTracking)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def getPropertyNames():
    '''returns Collection<String>\n\n
    getPropertyNames()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getEarlyStart():
    '''returns Date\n\n
    getEarlyStart()\n
    '''
def getEarlyFinish():
    '''returns Date\n\n
    getEarlyFinish()\n
    '''
def getLateStart():
    '''returns Date\n\n
    getLateStart()\n
    '''
def getLateFinish():
    '''returns Date\n\n
    getLateFinish()\n
    '''
def isCritical():
    '''returns Boolean\n\n
    isCritical()\n
    '''
def isParentAssign():
    '''returns boolean\n\n
    isParentAssign()\n
    '''
def setEarlyStart():
    '''returns None\n\n
    setEarlyStart(final Date earlyStart)\n
    '''
def setEarlyFinish():
    '''returns None\n\n
    setEarlyFinish(final Date earlyFinish)\n
    '''
def setLateStart():
    '''returns None\n\n
    setLateStart(final Date lateStart)\n
    '''
def setLateFinish():
    '''returns None\n\n
    setLateFinish(final Date lateFinish)\n
    '''
def setFloat():
    '''returns None\n\n
    setFloat(final Double floatValue)\n
    '''
def setCritical():
    '''returns None\n\n
    setCritical(final Boolean critical)\n
    '''
def setApplinkMap():
    '''returns None\n\n
    setApplinkMap(final HashMap<String, HashMap<String, String>> applinkMap)\n
    '''
def setDataGroupName():
    '''returns None\n\n
    setDataGroupName(final String dataGroupName)\n
    '''
def setParentAssign():
    '''returns None\n\n
    setParentAssign(final boolean isParentAssign)\n
    '''
def addLeftIconClass():
    '''returns None\n\n
    addLeftIconClass(final String className)\n
    addLeftIconClass(final String className, final String tip)\n
    '''
def addLeftIconClick():
    '''returns None\n\n
    addLeftIconClick(final String eventName)\n
    '''
def addRightIconClass():
    '''returns None\n\n
    addRightIconClass(final String className)\n
    addRightIconClass(final String className, final String tip)\n
    '''
def addRightIconClick():
    '''returns None\n\n
    addRightIconClick(final String eventName)\n
    '''
def showWorklogIcon():
    '''returns boolean\n\n
    showWorklogIcon()\n
    '''
