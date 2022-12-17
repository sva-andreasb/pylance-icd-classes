def ():
    '''returns IntegrationService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def restart():
    '''returns None\n\n
    restart()\n
    '''
def useIntegrationRules():
    '''returns boolean\n\n
    useIntegrationRules(String owner1sysid, String owner2sysid, String pcid, final UserInfo userInfo)\n
    '''
def put():
    '''returns Object\n\n
    put(String owner1sysid, String owner2sysid, String pcid, final boolean newvalue)\n
    '''
def remove():
    '''returns Object\n\n
    remove(String owner1sysid, String owner2sysid, String pcid)\n
    '''
def copySystem():
    '''returns MboSetRemote\n\n
    copySystem(final String fromSysID, final String toSysID, final UserInfo userInfo)\n
    '''
def deleteSystem():
    '''returns MboSetRemote\n\n
    deleteSystem(final String sysID, final String indicator, final UserInfo userInfo)\n
    '''
def getMxSysID():
    '''returns String\n\n
    getMxSysID(final UserInfo userInfo)\n
    '''
def isPCIDValid():
    '''returns boolean\n\n
    isPCIDValid(final String pcid, final UserInfo userInfo)\n
    '''
def getDefaultPCValue():
    '''returns boolean\n\n
    getDefaultPCValue(String owner1sysid, String owner2sysid, String pcid, final UserInfo userInfo)\n
    '''
