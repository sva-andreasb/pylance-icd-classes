def ():
    '''returns LeaseView\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def nullVendor():
    '''returns None\n\n
    nullVendor()\n
    '''
def initRelationship():
    '''returns None\n\n
    initRelationship(final String relationName, final MboSetRemote mboSet)\n
    '''
def canCreateSchedule():
    '''returns None\n\n
    canCreateSchedule()\n
    '''
def reCalcLeaseViewCost():
    '''returns double\n\n
    reCalcLeaseViewCost()\n
    '''
def setRentalReadOnlyFields():
    '''returns None\n\n
    setRentalReadOnlyFields()\n
    '''
def copyAssetsToContractAsset():
    '''returns None\n\n
    copyAssetsToContractAsset(final AssetSetRemote assetSetRemote)\n
    '''
def canAddAssetToContractAsset():
    '''returns None\n\n
    canAddAssetToContractAsset()\n
    '''
def canPurchaseOrReturnAsset():
    '''returns None\n\n
    canPurchaseOrReturnAsset()\n
    '''
def createEndLeaseInvoice():
    '''returns None\n\n
    createEndLeaseInvoice(final String invNumber, final String targetStatus, final MboSetRemote assetSet, final boolean purchaseFlag)\n
    '''
def createEndLeasePO():
    '''returns None\n\n
    createEndLeasePO(final String poNumber, final String targetStatus, final MboSetRemote assetSet, final boolean purchaseFlag)\n
    '''
def applyPriceAdjustment():
    '''returns None\n\n
    applyPriceAdjustment(final MboSetRemote contractLineSetRemote)\n
    '''
def applyPriceToLines():
    '''returns None\n\n
    applyPriceToLines()\n
    '''
def reviseContract():
    '''returns MboRemote\n\n
    reviseContract(final String revDescription)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final Date date, final String memo, final long accessModifier)\n
    '''
def cancelInvoices():
    '''returns None\n\n
    cancelInvoices(final MboSetRemote assetSet)\n
    '''
