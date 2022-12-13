def Invoice():
    '''public Invoice(final MboSet ms)
    '''
def getProcess():
    '''public String getProcess()
    '''
def init():
    '''public void init()
    '''
def initRelationship():
    '''public void initRelationship(final String relationName, final MboSetRemote mboSet)
    '''
def setRelatedMboEditibility():
    '''public void setRelatedMboEditibility(final String relationName, final MboSetRemote mboSet)
    '''
def setCompanyValues():
    '''public void setCompanyValues()
    '''
def getExternalStatus():
    '''public String getExternalStatus(final String internalStatus)
    '''
def getStatusListName():
    '''public String getStatusListName()
    '''
def isSyscodeSet():
    '''public boolean isSyscodeSet(final long field)
    public boolean isSyscodeSet()
    '''
def setSyscode():
    '''public void setSyscode(final long field)
    '''
def clearSyscode():
    '''public void clearSyscode(final long field)
    '''
def add():
    '''public void add()
    '''
def generateAutoKey():
    '''public void generateAutoKey()
    '''
def modify():
    '''public void modify()
    '''
def validateForApproval():
    '''public void validateForApproval()
    '''
def appValidate():
    '''public void appValidate()
    '''
def checkForServiceLinePOTolerance():
    '''public void checkForServiceLinePOTolerance()
    '''
def checkForPOLineTolerance():
    '''public void checkForPOLineTolerance()
    '''
def checkForServiceLineTolerance():
    '''public void checkForServiceLineTolerance()
    '''
def checkForTaxTolerance():
    '''public void checkForTaxTolerance()
    '''
def totalInclusiveTax():
    '''public double totalInclusiveTax()
    '''
def approve():
    '''public void approve()
    '''
def setExchangeRateLineCost2():
    '''public void setExchangeRateLineCost2()
    '''
def prorateTotalTaxDifference():
    '''public void prorateTotalTaxDifference()
    '''
def calcIntermediateLoadedCost():
    '''public void calcIntermediateLoadedCost()
    '''
def createInvoiceTransForTaxes():
    '''public void createInvoiceTransForTaxes()
    '''
def createInvoiceTransTotal():
    '''public void createInvoiceTransTotal()
    '''
def setRequiredInvoiceTransFields():
    '''public void setRequiredInvoiceTransFields(final MboRemote invoiceLine, final MboRemote newInvoiceTrans, final int j)
    '''
def createInvoiceForReceipt():
    '''public MboRemote createInvoiceForReceipt(final MboRemote receipt)
    '''
def canDelete():
    '''public void canDelete()
    '''
def delete():
    '''public void delete(final long accessModifier)
    '''
def getValidateOrder():
    '''public String[] getValidateOrder()
    '''
def getUninvoicedReceiptsInfo():
    '''public UninvoicedReceiptsInfo getUninvoicedReceiptsInfo()
    '''
def getAllUninvoicedReceipts():
    '''public Vector<MboRemote> getAllUninvoicedReceipts(final String poNum, final String poLineNum, final int receiptType, final String siteID, final boolean isNegativeLine, final String receiptID)
    '''
def getAllUninvoicedMatReceipts():
    '''public Vector<MboRemote> getAllUninvoicedMatReceipts(final String poNum, final String poLineNum, final String siteID, final boolean isNegativeLine, final String receiptID)
    '''
def getAllUninvoicedServReceipts():
    '''public Vector<MboRemote> getAllUninvoicedServReceipts(final String poNum, final String poLineNum, final String siteID, final boolean isNegativeLine, final String receiptID)
    '''
def findMatch():
    '''public Vector findMatch(final boolean exactFirst, final Vector uninvoicedReceipts, final double minimumSigned, final double maximumSigned, final boolean byCost, final boolean considerTax, final boolean partialAllowed, final InvoiceLineRemote invoiceLine, final POLineRemote poline)
    public Vector findMatch(final boolean exactFirst, final Vector uninvoicedReceipts, final double value, final boolean byCost, final InvoiceLineRemote invoiceLine, final POLineRemote poline)
    '''
def confirmMatch():
    '''public void confirmMatch(final MboRemote invoiceLine, final Vector matchReceipts)
    '''
def createInvoiceTransAfterAppr():
    '''public void createInvoiceTransAfterAppr(final MboRemote invoice, final double currencyVariance, final double priceVariance)
    public void createInvoiceTransAfterAppr(final String invoicenum, final double currencyVariance, final double priceVariance)
    '''
def duplicate():
    '''public MboRemote duplicate()
    '''
def copyPOLineToInvoiceLine():
    '''public MboSetRemote copyPOLineToInvoiceLine(final MboSetRemote poLineSet)
    '''
def changeStatus():
    '''public void changeStatus(final String status, final Date date, final String memo, final long accessModifier)
    public void changeStatus(final String status, final Date date, final String memo, final boolean autoClosePo)
    public void changeStatus(final String status, final Date date, final String memo)
    '''
def calculateUnInvoicedTotal():
    '''public double calculateUnInvoicedTotal()
    '''
def copyReceiptToInvoiceLine():
    '''public MboSetRemote copyReceiptToInvoiceLine(final MboSetRemote receiptSet)
    '''
def canAllocateService():
    '''public void canAllocateService()
    '''
def getAllocatePrepSets():
    '''public InvoiceLineSetRemote[] getAllocatePrepSets(final InvoiceLineSetRemote toBeAllocated, final InvoiceLineSetRemote acceptingLines)
    '''
def validateAndCompleteAllocation():
    '''public void validateAndCompleteAllocation(final InvoiceLineSetRemote toBeAllocated, final InvoiceLineSetRemote acceptingLines)
    '''
def allocateServices():
    '''public void allocateServices(final InvoiceLineSetRemote toBeAllocated, final InvoiceLineSetRemote acceptingLines)
    '''
def cancelAllocateService():
    '''public void cancelAllocateService()
    '''
def resetTotalAllocated():
    '''public void resetTotalAllocated(final InvoiceLineSetRemote lineSet)
    '''
def getPOReference():
    '''public MboRemote getPOReference()
    '''
def setPOReference():
    '''public void setPOReference(final MboRemote poRemote)
    '''
def checkForOpenStatus():
    '''public void checkForOpenStatus()
    '''
def getCopyPOLineSet():
    '''public MboSetRemote getCopyPOLineSet(final String tbName)
    '''
def isCreditInvoice():
    '''public boolean isCreditInvoice()
    '''
def save():
    '''public void save()
    '''
def getWOReference():
    '''public MboRemote getWOReference(final String wonum)
    public MboRemote getWOReference(final String wonum, final String siteID)
    '''
def setTaxGLs():
    '''public void setTaxGLs(final String taxCode, final int typeCode)
    '''
def copyTerms():
    '''public void copyTerms(final MboSetRemote termsSet)
    '''
def createInvoiceForPurchSched():
    '''public MboRemote createInvoiceForPurchSched(final MboRemote poLine, final MboRemote scheduleLine, final MboRemote receipt)
    '''
def createInvoiceForLabTrans():
    '''public MboRemote createInvoiceForLabTrans(final MboRemote labTrans, final double quantity, double lineCost, final boolean lineByLine)
    '''
def createInvoiceForLeaseSched():
    '''public MboRemote createInvoiceForLeaseSched(final MboRemote schedule, final double quantity, final double lineCost, final boolean singleLine)
    '''
def copyFromContract():
    '''public void copyFromContract(final MboRemote contractRemote)
    '''
def changeVendorTaxInfo():
    '''public void changeVendorTaxInfo(final MboRemote mboRemote)
    '''
def nullVendor():
    '''public void nullVendor()
    '''
def createInvoiceForWarrSched():
    '''public MboRemote createInvoiceForWarrSched(final MboRemote schedule, final double quantity, final double lineCost)
    '''
def getMboSet():
    '''public MboSetRemote getMboSet(final String name)
    '''
def checkAndClearAllocatedLines():
    '''public void checkAndClearAllocatedLines()
    '''
def canCopyPOLines():
    '''public void canCopyPOLines()
    '''
def getPOHash():
    '''public Hashtable<String, MboRemote> getPOHash()
    '''
def setPOHash():
    '''public void setPOHash(final PORemote thePO)
    '''
def isConditionEnabled():
    '''public void isConditionEnabled(final MboSetRemote poLineSet, final boolean copyFromPOLineTab)
    '''
def smartFindByObjectName():
    '''public MboSetRemote smartFindByObjectName(final String sourceObj, final String targetAttrName, final String value, final boolean exact)
    '''
def canReverseInvoice():
    '''public void canReverseInvoice()
    '''
def createReverseInvoice():
    '''public void createReverseInvoice(final String status)
    public void createReverseInvoice(final String invoiceNum, final String description, final String revReason, final Date glPostdate, final String status)
    '''
def canDeleteAttachedDocs():
    '''public void canDeleteAttachedDocs()
    '''
def canDuplicateInvoice():
    '''public void canDuplicateInvoice()
    '''
def canChangeVendor():
    '''public void canChangeVendor()
    '''
def isReverseInvoice():
    '''public boolean isReverseInvoice()
    '''
def defineSysCode():
    '''public long[] defineSysCode()
    '''
def getSysCode():
    '''public long getSysCode(final int i)
    '''
def setInvoiceMatchReversed():
    '''public void setInvoiceMatchReversed()
    '''
def createInvoiceLineForCons():
    '''public void createInvoiceLineForCons(final MboSetRemote transSet)
    public void createInvoiceLineForCons(final ArrayList consTransByVendorList)
    '''
def updateConsTransInvoiceNum():
    '''public void updateConsTransInvoiceNum(final boolean clearInvoiceNum)
    '''
def createVarTransForConInvoice():
    '''public void createVarTransForConInvoice()
    '''
def isConsignmentInvoice():
    '''public boolean isConsignmentInvoice()
    '''
def isOrgInvoiceSchedType():
    '''public boolean isOrgInvoiceSchedType()
    '''
def toPostDontCheckCompleteFlag():
    '''public boolean toPostDontCheckCompleteFlag(final MboRemote thePO, final MboRemote invoiceLine, final MboRemote theReceipt)
    '''
def taxWithinTolerance():
    '''public boolean taxWithinTolerance(final double lineTaxTotal, final double totalTax)
    '''
def createDepreciation():
    '''public void createDepreciation(final boolean recalculationPoint, final List<String> warnings)
    '''
def checkDepreciation():
    '''public boolean checkDepreciation()
    '''
def UninvoicedReceiptsInfo():
    '''public UninvoicedReceiptsInfo(final Invoice inv)
    '''
def destroy():
    '''public void destroy()
    '''
def getRemainingQty():
    '''public double getRemainingQty(final MboRemote receipt)
    '''
def getRemainingCost():
    '''public double getRemainingCost(final MboRemote receipt)
    '''
def getNewlyAllocated():
    '''public double[] getNewlyAllocated(final String invoiceLineNum, final String receiptID)
    '''
def getUninvoicedReceipts():
    '''public Vector<MboRemote> getUninvoicedReceipts(final String poNum, final String polinenum, final int type, final boolean isCreditInvoice, final String siteID, final boolean isNegativeLine, final String receiptID)
    '''
def update():
    '''public void update(final MboRemote invoiceLine, final MboRemote receipt, final double qty, final double cost)
    '''
def getIssueUnitCost():
    '''public double getIssueUnitCost(final MboRemote receipt, final MboRemote invoiceLine)
    '''
def MatchResult():
    '''public MatchResult(final MboRemote theReceipt, final double theQty, final double theCost)
    '''
def getQty():
    '''public double getQty()
    '''
def setQty():
    '''public void setQty(final double qtyToBe)
    '''
def getCost():
    '''public double getCost()
    '''
def setCost():
    '''public void setCost(final double costToBe)
    '''
def getReceipt():
    '''public MboRemote getReceipt()
    '''
def setReceipt():
    '''public void setReceipt(final MboRemote receiptToBe)
    '''
