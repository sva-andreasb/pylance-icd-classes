def ():
    '''returns PR\n\n
    (final MboSet ms)\n
    '''
def getProcess():
    '''returns String\n\n
    getProcess()\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def initFieldFlagsOnMbo():
    '''returns None\n\n
    initFieldFlagsOnMbo(final String attrName)\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def setBillToShipToInfo():
    '''returns None\n\n
    setBillToShipToInfo()\n
    '''
def appValidate():
    '''returns None\n\n
    appValidate()\n
    '''
def createPRLineFromReorder():
    '''returns PRLineRemote\n\n
    createPRLineFromReorder(final String description, final String storeloc, final ReorderRemote reoRemote)\n
    '''
def createPOsFromPR():
    '''returns Vector\n\n
    createPOsFromPR(final Date date)\n
    createPOsFromPR(final String ponums, final String description)\n
    createPOsFromPR(final Date date, final String ponum, final boolean isApprove, final String description)\n
    createPOsFromPR(final Date date, final String ponum, final boolean isApprove, final String description, final boolean fromUI)\n
    '''
def createPOHeaderFromPR():
    '''returns MboRemote\n\n
    createPOHeaderFromPR(final String ponum, final String description, final MboRemote sourceRemote)\n
    '''
def getPOsCreateByApproval():
    '''returns Vector\n\n
    getPOsCreateByApproval()\n
    '''
def createRFQHeaderFromPR():
    '''returns MboRemote\n\n
    createRFQHeaderFromPR(final String rfqnum)\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def generateAutoKey():
    '''returns None\n\n
    generateAutoKey()\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def initRelationship():
    '''returns None\n\n
    initRelationship(final String relationName, final MboSetRemote mboSet)\n
    '''
def setRelatedMboEditibility():
    '''returns None\n\n
    setRelatedMboEditibility(final String relationName, final MboSetRemote mboSet)\n
    '''
def copySpareParts():
    '''returns None\n\n
    copySpareParts(final MboSetRemote sparePartSet)\n
    '''
def addInvVendorItemsToPRLine():
    '''returns None\n\n
    addInvVendorItemsToPRLine(final MboSetRemote invVendorSetRemote)\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final Date date, final String memo, final long accessModifier)\n
    '''
def wapprPRCreatePO():
    '''returns boolean\n\n
    wapprPRCreatePO()\n
    '''
def allLinesHaveContracts():
    '''returns boolean\n\n
    allLinesHaveContracts(final boolean createPO)\n
    allLinesHaveContracts()\n
    '''
def checkingBeforeCreatePOCont():
    '''returns boolean\n\n
    checkingBeforeCreatePOCont(final boolean createPO)\n
    '''
def usePromptPO():
    '''returns boolean\n\n
    usePromptPO()\n
    '''
def setPromptPO():
    '''returns None\n\n
    setPromptPO(final boolean setPromptPO)\n
    '''
def createContractFromPR():
    '''returns None\n\n
    createContractFromPR(final String contractNum, final String description, final String contractType)\n
    '''
def isLineContNumFilled():
    '''returns boolean\n\n
    isLineContNumFilled(final MboSetRemote lineSet)\n
    '''
def checkWAPPRStatus():
    '''returns None\n\n
    checkWAPPRStatus()\n
    '''
def findMatchedPOVendor():
    '''returns MboRemote\n\n
    findMatchedPOVendor(final MboRemote targetMbo, final Hashtable poHashtable)\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def unapproveMR():
    '''returns None\n\n
    unapproveMR(final MboRemote prLine)\n
    unapproveMR()\n
    unapproveMR(final String itemnum)\n
    '''
def processMR():
    '''returns None\n\n
    processMR(final MboSetRemote mrLineSet)\n
    '''
def validatePR():
    '''returns None\n\n
    validatePR()\n
    '''
def changePRStatus():
    '''returns None\n\n
    changePRStatus(final MboRemote fromPRLine)\n
    '''
def getCreatedByReorderFlag():
    '''returns boolean\n\n
    getCreatedByReorderFlag()\n
    '''
def setPOTypeToConsignment():
    '''returns None\n\n
    setPOTypeToConsignment(final MboRemote noContractPOHeader, final MboRemote prLine, final boolean fromUI)\n
    '''
