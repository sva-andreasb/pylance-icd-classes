def ():
    '''returns MRService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def isMRValid():
    '''returns None\n\n
    isMRValid(final UserInfo userInfo, final String mrnum)\n
    '''
def getNewMRMboSet():
    '''returns MboSetRemote\n\n
    getNewMRMboSet(final String mrnum, final UserInfo userInfo)\n
    '''
def getFavorites():
    '''returns MboSetRemote\n\n
    getFavorites(final UserInfo userInfo)\n
    '''
def addToFavorites():
    '''returns None\n\n
    addToFavorites(final UserInfo userInfo, final MboRemote mrLineRemote)\n
    '''
def addFromFavorites():
    '''returns None\n\n
    addFromFavorites(final MboRemote mr, final MboSetRemote mrLineSetRemote, final MboSetRemote favItemSetRemote)\n
    '''
def itemOrServiceAlreadyOnFavorites():
    '''returns boolean\n\n
    itemOrServiceAlreadyOnFavorites(final MboSetRemote mrLineSetRemote, final String[] attrs, final String[] attrNames)\n
    '''
def changeStatus():
    '''returns None\n\n
    changeStatus(@WSMboKey("MR") final MRRemote mr, final String status, final Date date, final String memo)\n
    '''
