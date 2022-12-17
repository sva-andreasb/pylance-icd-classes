def ():
    '''returns MatchResult\n\n
    (final MboSet ms)\n
    (final Invoice inv)\n
    (final MboRemote theReceipt, final double theQty, final double theCost)\n
    '''
def getProcess():
    '''returns String\n\n
    getProcess()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def initRelationship():
    '''returns None\n\n
    initRelationship(final String relationName, final MboSetRemote mboSet)\n
    '''
def setRelatedMboEditibility():
    '''returns None\n\n
    setRelatedMboEditibility(final String relationName, final MboSetRemote mboSet)\n
    '''
def setCompanyValues():
    '''returns None\n\n
    setCompanyValues()\n
    '''
def getExternalStatus():
    '''returns String\n\n
    getExternalStatus(final String internalStatus)\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def isSyscodeSet():
    '''returns boolean\n\n
    isSyscodeSet(final long field)\n
    isSyscodeSet()\n
    '''
def setSyscode():
    '''returns None\n\n
    setSyscode(final long field)\n
    '''
def clearSyscode():
    '''returns None\n\n
    clearSyscode(final long field)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def generateAutoKey():
    '''returns None\n\n
    generateAutoKey()\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def validateForApproval():
    '''returns None\n\n
    validateForApproval()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def checkForServiceLinePOTolerance():
    '''returns None\n\n
    checkForServiceLinePOTolerance()\n
    '''
def checkForPOLineTolerance():
    '''returns None\n\n
    checkForPOLineTolerance()\n
    '''
def checkForServiceLineTolerance():
    '''returns None\n\n
    checkForServiceLineTolerance()\n
    '''
def checkForTaxTolerance():
    '''returns None\n\n
    checkForTaxTolerance()\n
    '''
def totalInclusiveTax():
    '''returns double\n\n
    totalInclusiveTax()\n
    '''
def approve():
    '''returns None\n\n
    approve()\n
    '''
def setExchangeRateLineCost2():
    '''returns None\n\n
    setExchangeRateLineCost2()\n
    '''
def prorateTotalTaxDifference():
    '''returns None\n\n
    prorateTotalTaxDifference()\n
    '''
def calcIntermediateLoadedCost():
    '''returns None\n\n
    calcIntermediateLoadedCost()\n
    '''
def createInvoiceTransForTaxes():
    '''returns None\n\n
    createInvoiceTransForTaxes()\n
    '''
def createInvoiceTransTotal():
    '''returns None\n\n
    createInvoiceTransTotal()\n
    '''
def setRequiredInvoiceTransFields():
    '''returns None\n\n
    setRequiredInvoiceTransFields(final MboRemote invoiceLine, final MboRemote newInvoiceTrans, final int j)\n
    '''
def createInvoiceForReceipt():
    '''returns MboRemote\n\n
    createInvoiceForReceipt(final MboRemote receipt)\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def getValidateOrder():
    '''returns String[]\n\n
    getValidateOrder()\n
    '''
def getUninvoicedReceiptsInfo():
    '''returns UninvoicedReceiptsInfo\n\n
    getUninvoicedReceiptsInfo()\n
    '''
def getAllUninvoicedReceipts():
    '''returns Vector<MboRemote>\n\n
    getAllUninvoicedReceipts(final String poNum, final String poLineNum, final int receiptType, final String siteID, final boolean isNegativeLine, final String receiptID)\n
    '''
def getAllUninvoicedMatReceipts():
    '''returns Vector<MboRemote>\n\n
    getAllUninvoicedMatReceipts(final String poNum, final String poLineNum, final String siteID, final boolean isNegativeLine, final String receiptID)\n
    '''
def getAllUninvoicedServReceipts():
    '''returns Vector<MboRemote>\n\n
    getAllUninvoicedServReceipts(final String poNum, final String poLineNum, final String siteID, final boolean isNegativeLine, final String receiptID)\n
    '''
def findMatch():
    '''returns Vector\n\n
    findMatch(final boolean exactFirst, final Vector uninvoicedReceipts, final double minimumSigned, final double maximumSigned, final boolean byCost, final boolean considerTax, final boolean partialAllowed, final InvoiceLineRemote invoiceLine, final POLineRemote poline)\n
    findMatch(final boolean exactFirst, final Vector uninvoicedReceipts, final double value, final boolean byCost, final InvoiceLineRemote invoiceLine, final POLineRemote poline)\n
    '''
def confirmMatch():
    '''returns None\n\n
    confirmMatch(final MboRemote invoiceLine, final Vector matchReceipts)\n
    '''
def createInvoiceTransAfterAppr():
    '''returns None\n\n
    createInvoiceTransAfterAppr(final MboRemote invoice, final double currencyVariance, final double priceVariance)\n
    createInvoiceTransAfterAppr(final String invoicenum, final double currencyVariance, final double priceVariance)\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def copyPOLineToInvoiceLine():
    '''returns MboSetRemote\n\n
    copyPOLineToInvoiceLine(final MboSetRemote poLineSet)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final Date date, final String memo, final long accessModifier)\n
    changeStatus(final String status, final Date date, final String memo, final boolean autoClosePo)\n
    changeStatus(final String status, final Date date, final String memo)\n
    '''
def calculateUnInvoicedTotal():
    '''returns double\n\n
    calculateUnInvoicedTotal()\n
    '''
def copyReceiptToInvoiceLine():
    '''returns MboSetRemote\n\n
    copyReceiptToInvoiceLine(final MboSetRemote receiptSet)\n
    '''
def canAllocateService():
    '''returns None\n\n
    canAllocateService()\n
    '''
def getAllocatePrepSets():
    '''returns InvoiceLineSetRemote[]\n\n
    getAllocatePrepSets(final InvoiceLineSetRemote toBeAllocated, final InvoiceLineSetRemote acceptingLines)\n
    '''
def validateAndCompleteAllocation():
    '''returns None\n\n
    validateAndCompleteAllocation(final InvoiceLineSetRemote toBeAllocated, final InvoiceLineSetRemote acceptingLines)\n
    '''
def allocateServices():
    '''returns None\n\n
    allocateServices(final InvoiceLineSetRemote toBeAllocated, final InvoiceLineSetRemote acceptingLines)\n
    '''
def cancelAllocateService():
    '''returns None\n\n
    cancelAllocateService()\n
    '''
def resetTotalAllocated():
    '''returns None\n\n
    resetTotalAllocated(final InvoiceLineSetRemote lineSet)\n
    '''
def getPOReference():
    '''returns MboRemote\n\n
    getPOReference()\n
    '''
def setPOReference():
    '''returns None\n\n
    setPOReference(final MboRemote poRemote)\n
    '''
def checkForOpenStatus():
    '''returns None\n\n
    checkForOpenStatus()\n
    '''
def getCopyPOLineSet():
    '''returns MboSetRemote\n\n
    getCopyPOLineSet(final String tbName)\n
    '''
def isCreditInvoice():
    '''returns boolean\n\n
    isCreditInvoice()\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def getWOReference():
    '''returns MboRemote\n\n
    getWOReference(final String wonum)\n
    getWOReference(final String wonum, final String siteID)\n
    '''
def setTaxGLs():
    '''returns None\n\n
    setTaxGLs(final String taxCode, final int typeCode)\n
    '''
def copyTerms():
    '''returns None\n\n
    copyTerms(final MboSetRemote termsSet)\n
    '''
def createInvoiceForPurchSched():
    '''returns MboRemote\n\n
    createInvoiceForPurchSched(final MboRemote poLine, final MboRemote scheduleLine, final MboRemote receipt)\n
    '''
def createInvoiceForLabTrans():
    '''returns MboRemote\n\n
    createInvoiceForLabTrans(final MboRemote labTrans, final double quantity, double lineCost, final boolean lineByLine)\n
    '''
def createInvoiceForLeaseSched():
    '''returns MboRemote\n\n
    createInvoiceForLeaseSched(final MboRemote schedule, final double quantity, final double lineCost, final boolean singleLine)\n
    '''
def copyFromContract():
    '''returns None\n\n
    copyFromContract(final MboRemote contractRemote)\n
    '''
def changeVendorTaxInfo():
    '''returns None\n\n
    changeVendorTaxInfo(final MboRemote mboRemote)\n
    '''
def nullVendor():
    '''returns None\n\n
    nullVendor()\n
    '''
def createInvoiceForWarrSched():
    '''returns MboRemote\n\n
    createInvoiceForWarrSched(final MboRemote schedule, final double quantity, final double lineCost)\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet(final String name)\n
    '''
def checkAndClearAllocatedLines():
    '''returns None\n\n
    checkAndClearAllocatedLines()\n
    '''
def canCopyPOLines():
    '''returns None\n\n
    canCopyPOLines()\n
    '''
def setPOHash():
    '''returns None\n\n
    setPOHash(final PORemote thePO)\n
    '''
def isConditionEnabled():
    '''returns None\n\n
    isConditionEnabled(final MboSetRemote poLineSet, final boolean copyFromPOLineTab)\n
    '''
def smartFindByObjectName():
    '''returns MboSetRemote\n\n
    smartFindByObjectName(final String sourceObj, final String targetAttrName, final String value, final boolean exact)\n
    '''
def canReverseInvoice():
    '''returns None\n\n
    canReverseInvoice()\n
    '''
def createReverseInvoice():
    '''returns None\n\n
    createReverseInvoice(final String status)\n
    createReverseInvoice(final String invoiceNum, final String description, final String revReason, final Date glPostdate, final String status)\n
    '''
def canDeleteAttachedDocs():
    '''returns None\n\n
    canDeleteAttachedDocs()\n
    '''
def canDuplicateInvoice():
    '''returns None\n\n
    canDuplicateInvoice()\n
    '''
def canChangeVendor():
    '''returns None\n\n
    canChangeVendor()\n
    '''
def isReverseInvoice():
    '''returns boolean\n\n
    isReverseInvoice()\n
    '''
def defineSysCode():
    '''returns long[]\n\n
    defineSysCode()\n
    '''
def getSysCode():
    '''returns long\n\n
    getSysCode(final int i)\n
    '''
def setInvoiceMatchReversed():
    '''returns None\n\n
    setInvoiceMatchReversed()\n
    '''
def createInvoiceLineForCons():
    '''returns None\n\n
    createInvoiceLineForCons(final MboSetRemote transSet)\n
    createInvoiceLineForCons(final ArrayList consTransByVendorList)\n
    '''
def updateConsTransInvoiceNum():
    '''returns None\n\n
    updateConsTransInvoiceNum(final boolean clearInvoiceNum)\n
    '''
def createVarTransForConInvoice():
    '''returns None\n\n
    createVarTransForConInvoice()\n
    '''
def isConsignmentInvoice():
    '''returns boolean\n\n
    isConsignmentInvoice()\n
    '''
def isOrgInvoiceSchedType():
    '''returns boolean\n\n
    isOrgInvoiceSchedType()\n
    '''
def toPostDontCheckCompleteFlag():
    '''returns boolean\n\n
    toPostDontCheckCompleteFlag(final MboRemote thePO, final MboRemote invoiceLine, final MboRemote theReceipt)\n
    '''
def taxWithinTolerance():
    '''returns boolean\n\n
    taxWithinTolerance(final double lineTaxTotal, final double totalTax)\n
    '''
def createDepreciation():
    '''returns None\n\n
    createDepreciation(final boolean recalculationPoint, final List<String> warnings)\n
    '''
def checkDepreciation():
    '''returns boolean\n\n
    checkDepreciation()\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def getRemainingQty():
    '''returns double\n\n
    getRemainingQty(final MboRemote receipt)\n
    '''
def getRemainingCost():
    '''returns double\n\n
    getRemainingCost(final MboRemote receipt)\n
    '''
def getNewlyAllocated():
    '''returns double[]\n\n
    getNewlyAllocated(final String invoiceLineNum, final String receiptID)\n
    '''
def getUninvoicedReceipts():
    '''returns Vector<MboRemote>\n\n
    getUninvoicedReceipts(final String poNum, final String polinenum, final int type, final boolean isCreditInvoice, final String siteID, final boolean isNegativeLine, final String receiptID)\n
    '''
def update():
    '''returns None\n\n
    update(final MboRemote invoiceLine, final MboRemote receipt, final double qty, final double cost)\n
    '''
def getIssueUnitCost():
    '''returns double\n\n
    getIssueUnitCost(final MboRemote receipt, final MboRemote invoiceLine)\n
    '''
def getQty():
    '''returns double\n\n
    getQty()\n
    '''
def setQty():
    '''returns None\n\n
    setQty(final double qtyToBe)\n
    '''
def getCost():
    '''returns double\n\n
    getCost()\n
    '''
def setCost():
    '''returns None\n\n
    setCost(final double costToBe)\n
    '''
def getReceipt():
    '''returns MboRemote\n\n
    getReceipt()\n
    '''
def setReceipt():
    '''returns None\n\n
    setReceipt(final MboRemote receiptToBe)\n
    '''
