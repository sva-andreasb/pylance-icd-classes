def PO():
'''public PO(final MboSet ms)
'''
pass
def getProcess():
'''public String getProcess()
'''
pass
def setCancelFlag():
'''public void setCancelFlag(final boolean po)
'''
pass
def getCancelFlag():
'''public boolean getCancelFlag()
'''
pass
def resetCancelFlag():
'''public void resetCancelFlag()
'''
pass
def getStatusListName():
'''public String getStatusListName()
'''
pass
def init():
'''public void init()
'''
pass
def initFieldFlagsOnMbo():
'''public void initFieldFlagsOnMbo(final String attrName)
'''
pass
def add():
'''public void add()
'''
pass
def isApproved():
'''public boolean isApproved()
'''
pass
def isInternal():
'''public boolean isInternal()
'''
pass
def createReceipt():
'''public MboRemote createReceipt(final MboSetRemote existingReceiptSet, final long polinenum, final String ownersysid)
'''
pass
def createReturn():
'''public MboRemote createReturn(final MatRecTransSet existingReceiptSet, final long polinenum, final MboRemote matRecTransMbo)
public MboRemote createReturn(final MboSetRemote existingReceiptSet, final long polinenum, final String ownersysid)
'''
pass
def receive():
'''public void receive(final MboSetRemote receiptSet, final int lineNumber, final double quantity, final String binnum)
'''
pass
def receiveRotatingItemOnInternalPO():
'''public void receiveRotatingItemOnInternalPO(final MboSetRemote receiptSet, final int lineNumber, final String binnum, final String assetnum)
'''
pass
def determineReceiptStatus():
'''public void determineReceiptStatus()
public void determineReceiptStatus(final POLineRemote poLine)
'''
pass
def validatePO():
'''public void validatePO()
'''
pass
def setTotalCost():
'''public void setTotalCost()
'''
pass
def canCreateChangeOrder():
'''public void canCreateChangeOrder()
'''
pass
def hasReceipts():
'''public void hasReceipts()
'''
pass
def prorateServices():
'''public void prorateServices()
'''
pass
def getAvailableFunds():
'''public double getAvailableFunds()
'''
pass
def createPOLineFromPR():
'''public MboRemote createPOLineFromPR(final MboRemote fromPR, final MboRemote fromPRLine, final MboSetRemote poLines)
'''
pass
def copySelectedLinesToRelease():
'''public void copySelectedLinesToRelease(final PORemote toPOMbo)
'''
pass
def copyBlanketLinesToRelease():
'''public void copyBlanketLinesToRelease(final PORemote toPOMbo)
'''
pass
def deleteDistributions():
'''public void deleteDistributions()
'''
pass
def isPOBuyAhead():
'''public boolean isPOBuyAhead()
'''
pass
def appValidate():
'''public void appValidate()
'''
pass
def isPOStatusAPPR():
'''public boolean isPOStatusAPPR()
'''
pass
def isPOStatusINPRG():
'''public boolean isPOStatusINPRG()
'''
pass
def getPORecord():
'''public Vector getPORecord()
'''
pass
def duplicate():
'''public MboRemote duplicate()
'''
pass
def createChangeOrder():
'''public MboRemote createChangeOrder(final String ponum, final String description)
'''
pass
def save():
'''public void save()
'''
pass
def generateAutoKey():
'''public void generateAutoKey()
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
def poSentToVendor():
'''public void poSentToVendor()
'''
pass
def modify():
'''public void modify()
'''
pass
def copyPRToCurrentPO():
'''public void copyPRToCurrentPO(final MboSetRemote sourcePRLineSet)
'''
pass
def copyPRToNewPO():
'''public void copyPRToNewPO(final MboSetRemote sourcePRLineSet)
'''
pass
def copySpareParts():
'''public void copySpareParts(final MboSetRemote sparePartSet)
'''
pass
def addInvVendorItemsToPOLine():
'''public void addInvVendorItemsToPOLine(final MboSetRemote invVendorSetRemote)
'''
pass
def canDuplicate():
'''public void canDuplicate()
'''
pass
def addToReceiptVector():
'''public void addToReceiptVector(final MboRemote receiptRemote)
'''
pass
def addToInvoiceLineVector():
'''public void addToInvoiceLineVector(final MboRemote invoiceLineRemote)
'''
pass
def getReceiptVector():
'''public Vector getReceiptVector()
'''
pass
def getInvoiceLineVector():
'''public Vector getInvoiceLineVector()
'''
pass
def changeStatus():
'''public void changeStatus(final String status, final Date date, final String memo, final long accessModifier)
'''
pass
def createContractFromPO():
'''public void createContractFromPO(final String contractNum, final String description, final String contractType)
'''
pass
def checkingBeforeCreateContract():
'''public void checkingBeforeCreateContract()
'''
pass
def checkWAPPRStatus():
'''public void checkWAPPRStatus()
'''
pass
def copyDefaultTerms():
'''public void copyDefaultTerms()
'''
pass
def updateReleasePO():
'''public void updateReleasePO(final MboRemote contractRemote)
'''
pass
def createInvoicesForSchedule():
'''public void createInvoicesForSchedule()
'''
pass
def canDelete():
'''public void canDelete()
'''
pass
def checkingBeforeCompleteReceipts():
'''public void checkingBeforeCompleteReceipts()
'''
pass
def getSharedWorkorder():
'''public MboRemote getSharedWorkorder(final MboRemote mboRemote, final String wonum)
'''
pass
def setFromOnePO():
'''public void setFromOnePO(final boolean flag)
'''
pass
def getFromOnePO():
'''public boolean getFromOnePO()
'''
pass
def generateWO():
'''public void generateWO()
'''
pass
def createSoftwareContractHeader():
'''public MboRemote createSoftwareContractHeader(final String contractNum, final String description, final String contractType)
'''
pass
def getValidateOrder():
'''public String[] getValidateOrder()
'''
pass
def canRevisePO():
'''public void canRevisePO()
'''
pass
def revisePO():
'''public MboRemote revisePO()
public MboRemote revisePO(final String revDescription)
public MboRemote revisePO(final String revDescription, boolean allowReceipt)
'''
pass
def getNextRevision():
'''public MboRemote getNextRevision()
'''
pass
def getPreviousRevision():
'''public MboRemote getPreviousRevision()
'''
pass
def getApprRevision():
'''public MboRemote getApprRevision()
'''
pass
def updatePndRevPO():
'''public void updatePndRevPO()
'''
pass
def checkPOLineQtyCost():
'''public void checkPOLineQtyCost(final MboRemote pndrevPOLine)
public void checkPOLineQtyCost(final MboRemote apprPOLine, final MboRemote pndrevPOLine)
'''
pass
def useLineOrLoadedCost():
'''public String useLineOrLoadedCost()
'''
pass
def getMboSet():
'''public MboSetRemote getMboSet(final String name)
'''
pass
def setDontCheckCompleteFlag():
'''public void setDontCheckCompleteFlag(final boolean flag)
'''
pass
def getDontCheckCompleteFlag():
'''public boolean getDontCheckCompleteFlag()
'''
pass
