PRODUCT_NAME = "String  \"ProductName\""
def getDISService():
    '''public static synchronized DISService getDISService(final UserInfo userInfo)
    '''
def shutDown():
    '''public void shutDown()
    '''
def getMSS():
    '''public Guid getMSS(final String productName)
    '''
def registerByMbo():
    '''public Guid registerByMbo(final MboRemote mbo, final boolean setValue)
    public Guid registerByMbo(final MboRemote mbo, final boolean setValue, final UserInfo callersUserInfo)
    '''
def registerByMboSet():
    '''public Guid[] registerByMboSet(final MboSetRemote mbos, final boolean setValue)
    '''
def registerByCdm():
    '''public Guid[] registerByCdm(final String productName, HashMap[] cdmAttributes)
    '''
def getAllClassesForMBO():
    '''public List<String> getAllClassesForMBO(final String mboObjectName)
    '''
def namingAttributeChanged():
    '''public boolean namingAttributeChanged(final MboRemote mbo)
    '''
def cleanse():
    '''public String cleanse(final String cdmObjectName, final String cdmAttributeName, final String value)
    '''
def hasVMID():
    '''public boolean hasVMID(final MboRemote mbo)
    '''
