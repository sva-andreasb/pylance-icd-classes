def ():
    '''returns SFWView\n\n
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
    '''
def createReleaseHeaderAndLines():
    '''returns MboRemote\n\n
    createReleaseHeaderAndLines(final MboSetRemote contractLineSetRemote)\n
    '''
def copySelectedLinesToRelease():
    '''returns None\n\n
    copySelectedLinesToRelease(final MboRemote releasePOHeader, final Vector selectedMbos)\n
    '''
def canCreateRelease():
    '''returns None\n\n
    canCreateRelease()\n
    '''
def createPOHeader():
    '''returns MboRemote\n\n
    createPOHeader()\n
    '''
def copyPurchContractValuesToPOHeader():
    '''returns None\n\n
    copyPurchContractValuesToPOHeader(final MboRemote poHeaderRemote)\n
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
def setFullyLic():
    '''returns None\n\n
    setFullyLic(MboSetRemote contractLineSet)\n
    '''
def applyPriceToLines():
    '''returns None\n\n
    applyPriceToLines()\n
    '''
def canAddAssetToContractAsset():
    '''returns None\n\n
    canAddAssetToContractAsset()\n
    '''
def canAddPeopleToNamedUsers():
    '''returns None\n\n
    canAddPeopleToNamedUsers()\n
    '''
def canAssociatLicense():
    '''returns None\n\n
    canAssociatLicense()\n
    '''
def canDeleteAssociation():
    '''returns None\n\n
    canDeleteAssociation()\n
    '''
def copyAssetsToContractAsset():
    '''returns None\n\n
    copyAssetsToContractAsset(final AssetSetRemote assetSetRemote)\n
    '''
def reviseContract():
    '''returns MboRemote\n\n
    reviseContract(final String revDescription)\n
    '''
def validateAssetsToContractAsset():
    '''returns None\n\n
    validateAssetsToContractAsset(final AssetSetRemote assetSetRemote)\n
    '''
