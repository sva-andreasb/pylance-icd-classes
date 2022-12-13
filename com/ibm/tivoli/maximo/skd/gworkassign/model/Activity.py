PARENT_WOGROUP = "String  \"_PARENT_WONUM\""
PARENT_WONUM = "String  \"WOPARENT\""
ORIGINAL_WONUM = "String  \"_WONUM\""
ISASSIGNMENT = "String  \"ISASSIGNMENT\""
UNPLANNEDWORK = "String  \"UNPLANNEDWORK\""
CREWWORKGROUP = "String  \"CREWWORKGROUP\""
PERSONGROUP = "String  \"PERSONGROUP\""
WORKDAY = "String  \"_WorkDay\""
def Activity():
    '''    public Activity()
    public Activity(final String id)
    '''
def setParent():
    '''    public void setParent(final Resource res)
    '''
def getParent():
    '''    public Resource getParent()
    '''
def setWorkOrderId():
    '''    public void setWorkOrderId(final Long workOrderId)
    '''
def getWorkOrderId():
    '''    public Long getWorkOrderId()
    '''
def setAssignmentId():
    '''    public void setAssignmentId(final Long assignmentId)
    '''
def getAssignmentId():
    '''    public Long getAssignmentId()
    '''
def setParentAssignmentId():
    '''    public void setParentAssignmentId(final Long parentassignId)
    '''
def getParentAssignmentId():
    '''    public Long getParentAssignmentId()
    '''
def isModified():
    '''    public boolean isModified()
    '''
def getDuration():
    '''    public Double getDuration()
    '''
def setObjectName():
    '''    public void setObjectName(final String objectName)
    '''
def setRefObjectName():
    '''    public void setRefObjectName(final String refObjectName)
    '''
def setObjectID():
    '''    public void setObjectID(final Long objectID)
    '''
def getStartTime():
    '''    public Date getStartTime()
    '''
def getEndTime():
    '''    public Date getEndTime()
    '''
def getModifiedProperties():
    '''    public Iterator getModifiedProperties()
    '''
def getTimeInterval():
    '''    public DateRange getTimeInterval()
    '''
def setID():
    '''    public void setID(final String id)
    '''
def setName():
    '''    public void setName(final String name)
    '''
def setParentID():
    '''    public void setParentID(final String parentId)
    '''
def setStartTime():
    '''    public void setStartTime(final Date startTime)
    '''
def setEndTime():
    '''    public void setEndTime(final Date endTime)
    '''
def setDuration():
    '''    public void setDuration(final Double duration)
    '''
def setModified():
    '''    public void setModified(final boolean modified)
    '''
def setUncommitted():
    '''    public void setUncommitted(final boolean uncommitted)
    '''
def markStartTimeModified():
    '''    public void markStartTimeModified()
    '''
def markEndTimeModified():
    '''    public void markEndTimeModified()
    '''
def setReadOnly():
    '''    public void setReadOnly(final Boolean readOnly)
    '''
def setTimeInterval():
    '''    public void setTimeInterval(final Date activityStart, final Date activityEnd)
    '''
def getId():
    '''    public String getId()
    '''
def getProperty():
    '''    public Object getProperty(final String key)
    '''
def getInt():
    '''    public int getInt(final String prop)
    '''
def getLong():
    '''    public long getLong(final String prop)
    '''
def getFloat():
    '''    public float getFloat(final String prop)
    public Double getFloat()
    '''
def getDouble():
    '''    public double getDouble(final String prop)
    '''
def getBoolean():
    '''    public boolean getBoolean(final String prop)
    '''
def getString():
    '''    public String getString(final String prop)
    public String getString(final String prop, final String defValue)
    '''
def getDate():
    '''    public Date getDate(final String prop)
    '''
def getObjectName():
    '''    public String getObjectName()
    '''
def getObjectId():
    '''    public long getObjectId()
    '''
def getID():
    '''    public String getID()
    '''
def setProperty():
    '''    public Object setProperty(final String prop, final Object value)
    public Object setProperty(final String prop, final Object value, final boolean ignoreChangeTracking)
    '''
def equals():
    '''    public boolean equals(final Object o)
    '''
def hashCode():
    '''    public int hashCode()
    '''
def getPropertyNames():
    '''    public Collection<String> getPropertyNames()
    '''
def getName():
    '''    public String getName()
    '''
def getEarlyStart():
    '''    public Date getEarlyStart()
    '''
def getEarlyFinish():
    '''    public Date getEarlyFinish()
    '''
def getLateStart():
    '''    public Date getLateStart()
    '''
def getLateFinish():
    '''    public Date getLateFinish()
    '''
def isCritical():
    '''    public Boolean isCritical()
    '''
def isParentAssign():
    '''    public boolean isParentAssign()
    '''
def setEarlyStart():
    '''    public void setEarlyStart(final Date earlyStart)
    '''
def setEarlyFinish():
    '''    public void setEarlyFinish(final Date earlyFinish)
    '''
def setLateStart():
    '''    public void setLateStart(final Date lateStart)
    '''
def setLateFinish():
    '''    public void setLateFinish(final Date lateFinish)
    '''
def setFloat():
    '''    public void setFloat(final Double floatValue)
    '''
def setCritical():
    '''    public void setCritical(final Boolean critical)
    '''
def getApplinkMap():
    '''    public HashMap<String, HashMap<String, String>> getApplinkMap()
    '''
def setApplinkMap():
    '''    public void setApplinkMap(final HashMap<String, HashMap<String, String>> applinkMap)
    '''
def setDataGroupName():
    '''    public void setDataGroupName(final String dataGroupName)
    '''
def setParentAssign():
    '''    public void setParentAssign(final boolean isParentAssign)
    '''
def addLeftIconClass():
    '''    public void addLeftIconClass(final String className)
    public void addLeftIconClass(final String className, final String tip)
    '''
def addLeftIconClick():
    '''    public void addLeftIconClick(final String eventName)
    '''
def addRightIconClass():
    '''    public void addRightIconClass(final String className)
    public void addRightIconClass(final String className, final String tip)
    '''
def addRightIconClick():
    '''    public void addRightIconClick(final String eventName)
    '''
def showWorklogIcon():
    '''    public boolean showWorklogIcon()
    '''
