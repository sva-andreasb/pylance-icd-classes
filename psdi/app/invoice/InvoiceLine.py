def InvoiceLine():
'''public InvoiceLine(final MboSet ms)
'''
pass
def getNewInvoiceCost():
'''public InvoiceCostRemote getNewInvoiceCost()
'''
pass
def init():
'''public void init()
'''
pass
def add():
'''public void add()
'''
pass
def modify():
'''public void modify()
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
def getPOToInvCur():
'''public double getPOToInvCur()
'''
pass
def recalculatePreTaxTotalWhenDelete():
'''public void recalculatePreTaxTotalWhenDelete()
'''
pass
def appValidate():
'''public void appValidate()
'''
pass
def validateInvoiceMatch():
'''public void validateInvoiceMatch()
'''
pass
def copyPOLine():
'''public void copyPOLine()
'''
pass
def clearPOLine():
'''public void clearPOLine()
'''
pass
def validateCurrency():
'''public void validateCurrency(final String invoiceCurrency)
'''
pass
def validateInvoiceMatchForApproval():
'''public void validateInvoiceMatchForApproval()
'''
pass
def checkForServiceProrating():
'''public void checkForServiceProrating()
'''
pass
def checkForPOLineTolerance():
'''public void checkForPOLineTolerance(final Double upperTolerancePct, final Double lowerTolerancePct, final Double upperToleranceAmt, final Double lowerToleranceAmt)
'''
pass
def createDefaultServiceReceipt():
'''public MboRemote createDefaultServiceReceipt()
'''
pass
def createDefaultMaterialReceipt():
'''public MboRemote createDefaultMaterialReceipt()
'''
pass
def createDefaultReceipt():
'''public MboRemote createDefaultReceipt()
public MboRemote createDefaultReceipt(final MboSetRemote desiredReceipts)
'''
pass
def getInvoiceMatchSet():
'''public InvoiceMatchSetRemote getInvoiceMatchSet()
'''
pass
def createReceipts():
'''public void createReceipts()
'''
pass
def calcProrateCostForReceipt():
'''public double calcProrateCostForReceipt()
'''
pass
def getRatioForTransaction():
'''public double getRatioForTransaction()
'''
pass
def needProcessVariance():
'''public boolean needProcessVariance()
'''
pass
def createReceiptOrTransactionForVariance():
'''public void createReceiptOrTransactionForVariance()
'''
pass
def createTransactionsAfterAppr():
'''public void createTransactionsAfterAppr(final double currencyVar, final double priceVar)
'''
pass
def findOrigReceiptSum():
'''public double findOrigReceiptSum(final String attribute)
'''
pass
def createInvoiceTrans():
'''public void createInvoiceTrans()
'''
pass
def returnGls():
'''public Vector returnGls(final boolean updateInventory, final boolean varType)
public Vector returnGls(final boolean updateInventory, final boolean varType, final MboRemote transMbo)
'''
pass
def getIssue():
'''public boolean getIssue()
'''
pass
def moveToTop():
'''public synchronized void moveToTop(final Vector<MboRemote> receipts, final String receiptId)
'''
pass
def getUnmatched():
'''public double getUnmatched()
'''
pass
def afterAdd():
'''public void afterAdd()
'''
pass
def getValidateOrder():
'''public String[] getValidateOrder()
'''
pass
def setCurVarTotal():
'''public void setCurVarTotal(final double currencyVariance)
'''
pass
def setPriceVarTotal():
'''public void setPriceVarTotal(final double priceVariance)
'''
pass
def copyReceiptPOLineToInvoiceLine():
'''public void copyReceiptPOLineToInvoiceLine(final MboRemote receiptOrPOLine, final double qty, final double cost)
'''
pass
def copyReceiptToInvoiceLine():
'''public void copyReceiptToInvoiceLine(final MboRemote receipt, final double qty, final double cost)
'''
pass
def copyPOLineToInvoiceLine():
'''public void copyPOLineToInvoiceLine(final MboRemote poLine, final double qty, final double cost)
'''
pass
def createInvoiceCostFromInvoiceLine():
'''public void createInvoiceCostFromInvoiceLine(final MboRemote newInvoiceLine, final MboRemote poLine)
'''
pass
def copy():
'''public MboRemote copy(final MboSetRemote mboSet)
'''
pass
def canDistributeInvoiceLine():
'''public void canDistributeInvoiceLine()
'''
pass
def canDistributeProrateInvoiceLine():
'''public void canDistributeProrateInvoiceLine()
'''
pass
def canAllocateServices():
'''public void canAllocateServices()
'''
pass
def CanAllocateServIfEnteredOrWappr():
'''public void CanAllocateServIfEnteredOrWappr()
'''
pass
def initRelationship():
'''public void initRelationship(final String relationName, final MboSetRemote mboSet)
'''
pass
def canDistributeIssueInvoiceLine():
'''public void canDistributeIssueInvoiceLine()
'''
pass
def updateWOCosts():
'''public void updateWOCosts()
'''
pass
def undelete():
'''public void undelete()
'''
pass
def creatInvTransForProrate():
'''public void creatInvTransForProrate(final double prorateCostForInvTrans)
'''
pass
def getRatioGoesToReceipt():
'''public double getRatioGoesToReceipt()
'''
pass
def recalcDistribution():
'''public void recalcDistribution()
'''
pass
def getInternalLineType():
'''public String getInternalLineType()
'''
pass
def addCostFromPOLine():
'''public void addCostFromPOLine(final InvoiceCostSetRemote invCostSet, final MboRemote poLine)
'''
pass
def isServiceType():
'''public boolean isServiceType()
'''
pass
def setPriceQtyFields():
'''public void setPriceQtyFields()
'''
pass
def checkWOAssetLocGLDebitForLine():
'''public void checkWOAssetLocGLDebitForLine()
'''
pass
def clearClassification():
'''public void clearClassification()
'''
pass
def getDefaultTaxExempt():
'''public void getDefaultTaxExempt(final MboRemote itemRemote, final MboRemote invVendor)
'''
pass
def getDefaultTaxCodes():
'''public void getDefaultTaxCodes(final MboRemote itemRemote, final MboRemote invVendor)
'''
pass
def getInventoryCurbal():
'''public double getInventoryCurbal()
'''
pass
def getActivePO():
'''public MboRemote getActivePO()
'''
pass
def copyConsTransToInvoiceLine():
'''public void copyConsTransToInvoiceLine(final MboRemote transMbo)
'''
pass
def updateConsTransInvoiceNum():
'''public void updateConsTransInvoiceNum(final boolean clearInvoiceNum)
'''
pass
def createVarTransForConsInvoiceLine():
'''public void createVarTransForConsInvoiceLine()
'''
pass
def setReadOnlyForConsInvoice():
'''public void setReadOnlyForConsInvoice()
'''
pass
def getConsTransMbo():
'''public MboRemote getConsTransMbo(final String origTransaction, final int transID)
'''
pass
def save():
'''public void save()
'''
pass
def clearLabTransOnDelete():
'''public void clearLabTransOnDelete()
'''
pass
def setPOLineFromCopyPOLine():
'''public void setPOLineFromCopyPOLine(final MboRemote poLineFromCopyPOline)
'''
pass
def getPOLineFromCopyPOLine():
'''public MboRemote getPOLineFromCopyPOLine()
'''
pass
