PROPERTY_LOADDATAVALUE = "String  \"loadDataValue\""
PROPERTY_PMLOADDATAVALUE = "String  \"pmloadDataValue\""
PROPERTY_LOADLABORHRS = "String  \"loadLaborHrs\""
PROPERTY_LOADTOOLHRS = "String  \"loadToolHrs\""
PROPERTY_LOADTOOLQTY = "String  \"loadToolQty\""
PROPERTY_LOADZONECAPACITY = "String  \"loadZoneCapacity\""
def ():
    '''returns MXReservation\n\n
    (final IlvResource resource, final IlvActivity activity)\n
    '''
def setProperty():
    '''returns Object\n\n
    setProperty(final String property, final Object value)\n
    setProperty(final String property, final Object value, final boolean ignoreChangeTracking)\n
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
def getMXActivity():
    '''returns IMXActivity\n\n
    getMXActivity()\n
    '''
def getMXResource():
    '''returns IMXResource\n\n
    getMXResource()\n
    '''
def createReservation():
    '''returns MXReservation\n\n
    createReservation(final MXResource resource, final MXActivity activity)\n
    '''
