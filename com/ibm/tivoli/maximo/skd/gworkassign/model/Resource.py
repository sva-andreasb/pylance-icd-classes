PROPERTY_ALLOCATION = "String  \"ALLOCATION\""
PROPERTY_SKILL = "String  \"SKILLLEVEL\""
PROPERTY_DAY = "String  \"DAY\""
PROPERTY_UNASSIGNHOURSDAY = "String  \"UNASSIGNHOURSDAY\""
PROPERTY_WORKHOURSDAY = "String  \"WORKHOURSDAY\""
PROPERTY_CREWWORKGROUP = "String  \"CREWWORKGROUP\""
PROPERTY_HASWORKPERIOD = "String  \"HASWORKPERIOD\""
PROPERTY_FULLDAY = "String  \"FULLDAY\""
PROPERTY_EXTERNALASSIGNMENTS = "String  \"EXTERNALASSIGNMENTS\""
PROPERTY_PRIMARYCRAFT = "String  \"PRIMARYCRAFT\""
PROPERTY_SECONDARYCRAFTS = "String  \"SECONDARYCRAFTS\""
PROPERTY_MODAVAILFONTCOLOR = "String  \"MODAVAILFONTCOLOR\""
PROPERTY_MODAVAILCOLOR = "String  \"MODAVAILCOLOR\""
PROPERTY_SHIFTINFO = "String  \"SHIFTINFO\""
PROPERTY_STATICSHIFTINFO = "String  \"STATICSHIFTINFO\""
PROPERTY_MODAVAILINFO = "String  \"MODAVAILINFO\""
PROPERTY_NAME = "String  \"RESOURCENAME\""
PROPERTY_PATTERNDAYNAME = "String  \"PATTERNDAYNAME\""
PROPERTY_PATTERNDAYDESC = "String  \"PATTERNDAYDESC\""
PROPERTY_WORKLOCATION = "String  \"WORKLOCATION\""
PROPERTY_CREWASSIGNMENT = "String  \"CREWASSIGNMENT\""
AVAIL = "String  \"AVAIL\""
FULLYBOOKED = "String  \"FULLYBOOKED\""
OVERBOOKED = "String  \"OVERBOOKED\""
NONWORKTIME = "String  \"NONWORKTIME\""
def Resource():
    '''    public Resource()
    '''
def getProperty():
    '''    public Object getProperty(final String prop)
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
def setProperty():
    '''    public Object setProperty(final String prop, final Object value)
    public Object setProperty(final String prop, final Object value, final boolean ignoreChangeTracking)
    '''
def getID():
    '''    public String getID()
    '''
def getUserData():
    '''    public <T> T getUserData(final String key)
    '''
def setUserData():
    '''    public <T> void setUserData(final String key, final T data)
    '''
def getQuantity():
    '''    public float getQuantity()
    '''
def getPropertyNames():
    '''    public Collection<String> getPropertyNames()
    '''
def setObjectName():
    '''    public void setObjectName(final String objectName)
    '''
def setRefObjectName():
    '''    public void setRefObjectName(final String refObjectName)
    '''
def getObjectName():
    '''    public String getObjectName()
    '''
def getRefObjectName():
    '''    public String getRefObjectName()
    '''
def put():
    '''    public Object put(final Object key, final Object value)
    '''
def remove():
    '''    public Object remove(final Object key)
    '''
