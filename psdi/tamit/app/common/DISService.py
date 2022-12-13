PRODUCT_NAME = "String  ProductName""
def getDISService():
'''public static synchronized DISService getDISService(final UserInfo userInfo)
'''
pass
def shutDown():
'''public void shutDown()
'''
pass
def getMSS():
'''public Guid getMSS(final String productName)
'''
pass
def registerByMbo():
'''public Guid registerByMbo(final MboRemote mbo, final boolean setValue)
public Guid registerByMbo(final MboRemote mbo, final boolean setValue, final UserInfo callersUserInfo)
'''
pass
def registerByMboSet():
'''public Guid[] registerByMboSet(final MboSetRemote mbos, final boolean setValue)
'''
pass
def registerByCdm():
'''public Guid[] registerByCdm(final String productName, HashMap[] cdmAttributes)
'''
pass
def getAllClassesForMBO():
'''public List<String> getAllClassesForMBO(final String mboObjectName)
'''
pass
def namingAttributeChanged():
'''public boolean namingAttributeChanged(final MboRemote mbo)
'''
pass
def cleanse():
'''public String cleanse(final String cdmObjectName, final String cdmAttributeName, final String value)
'''
pass
def hasVMID():
'''public boolean hasVMID(final MboRemote mbo)
'''
pass
