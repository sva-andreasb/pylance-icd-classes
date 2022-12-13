def SCConfigService():
'''public SCConfigService()
public SCConfigService(final MXServer mxServer)
'''
pass
def loadStartCenter():
'''public void loadStartCenter(final String groupName, final UserInfo ui)
'''
pass
def loadStartCenterFromTemplate():
'''public long loadStartCenterFromTemplate(final String templateId, final String groupName, final UserInfo ui, final boolean modifyTemplate)
'''
pass
def saveAsTemplate():
'''public void saveAsTemplate(final String startCenterToCopy, final UserInfo ui)
'''
pass
def getStartCenters():
'''public Object[] getStartCenters(final UserInfo ui)
'''
pass
def checkGroupAssociation():
'''public Hashtable checkGroupAssociation(final UserInfo ui)
public Hashtable checkGroupAssociation(final MboSetRemote scconfigSet)
'''
pass
def updateStartCenter():
'''public synchronized long updateStartCenter(final MboRemote startCenter)
'''
pass
def doesAttributeExist():
'''public boolean doesAttributeExist(final MboSetRemote msr, final String attributeName)
'''
pass
def getPortletControlNameMap():
'''public Hashtable getPortletControlNameMap(final UserInfo ui)
'''
pass
def templateBeingModified():
'''public boolean templateBeingModified(final UserInfo ui, final long templateID)
'''
pass
def isTemplate():
'''public boolean isTemplate(final UserInfo ui, final long startCenterId)
'''
pass
