def ():
    '''returns PersonService\n\n
    (final MXServer mxServer)\n
    '''
def getDefaultDisplayName():
    '''returns String\n\n
    getDefaultDisplayName(String firstName, String lastName, final UserInfo userInfo)\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def setDfltApp():
    '''returns String\n\n
    setDfltApp(final String newdfltapp, final String personid)\n
    '''
def deactivateUser():
    '''returns None\n\n
    deactivateUser(@WSMboKey("PERSON") final MboRemote person, final String memo)\n
    '''
def activateUser():
    '''returns None\n\n
    activateUser(@WSMboKey("PERSON") final MboRemote person, final String memo, final MXTransaction mxTran)\n
    '''
