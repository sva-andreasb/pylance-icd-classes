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
def ():
    '''returns MXResource\n\n
    (final String id, final String name, final float quantity)\n
    (final String id, final String name)\n
    '''
def setProperty():
    '''returns Object\n\n
    setProperty(final String property, final Object value, final boolean ignoreChangeTracking)\n
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
def setUserData():
    '''returns None\n\n
    setUserData(final String key, final Object value)\n
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
def createResource():
    '''returns MXResource\n\n
    createResource()\n
    '''
