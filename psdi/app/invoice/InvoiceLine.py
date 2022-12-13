def InvoiceLine():
    '''public InvoiceLine(final MboSet ms)
    '''
def getNewInvoiceCost():
    '''public InvoiceCostRemote getNewInvoiceCost()
    '''
def init():
    '''public void init()
    '''
def add():
    '''public void add()
    '''
def modify():
    '''public void modify()
    '''
def canDelete():
    '''public void canDelete()
    '''
def delete():
    '''public void delete(final long accessModifier)
    '''
def getPOToInvCur():
    '''public double getPOToInvCur()
    '''
def recalculatePreTaxTotalWhenDelete():
    '''public void recalculatePreTaxTotalWhenDelete()
    '''
def appValidate():
    '''public void appValidate()
    '''
def validateInvoiceMatch():
    '''public void validateInvoiceMatch()
    '''
def copyPOLine():
    '''public void copyPOLine()
    '''
def clearPOLine():
    '''public void clearPOLine()
    '''
def validateCurrency():
    '''public void validateCurrency(final String invoiceCurrency)
    '''
def validateInvoiceMatchForApproval():
    '''public void validateInvoiceMatchForApproval()
    '''
def checkForServiceProrating():
    '''public void checkForServiceProrating()
    '''
def checkForPOLineTolerance():
    '''public void checkForPOLineTolerance(final Double upperTolerancePct, final Double lowerTolerancePct, final Double upperToleranceAmt, final Double lowerToleranceAmt)
    '''
def createDefaultServiceReceipt():
    '''public MboRemote createDefaultServiceReceipt()
    '''
def createDefaultMaterialReceipt():
    '''public MboRemote createDefaultMaterialReceipt()
    '''
def createDefaultReceipt():
    '''public MboRemote createDefaultReceipt()
    public MboRemote createDefaultReceipt(final MboSetRemote desiredReceipts)
    '''
def getInvoiceMatchSet():
    '''public InvoiceMatchSetRemote getInvoiceMatchSet()
    '''
def createReceipts():
    '''public void createReceipts()
    '''
def calcProrateCostForReceipt():
    '''public double calcProrateCostForReceipt()
    '''
def getRatioForTransaction():
    '''public double getRatioForTransaction()
    '''
def needProcessVariance():
    '''public boolean needProcessVariance()
    '''
def createReceiptOrTransactionForVariance():
    '''public void createReceiptOrTransactionForVariance()
    '''
def createTransactionsAfterAppr():
    '''public void createTransactionsAfterAppr(final double currencyVar, final double priceVar)
    '''
def findOrigReceiptSum():
    '''public double findOrigReceiptSum(final String attribute)
    '''
def createInvoiceTrans():
    '''public void createInvoiceTrans()
    '''
def returnGls():
    '''public Vector returnGls(final boolean updateInventory, final boolean varType)
    public Vector returnGls(final boolean updateInventory, final boolean varType, final MboRemote transMbo)
    '''
def getIssue():
    '''public boolean getIssue()
    '''
def moveToTop():
    '''public synchronized void moveToTop(final Vector<MboRemote> receipts, final String receiptId)
    '''
def getUnmatched():
    '''public double getUnmatched()
    '''
def afterAdd():
    '''public void afterAdd()
    '''
def getValidateOrder():
    '''public String[] getValidateOrder()
    '''
def setCurVarTotal():
    '''public void setCurVarTotal(final double currencyVariance)
    '''
def setPriceVarTotal():
    '''public void setPriceVarTotal(final double priceVariance)
    '''
def copyReceiptPOLineToInvoiceLine():
    '''public void copyReceiptPOLineToInvoiceLine(final MboRemote receiptOrPOLine, final double qty, final double cost)
    '''
def copyReceiptToInvoiceLine():
    '''public void copyReceiptToInvoiceLine(final MboRemote receipt, final double qty, final double cost)
    '''
def copyPOLineToInvoiceLine():
    '''public void copyPOLineToInvoiceLine(final MboRemote poLine, final double qty, final double cost)
    '''
def createInvoiceCostFromInvoiceLine():
    '''public void createInvoiceCostFromInvoiceLine(final MboRemote newInvoiceLine, final MboRemote poLine)
    '''
def copy():
    '''public MboRemote copy(final MboSetRemote mboSet)
    '''
def canDistributeInvoiceLine():
    '''public void canDistributeInvoiceLine()
    '''
def canDistributeProrateInvoiceLine():
    '''public void canDistributeProrateInvoiceLine()
    '''
def canAllocateServices():
    '''public void canAllocateServices()
    '''
def CanAllocateServIfEnteredOrWappr():
    '''public void CanAllocateServIfEnteredOrWappr()
    '''
def initRelationship():
    '''public void initRelationship(final String relationName, final MboSetRemote mboSet)
    '''
def canDistributeIssueInvoiceLine():
    '''public void canDistributeIssueInvoiceLine()
    '''
def updateWOCosts():
    '''public void updateWOCosts()
    '''
def undelete():
    '''public void undelete()
    '''
def creatInvTransForProrate():
    '''public void creatInvTransForProrate(final double prorateCostForInvTrans)
    '''
def getRatioGoesToReceipt():
    '''public double getRatioGoesToReceipt()
    '''
def recalcDistribution():
    '''public void recalcDistribution()
    '''
def getInternalLineType():
    '''public String getInternalLineType()
    '''
def addCostFromPOLine():
    '''public void addCostFromPOLine(final InvoiceCostSetRemote invCostSet, final MboRemote poLine)
    '''
def isServiceType():
    '''public boolean isServiceType()
    '''
def setPriceQtyFields():
    '''public void setPriceQtyFields()
    '''
def checkWOAssetLocGLDebitForLine():
    '''public void checkWOAssetLocGLDebitForLine()
    '''
def clearClassification():
    '''public void clearClassification()
    '''
def getDefaultTaxExempt():
    '''public void getDefaultTaxExempt(final MboRemote itemRemote, final MboRemote invVendor)
    '''
def getDefaultTaxCodes():
    '''public void getDefaultTaxCodes(final MboRemote itemRemote, final MboRemote invVendor)
    '''
def getInventoryCurbal():
    '''public double getInventoryCurbal()
    '''
def getActivePO():
    '''public MboRemote getActivePO()
    '''
def copyConsTransToInvoiceLine():
    '''public void copyConsTransToInvoiceLine(final MboRemote transMbo)
    '''
def updateConsTransInvoiceNum():
    '''public void updateConsTransInvoiceNum(final boolean clearInvoiceNum)
    '''
def createVarTransForConsInvoiceLine():
    '''public void createVarTransForConsInvoiceLine()
    '''
def setReadOnlyForConsInvoice():
    '''public void setReadOnlyForConsInvoice()
    '''
def getConsTransMbo():
    '''public MboRemote getConsTransMbo(final String origTransaction, final int transID)
    '''
def save():
    '''public void save()
    '''
def clearLabTransOnDelete():
    '''public void clearLabTransOnDelete()
    '''
def setPOLineFromCopyPOLine():
    '''public void setPOLineFromCopyPOLine(final MboRemote poLineFromCopyPOline)
    '''
def getPOLineFromCopyPOLine():
    '''public MboRemote getPOLineFromCopyPOLine()
    '''
