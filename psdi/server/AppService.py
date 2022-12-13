def isRunning():
'''public boolean isRunning()
'''
pass
def setRunning():
'''public void setRunning(final boolean value)
'''
pass
def AppService():
'''public AppService()
public AppService(final MXServer mxServer)
'''
pass
def configure():
'''public void configure(final Properties cf)
'''
pass
def setProxy():
'''public void setProxy(final Remote proxy)
'''
pass
def getProxy():
'''public Remote getProxy()
'''
pass
def init():
'''public void init()
'''
pass
def destroy():
'''public void destroy()
'''
pass
def getMXServer():
'''public MXServer getMXServer()
'''
pass
def getName():
'''public String getName()
'''
pass
def getURL():
'''public String getURL()
'''
pass
def setURL():
'''public void setURL(final String url)
'''
pass
def getLoad():
'''public int getLoad()
'''
pass
def isAppService():
'''public boolean isAppService()
'''
pass
def isSingletonService():
'''public boolean isSingletonService()
'''
pass
def getServiceInfo():
'''public String getServiceInfo()
'''
pass
def getMaxVar():
'''public MaxVarServiceRemote getMaxVar()
'''
pass
def getProfile():
'''public ProfileRemote getProfile(final UserInfo userInfo)
'''
pass
def getMaximoDD():
'''public MaximoDD getMaximoDD()
'''
pass
def getSchemaOwner():
'''public String getSchemaOwner()
'''
pass
def getSetFromKeys():
'''public MboSetRemote getSetFromKeys(final String setName, final String[] keyNames, final String[][] keyValues, final UserInfo user)
'''
pass
def getMboSet():
'''public MboSetRemote getMboSet(final String setName, final UserInfo user)
'''
pass
def freeMboSet():
'''public synchronized void freeMboSet()
'''
pass
def getLiveObjCount():
'''public synchronized int getLiveObjCount()
'''
pass
def getDBConnection():
'''public Connection getDBConnection(final ConnectionKey conKey)
'''
pass
def freeDBConnection():
'''public void freeDBConnection(final ConnectionKey conKey)
'''
pass
def getCurrentState():
'''public String getCurrentState()
'''
pass
def getStateList():
'''public String[] getStateList()
'''
pass
def getStateCmdList():
'''public String[] getStateCmdList()
'''
pass
def restart():
'''public void restart()
'''
pass
def initCriteriaList():
'''public void initCriteriaList(final Hashtable criteriaTable)
'''
pass
def getCriteria():
'''public String getCriteria(final String criteriaName)
'''
pass
def verifyUser():
'''public void verifyUser(final String loginCheck, final String passCheck, final UserInfo userinfo)
public boolean verifyUser(final String loginCheck, final String passCheck, final UserInfo userinfo, final String app, final String reason, final String transid, final String[] keyvalue)
'''
pass
def getSetForRelationship():
'''public MboSetRemote getSetForRelationship(final String relOwner, final String relName, final String[] relColumn, final String[] relValue, final UserInfo userInfo)
'''
pass
def getServiceLogger():
'''public MXLogger getServiceLogger()
'''
pass
def checkSecurity():
'''public boolean checkSecurity(final String methodname, final UserInfo userInfo)
'''
pass
