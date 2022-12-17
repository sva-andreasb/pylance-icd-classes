def ():
    '''returns Contract\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def setContractTypeEditibilityAndValues():
    '''returns None\n\n
    setContractTypeEditibilityAndValues(final boolean fromInit)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def changeLineStatus():
    '''returns None\n\n
    changeLineStatus(final MboSetRemote contractLineSetRemote)\n
    '''
def canChangeLineStatus():
    '''returns None\n\n
    canChangeLineStatus()\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final Date date, final String memo, final long accessModifier)\n
    '''
def canEditContractLine():
    '''returns boolean\n\n
    canEditContractLine()\n
    '''
def validateDates():
    '''returns None\n\n
    validateDates()\n
    '''
def validateContract():
    '''returns None\n\n
    validateContract()\n
    '''
def checkMasterMaxValue():
    '''returns None\n\n
    checkMasterMaxValue()\n
    '''
def getContractReleaseSeqNumber():
    '''returns int\n\n
    getContractReleaseSeqNumber()\n
    '''
def getAvailableFunds():
    '''returns double\n\n
    getAvailableFunds()\n
    '''
def reviseContract():
    '''returns MboRemote\n\n
    reviseContract(final String revDescription)\n
    '''
def copySitesToContractAuth():
    '''returns None\n\n
    copySitesToContractAuth(final SiteSetRemote siteSetRemote)\n
    '''
def copySLAToSLAContract():
    '''returns None\n\n
    copySLAToSLAContract(final SLASetRemote slaSetRemote)\n
    '''
def initRelationship():
    '''returns None\n\n
    initRelationship(final String relationName, final MboSetRemote mboSet)\n
    '''
def canPerformAction():
    '''returns None\n\n
    canPerformAction()\n
    '''
def canReviseContract():
    '''returns None\n\n
    canReviseContract()\n
    '''
def addInvVendorItemsToContractLine():
    '''returns None\n\n
    addInvVendorItemsToContractLine(final MboSetRemote invVendorSetRemote)\n
    '''
def getInternalContractType():
    '''returns String\n\n
    getInternalContractType()\n
    '''
def nullVendor():
    '''returns None\n\n
    nullVendor()\n
    '''
def findLatestMasterRevision():
    '''returns MboRemote\n\n
    findLatestMasterRevision()\n
    '''
def canAuthSites():
    '''returns None\n\n
    canAuthSites()\n
    '''
def setContractTypeTerm():
    '''returns None\n\n
    setContractTypeTerm()\n
    '''
def cancelOrSusupndPreviousRevision():
    '''returns None\n\n
    cancelOrSusupndPreviousRevision(final String internalStatus)\n
    '''
def setNextRevisionReference():
    '''returns None\n\n
    setNextRevisionReference(final MboRemote nextRevisionRef)\n
    '''
def getNextRevisionReference():
    '''returns MboRemote\n\n
    getNextRevisionReference()\n
    '''
def getPreviousRevision():
    '''returns MboRemote\n\n
    getPreviousRevision()\n
    '''
def getNextRevision():
    '''returns MboRemote\n\n
    getNextRevision()\n
    '''
def setInvoiceCreationFlag():
    '''returns None\n\n
    setInvoiceCreationFlag(final boolean hasCreatedInvoice)\n
    '''
def getInvoiceCreationFlag():
    '''returns boolean\n\n
    getInvoiceCreationFlag()\n
    '''
def doesContractReferenceExistOnPO():
    '''returns boolean\n\n
    doesContractReferenceExistOnPO()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def getAssetList():
    '''returns MboSetRemote\n\n
    getAssetList()\n
    '''
def getLocationsList():
    '''returns MboSetRemote\n\n
    getLocationsList()\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def revisionInProgress():
    '''returns None\n\n
    revisionInProgress(final boolean flag)\n
    '''
def isRevisionInProgress():
    '''returns boolean\n\n
    isRevisionInProgress()\n
    '''
def useLineOrLoadedCost():
    '''returns String\n\n
    useLineOrLoadedCost()\n
    '''
def setRouteWF():
    '''returns None\n\n
    setRouteWF(final boolean route)\n
    '''
def getRouteWF():
    '''returns boolean\n\n
    getRouteWF()\n
    '''
def prevStatusRemainApproved():
    '''returns boolean\n\n
    prevStatusRemainApproved()\n
    '''
