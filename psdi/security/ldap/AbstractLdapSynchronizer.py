USER_SEARCH_PAGE_SIZE = "int  500"
GROUP_SEARCH_PAGE_SIZE = "int  20"
def ():
    '''returns AbstractLdapSynchronizer\n\n
    ()\n
    '''
def init():
    '''returns None\n\n
    init(final LdapSynchronizerInitData initData)\n
    '''
def getSyncParameters():
    '''returns SyncParameters\n\n
    getSyncParameters()\n
    '''
def getSynchronizerSettings():
    '''returns SynchronizerSettings\n\n
    getSynchronizerSettings()\n
    '''
def performSync():
    '''returns None\n\n
    performSync(final Connection con, final SyncParameters syncParams, final UserInfo userInfo)\n
    '''
def setOwner():
    '''returns None\n\n
    setOwner(final LdapSyncTask val)\n
    '''
def isFullSyncNeeded():
    '''returns boolean\n\n
    isFullSyncNeeded()\n
    '''
def isSyncNeeded():
    '''returns boolean\n\n
    isSyncNeeded()\n
    '''
def setLDAPSyncListener():
    '''returns None\n\n
    setLDAPSyncListener(final LdapSyncListener ldapSyncListener)\n
    '''
def getLDAPSyncListener():
    '''returns LdapSyncListener\n\n
    getLDAPSyncListener()\n
    '''
