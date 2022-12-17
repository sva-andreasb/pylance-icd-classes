PRODUCT_NAME = "String  \"ProductName\""
def shutDown():
    '''returns None\n\n
    shutDown()\n
    '''
def getMSS():
    '''returns Guid\n\n
    getMSS(final String productName)\n
    '''
def registerByMbo():
    '''returns Guid\n\n
    registerByMbo(final MboRemote mbo, final boolean setValue)\n
    registerByMbo(final MboRemote mbo, final boolean setValue, final UserInfo callersUserInfo)\n
    '''
def registerByMboSet():
    '''returns Guid[]\n\n
    registerByMboSet(final MboSetRemote mbos, final boolean setValue)\n
    '''
def registerByCdm():
    '''returns Guid[]\n\n
    registerByCdm(final String productName, HashMap[] cdmAttributes)\n
    '''
def getAllClassesForMBO():
    '''returns List<String>\n\n
    getAllClassesForMBO(final String mboObjectName)\n
    '''
def namingAttributeChanged():
    '''returns boolean\n\n
    namingAttributeChanged(final MboRemote mbo)\n
    '''
def cleanse():
    '''returns String\n\n
    cleanse(final String cdmObjectName, final String cdmAttributeName, final String value)\n
    '''
def hasVMID():
    '''returns boolean\n\n
    hasVMID(final MboRemote mbo)\n
    '''
