PARENT_WONUM = "String  \"_PARENT_WONUM\""
ORIGINAL_WONUM = "String  \"_WONUM\""
STARTTIME_DIFF = "String  \"_STARTTIME_DIFF\""
COUNT = "String  \"Count\""
EXPANDED = "String  \"Expanded\""
OFFSET_RECORD = "String  \"OffsetRecord\""
LEVEL = "String  \"Level\""
SCENARIO = "String  \"Scenario\""
IN_LOOP = "String  \"_IN_LOOP\""
ACCESSPANEL = "String  \"ACCESSPANEL\""
ZONE = "String  \"ZONE\""
def Activity():
    '''public Activity()
    public Activity(final String id)
    '''
def setParent():
    '''public void setParent(final Activity act)
    '''
def getParent():
    '''public Activity getParent()
    '''
def setWorkOrderId():
    '''public void setWorkOrderId(final Long workOrderId)
    '''
def getWorkOrderId():
    '''public Long getWorkOrderId()
    '''
def Items():
    '''public JSONArray Items()
    '''
def addRow():
    '''public Activity addRow()
    public Activity addRow(final Activity row)
    '''
def isInitialized():
    '''public boolean isInitialized()
    '''
def isModified():
    '''public boolean isModified()
    '''
def getDuration():
    '''public Double getDuration()
    '''
def getObjectID():
    '''public Long getObjectID()
    '''
def getStartTime():
    '''public Date getStartTime()
    '''
def getEndTime():
    '''public Date getEndTime()
    '''
def getModifiedProperties():
    '''public Iterator getModifiedProperties()
    '''
def getTimeInterval():
    '''public DateRange getTimeInterval()
    '''
def setID():
    '''public void setID(final String id)
    '''
def setName():
    '''public void setName(final String name)
    '''
def setParentID():
    '''public void setParentID(final String parentId)
    '''
def setObjectName():
    '''public void setObjectName(final String objectName)
    '''
def setRefObjectName():
    '''public void setRefObjectName(final String refObjectName)
    '''
def setObjectID():
    '''public void setObjectID(final Long objectID)
    '''
def setInitialized():
    '''public void setInitialized(final Boolean initialized)
    '''
def setStartTime():
    '''public void setStartTime(final Date startTime)
    '''
def setEndTime():
    '''public void setEndTime(final Date endTime)
    '''
def setReadOnly():
    '''public void setReadOnly(final Boolean readOnly)
    '''
def setDuration():
    '''public void setDuration(final Double duration)
    '''
def setModified():
    '''public void setModified(final boolean modified)
    '''
def setDataGroupName():
    '''public void setDataGroupName(final String dataGroupName)
    '''
def setUncommitted():
    '''public void setUncommitted(final boolean uncommitted)
    '''
def markStartTimeModified():
    '''public void markStartTimeModified()
    '''
def markEndTimeModified():
    '''public void markEndTimeModified()
    '''
def setTimeInterval():
    '''public void setTimeInterval(final Date activityStart, final Date activityEnd)
    '''
def getId():
    '''public String getId()
    '''
def getProperty():
    '''public Object getProperty(final String key)
    '''
def getInt():
    '''public int getInt(final String prop)
    '''
def getLong():
    '''public long getLong(final String prop)
    '''
def getFloat():
    '''public float getFloat(final String prop)
    public Double getFloat()
    '''
def getDouble():
    '''public double getDouble(final String prop)
    '''
def getBoolean():
    '''public boolean getBoolean(final String prop)
    '''
def getString():
    '''public String getString(final String prop)
    public String getString(final String prop, final String defValue)
    '''
def getDate():
    '''public Date getDate(final String prop)
    '''
def getObjectName():
    '''public String getObjectName()
    '''
def getFromConstraints():
    '''public List<Constraint> getFromConstraints()
    '''
def getToConstraints():
    '''public List<Constraint> getToConstraints()
    '''
def getApplinkMap():
    '''public HashMap<String, HashMap<String, String>> getApplinkMap()
    '''
def setApplinkMap():
    '''public void setApplinkMap(final HashMap<String, HashMap<String, String>> applinkMap)
    '''
def setAncestors():
    '''public void setAncestors(final List<Activity> ancestors)
    '''
def getAncestors():
    '''public List<Activity> getAncestors()
    '''
def getID():
    '''public String getID()
    '''
def setProperty():
    '''public Object setProperty(final String prop, final Object value)
    public Object setProperty(final String prop, final Object value, final boolean ignoreChangeTracking)
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
def hashCode():
    '''public int hashCode()
    '''
def getPropertyNames():
    '''public Collection<String> getPropertyNames()
    '''
def getName():
    '''public String getName()
    '''
def getEarlyStart():
    '''public Date getEarlyStart()
    '''
def getEarlyFinish():
    '''public Date getEarlyFinish()
    '''
def getLateStart():
    '''public Date getLateStart()
    '''
def getLateFinish():
    '''public Date getLateFinish()
    '''
def isCritical():
    '''public Boolean isCritical()
    '''
def setEarlyStart():
    '''public void setEarlyStart(final Date earlyStart)
    '''
def setEarlyFinish():
    '''public void setEarlyFinish(final Date earlyFinish)
    '''
def setLateStart():
    '''public void setLateStart(final Date lateStart)
    '''
def setLateFinish():
    '''public void setLateFinish(final Date lateFinish)
    '''
def setFloat():
    '''public void setFloat(final Double floatValue)
    '''
def setCritical():
    '''public void setCritical(final Boolean critical)
    '''
def addLeftIconClass():
    '''public void addLeftIconClass(final String className)
    public void addLeftIconClass(final String className, final String tip)
    '''
def addLeftIconClick():
    '''public void addLeftIconClick(final String eventName)
    '''
def addRightIconClass():
    '''public void addRightIconClass(final String className)
    public void addRightIconClass(final String className, final String tip)
    '''
def addRightIconClick():
    '''public void addRightIconClick(final String eventName)
    '''
def showWorklogIcon():
    '''public boolean showWorklogIcon()
    '''
