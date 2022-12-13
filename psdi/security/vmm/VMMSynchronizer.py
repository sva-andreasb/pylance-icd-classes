USER_SEARCH_PAGE_SIZE = "int  100"
GROUP_SEARCH_PAGE_SIZE = "int  50"
CHECKPOINT = "String  \"CheckPoint\""
def VMMSynchronizer():
    '''public VMMSynchronizer()
    '''
def init():
    '''public void init(final VMMSynchronizerInitData initData)
    '''
def getSyncParameters():
    '''public VMMSyncParameters getSyncParameters()
    '''
def getSynchronizerSettings():
    '''public VMMSynchronizerSettings getSynchronizerSettings()
    '''
def performSync():
    '''public void performSync(final Connection con, final VMMSyncParameters syncParams, final UserInfo userInfo)
    '''
def setOwner():
    '''public void setOwner(final VMMSyncTask val)
    '''
def isFullSyncNeeded():
    '''public boolean isFullSyncNeeded()
    '''
def isSyncNeeded():
    '''public boolean isSyncNeeded()
    '''
def setVMMSyncListener():
    '''public void setVMMSyncListener(final VMMSyncListener vmmSyncListener)
    '''
def getVMMSyncListener():
    '''public VMMSyncListener getVMMSyncListener()
    '''
