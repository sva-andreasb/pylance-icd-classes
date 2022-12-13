PROPERTY_LOADDATAVALUE = "String  \"loadDataValue\""
PROPERTY_PMLOADDATAVALUE = "String  \"pmloadDataValue\""
PROPERTY_LOADLABORHRS = "String  \"loadLaborHrs\""
PROPERTY_LOADTOOLHRS = "String  \"loadToolHrs\""
PROPERTY_LOADTOOLQTY = "String  \"loadToolQty\""
PROPERTY_LOADZONECAPACITY = "String  \"loadZoneCapacity\""
def MXReservation():
    '''    public MXReservation(final IlvResource resource, final IlvActivity activity)
    '''
def setProperty():
    '''    public Object setProperty(final String property, final Object value)
    public Object setProperty(final String property, final Object value, final boolean ignoreChangeTracking)
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
def getMXActivity():
    '''    public IMXActivity getMXActivity()
    '''
def getMXResource():
    '''    public IMXResource getMXResource()
    '''
def createReservation():
    '''    public MXReservation createReservation(final MXResource resource, final MXActivity activity)
    '''
