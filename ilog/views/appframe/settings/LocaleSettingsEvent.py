LOCALE_FIRST = "int  200"
LOCALE_CHANGED = "int  200"
RESOURCE_BUNDLE_ADDED = "int  201"
RESOURCE_BUNDLE_REMOVED = "int  202"
RESOURCE_BUNDLE_MANAGER_CHANGED = "int  203"
COMPONENT_ORIENTATION_CHANGED = "int  204"
LOCALE_LAST = "int  204"
def ():
    '''returns LocaleSettingsEvent\n\n
    (final int b, final IlvApplication ilvApplication)\n
    '''
def getID():
    '''returns int\n\n
    getID()\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def getApplication():
    '''returns IlvApplication\n\n
    getApplication()\n
    '''
def getResourceBundle():
    '''returns ResourceBundle\n\n
    getResourceBundle()\n
    '''
def setResourceBundle():
    '''returns None\n\n
    setResourceBundle(final ResourceBundle c)\n
    '''
