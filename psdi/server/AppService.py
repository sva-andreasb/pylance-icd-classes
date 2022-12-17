def isRunning():
    '''returns boolean\n\n
    isRunning()\n
    '''
def setRunning():
    '''returns None\n\n
    setRunning(final boolean value)\n
    '''
def ():
    '''returns AppService\n\n
    ()\n
    (final MXServer mxServer)\n
    '''
def configure():
    '''returns None\n\n
    configure(final Properties cf)\n
    '''
def setProxy():
    '''returns None\n\n
    setProxy(final Remote proxy)\n
    '''
def getProxy():
    '''returns Remote\n\n
    getProxy()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def getMXServer():
    '''returns MXServer\n\n
    getMXServer()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getURL():
    '''returns String\n\n
    getURL()\n
    '''
def setURL():
    '''returns None\n\n
    setURL(final String url)\n
    '''
def getLoad():
    '''returns int\n\n
    getLoad()\n
    '''
def isAppService():
    '''returns boolean\n\n
    isAppService()\n
    '''
def isSingletonService():
    '''returns boolean\n\n
    isSingletonService()\n
    '''
def getServiceInfo():
    '''returns String\n\n
    getServiceInfo()\n
    '''
def getMaxVar():
    '''returns MaxVarServiceRemote\n\n
    getMaxVar()\n
    '''
def getProfile():
    '''returns ProfileRemote\n\n
    getProfile(final UserInfo userInfo)\n
    '''
def getMaximoDD():
    '''returns MaximoDD\n\n
    getMaximoDD()\n
    '''
def getSchemaOwner():
    '''returns String\n\n
    getSchemaOwner()\n
    '''
def getSetFromKeys():
    '''returns MboSetRemote\n\n
    getSetFromKeys(final String setName, final String[] keyNames, final String[][] keyValues, final UserInfo user)\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet(final String setName, final UserInfo user)\n
    '''
def getDBConnection():
    '''returns Connection\n\n
    getDBConnection(final ConnectionKey conKey)\n
    '''
def freeDBConnection():
    '''returns None\n\n
    freeDBConnection(final ConnectionKey conKey)\n
    '''
def getCurrentState():
    '''returns String\n\n
    getCurrentState()\n
    '''
def getStateList():
    '''returns String[]\n\n
    getStateList()\n
    '''
def getStateCmdList():
    '''returns String[]\n\n
    getStateCmdList()\n
    '''
def restart():
    '''returns None\n\n
    restart()\n
    '''
def initCriteriaList():
    '''returns None\n\n
    initCriteriaList(final Hashtable criteriaTable)\n
    '''
def getCriteria():
    '''returns String\n\n
    getCriteria(final String criteriaName)\n
    '''
def verifyUser():
    '''returns boolean\n\n
    verifyUser(final String loginCheck, final String passCheck, final UserInfo userinfo)\n
    verifyUser(final String loginCheck, final String passCheck, final UserInfo userinfo, final String app, final String reason, final String transid, final String[] keyvalue)\n
    '''
def getSetForRelationship():
    '''returns MboSetRemote\n\n
    getSetForRelationship(final String relOwner, final String relName, final String[] relColumn, final String[] relValue, final UserInfo userInfo)\n
    '''
def getServiceLogger():
    '''returns MXLogger\n\n
    getServiceLogger()\n
    '''
def checkSecurity():
    '''returns boolean\n\n
    checkSecurity(final String methodname, final UserInfo userInfo)\n
    '''
