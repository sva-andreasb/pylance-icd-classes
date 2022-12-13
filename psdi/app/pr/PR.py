def PR():
    '''    public PR(final MboSet ms)
    '''
def getProcess():
    '''    public String getProcess()
    '''
def getStatusListName():
    '''    public String getStatusListName()
    '''
def init():
    '''    public void init()
    '''
def initFieldFlagsOnMbo():
    '''    public void initFieldFlagsOnMbo(final String attrName)
    '''
def add():
    '''    public void add()
    '''
def setBillToShipToInfo():
    '''    public void setBillToShipToInfo()
    '''
def appValidate():
    '''    public void appValidate()
    '''
def createPRLineFromReorder():
    '''    public PRLineRemote createPRLineFromReorder(final String description, final String storeloc, final ReorderRemote reoRemote)
    '''
def createPOsFromPR():
    '''    public Vector createPOsFromPR(final Date date)
    public void createPOsFromPR(final String ponums, final String description)
    public Vector createPOsFromPR(final Date date, final String ponum, final boolean isApprove, final String description)
    public Vector createPOsFromPR(final Date date, final String ponum, final boolean isApprove, final String description, final boolean fromUI)
    '''
def createPOHeaderFromPR():
    '''    public MboRemote createPOHeaderFromPR(final String ponum, final String description, final MboRemote sourceRemote)
    '''
def getPOsCreateByApproval():
    '''    public Vector getPOsCreateByApproval()
    '''
def createRFQHeaderFromPR():
    '''    public MboRemote createRFQHeaderFromPR(final String rfqnum)
    '''
def duplicate():
    '''    public MboRemote duplicate()
    '''
def generateAutoKey():
    '''    public void generateAutoKey()
    '''
def modify():
    '''    public void modify()
    '''
def initRelationship():
    '''    public void initRelationship(final String relationName, final MboSetRemote mboSet)
    '''
def setRelatedMboEditibility():
    '''    public void setRelatedMboEditibility(final String relationName, final MboSetRemote mboSet)
    '''
def copySpareParts():
    '''    public void copySpareParts(final MboSetRemote sparePartSet)
    '''
def addInvVendorItemsToPRLine():
    '''    public void addInvVendorItemsToPRLine(final MboSetRemote invVendorSetRemote)
    '''
def save():
    '''    public void save()
    '''
def changeStatus():
    '''    public void changeStatus(final String status, final Date date, final String memo, final long accessModifier)
    '''
def wapprPRCreatePO():
    '''    public boolean wapprPRCreatePO()
    '''
def allLinesHaveContracts():
    '''    public boolean allLinesHaveContracts(final boolean createPO)
    public boolean allLinesHaveContracts()
    '''
def checkingBeforeCreatePOCont():
    '''    public boolean checkingBeforeCreatePOCont(final boolean createPO)
    '''
def usePromptPO():
    '''    public boolean usePromptPO()
    '''
def setPromptPO():
    '''    public void setPromptPO(final boolean setPromptPO)
    '''
def createContractFromPR():
    '''    public void createContractFromPR(final String contractNum, final String description, final String contractType)
    '''
def isLineContNumFilled():
    '''    public boolean isLineContNumFilled(final MboSetRemote lineSet)
    '''
def checkWAPPRStatus():
    '''    public void checkWAPPRStatus()
    '''
def findMatchedPOVendor():
    '''    public MboRemote findMatchedPOVendor(final MboRemote targetMbo, final Hashtable poHashtable)
    '''
def canDelete():
    '''    public void canDelete()
    '''
def unapproveMR():
    '''    public void unapproveMR(final MboRemote prLine)
    public void unapproveMR()
    public void unapproveMR(final String itemnum)
    '''
def processMR():
    '''    public void processMR(final MboSetRemote mrLineSet)
    '''
def validatePR():
    '''    public void validatePR()
    '''
def changePRStatus():
    '''    public void changePRStatus(final MboRemote fromPRLine)
    '''
def getCreatedByReorderFlag():
    '''    public boolean getCreatedByReorderFlag()
    '''
def setPOTypeToConsignment():
    '''    public void setPOTypeToConsignment(final MboRemote noContractPOHeader, final MboRemote prLine, final boolean fromUI)
    '''
