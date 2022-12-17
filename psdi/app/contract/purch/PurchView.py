def ():
    '''returns PurchView\n\n
    (final MboSet ms)\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def copyPOLinesToCurrentContract():
    '''returns None\n\n
    copyPOLinesToCurrentContract(final MboSetRemote sourcePOLineSet)\n
    '''
def copyPRLinesToCurrentContract():
    '''returns None\n\n
    copyPRLinesToCurrentContract(final MboSetRemote sourcePRLineSet)\n
    '''
def copyPRLineToContract():
    '''returns MboRemote\n\n
    copyPRLineToContract(final MboRemote sourcePRLine, final MboSetRemote contractLineSetRemote)\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def createRelease():
    '''returns MboRemote\n\n
    createRelease(final MboSetRemote contractLineSetRemote)\n
    createRelease(final String ponum, final MboSetRemote contractLineSetRemote)\n
    createRelease(final String ponum, final MboSetRemote contractLineSetRemote, final String siteID)\n
    '''
def createReleaseHeaderAndLines():
    '''returns MboRemote\n\n
    createReleaseHeaderAndLines(final MboSetRemote contractLineSetRemote)\n
    createReleaseHeaderAndLines(final MboSetRemote contractLineSetRemote, final String siteID)\n
    '''
def copySelectedLinesToRelease():
    '''returns None\n\n
    copySelectedLinesToRelease(final MboRemote releasePOHeader, final Vector selectedMbos)\n
    '''
def canCreateRelease():
    '''returns None\n\n
    canCreateRelease()\n
    '''
def canCreateRFQ():
    '''returns None\n\n
    canCreateRFQ()\n
    '''
def createPOHeader():
    '''returns MboRemote\n\n
    createPOHeader()\n
    createPOHeader(final String siteID)\n
    '''
def copyPurchContractValuesToPOHeader():
    '''returns None\n\n
    copyPurchContractValuesToPOHeader(final MboRemote poHeaderRemote)\n
    copyPurchContractValuesToPOHeader(final MboRemote poHeaderRemote, final String siteID)\n
    '''
def applyPriceAdjustment():
    '''returns None\n\n
    applyPriceAdjustment(final MboSetRemote contractLineSetRemote)\n
    '''
def createRFQ():
    '''returns MboRemote\n\n
    createRFQ(final MboSetRemote contractLineSetRemote)\n
    '''
def nullVendor():
    '''returns None\n\n
    nullVendor()\n
    '''
def canChangeLineStatus():
    '''returns None\n\n
    canChangeLineStatus()\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def initRelationship():
    '''returns None\n\n
    initRelationship(final String relationName, final MboSetRemote mboSet)\n
    '''
def getUnCommittedReleases():
    '''returns double\n\n
    getUnCommittedReleases()\n
    '''
def getCommittedReleases():
    '''returns double\n\n
    getCommittedReleases()\n
    '''
def getUnCommitedCost():
    '''returns double\n\n
    getUnCommitedCost()\n
    '''
def getAmountOnOrder():
    '''returns double\n\n
    getAmountOnOrder()\n
    '''
def getInvoiceVariance():
    '''returns double\n\n
    getInvoiceVariance()\n
    '''
def getAmountReceived():
    '''returns double\n\n
    getAmountReceived()\n
    '''
def canViewRelCost():
    '''returns None\n\n
    canViewRelCost()\n
    '''
def createSWLic():
    '''returns None\n\n
    createSWLic()\n
    '''
def deleteSWLic():
    '''returns None\n\n
    deleteSWLic()\n
    '''
def canCreateSWLic():
    '''returns None\n\n
    canCreateSWLic()\n
    '''
def copyPersonsToNamedUsers():
    '''returns None\n\n
    copyPersonsToNamedUsers(final MboSetRemote personSetRemote)\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def removeContractReferencesFromPR():
    '''returns None\n\n
    removeContractReferencesFromPR()\n
    '''
def removeContractReferencesFromRFQ():
    '''returns None\n\n
    removeContractReferencesFromRFQ()\n
    '''
def applyPriceToLines():
    '''returns None\n\n
    applyPriceToLines()\n
    '''
def getPOCurrency():
    '''returns None\n\n
    getPOCurrency(final String[] statuses)\n
    '''
def getSqlLineOrLoadedCost():
    '''returns None\n\n
    getSqlLineOrLoadedCost()\n
    '''
