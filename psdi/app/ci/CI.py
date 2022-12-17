def ():
    '''returns CI\n\n
    (final MboSet ms)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def add():
    '''returns None\n\n
    add()\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet(final String name)\n
    '''
def save():
    '''returns None\n\n
    save()\n
    '''
def modify():
    '''returns None\n\n
    modify()\n
    '''
def getStatusListName():
    '''returns String\n\n
    getStatusListName()\n
    '''
def duplicate():
    '''returns MboRemote\n\n
    duplicate()\n
    '''
def canDelete():
    '''returns None\n\n
    canDelete()\n
    '''
def delete():
    '''returns None\n\n
    delete(final long accessModifier)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(final String status, final Date date, final String memo)\n
    '''
def generateAutoKey():
    '''returns None\n\n
    generateAutoKey()\n
    '''
def clearClassification():
    '''returns None\n\n
    clearClassification()\n
    '''
def copyCollectionToCollectDetailsSet():
    '''returns None\n\n
    copyCollectionToCollectDetailsSet(final MboSetRemote collectionSet)\n
    '''
def createTicket():
    '''returns None\n\n
    createTicket(final MboRemote tkMbo)\n
    '''
def createWO():
    '''returns None\n\n
    createWO(final MboRemote workorderMbo)\n
    '''
def setCIAttributesForWO():
    '''returns None\n\n
    setCIAttributesForWO(final MboSetRemote autoAttrUpdateSet)\n
    '''
def addCIToCollectDetails():
    '''returns None\n\n
    addCIToCollectDetails(final String collectionNum)\n
    '''
def createWorkorder():
    '''returns MboRemote\n\n
    createWorkorder(final String jpnum)\n
    '''
def createChange():
    '''returns MboRemote\n\n
    createChange(final String jpnum)\n
    '''
def createRelease():
    '''returns MboRemote\n\n
    createRelease(final String jpnum)\n
    '''
def createServiceRequest():
    '''returns MboRemote\n\n
    createServiceRequest(final String tickettemplateid)\n
    '''
def createProblem():
    '''returns MboRemote\n\n
    createProblem(final String tickettemplateid)\n
    '''
def createIncident():
    '''returns MboRemote\n\n
    createIncident(final String tickettemplateid)\n
    '''
def undelete():
    '''returns None\n\n
    undelete()\n
    undelete(final Hashtable<String, String> cisToBeUndeleted)\n
    '''
def clearChangeStatusCacheForCIs():
    '''returns None\n\n
    clearChangeStatusCacheForCIs()\n
    '''
def clearChangeStatusForAllSessions():
    '''returns None\n\n
    clearChangeStatusForAllSessions()\n
    '''
def actionOnAssetNumFld():
    '''returns None\n\n
    actionOnAssetNumFld(final MboRemote asset)\n
    '''
def setLinkToActualCI():
    '''returns None\n\n
    setLinkToActualCI(final String actcinum, final long accessModifier)\n
    '''
def statusAllowsChange():
    '''returns boolean\n\n
    statusAllowsChange()\n
    '''
def getKeyForSession():
    '''returns String\n\n
    getKeyForSession(final UserInfo userInfo)\n
    '''
