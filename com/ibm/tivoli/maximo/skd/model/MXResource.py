PROPERTY_CRAFT = "String  \"CRAFT\""
PROPERTY_PARENTID = "String  \"_PARENTID\""
PROPERTY_OLDPARENTID = "String  \"_OLDPARENTID\""
PROPERTY_DUMMY = "String  \"_DUMMY\""
PROPERTY_RESOURCEAVAILABILITY = "String  \"_RESOURCEAVAILABILITY\""
PROPERTY_NONWORKHRS = "String  \"_NONWORKHRS\""
PROPERTY_WORKHRS = "String  \"_WORKHRS\""
PROPERTY_SUMMEDVIEW = "String  \"_SUMMEDVIEW\""
PROPERTY_LABORSHIFTNUM = "String  \"_LABORSHIFTNUM\""
PROPERTY_LABORCALNUM = "String  \"_LABORCALNUM\""
PROPERTY_LABORDEFAULTSKILL = "String  \"_LABORDEFAULTSKILL\""
PROPERTY_CRAFTSKILLMAP = "String  \"_CRAFTSKILLMAP\""
PROPERTY_CRAFTSKILLRANK = "String  \"_CRAFTSKILLRANK\""
PROPERTY_DEFAULTVENDOR = "String  \"_DEFAULTVENDOR\""
PROPERTY_DEFAULTCONTRACTNUM = "String  \"_DEFAULTCONTRACTNUM\""
PROPERTY_ROTTOOLAVAILABILITY = "String  \"_ROTTOOLAVAILABILITY\""
PROPERTY_PMROTTOOLAVAILABILITY = "String  \"_PMROTTOOLAVAILABILITY\""
PROPERTY_REPAIRLOC = "String  \"REPAIRLOC\""
PROPERTY_SHIFTNUM = "String  \"SHIFTNUM\""
PROPERTY_CREWWORKGROUP = "String  \"_CREWWORKGROUP\""
PROPERTY_SECONDARYASSIGNLOC = "String  \"SECONDARYASSIGNLOC\""
PROPERTY_ZONEAVAILABILITY = "String  \"_ZONEAVAILABILITY\""
USERDATA_CHARTDATA = "String  \"CHARTDATA\""
USERDATA_AVAILSHIFTBUCKET = "String  \"AVAILSHIFTBUCKET\""
USERDATA_LOADSHIFTBUCKET = "String  \"USERDATA_LOADSHIFTBUCKET\""
PROPERTY_TIMEBASED = "String  \"_TIMEBASED\""
def MXResource():
    '''    public MXResource(final String id, final String name, final float quantity)
    public MXResource(final String id, final String name)
    '''
def setProperty():
    '''    public Object setProperty(final String property, final Object value, final boolean ignoreChangeTracking)
    public Object setProperty(final String property, final Object value)
    '''
def getModifiedProperties():
    '''    public Iterator getModifiedProperties()
    '''
def isModified():
    '''    public boolean isModified()
    '''
def getObjectName():
    '''    public String getObjectName()
    '''
def getObjectId():
    '''    public long getObjectId()
    '''
def getApplinkObject():
    '''    public String getApplinkObject(final String propertyName)
    '''
def getApplinkAppList():
    '''    public HashMap<String, String> getApplinkAppList(final String propertyName)
    '''
def setUserData():
    '''    public void setUserData(final String key, final Object value)
    '''
def getUserData():
    '''    public <T> T getUserData(final String key)
    '''
def getInt():
    '''    public int getInt(final String prop)
    '''
def getLong():
    '''    public long getLong(final String prop)
    '''
def getFloat():
    '''    public float getFloat(final String prop)
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
def createResource():
    '''    public MXResource createResource()
    '''
