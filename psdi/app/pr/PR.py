def PR():
'''public PR(final MboSet ms)
'''
pass
def getProcess():
'''public String getProcess()
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
def setBillToShipToInfo():
'''public void setBillToShipToInfo()
'''
pass
def appValidate():
'''public void appValidate()
'''
pass
def createPRLineFromReorder():
'''public PRLineRemote createPRLineFromReorder(final String description, final String storeloc, final ReorderRemote reoRemote)
'''
pass
def createPOsFromPR():
'''public Vector createPOsFromPR(final Date date)
public void createPOsFromPR(final String ponums, final String description)
public Vector createPOsFromPR(final Date date, final String ponum, final boolean isApprove, final String description)
public Vector createPOsFromPR(final Date date, final String ponum, final boolean isApprove, final String description, final boolean fromUI)
'''
pass
def createPOHeaderFromPR():
'''public MboRemote createPOHeaderFromPR(final String ponum, final String description, final MboRemote sourceRemote)
'''
pass
def getPOsCreateByApproval():
'''public Vector getPOsCreateByApproval()
'''
pass
def createRFQHeaderFromPR():
'''public MboRemote createRFQHeaderFromPR(final String rfqnum)
'''
pass
def duplicate():
'''public MboRemote duplicate()
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
def initRelationship():
'''public void initRelationship(final String relationName, final MboSetRemote mboSet)
'''
pass
def setRelatedMboEditibility():
'''public void setRelatedMboEditibility(final String relationName, final MboSetRemote mboSet)
'''
pass
def copySpareParts():
'''public void copySpareParts(final MboSetRemote sparePartSet)
'''
pass
def addInvVendorItemsToPRLine():
'''public void addInvVendorItemsToPRLine(final MboSetRemote invVendorSetRemote)
'''
pass
def save():
'''public void save()
'''
pass
def changeStatus():
'''public void changeStatus(final String status, final Date date, final String memo, final long accessModifier)
'''
pass
def wapprPRCreatePO():
'''public boolean wapprPRCreatePO()
'''
pass
def allLinesHaveContracts():
'''public boolean allLinesHaveContracts(final boolean createPO)
public boolean allLinesHaveContracts()
'''
pass
def checkingBeforeCreatePOCont():
'''public boolean checkingBeforeCreatePOCont(final boolean createPO)
'''
pass
def usePromptPO():
'''public boolean usePromptPO()
'''
pass
def setPromptPO():
'''public void setPromptPO(final boolean setPromptPO)
'''
pass
def createContractFromPR():
'''public void createContractFromPR(final String contractNum, final String description, final String contractType)
'''
pass
def isLineContNumFilled():
'''public boolean isLineContNumFilled(final MboSetRemote lineSet)
'''
pass
def checkWAPPRStatus():
'''public void checkWAPPRStatus()
'''
pass
def findMatchedPOVendor():
'''public MboRemote findMatchedPOVendor(final MboRemote targetMbo, final Hashtable poHashtable)
'''
pass
def canDelete():
'''public void canDelete()
'''
pass
def unapproveMR():
'''public void unapproveMR(final MboRemote prLine)
public void unapproveMR()
public void unapproveMR(final String itemnum)
'''
pass
def processMR():
'''public void processMR(final MboSetRemote mrLineSet)
'''
pass
def validatePR():
'''public void validatePR()
'''
pass
def changePRStatus():
'''public void changePRStatus(final MboRemote fromPRLine)
'''
pass
def getCreatedByReorderFlag():
'''public boolean getCreatedByReorderFlag()
'''
pass
def setPOTypeToConsignment():
'''public void setPOTypeToConsignment(final MboRemote noContractPOHeader, final MboRemote prLine, final boolean fromUI)
'''
pass
