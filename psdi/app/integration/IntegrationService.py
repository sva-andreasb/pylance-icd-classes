def IntegrationService():
    '''    public IntegrationService()
    public IntegrationService(final MXServer mxServer)
    '''
def restart():
    '''    public void restart()
    '''
def useIntegrationRules():
    '''    public boolean useIntegrationRules(String owner1sysid, String owner2sysid, String pcid, final UserInfo userInfo)
    '''
def put():
    '''    public Object put(String owner1sysid, String owner2sysid, String pcid, final boolean newvalue)
    '''
def remove():
    '''    public Object remove(String owner1sysid, String owner2sysid, String pcid)
    '''
def copySystem():
    '''    public MboSetRemote copySystem(final String fromSysID, final String toSysID, final UserInfo userInfo)
    '''
def deleteSystem():
    '''    public MboSetRemote deleteSystem(final String sysID, final String indicator, final UserInfo userInfo)
    '''
def getMxSysID():
    '''    public String getMxSysID(final UserInfo userInfo)
    '''
def isPCIDValid():
    '''    public boolean isPCIDValid(final String pcid, final UserInfo userInfo)
    '''
def getDefaultPCValue():
    '''    public boolean getDefaultPCValue(String owner1sysid, String owner2sysid, String pcid, final UserInfo userInfo)
    '''
