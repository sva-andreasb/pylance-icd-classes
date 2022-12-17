LOCALIZATION_SERVICES = "String  \"Localization\""
URL_SERVICES = "String  \"URLServices\""
ACTION_SERVICES = "String  \"ActionServices\""
PROPERTY_SERVICES = "String  \"PropertyServices\""
CLASS_SERVICES = "String  \"ClassServices\""
def ():
    '''returns IlvServicesProvider\n\n
    ()\n
    '''
def getLocalizationServices():
    '''returns IlvLocalizationServices\n\n
    getLocalizationServices()\n
    '''
def getURLServices():
    '''returns IlvURLServices\n\n
    getURLServices()\n
    '''
def getActionServices():
    '''returns IlvActionServices\n\n
    getActionServices()\n
    '''
def getPropertyServices():
    '''returns IlvPropertyServices\n\n
    getPropertyServices()\n
    '''
def getClassServices():
    '''returns IlvClassServices\n\n
    getClassServices()\n
    '''
def getServices():
    '''returns IlvServices\n\n
    getServices(final String s)\n
    '''
def addServices():
    '''returns None\n\n
    addServices(final String s, final IlvServices servicesDelegate)\n
    '''
def removeServices():
    '''returns boolean\n\n
    removeServices(final String s, final IlvServices ilvServices)\n
    '''
