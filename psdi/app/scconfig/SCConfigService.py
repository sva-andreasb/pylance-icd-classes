def SCConfigService():
    '''public SCConfigService()
    public SCConfigService(final MXServer mxServer)
    '''
def loadStartCenter():
    '''public void loadStartCenter(final String groupName, final UserInfo ui)
    '''
def loadStartCenterFromTemplate():
    '''public long loadStartCenterFromTemplate(final String templateId, final String groupName, final UserInfo ui, final boolean modifyTemplate)
    '''
def saveAsTemplate():
    '''public void saveAsTemplate(final String startCenterToCopy, final UserInfo ui)
    '''
def getStartCenters():
    '''public Object[] getStartCenters(final UserInfo ui)
    '''
def checkGroupAssociation():
    '''public Hashtable checkGroupAssociation(final UserInfo ui)
    public Hashtable checkGroupAssociation(final MboSetRemote scconfigSet)
    '''
def updateStartCenter():
    '''public synchronized long updateStartCenter(final MboRemote startCenter)
    '''
def doesAttributeExist():
    '''public boolean doesAttributeExist(final MboSetRemote msr, final String attributeName)
    '''
def getPortletControlNameMap():
    '''public Hashtable getPortletControlNameMap(final UserInfo ui)
    '''
def templateBeingModified():
    '''public boolean templateBeingModified(final UserInfo ui, final long templateID)
    '''
def isTemplate():
    '''public boolean isTemplate(final UserInfo ui, final long startCenterId)
    '''
