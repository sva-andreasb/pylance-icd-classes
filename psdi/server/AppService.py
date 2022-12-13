def isRunning():
    '''public boolean isRunning()
    '''
def setRunning():
    '''public void setRunning(final boolean value)
    '''
def AppService():
    '''public AppService()
    public AppService(final MXServer mxServer)
    '''
def configure():
    '''public void configure(final Properties cf)
    '''
def setProxy():
    '''public void setProxy(final Remote proxy)
    '''
def getProxy():
    '''public Remote getProxy()
    '''
def init():
    '''public void init()
    '''
def destroy():
    '''public void destroy()
    '''
def getMXServer():
    '''public MXServer getMXServer()
    '''
def getName():
    '''public String getName()
    '''
def getURL():
    '''public String getURL()
    '''
def setURL():
    '''public void setURL(final String url)
    '''
def getLoad():
    '''public int getLoad()
    '''
def isAppService():
    '''public boolean isAppService()
    '''
def isSingletonService():
    '''public boolean isSingletonService()
    '''
def getServiceInfo():
    '''public String getServiceInfo()
    '''
def getMaxVar():
    '''public MaxVarServiceRemote getMaxVar()
    '''
def getProfile():
    '''public ProfileRemote getProfile(final UserInfo userInfo)
    '''
def getMaximoDD():
    '''public MaximoDD getMaximoDD()
    '''
def getSchemaOwner():
    '''public String getSchemaOwner()
    '''
def getSetFromKeys():
    '''public MboSetRemote getSetFromKeys(final String setName, final String[] keyNames, final String[][] keyValues, final UserInfo user)
    '''
def getMboSet():
    '''public MboSetRemote getMboSet(final String setName, final UserInfo user)
    '''
def freeMboSet():
    '''public synchronized void freeMboSet()
    '''
def getLiveObjCount():
    '''public synchronized int getLiveObjCount()
    '''
def getDBConnection():
    '''public Connection getDBConnection(final ConnectionKey conKey)
    '''
def freeDBConnection():
    '''public void freeDBConnection(final ConnectionKey conKey)
    '''
def getCurrentState():
    '''public String getCurrentState()
    '''
def getStateList():
    '''public String[] getStateList()
    '''
def getStateCmdList():
    '''public String[] getStateCmdList()
    '''
def restart():
    '''public void restart()
    '''
def initCriteriaList():
    '''public void initCriteriaList(final Hashtable criteriaTable)
    '''
def getCriteria():
    '''public String getCriteria(final String criteriaName)
    '''
def verifyUser():
    '''public void verifyUser(final String loginCheck, final String passCheck, final UserInfo userinfo)
    public boolean verifyUser(final String loginCheck, final String passCheck, final UserInfo userinfo, final String app, final String reason, final String transid, final String[] keyvalue)
    '''
def getSetForRelationship():
    '''public MboSetRemote getSetForRelationship(final String relOwner, final String relName, final String[] relColumn, final String[] relValue, final UserInfo userInfo)
    '''
def getServiceLogger():
    '''public MXLogger getServiceLogger()
    '''
def checkSecurity():
    '''public boolean checkSecurity(final String methodname, final UserInfo userInfo)
    '''
