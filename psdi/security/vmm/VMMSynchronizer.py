USER_SEARCH_PAGE_SIZE = "int  100"
GROUP_SEARCH_PAGE_SIZE = "int  50"
CHECKPOINT = "String  \"CheckPoint\""
def ():
    '''returns VMMSynchronizer\n\n
    ()\n
    '''
def init():
    '''returns None\n\n
    init(final VMMSynchronizerInitData initData)\n
    '''
def getSyncParameters():
    '''returns VMMSyncParameters\n\n
    getSyncParameters()\n
    '''
def getSynchronizerSettings():
    '''returns VMMSynchronizerSettings\n\n
    getSynchronizerSettings()\n
    '''
def performSync():
    '''returns None\n\n
    performSync(final Connection con, final VMMSyncParameters syncParams, final UserInfo userInfo)\n
    '''
def setOwner():
    '''returns None\n\n
    setOwner(final VMMSyncTask val)\n
    '''
def isFullSyncNeeded():
    '''returns boolean\n\n
    isFullSyncNeeded()\n
    '''
def isSyncNeeded():
    '''returns boolean\n\n
    isSyncNeeded()\n
    '''
def setVMMSyncListener():
    '''returns None\n\n
    setVMMSyncListener(final VMMSyncListener vmmSyncListener)\n
    '''
def getVMMSyncListener():
    '''returns VMMSyncListener\n\n
    getVMMSyncListener()\n
    '''
