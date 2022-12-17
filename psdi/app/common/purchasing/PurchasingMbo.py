def ():
    '''returns PurchasingMbo\n\n
    (final MboSet ms)\n
    '''
def recalculateTotalCost():
    '''returns None\n\n
    recalculateTotalCost()\n
    '''
def recalculateTotalTax():
    '''returns double\n\n
    recalculateTotalTax()\n
    '''
def noLimitWhenApprove():
    '''returns None\n\n
    noLimitWhenApprove()\n
    '''
def getInvoiceMgtMaxVar():
    '''returns boolean\n\n
    getInvoiceMgtMaxVar()\n
    '''
def copyTerms():
    '''returns None\n\n
    copyTerms(final MboSetRemote termsSet)\n
    '''
def copyAllTerms():
    '''returns None\n\n
    copyAllTerms(final MboSetRemote toTermsSet)\n
    '''
def compareCopyTerms():
    '''returns None\n\n
    compareCopyTerms(final MboRemote fromMbo)\n
    '''
def createContractHeader():
    '''returns MboRemote\n\n
    createContractHeader(final String contractNum, final String description, final String contractType)\n
    '''
def getExchangeRate():
    '''returns double\n\n
    getExchangeRate(final Date date)\n
    '''
def getExchangeRate2():
    '''returns double\n\n
    getExchangeRate2(final Date date)\n
    '''
def copyFromContract():
    '''returns None\n\n
    copyFromContract(final MboRemote contractRemote, final MboRemote contractAuthFind)\n
    '''
def getContractAuth():
    '''returns MboRemote\n\n
    getContractAuth(final MboRemote contractRemote)\n
    '''
def getShowconswarningFlag():
    '''returns boolean\n\n
    getShowconswarningFlag()\n
    '''
def setShowconswarningFlag():
    '''returns None\n\n
    setShowconswarningFlag(final boolean flag)\n
    '''
def copyContractToPOPR():
    '''returns None\n\n
    copyContractToPOPR(final MboSetRemote sourceContractLineSet)\n
    '''
def checkConsignmentItemsInContractSet():
    '''returns Vector<MboRemote>\n\n
    checkConsignmentItemsInContractSet(final MboSetRemote contractLineSetRemote, final String storeloc)\n
    '''
def checkConsignmentItems():
    '''returns Vector<MboRemote>\n\n
    checkConsignmentItems(final MboSetRemote itemSetRemote, final String storeloc)\n
    '''
def setPOPRLineSet():
    '''returns None\n\n
    setPOPRLineSet(final MboSetRemote mboLineSet)\n
    '''
def getPOPRLineSet():
    '''returns MboSetRemote\n\n
    getPOPRLineSet()\n
    '''
def showConsVendorWarningMessageForContracts():
    '''returns None\n\n
    showConsVendorWarningMessageForContracts(final MboSetRemote mboLineSet)\n
    '''
def showConsVendorWarningMessage():
    '''returns Vector<MboRemote>\n\n
    showConsVendorWarningMessage(final MboSetRemote invVendorSetRemote, final Vector<MboRemote> vendorItemsVec, final String storeloc)\n
    '''
def addConsignmentItems():
    '''returns None\n\n
    addConsignmentItems(final MboSetRemote mboLineSet, final Vector<MboRemote> itemsVec)\n
    '''
def copyContarctTerm():
    '''returns None\n\n
    copyContarctTerm(final MboRemote contractRemote)\n
    '''
def nullVendor():
    '''returns None\n\n
    nullVendor()\n
    '''
def nullVendorContract():
    '''returns None\n\n
    nullVendorContract()\n
    '''
def checkContractType():
    '''returns MboRemote\n\n
    checkContractType(final MboRemote contractRemote)\n
    '''
def checkInvalidItemStatus():
    '''returns boolean\n\n
    checkInvalidItemStatus(final MboSetRemote invVendorSetRemote)\n
    '''
