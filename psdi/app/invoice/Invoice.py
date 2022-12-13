def Invoice():
'''public Invoice(final MboSet ms)
'''
pass
def getProcess():
'''public String getProcess()
'''
pass
def init():
'''public void init()
'''
pass
def initRelationship():
'''public void initRelationship(final String relationName, final MboSetRemote mboSet)
'''
pass
def setRelatedMboEditibility():
'''public void setRelatedMboEditibility(final String relationName, final MboSetRemote mboSet)
'''
pass
def setCompanyValues():
'''public void setCompanyValues()
'''
pass
def getExternalStatus():
'''public String getExternalStatus(final String internalStatus)
'''
pass
def getStatusListName():
'''public String getStatusListName()
'''
pass
def isSyscodeSet():
'''public boolean isSyscodeSet(final long field)
public boolean isSyscodeSet()
'''
pass
def setSyscode():
'''public void setSyscode(final long field)
'''
pass
def clearSyscode():
'''public void clearSyscode(final long field)
'''
pass
def add():
'''public void add()
'''
pass
def generateAutoKey():
'''public void generateAutoKey()
'''
pass
def modify():
'''public void modify()
'''
pass
def validateForApproval():
'''public void validateForApproval()
'''
pass
def appValidate():
'''public void appValidate()
'''
pass
def checkForServiceLinePOTolerance():
'''public void checkForServiceLinePOTolerance()
'''
pass
def checkForPOLineTolerance():
'''public void checkForPOLineTolerance()
'''
pass
def checkForServiceLineTolerance():
'''public void checkForServiceLineTolerance()
'''
pass
def checkForTaxTolerance():
'''public void checkForTaxTolerance()
'''
pass
def totalInclusiveTax():
'''public double totalInclusiveTax()
'''
pass
def approve():
'''public void approve()
'''
pass
def setExchangeRateLineCost2():
'''public void setExchangeRateLineCost2()
'''
pass
def prorateTotalTaxDifference():
'''public void prorateTotalTaxDifference()
'''
pass
def calcIntermediateLoadedCost():
'''public void calcIntermediateLoadedCost()
'''
pass
def createInvoiceTransForTaxes():
'''public void createInvoiceTransForTaxes()
'''
pass
def createInvoiceTransTotal():
'''public void createInvoiceTransTotal()
'''
pass
def setRequiredInvoiceTransFields():
'''public void setRequiredInvoiceTransFields(final MboRemote invoiceLine, final MboRemote newInvoiceTrans, final int j)
'''
pass
def createInvoiceForReceipt():
'''public MboRemote createInvoiceForReceipt(final MboRemote receipt)
'''
pass
def canDelete():
'''public void canDelete()
'''
pass
def delete():
'''public void delete(final long accessModifier)
'''
pass
def getValidateOrder():
'''public String[] getValidateOrder()
'''
pass
def getUninvoicedReceiptsInfo():
'''public UninvoicedReceiptsInfo getUninvoicedReceiptsInfo()
'''
pass
def getAllUninvoicedReceipts():
'''public Vector<MboRemote> getAllUninvoicedReceipts(final String poNum, final String poLineNum, final int receiptType, final String siteID, final boolean isNegativeLine, final String receiptID)
'''
pass
def getAllUninvoicedMatReceipts():
'''public Vector<MboRemote> getAllUninvoicedMatReceipts(final String poNum, final String poLineNum, final String siteID, final boolean isNegativeLine, final String receiptID)
'''
pass
def getAllUninvoicedServReceipts():
'''public Vector<MboRemote> getAllUninvoicedServReceipts(final String poNum, final String poLineNum, final String siteID, final boolean isNegativeLine, final String receiptID)
'''
pass
def findMatch():
'''public Vector findMatch(final boolean exactFirst, final Vector uninvoicedReceipts, final double minimumSigned, final double maximumSigned, final boolean byCost, final boolean considerTax, final boolean partialAllowed, final InvoiceLineRemote invoiceLine, final POLineRemote poline)
public Vector findMatch(final boolean exactFirst, final Vector uninvoicedReceipts, final double value, final boolean byCost, final InvoiceLineRemote invoiceLine, final POLineRemote poline)
'''
pass
def confirmMatch():
'''public void confirmMatch(final MboRemote invoiceLine, final Vector matchReceipts)
'''
pass
def createInvoiceTransAfterAppr():
'''public void createInvoiceTransAfterAppr(final MboRemote invoice, final double currencyVariance, final double priceVariance)
public void createInvoiceTransAfterAppr(final String invoicenum, final double currencyVariance, final double priceVariance)
'''
pass
def duplicate():
'''public MboRemote duplicate()
'''
pass
def copyPOLineToInvoiceLine():
'''public MboSetRemote copyPOLineToInvoiceLine(final MboSetRemote poLineSet)
'''
pass
def changeStatus():
'''public void changeStatus(final String status, final Date date, final String memo, final long accessModifier)
public void changeStatus(final String status, final Date date, final String memo, final boolean autoClosePo)
public void changeStatus(final String status, final Date date, final String memo)
'''
pass
def calculateUnInvoicedTotal():
'''public double calculateUnInvoicedTotal()
'''
pass
def copyReceiptToInvoiceLine():
'''public MboSetRemote copyReceiptToInvoiceLine(final MboSetRemote receiptSet)
'''
pass
def canAllocateService():
'''public void canAllocateService()
'''
pass
def getAllocatePrepSets():
'''public InvoiceLineSetRemote[] getAllocatePrepSets(final InvoiceLineSetRemote toBeAllocated, final InvoiceLineSetRemote acceptingLines)
'''
pass
def validateAndCompleteAllocation():
'''public void validateAndCompleteAllocation(final InvoiceLineSetRemote toBeAllocated, final InvoiceLineSetRemote acceptingLines)
'''
pass
def allocateServices():
'''public void allocateServices(final InvoiceLineSetRemote toBeAllocated, final InvoiceLineSetRemote acceptingLines)
'''
pass
def cancelAllocateService():
'''public void cancelAllocateService()
'''
pass
def resetTotalAllocated():
'''public void resetTotalAllocated(final InvoiceLineSetRemote lineSet)
'''
pass
def getPOReference():
'''public MboRemote getPOReference()
'''
pass
def setPOReference():
'''public void setPOReference(final MboRemote poRemote)
'''
pass
def checkForOpenStatus():
'''public void checkForOpenStatus()
'''
pass
def getCopyPOLineSet():
'''public MboSetRemote getCopyPOLineSet(final String tbName)
'''
pass
def isCreditInvoice():
'''public boolean isCreditInvoice()
'''
pass
def save():
'''public void save()
'''
pass
def getWOReference():
'''public MboRemote getWOReference(final String wonum)
public MboRemote getWOReference(final String wonum, final String siteID)
'''
pass
def setTaxGLs():
'''public void setTaxGLs(final String taxCode, final int typeCode)
'''
pass
def copyTerms():
'''public void copyTerms(final MboSetRemote termsSet)
'''
pass
def createInvoiceForPurchSched():
'''public MboRemote createInvoiceForPurchSched(final MboRemote poLine, final MboRemote scheduleLine, final MboRemote receipt)
'''
pass
def createInvoiceForLabTrans():
'''public MboRemote createInvoiceForLabTrans(final MboRemote labTrans, final double quantity, double lineCost, final boolean lineByLine)
'''
pass
def createInvoiceForLeaseSched():
'''public MboRemote createInvoiceForLeaseSched(final MboRemote schedule, final double quantity, final double lineCost, final boolean singleLine)
'''
pass
def copyFromContract():
'''public void copyFromContract(final MboRemote contractRemote)
'''
pass
def changeVendorTaxInfo():
'''public void changeVendorTaxInfo(final MboRemote mboRemote)
'''
pass
def nullVendor():
'''public void nullVendor()
'''
pass
def createInvoiceForWarrSched():
'''public MboRemote createInvoiceForWarrSched(final MboRemote schedule, final double quantity, final double lineCost)
'''
pass
def getMboSet():
'''public MboSetRemote getMboSet(final String name)
'''
pass
def checkAndClearAllocatedLines():
'''public void checkAndClearAllocatedLines()
'''
pass
def canCopyPOLines():
'''public void canCopyPOLines()
'''
pass
def getPOHash():
'''public Hashtable<String, MboRemote> getPOHash()
'''
pass
def setPOHash():
'''public void setPOHash(final PORemote thePO)
'''
pass
def isConditionEnabled():
'''public void isConditionEnabled(final MboSetRemote poLineSet, final boolean copyFromPOLineTab)
'''
pass
def smartFindByObjectName():
'''public MboSetRemote smartFindByObjectName(final String sourceObj, final String targetAttrName, final String value, final boolean exact)
'''
pass
def canReverseInvoice():
'''public void canReverseInvoice()
'''
pass
def createReverseInvoice():
'''public void createReverseInvoice(final String status)
public void createReverseInvoice(final String invoiceNum, final String description, final String revReason, final Date glPostdate, final String status)
'''
pass
def canDeleteAttachedDocs():
'''public void canDeleteAttachedDocs()
'''
pass
def canDuplicateInvoice():
'''public void canDuplicateInvoice()
'''
pass
def canChangeVendor():
'''public void canChangeVendor()
'''
pass
def isReverseInvoice():
'''public boolean isReverseInvoice()
'''
pass
def defineSysCode():
'''public long[] defineSysCode()
'''
pass
def getSysCode():
'''public long getSysCode(final int i)
'''
pass
def setInvoiceMatchReversed():
'''public void setInvoiceMatchReversed()
'''
pass
def createInvoiceLineForCons():
'''public void createInvoiceLineForCons(final MboSetRemote transSet)
public void createInvoiceLineForCons(final ArrayList consTransByVendorList)
'''
pass
def updateConsTransInvoiceNum():
'''public void updateConsTransInvoiceNum(final boolean clearInvoiceNum)
'''
pass
def createVarTransForConInvoice():
'''public void createVarTransForConInvoice()
'''
pass
def isConsignmentInvoice():
'''public boolean isConsignmentInvoice()
'''
pass
def isOrgInvoiceSchedType():
'''public boolean isOrgInvoiceSchedType()
'''
pass
def toPostDontCheckCompleteFlag():
'''public boolean toPostDontCheckCompleteFlag(final MboRemote thePO, final MboRemote invoiceLine, final MboRemote theReceipt)
'''
pass
def taxWithinTolerance():
'''public boolean taxWithinTolerance(final double lineTaxTotal, final double totalTax)
'''
pass
def createDepreciation():
'''public void createDepreciation(final boolean recalculationPoint, final List<String> warnings)
'''
pass
def checkDepreciation():
'''public boolean checkDepreciation()
'''
pass
def UninvoicedReceiptsInfo():
'''public UninvoicedReceiptsInfo(final Invoice inv)
'''
pass
def destroy():
'''public void destroy()
'''
pass
def getRemainingQty():
'''public double getRemainingQty(final MboRemote receipt)
'''
pass
def getRemainingCost():
'''public double getRemainingCost(final MboRemote receipt)
'''
pass
def getNewlyAllocated():
'''public double[] getNewlyAllocated(final String invoiceLineNum, final String receiptID)
'''
pass
def getUninvoicedReceipts():
'''public Vector<MboRemote> getUninvoicedReceipts(final String poNum, final String polinenum, final int type, final boolean isCreditInvoice, final String siteID, final boolean isNegativeLine, final String receiptID)
'''
pass
def update():
'''public void update(final MboRemote invoiceLine, final MboRemote receipt, final double qty, final double cost)
'''
pass
def getIssueUnitCost():
'''public double getIssueUnitCost(final MboRemote receipt, final MboRemote invoiceLine)
'''
pass
def MatchResult():
'''public MatchResult(final MboRemote theReceipt, final double theQty, final double theCost)
'''
pass
def getQty():
'''public double getQty()
'''
pass
def setQty():
'''public void setQty(final double qtyToBe)
'''
pass
def getCost():
'''public double getCost()
'''
pass
def setCost():
'''public void setCost(final double costToBe)
'''
pass
def getReceipt():
'''public MboRemote getReceipt()
'''
pass
def setReceipt():
'''public void setReceipt(final MboRemote receiptToBe)
'''
pass
