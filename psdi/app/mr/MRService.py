def MRService():
'''public MRService()
public MRService(final MXServer mxServer)
'''
pass
def isMRValid():
'''public void isMRValid(final UserInfo userInfo, final String mrnum)
'''
pass
def getNewMRMboSet():
'''public MboSetRemote getNewMRMboSet(final String mrnum, final UserInfo userInfo)
'''
pass
def getFavorites():
'''public MboSetRemote getFavorites(final UserInfo userInfo)
'''
pass
def addToFavorites():
'''public void addToFavorites(final UserInfo userInfo, final MboRemote mrLineRemote)
'''
pass
def addFromFavorites():
'''public void addFromFavorites(final MboRemote mr, final MboSetRemote mrLineSetRemote, final MboSetRemote favItemSetRemote)
'''
pass
def itemOrServiceAlreadyOnFavorites():
'''public boolean itemOrServiceAlreadyOnFavorites(final MboSetRemote mrLineSetRemote, final String[] attrs, final String[] attrNames)
'''
pass
def changeStatus():
'''public void changeStatus(@WSMboKey("MR") final MRRemote mr, final String status, final Date date, final String memo)
'''
pass
