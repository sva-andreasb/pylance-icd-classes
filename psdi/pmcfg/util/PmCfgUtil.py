ERROR_GROUP = "String  \"PMCFG\""
REMOTE_EXC = "String  \"UnexpectedRemoteException\""
UNEXPECTED_EXC = "String  \"UnexpectedException\""
def getUniqueMbo():
    '''public static MboRemote getUniqueMbo(final MboRemote mbo, final String table, final String tableKey, final String keyValue)
    public static MboRemote getUniqueMbo(final MboRemote mbo, final String table, final String[] tableKeys, final String[] keyValues)
    '''
def wrapRemote():
    '''public static MXApplicationException wrapRemote(final RemoteException ex)
    '''
def sendMessage():
    '''public static void sendMessage(final String templateID, final MboRemote targetMbo)
    '''
def getMaxMessage():
    '''public static String getMaxMessage(final String msggroup, final String msgkey, final Object[] parameters)
    '''
def getDefaultCILifecycle():
    '''public static MboRemote getDefaultCILifecycle(final UserInfo userInfo)
    '''
