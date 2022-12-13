def PO():
    '''public PO(final MboSet ms)
    '''
def getProcess():
    '''public String getProcess()
    '''
def setCancelFlag():
    '''public void setCancelFlag(final boolean po)
    '''
def getCancelFlag():
    '''public boolean getCancelFlag()
    '''
def resetCancelFlag():
    '''public void resetCancelFlag()
    '''
def getStatusListName():
    '''public String getStatusListName()
    '''
def init():
    '''public void init()
    '''
def initFieldFlagsOnMbo():
    '''public void initFieldFlagsOnMbo(final String attrName)
    '''
def add():
    '''public void add()
    '''
def isApproved():
    '''public boolean isApproved()
    '''
def isInternal():
    '''public boolean isInternal()
    '''
def createReceipt():
    '''public MboRemote createReceipt(final MboSetRemote existingReceiptSet, final long polinenum, final String ownersysid)
    '''
def createReturn():
    '''public MboRemote createReturn(final MatRecTransSet existingReceiptSet, final long polinenum, final MboRemote matRecTransMbo)
    public MboRemote createReturn(final MboSetRemote existingReceiptSet, final long polinenum, final String ownersysid)
    '''
def receive():
    '''public void receive(final MboSetRemote receiptSet, final int lineNumber, final double quantity, final String binnum)
    '''
def receiveRotatingItemOnInternalPO():
    '''public void receiveRotatingItemOnInternalPO(final MboSetRemote receiptSet, final int lineNumber, final String binnum, final String assetnum)
    '''
def determineReceiptStatus():
    '''public void determineReceiptStatus()
    public void determineReceiptStatus(final POLineRemote poLine)
    '''
def validatePO():
    '''public void validatePO()
    '''
def setTotalCost():
    '''public void setTotalCost()
    '''
def canCreateChangeOrder():
    '''public void canCreateChangeOrder()
    '''
def hasReceipts():
    '''public void hasReceipts()
    '''
def prorateServices():
    '''public void prorateServices()
    '''
def getAvailableFunds():
    '''public double getAvailableFunds()
    '''
def createPOLineFromPR():
    '''public MboRemote createPOLineFromPR(final MboRemote fromPR, final MboRemote fromPRLine, final MboSetRemote poLines)
    '''
def copySelectedLinesToRelease():
    '''public void copySelectedLinesToRelease(final PORemote toPOMbo)
    '''
def copyBlanketLinesToRelease():
    '''public void copyBlanketLinesToRelease(final PORemote toPOMbo)
    '''
def deleteDistributions():
    '''public void deleteDistributions()
    '''
def isPOBuyAhead():
    '''public boolean isPOBuyAhead()
    '''
def appValidate():
    '''public void appValidate()
    '''
def isPOStatusAPPR():
    '''public boolean isPOStatusAPPR()
    '''
def isPOStatusINPRG():
    '''public boolean isPOStatusINPRG()
    '''
def getPORecord():
    '''public Vector getPORecord()
    '''
def duplicate():
    '''public MboRemote duplicate()
    '''
def createChangeOrder():
    '''public MboRemote createChangeOrder(final String ponum, final String description)
    '''
def save():
    '''public void save()
    '''
def generateAutoKey():
    '''public void generateAutoKey()
    '''
def initRelationship():
    '''public void initRelationship(final String relationName, final MboSetRemote mboSet)
    '''
def setRelatedMboEditibility():
    '''public void setRelatedMboEditibility(final String relationName, final MboSetRemote mboSet)
    '''
def poSentToVendor():
    '''public void poSentToVendor()
    '''
def modify():
    '''public void modify()
    '''
def copyPRToCurrentPO():
    '''public void copyPRToCurrentPO(final MboSetRemote sourcePRLineSet)
    '''
def copyPRToNewPO():
    '''public void copyPRToNewPO(final MboSetRemote sourcePRLineSet)
    '''
def copySpareParts():
    '''public void copySpareParts(final MboSetRemote sparePartSet)
    '''
def addInvVendorItemsToPOLine():
    '''public void addInvVendorItemsToPOLine(final MboSetRemote invVendorSetRemote)
    '''
def canDuplicate():
    '''public void canDuplicate()
    '''
def addToReceiptVector():
    '''public void addToReceiptVector(final MboRemote receiptRemote)
    '''
def addToInvoiceLineVector():
    '''public void addToInvoiceLineVector(final MboRemote invoiceLineRemote)
    '''
def getReceiptVector():
    '''public Vector getReceiptVector()
    '''
def getInvoiceLineVector():
    '''public Vector getInvoiceLineVector()
    '''
def changeStatus():
    '''public void changeStatus(final String status, final Date date, final String memo, final long accessModifier)
    '''
def createContractFromPO():
    '''public void createContractFromPO(final String contractNum, final String description, final String contractType)
    '''
def checkingBeforeCreateContract():
    '''public void checkingBeforeCreateContract()
    '''
def checkWAPPRStatus():
    '''public void checkWAPPRStatus()
    '''
def copyDefaultTerms():
    '''public void copyDefaultTerms()
    '''
def updateReleasePO():
    '''public void updateReleasePO(final MboRemote contractRemote)
    '''
def createInvoicesForSchedule():
    '''public void createInvoicesForSchedule()
    '''
def canDelete():
    '''public void canDelete()
    '''
def checkingBeforeCompleteReceipts():
    '''public void checkingBeforeCompleteReceipts()
    '''
def getSharedWorkorder():
    '''public MboRemote getSharedWorkorder(final MboRemote mboRemote, final String wonum)
    '''
def setFromOnePO():
    '''public void setFromOnePO(final boolean flag)
    '''
def getFromOnePO():
    '''public boolean getFromOnePO()
    '''
def generateWO():
    '''public void generateWO()
    '''
def createSoftwareContractHeader():
    '''public MboRemote createSoftwareContractHeader(final String contractNum, final String description, final String contractType)
    '''
def getValidateOrder():
    '''public String[] getValidateOrder()
    '''
def canRevisePO():
    '''public void canRevisePO()
    '''
def revisePO():
    '''public MboRemote revisePO()
    public MboRemote revisePO(final String revDescription)
    public MboRemote revisePO(final String revDescription, boolean allowReceipt)
    '''
def getNextRevision():
    '''public MboRemote getNextRevision()
    '''
def getPreviousRevision():
    '''public MboRemote getPreviousRevision()
    '''
def getApprRevision():
    '''public MboRemote getApprRevision()
    '''
def updatePndRevPO():
    '''public void updatePndRevPO()
    '''
def checkPOLineQtyCost():
    '''public void checkPOLineQtyCost(final MboRemote pndrevPOLine)
    public void checkPOLineQtyCost(final MboRemote apprPOLine, final MboRemote pndrevPOLine)
    '''
def useLineOrLoadedCost():
    '''public String useLineOrLoadedCost()
    '''
def getMboSet():
    '''public MboSetRemote getMboSet(final String name)
    '''
def setDontCheckCompleteFlag():
    '''public void setDontCheckCompleteFlag(final boolean flag)
    '''
def getDontCheckCompleteFlag():
    '''public boolean getDontCheckCompleteFlag()
    '''
