USER_SEARCH_PAGE_SIZE = "int  500"
GROUP_SEARCH_PAGE_SIZE = "int  20"
def AbstractLdapSynchronizer():
'''public AbstractLdapSynchronizer()
'''
pass
def init():
'''public void init(final LdapSynchronizerInitData initData)
'''
pass
def getSyncParameters():
'''public SyncParameters getSyncParameters()
'''
pass
def getSynchronizerSettings():
'''public SynchronizerSettings getSynchronizerSettings()
'''
pass
def performSync():
'''public void performSync(final Connection con, final SyncParameters syncParams, final UserInfo userInfo)
'''
pass
def setOwner():
'''public void setOwner(final LdapSyncTask val)
'''
pass
def isFullSyncNeeded():
'''public boolean isFullSyncNeeded()
'''
pass
def isSyncNeeded():
'''public boolean isSyncNeeded()
'''
pass
def setLDAPSyncListener():
'''public void setLDAPSyncListener(final LdapSyncListener ldapSyncListener)
'''
pass
def getLDAPSyncListener():
'''public LdapSyncListener getLDAPSyncListener()
'''
pass
