USER_SEARCH_PAGE_SIZE = "int  500"
GROUP_SEARCH_PAGE_SIZE = "int  20"
def AbstractLdapSynchronizer():
    '''    public AbstractLdapSynchronizer()
    '''
def init():
    '''    public void init(final LdapSynchronizerInitData initData)
    '''
def getSyncParameters():
    '''    public SyncParameters getSyncParameters()
    '''
def getSynchronizerSettings():
    '''    public SynchronizerSettings getSynchronizerSettings()
    '''
def performSync():
    '''    public void performSync(final Connection con, final SyncParameters syncParams, final UserInfo userInfo)
    '''
def setOwner():
    '''    public void setOwner(final LdapSyncTask val)
    '''
def isFullSyncNeeded():
    '''    public boolean isFullSyncNeeded()
    '''
def isSyncNeeded():
    '''    public boolean isSyncNeeded()
    '''
def setLDAPSyncListener():
    '''    public void setLDAPSyncListener(final LdapSyncListener ldapSyncListener)
    '''
def getLDAPSyncListener():
    '''    public LdapSyncListener getLDAPSyncListener()
    '''
