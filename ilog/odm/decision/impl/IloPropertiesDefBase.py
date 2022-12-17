COPYRIGHT_NOTICE = "String  \"Copyright IBM Corporation 2005,2012\""
def ():
    '''returns IloPropertiesDefBase\n\n
    ()\n
    '''
def getPropertyIndex():
    '''returns int\n\n
    getPropertyIndex(String name)\n
    '''
def getPropertyName():
    '''returns String\n\n
    getPropertyName(final int index)\n
    '''
def getPropertyGetter():
    '''returns Getter\n\n
    getPropertyGetter(final int index)\n
    '''
def getPropertySetter():
    '''returns Setter\n\n
    getPropertySetter(final int index)\n
    '''
def addProperty():
    '''returns None\n\n
    addProperty(final String propName, final Class<?> propType, final boolean isMandatory, final boolean isStored, final boolean isExported, final Getter getter, final Setter setter)\n
    '''
def selectProperty():
    '''returns None\n\n
    selectProperty(final String propName)\n
    '''
def propertyCount():
    '''returns int\n\n
    propertyCount(final Selector select)\n
    '''
def exportedProperties():
    '''returns Property[]\n\n
    exportedProperties()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
