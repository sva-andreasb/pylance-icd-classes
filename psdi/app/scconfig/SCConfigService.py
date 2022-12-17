def ():
    '''returns SCConfigService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def loadStartCenter():
    '''returns None\n\n
    loadStartCenter(final String groupName, final UserInfo ui)\n
    '''
def loadStartCenterFromTemplate():
    '''returns long\n\n
    loadStartCenterFromTemplate(final String templateId, final String groupName, final UserInfo ui, final boolean modifyTemplate)\n
    '''
def saveAsTemplate():
    '''returns None\n\n
    saveAsTemplate(final String startCenterToCopy, final UserInfo ui)\n
    '''
def getStartCenters():
    '''returns Object[]\n\n
    getStartCenters(final UserInfo ui)\n
    '''
def checkGroupAssociation():
    '''returns Hashtable\n\n
    checkGroupAssociation(final UserInfo ui)\n
    checkGroupAssociation(final MboSetRemote scconfigSet)\n
    '''
def doesAttributeExist():
    '''returns boolean\n\n
    doesAttributeExist(final MboSetRemote msr, final String attributeName)\n
    '''
def getPortletControlNameMap():
    '''returns Hashtable\n\n
    getPortletControlNameMap(final UserInfo ui)\n
    '''
def templateBeingModified():
    '''returns boolean\n\n
    templateBeingModified(final UserInfo ui, final long templateID)\n
    '''
def isTemplate():
    '''returns boolean\n\n
    isTemplate(final UserInfo ui, final long startCenterId)\n
    '''
