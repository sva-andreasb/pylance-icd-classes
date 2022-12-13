def CI():
    '''public CI(final MboSet ms)
    '''
def init():
    '''public void init()
    '''
def add():
    '''public void add()
    '''
def getMboSet():
    '''public MboSetRemote getMboSet(final String name)
    '''
def save():
    '''public void save()
    '''
def modify():
    '''public void modify()
    '''
def getStatusListName():
    '''public String getStatusListName()
    '''
def duplicate():
    '''public MboRemote duplicate()
    '''
def canDelete():
    '''public void canDelete()
    '''
def delete():
    '''public void delete(final long accessModifier)
    '''
def changeStatus():
    '''public void changeStatus(final String status, final Date date, final String memo)
    '''
def generateAutoKey():
    '''public void generateAutoKey()
    '''
def clearClassification():
    '''public void clearClassification()
    '''
def copyCollectionToCollectDetailsSet():
    '''public void copyCollectionToCollectDetailsSet(final MboSetRemote collectionSet)
    '''
def createTicket():
    '''public void createTicket(final MboRemote tkMbo)
    '''
def createWO():
    '''public void createWO(final MboRemote workorderMbo)
    '''
def setCIAttributesForWO():
    '''public void setCIAttributesForWO(final MboSetRemote autoAttrUpdateSet)
    '''
def addCIToCollectDetails():
    '''public void addCIToCollectDetails(final String collectionNum)
    '''
def createWorkorder():
    '''public MboRemote createWorkorder(final String jpnum)
    '''
def createChange():
    '''public MboRemote createChange(final String jpnum)
    '''
def createRelease():
    '''public MboRemote createRelease(final String jpnum)
    '''
def createServiceRequest():
    '''public MboRemote createServiceRequest(final String tickettemplateid)
    '''
def createProblem():
    '''public MboRemote createProblem(final String tickettemplateid)
    '''
def createIncident():
    '''public MboRemote createIncident(final String tickettemplateid)
    '''
def undelete():
    '''public void undelete()
    public void undelete(final Hashtable<String, String> cisToBeUndeleted)
    '''
def clearChangeStatusCacheForCIs():
    '''public void clearChangeStatusCacheForCIs()
    '''
def clearChangeStatusForAllSessions():
    '''public void clearChangeStatusForAllSessions()
    '''
def actionOnAssetNumFld():
    '''public void actionOnAssetNumFld(final MboRemote asset)
    '''
def setLinkToActualCI():
    '''public void setLinkToActualCI(final String actcinum, final long accessModifier)
    '''
def statusAllowsChange():
    '''public boolean statusAllowsChange()
    '''
def getKeyForSession():
    '''public String getKeyForSession(final UserInfo userInfo)
    '''
def clearStatusChangeFields():
    '''public synchronized void clearStatusChangeFields()
    '''
