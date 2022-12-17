def ():
    '''returns ConfigPropertyOverride\n\n
    (final ReadWriteConfiguration configProperties)\n
    (final ReadWriteConfiguration configProperties, final Properties overrides)\n
    '''
def override():
    '''returns Object\n\n
    override(final CfgPropertyDescriptorEnum key, final Object value)\n
    '''
def getProperty():
    '''returns String\n\n
    getProperty(final CfgPropertyDescriptorEnum key)\n
    getProperty(final String key)\n
    '''
def addProperty():
    '''returns None\n\n
    addProperty(final CfgPropertyDescriptorEnum key, final String value)\n
    addProperty(final String key, final String value)\n
    '''
def updateProperty():
    '''returns None\n\n
    updateProperty(final CfgPropertyDescriptorEnum key, final String value)\n
    updateProperty(final String key, final String value)\n
    '''
def storeProperties():
    '''returns None\n\n
    storeProperties()\n
    '''
def getPropertyKeys():
    '''returns String[]\n\n
    getPropertyKeys()\n
    '''
def getPropertiesByFilter():
    '''returns Properties\n\n
    getPropertiesByFilter(final String filter)\n
    '''
def getPropertyKeySet():
    '''returns Set<String>\n\n
    getPropertyKeySet()\n
    '''
def preventPropertyUpdates():
    '''returns None\n\n
    preventPropertyUpdates(final boolean preventPropertyUpdates)\n
    '''
def willPropertiesBeSavedIfStorePropertiesCalled():
    '''returns boolean\n\n
    willPropertiesBeSavedIfStorePropertiesCalled()\n
    '''
def nullOverrideValue():
    '''returns String\n\n
    nullOverrideValue()\n
    '''
def storeAndReloadProperties():
    '''returns None\n\n
    storeAndReloadProperties(final boolean overwriteNullableProp)\n
    '''
def removePropertiesValuesFromDB():
    '''returns None\n\n
    removePropertiesValuesFromDB(final List<String> properties)\n
    '''
