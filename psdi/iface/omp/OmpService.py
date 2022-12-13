def OmpService():
'''public OmpService()
public OmpService(final MXServer mxServer)
'''
pass
def getOMPListForLMO():
'''public OmpSetRemote getOMPListForLMO(final String ompProductname, final String lmoName, final String lmoNamespace)
'''
pass
def getOMPListForIM():
'''public OmpSetRemote getOMPListForIM(final String imName, final String imVersion)
'''
pass
def getLMOListForIM():
'''public LMOSetRemote getLMOListForIM(final String imName, final String imVersion)
'''
pass
def getPreferredIM():
'''public OmpImLmoRelInfo getPreferredIM(final String ompGUID, final String lmoName, final String lmoNamespace)
public OmpImLmoRelInfo getPreferredIM(final String ompHostname, final String ompProductname, final String ompManufacturer, final String lmoName, final String lmoNamespace)
'''
pass
def getIMListForOMPAndLMO():
'''public Collection getIMListForOMPAndLMO(final String ompGUID, final String lmoName, final String lmoNamespace)
public Collection getIMListForOMPAndLMO(final String ompHostname, final String ompProductname, final String ompManufacturer, final String lmoName, final String lmoNamespace)
'''
pass
def getIMListForOMP():
'''public MaxIMSetRemote getIMListForOMP(final String ompGuid)
'''
pass
def getIMListForLMO():
'''public MaxIMSetRemote getIMListForLMO(final String lmoName, final String lmoNamespace)
'''
pass
def getIMListForLMOWithOMP():
'''public MaxIMSetRemote getIMListForLMOWithOMP(final String lmoName, final String lmoNamespace)
'''
pass
def getServiceInvokerListForCIAndLMO():
'''public Collection getServiceInvokerListForCIAndLMO(final String ciGUID, final String lmoName, final String lmoNamespace, final UserInfo userInfo)
'''
pass
def getServiceInvoker():
'''public Map getServiceInvoker(final String ompGUID, final String lmoName, final String lmoNamespace, final UserInfo userInfo)
public Map getServiceInvoker(final OmpImLmoRelRemote ompImLmoRelRemote, final UserInfo userInfo)
public Map getServiceInvoker(final String ompGUID, final String imName, final String imVersion, final String lmoName, final String lmoNamespace, final UserInfo userInfo)
public Map getServiceInvoker(final OmpImLmoRelInfo ompImLmoRelInfo, final UserInfo userInfo)
'''
pass
def getCredentialMapper():
'''public BaseCredentialMapper getCredentialMapper(final UserInfo userInfo, final String endPointName)
'''
pass
def setupEndPoint():
'''public Map setupEndPoint(final Map<String, Object> invokerPropMap, final String endPointName, final UserInfo userInfo)
'''
pass
def getLMOsNotAssociatedWithIM():
'''public LMOSetRemote getLMOsNotAssociatedWithIM(final MboRemote imMbo)
'''
pass
def getLMOListForOMP():
'''public LMOSetRemote getLMOListForOMP(final String ompGuid)
'''
pass
def getSourceToken():
'''public String getSourceToken(final String ciGUID, final String ompGUID)
public String getSourceToken(final String ciGUID, final OmpRemote omp)
public String getSourceToken(final ActCIRemote ci, final OmpRemote omp)
'''
pass
def getCIGUIDFromMBO():
'''public String getCIGUIDFromMBO(final MboRemote mainMbo)
'''
pass
def checkContext():
'''public int checkContext(final MaxLaunchEntryInfo entry, final MboRemote mainMbo)
'''
pass
def getLaunchEntry():
'''public MaxLaunchEntryInfo getLaunchEntry(final String launchEntryName)
'''
pass
def getURL():
'''public String getURL(final String launchEntryName, final OmpRemote omp, final MboRemote mainMbo)
'''
pass
def getOMPList():
'''public OmpSetRemote getOMPList(final String launchEntryName, final MboRemote mainMbo)
'''
pass
def getLMOsNotAssociatedWithIMAndOmp():
'''public LMOSetRemote getLMOsNotAssociatedWithIMAndOmp(final MboRemote ompImRel)
'''
pass
def testCredentialMapper():
'''public static void testCredentialMapper()
'''
pass
def test():
'''public void test()
'''
pass
