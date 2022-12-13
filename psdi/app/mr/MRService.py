def MRService():
    '''public MRService()
    public MRService(final MXServer mxServer)
    '''
def isMRValid():
    '''public void isMRValid(final UserInfo userInfo, final String mrnum)
    '''
def getNewMRMboSet():
    '''public MboSetRemote getNewMRMboSet(final String mrnum, final UserInfo userInfo)
    '''
def getFavorites():
    '''public MboSetRemote getFavorites(final UserInfo userInfo)
    '''
def addToFavorites():
    '''public void addToFavorites(final UserInfo userInfo, final MboRemote mrLineRemote)
    '''
def addFromFavorites():
    '''public void addFromFavorites(final MboRemote mr, final MboSetRemote mrLineSetRemote, final MboSetRemote favItemSetRemote)
    '''
def itemOrServiceAlreadyOnFavorites():
    '''public boolean itemOrServiceAlreadyOnFavorites(final MboSetRemote mrLineSetRemote, final String[] attrs, final String[] attrNames)
    '''
def changeStatus():
    '''public void changeStatus(@WSMboKey("MR") final MRRemote mr, final String status, final Date date, final String memo)
    '''
