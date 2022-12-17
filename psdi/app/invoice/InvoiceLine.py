def ():
    '''returns InvoiceLine\n\n
    (final MboSet ms)\n
    '''
def getNewInvoiceCost():
    '''returns InvoiceCostRemote\n\n
    getNewInvoiceCost()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def getPOToInvCur():
    '''returns double\n\n
    getPOToInvCur()\n
    '''
def recalculatePreTaxTotalWhenDelete():
    '''returns None\n\n
    recalculatePreTaxTotalWhenDelete()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def validateInvoiceMatch():
    '''returns None\n\n
    validateInvoiceMatch()\n
    '''
def copyPOLine():
    '''returns None\n\n
    copyPOLine()\n
    '''
def clearPOLine():
    '''returns None\n\n
    clearPOLine()\n
    '''
def validateCurrency():
    '''returns None\n\n
    validateCurrency(final String invoiceCurrency)\n
    '''
def validateInvoiceMatchForApproval():
    '''returns None\n\n
    validateInvoiceMatchForApproval()\n
    '''
def checkForServiceProrating():
    '''returns None\n\n
    checkForServiceProrating()\n
    '''
def checkForPOLineTolerance():
    '''returns None\n\n
    checkForPOLineTolerance(final Double upperTolerancePct, final Double lowerTolerancePct, final Double upperToleranceAmt, final Double lowerToleranceAmt)\n
    '''
def createDefaultServiceReceipt():
    '''returns MboRemote\n\n
    createDefaultServiceReceipt()\n
    '''
def createDefaultMaterialReceipt():
    '''returns MboRemote\n\n
    createDefaultMaterialReceipt()\n
    '''
def createDefaultReceipt():
    '''returns MboRemote\n\n
    createDefaultReceipt()\n
    createDefaultReceipt(final MboSetRemote desiredReceipts)\n
    '''
def getInvoiceMatchSet():
    '''returns InvoiceMatchSetRemote\n\n
    getInvoiceMatchSet()\n
    '''
def createReceipts():
    '''returns None\n\n
    createReceipts()\n
    '''
def calcProrateCostForReceipt():
    '''returns double\n\n
    calcProrateCostForReceipt()\n
    '''
def getRatioForTransaction():
    '''returns double\n\n
    getRatioForTransaction()\n
    '''
def needProcessVariance():
    '''returns boolean\n\n
    needProcessVariance()\n
    '''
def createReceiptOrTransactionForVariance():
    '''returns None\n\n
    createReceiptOrTransactionForVariance()\n
    '''
def createTransactionsAfterAppr():
    '''returns None\n\n
    createTransactionsAfterAppr(final double currencyVar, final double priceVar)\n
    '''
def findOrigReceiptSum():
    '''returns double\n\n
    findOrigReceiptSum(final String attribute)\n
    '''
def createInvoiceTrans():
    '''returns None\n\n
    createInvoiceTrans()\n
    '''
def returnGls():
    '''returns Vector\n\n
    returnGls(final boolean updateInventory, final boolean varType)\n
    returnGls(final boolean updateInventory, final boolean varType, final MboRemote transMbo)\n
    '''
def getIssue():
    '''returns boolean\n\n
    getIssue()\n
    '''
def getUnmatched():
    '''returns double\n\n
    getUnmatched()\n
    '''
def afterAdd():
    '''returns None\n\n
    afterAdd()\n
    '''
def getValidateOrder():
    '''returns String[]\n\n
    getValidateOrder()\n
    '''
def setCurVarTotal():
    '''returns None\n\n
    setCurVarTotal(final double currencyVariance)\n
    '''
def setPriceVarTotal():
    '''returns None\n\n
    setPriceVarTotal(final double priceVariance)\n
    '''
def copyReceiptPOLineToInvoiceLine():
    '''returns None\n\n
    copyReceiptPOLineToInvoiceLine(final MboRemote receiptOrPOLine, final double qty, final double cost)\n
    '''
def copyReceiptToInvoiceLine():
    '''returns None\n\n
    copyReceiptToInvoiceLine(final MboRemote receipt, final double qty, final double cost)\n
    '''
def copyPOLineToInvoiceLine():
    '''returns None\n\n
    copyPOLineToInvoiceLine(final MboRemote poLine, final double qty, final double cost)\n
    '''
def createInvoiceCostFromInvoiceLine():
    '''returns None\n\n
    createInvoiceCostFromInvoiceLine(final MboRemote newInvoiceLine, final MboRemote poLine)\n
    '''
def copy():
    '''returns MboRemote\n\n
    copy(final MboSetRemote mboSet)\n
    '''
def canDistributeInvoiceLine():
    '''returns None\n\n
    canDistributeInvoiceLine()\n
    '''
def canDistributeProrateInvoiceLine():
    '''returns None\n\n
    canDistributeProrateInvoiceLine()\n
    '''
def canAllocateServices():
    '''returns None\n\n
    canAllocateServices()\n
    '''
def CanAllocateServIfEnteredOrWappr():
    '''returns None\n\n
    CanAllocateServIfEnteredOrWappr()\n
    '''
def initRelationship():
    '''returns None\n\n
    initRelationship(final String relationName, final MboSetRemote mboSet)\n
    '''
def canDistributeIssueInvoiceLine():
    '''returns None\n\n
    canDistributeIssueInvoiceLine()\n
    '''
def updateWOCosts():
    '''returns None\n\n
    updateWOCosts()\n
    '''
def undelete():
    '''returns None\n\n
    undelete()\n
    '''
def creatInvTransForProrate():
    '''returns None\n\n
    creatInvTransForProrate(final double prorateCostForInvTrans)\n
    '''
def getRatioGoesToReceipt():
    '''returns double\n\n
    getRatioGoesToReceipt()\n
    '''
def recalcDistribution():
    '''returns None\n\n
    recalcDistribution()\n
    '''
def getInternalLineType():
    '''returns String\n\n
    getInternalLineType()\n
    '''
def addCostFromPOLine():
    '''returns None\n\n
    addCostFromPOLine(final InvoiceCostSetRemote invCostSet, final MboRemote poLine)\n
    '''
def isServiceType():
    '''returns boolean\n\n
    isServiceType()\n
    '''
def setPriceQtyFields():
    '''returns None\n\n
    setPriceQtyFields()\n
    '''
def checkWOAssetLocGLDebitForLine():
    '''returns None\n\n
    checkWOAssetLocGLDebitForLine()\n
    '''
def clearClassification():
    '''returns None\n\n
    clearClassification()\n
    '''
def getDefaultTaxExempt():
    '''returns None\n\n
    getDefaultTaxExempt(final MboRemote itemRemote, final MboRemote invVendor)\n
    '''
def getDefaultTaxCodes():
    '''returns None\n\n
    getDefaultTaxCodes(final MboRemote itemRemote, final MboRemote invVendor)\n
    '''
def getInventoryCurbal():
    '''returns double\n\n
    getInventoryCurbal()\n
    '''
def getActivePO():
    '''returns MboRemote\n\n
    getActivePO()\n
    '''
def copyConsTransToInvoiceLine():
    '''returns None\n\n
    copyConsTransToInvoiceLine(final MboRemote transMbo)\n
    '''
def updateConsTransInvoiceNum():
    '''returns None\n\n
    updateConsTransInvoiceNum(final boolean clearInvoiceNum)\n
    '''
def createVarTransForConsInvoiceLine():
    '''returns None\n\n
    createVarTransForConsInvoiceLine()\n
    '''
def setReadOnlyForConsInvoice():
    '''returns None\n\n
    setReadOnlyForConsInvoice()\n
    '''
def getConsTransMbo():
    '''returns MboRemote\n\n
    getConsTransMbo(final String origTransaction, final int transID)\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def clearLabTransOnDelete():
    '''returns None\n\n
    clearLabTransOnDelete()\n
    '''
def setPOLineFromCopyPOLine():
    '''returns None\n\n
    setPOLineFromCopyPOLine(final MboRemote poLineFromCopyPOline)\n
    '''
def getPOLineFromCopyPOLine():
    '''returns MboRemote\n\n
    getPOLineFromCopyPOLine()\n
    '''
