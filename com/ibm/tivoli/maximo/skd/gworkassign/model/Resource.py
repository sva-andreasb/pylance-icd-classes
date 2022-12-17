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
def ():
    '''returns Resource\n\n
    ()\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String prop)\n
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
    '''returns float\n\n
    getFloat(final String prop)\n
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
def setProperty():
    '''returns Object\n\n
    setProperty(final String prop, final Object value)\n
    setProperty(final String prop, final Object value, final boolean ignoreChangeTracking)\n
    '''
def getID():
    '''returns String\n\n
    getID()\n
    '''
def getQuantity():
    '''returns float\n\n
    getQuantity()\n
    '''
def getPropertyNames():
    '''returns Collection<String>\n\n
    getPropertyNames()\n
    '''
def setObjectName():
    '''returns None\n\n
    setObjectName(final String objectName)\n
    '''
def setRefObjectName():
    '''returns None\n\n
    setRefObjectName(final String refObjectName)\n
    '''
def getObjectName():
    '''returns String\n\n
    getObjectName()\n
    '''
def getRefObjectName():
    '''returns String\n\n
    getRefObjectName()\n
    '''
def put():
    '''returns Object\n\n
    put(final Object key, final Object value)\n
    '''
def remove():
    '''returns Object\n\n
    remove(final Object key)\n
    '''
