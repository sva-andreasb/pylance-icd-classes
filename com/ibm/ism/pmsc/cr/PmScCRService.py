COPYRIGHT = "String  \"IBM Confidential OCO Source Material\n5725-E24 (C) COPYRIGHT International Business Machines Corp. 2007, 2017\nThe source code for this program is not published or otherwise divested\nof its trade secrets, irrespective of what has been deposited with the\nU.S. Copyright Office.\""
def ():
    '''returns PmScCRService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def init():
    '''returns None\n\n
    init()\n
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
