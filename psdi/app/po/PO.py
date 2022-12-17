def ():
    '''returns PO\n\n
    (final MboSet ms)\n
    '''
def getProcess():
    '''returns String\n\n
    getProcess()\n
    '''
def setCancelFlag():
    '''returns None\n\n
    setCancelFlag(final boolean po)\n
    '''
def getCancelFlag():
    '''returns boolean\n\n
    getCancelFlag()\n
    '''
def resetCancelFlag():
    '''returns None\n\n
    resetCancelFlag()\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def initFieldFlagsOnMbo():
    '''returns None\n\n
    initFieldFlagsOnMbo(final String attrName)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def isApproved():
    '''returns boolean\n\n
    isApproved()\n
    '''
def isInternal():
    '''returns boolean\n\n
    isInternal()\n
    '''
def createReceipt():
    '''returns MboRemote\n\n
    createReceipt(final MboSetRemote existingReceiptSet, final long polinenum, final String ownersysid)\n
    '''
def createReturn():
    '''returns MboRemote\n\n
    createReturn(final MatRecTransSet existingReceiptSet, final long polinenum, final MboRemote matRecTransMbo)\n
    createReturn(final MboSetRemote existingReceiptSet, final long polinenum, final String ownersysid)\n
    '''
def receive():
    '''returns None\n\n
    receive(final MboSetRemote receiptSet, final int lineNumber, final double quantity, final String binnum)\n
    '''
def receiveRotatingItemOnInternalPO():
    '''returns None\n\n
    receiveRotatingItemOnInternalPO(final MboSetRemote receiptSet, final int lineNumber, final String binnum, final String assetnum)\n
    '''
def determineReceiptStatus():
    '''returns None\n\n
    determineReceiptStatus()\n
    determineReceiptStatus(final POLineRemote poLine)\n
    '''
def validatePO():
    '''returns None\n\n
    validatePO()\n
    '''
def setTotalCost():
    '''returns None\n\n
    setTotalCost()\n
    '''
def canCreateChangeOrder():
    '''returns None\n\n
    canCreateChangeOrder()\n
    '''
def hasReceipts():
    '''returns None\n\n
    hasReceipts()\n
    '''
def prorateServices():
    '''returns None\n\n
    prorateServices()\n
    '''
def getAvailableFunds():
    '''returns double\n\n
    getAvailableFunds()\n
    '''
def createPOLineFromPR():
    '''returns MboRemote\n\n
    createPOLineFromPR(final MboRemote fromPR, final MboRemote fromPRLine, final MboSetRemote poLines)\n
    '''
def copySelectedLinesToRelease():
    '''returns None\n\n
    copySelectedLinesToRelease(final PORemote toPOMbo)\n
    '''
def copyBlanketLinesToRelease():
    '''returns None\n\n
    copyBlanketLinesToRelease(final PORemote toPOMbo)\n
    '''
def deleteDistributions():
    '''returns None\n\n
    deleteDistributions()\n
    '''
def isPOBuyAhead():
    '''returns boolean\n\n
    isPOBuyAhead()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def isPOStatusAPPR():
    '''returns boolean\n\n
    isPOStatusAPPR()\n
    '''
def isPOStatusINPRG():
    '''returns boolean\n\n
    isPOStatusINPRG()\n
    '''
def getPORecord():
    '''returns Vector\n\n
    getPORecord()\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def createChangeOrder():
    '''returns MboRemote\n\n
    createChangeOrder(final String ponum, final String description)\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def generateAutoKey():
    '''returns None\n\n
    generateAutoKey()\n
    '''
def initRelationship():
    '''returns None\n\n
    initRelationship(final String relationName, final MboSetRemote mboSet)\n
    '''
def setRelatedMboEditibility():
    '''returns None\n\n
    setRelatedMboEditibility(final String relationName, final MboSetRemote mboSet)\n
    '''
def poSentToVendor():
    '''returns None\n\n
    poSentToVendor()\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def copyPRToCurrentPO():
    '''returns None\n\n
    copyPRToCurrentPO(final MboSetRemote sourcePRLineSet)\n
    '''
def copyPRToNewPO():
    '''returns None\n\n
    copyPRToNewPO(final MboSetRemote sourcePRLineSet)\n
    '''
def copySpareParts():
    '''returns None\n\n
    copySpareParts(final MboSetRemote sparePartSet)\n
    '''
def addInvVendorItemsToPOLine():
    '''returns None\n\n
    addInvVendorItemsToPOLine(final MboSetRemote invVendorSetRemote)\n
    '''
def canDuplicate():
    '''returns None\n\n
    canDuplicate()\n
    '''
def addToReceiptVector():
    '''returns None\n\n
    addToReceiptVector(final MboRemote receiptRemote)\n
    '''
def addToInvoiceLineVector():
    '''returns None\n\n
    addToInvoiceLineVector(final MboRemote invoiceLineRemote)\n
    '''
def getReceiptVector():
    '''returns Vector\n\n
    getReceiptVector()\n
    '''
def getInvoiceLineVector():
    '''returns Vector\n\n
    getInvoiceLineVector()\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final Date date, final String memo, final long accessModifier)\n
    '''
def createContractFromPO():
    '''returns None\n\n
    createContractFromPO(final String contractNum, final String description, final String contractType)\n
    '''
def checkingBeforeCreateContract():
    '''returns None\n\n
    checkingBeforeCreateContract()\n
    '''
def checkWAPPRStatus():
    '''returns None\n\n
    checkWAPPRStatus()\n
    '''
def copyDefaultTerms():
    '''returns None\n\n
    copyDefaultTerms()\n
    '''
def updateReleasePO():
    '''returns None\n\n
    updateReleasePO(final MboRemote contractRemote)\n
    '''
def createInvoicesForSchedule():
    '''returns None\n\n
    createInvoicesForSchedule()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def checkingBeforeCompleteReceipts():
    '''returns None\n\n
    checkingBeforeCompleteReceipts()\n
    '''
def getSharedWorkorder():
    '''returns MboRemote\n\n
    getSharedWorkorder(final MboRemote mboRemote, final String wonum)\n
    '''
def setFromOnePO():
    '''returns None\n\n
    setFromOnePO(final boolean flag)\n
    '''
def getFromOnePO():
    '''returns boolean\n\n
    getFromOnePO()\n
    '''
def generateWO():
    '''returns None\n\n
    generateWO()\n
    '''
def createSoftwareContractHeader():
    '''returns MboRemote\n\n
    createSoftwareContractHeader(final String contractNum, final String description, final String contractType)\n
    '''
def getValidateOrder():
    '''returns String[]\n\n
    getValidateOrder()\n
    '''
def canRevisePO():
    '''returns None\n\n
    canRevisePO()\n
    '''
def revisePO():
    '''returns MboRemote\n\n
    revisePO()\n
    revisePO(final String revDescription)\n
    revisePO(final String revDescription, boolean allowReceipt)\n
    '''
def getNextRevision():
    '''returns MboRemote\n\n
    getNextRevision()\n
    '''
def getPreviousRevision():
    '''returns MboRemote\n\n
    getPreviousRevision()\n
    '''
def getApprRevision():
    '''returns MboRemote\n\n
    getApprRevision()\n
    '''
def updatePndRevPO():
    '''returns None\n\n
    updatePndRevPO()\n
    '''
def checkPOLineQtyCost():
    '''returns None\n\n
    checkPOLineQtyCost(final MboRemote pndrevPOLine)\n
    checkPOLineQtyCost(final MboRemote apprPOLine, final MboRemote pndrevPOLine)\n
    '''
def useLineOrLoadedCost():
    '''returns String\n\n
    useLineOrLoadedCost()\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet(final String name)\n
    '''
def setDontCheckCompleteFlag():
    '''returns None\n\n
    setDontCheckCompleteFlag(final boolean flag)\n
    '''
def getDontCheckCompleteFlag():
    '''returns boolean\n\n
    getDontCheckCompleteFlag()\n
    '''
