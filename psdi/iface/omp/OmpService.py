def ():
    '''returns OmpService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def getOMPListForLMO():
    '''returns OmpSetRemote\n\n
    getOMPListForLMO(final String ompProductname, final String lmoName, final String lmoNamespace)\n
    '''
def getOMPListForIM():
    '''returns OmpSetRemote\n\n
    getOMPListForIM(final String imName, final String imVersion)\n
    '''
def getLMOListForIM():
    '''returns LMOSetRemote\n\n
    getLMOListForIM(final String imName, final String imVersion)\n
    '''
def getPreferredIM():
    '''returns OmpImLmoRelInfo\n\n
    getPreferredIM(final String ompGUID, final String lmoName, final String lmoNamespace)\n
    getPreferredIM(final String ompHostname, final String ompProductname, final String ompManufacturer, final String lmoName, final String lmoNamespace)\n
    '''
def getIMListForOMPAndLMO():
    '''returns Collection\n\n
    getIMListForOMPAndLMO(final String ompGUID, final String lmoName, final String lmoNamespace)\n
    getIMListForOMPAndLMO(final String ompHostname, final String ompProductname, final String ompManufacturer, final String lmoName, final String lmoNamespace)\n
    '''
def getIMListForOMP():
    '''returns MaxIMSetRemote\n\n
    getIMListForOMP(final String ompGuid)\n
    '''
def getIMListForLMO():
    '''returns MaxIMSetRemote\n\n
    getIMListForLMO(final String lmoName, final String lmoNamespace)\n
    '''
def getIMListForLMOWithOMP():
    '''returns MaxIMSetRemote\n\n
    getIMListForLMOWithOMP(final String lmoName, final String lmoNamespace)\n
    '''
def getServiceInvokerListForCIAndLMO():
    '''returns Collection\n\n
    getServiceInvokerListForCIAndLMO(final String ciGUID, final String lmoName, final String lmoNamespace, final UserInfo userInfo)\n
    '''
def getServiceInvoker():
    '''returns Map\n\n
    getServiceInvoker(final String ompGUID, final String lmoName, final String lmoNamespace, final UserInfo userInfo)\n
    getServiceInvoker(final OmpImLmoRelRemote ompImLmoRelRemote, final UserInfo userInfo)\n
    getServiceInvoker(final String ompGUID, final String imName, final String imVersion, final String lmoName, final String lmoNamespace, final UserInfo userInfo)\n
    getServiceInvoker(final OmpImLmoRelInfo ompImLmoRelInfo, final UserInfo userInfo)\n
    '''
def getCredentialMapper():
    '''returns BaseCredentialMapper\n\n
    getCredentialMapper(final UserInfo userInfo, final String endPointName)\n
    '''
def setupEndPoint():
    '''returns Map\n\n
    setupEndPoint(final Map<String, Object> invokerPropMap, final String endPointName, final UserInfo userInfo)\n
    '''
def getLMOsNotAssociatedWithIM():
    '''returns LMOSetRemote\n\n
    getLMOsNotAssociatedWithIM(final MboRemote imMbo)\n
    '''
def getLMOListForOMP():
    '''returns LMOSetRemote\n\n
    getLMOListForOMP(final String ompGuid)\n
    '''
def getSourceToken():
    '''returns String\n\n
    getSourceToken(final String ciGUID, final String ompGUID)\n
    getSourceToken(final String ciGUID, final OmpRemote omp)\n
    getSourceToken(final ActCIRemote ci, final OmpRemote omp)\n
    '''
def getCIGUIDFromMBO():
    '''returns String\n\n
    getCIGUIDFromMBO(final MboRemote mainMbo)\n
    '''
def checkContext():
    '''returns int\n\n
    checkContext(final MaxLaunchEntryInfo entry, final MboRemote mainMbo)\n
    '''
def getLaunchEntry():
    '''returns MaxLaunchEntryInfo\n\n
    getLaunchEntry(final String launchEntryName)\n
    '''
def getURL():
    '''returns String\n\n
    getURL(final String launchEntryName, final OmpRemote omp, final MboRemote mainMbo)\n
    '''
def getOMPList():
    '''returns OmpSetRemote\n\n
    getOMPList(final String launchEntryName, final MboRemote mainMbo)\n
    '''
def getLMOsNotAssociatedWithIMAndOmp():
    '''returns LMOSetRemote\n\n
    getLMOsNotAssociatedWithIMAndOmp(final MboRemote ompImRel)\n
    '''
def test():
    '''returns None\n\n
    test()\n
    '''
