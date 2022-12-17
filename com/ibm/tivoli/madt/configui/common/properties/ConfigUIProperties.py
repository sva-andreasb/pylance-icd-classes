def saveProperties():
    '''returns boolean\n\n
    saveProperties()\n
    '''
def getProperty():
    '''returns String\n\n
    getProperty(final String propertyName)\n
    getProperty(final ConfigUIPropertyEnum prop)\n
    '''
def getPropertyOrDefault():
    '''returns String\n\n
    getPropertyOrDefault(final String propertyName)\n
    getPropertyOrDefault(final ConfigUIPropertyEnum prop)\n
    '''
def getApplicationInformation():
    '''returns ApplicationInformation\n\n
    getApplicationInformation(final String applicationName)\n
    '''
def setApplicationInformation():
    '''returns None\n\n
    setApplicationInformation(final String applicationName, final ApplicationInformation applicationInfo)\n
    '''
def clearApplicationInformation():
    '''returns None\n\n
    clearApplicationInformation()\n
    '''
def getApplicationNames():
    '''returns Set<String>\n\n
    getApplicationNames()\n
    '''
def setProperty():
    '''returns String\n\n
    setProperty(final ConfigUIPropertyEnum prop, String value)\n
    '''
def getPropertyKeySet():
    '''returns Set<ConfigUIPropertyEnum>\n\n
    getPropertyKeySet()\n
    '''
def addProperty():
    '''returns None\n\n
    addProperty(final String propertyName, final String value)\n
    '''
def removeProperty():
    '''returns String\n\n
    removeProperty(final ConfigUIPropertyEnum prop)\n
    '''
