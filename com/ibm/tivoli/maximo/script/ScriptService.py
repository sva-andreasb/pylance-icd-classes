YNC_NULL = "int  -1"
YNC_YES = "int  8"
YNC_NO = "int  16"
YNC_OK = "int  2"
YNC_CANCEL = "int  4"
def ():
    '''returns ScriptService\n\n
    (final String scriptName, final String launchPointName, final Mbo mbo)\n
    '''
def getScriptName():
    '''returns String\n\n
    getScriptName()\n
    '''
def getMbo():
    '''returns Mbo\n\n
    getMbo()\n
    '''
def getMboName():
    '''returns String\n\n
    getMboName()\n
    '''
def jsonToString():
    '''returns String\n\n
    jsonToString(final JSONObject ojo)\n
    '''
def jsonarrayToString():
    '''returns String\n\n
    jsonarrayToString(final JSONArray ja)\n
    '''
def tojsonarray():
    '''returns JSONArray\n\n
    tojsonarray(final String ja)\n
    '''
def tojsonobject():
    '''returns JSONObject\n\n
    tojsonobject(final String jo)\n
    '''
def webclientsession():
    '''returns Object\n\n
    webclientsession()\n
    '''
def closeDialog():
    '''returns None\n\n
    closeDialog()\n
    '''
def getMboSet():
    '''returns MboSetRemote\n\n
    getMboSet(final String mboSetName, final UserInfo userInfo)\n
    '''
def launchDialog():
    '''returns None\n\n
    launchDialog(final String dialogId)\n
    '''
def openURL():
    '''returns None\n\n
    openURL(final String url, final boolean newWindow)\n
    '''
def httpget():
    '''returns String\n\n
    httpget(final String url)\n
    httpget(final String url, final String user, final String pass)\n
    '''
def httppost():
    '''returns String\n\n
    httppost(final String url, final String data)\n
    httppost(final String url, final String user, final String pass, final String data)\n
    '''
def httppostasbytes():
    '''returns byte[]\n\n
    httppostasbytes(final String url, final String user, final String pass, final byte[] data)\n
    '''
def httppostasjson():
    '''returns JSONArtifact\n\n
    httppostasjson(final String url, final String user, final String pass, final String headers, final JSONArtifact ja)\n
    '''
def httpgetasjson():
    '''returns JSONArtifact\n\n
    httpgetasjson(final String url, final String user, final String headers, final String pass)\n
    '''
def httpgetasbytes():
    '''returns byte[]\n\n
    httpgetasbytes(final String url, final String user, final String pass)\n
    '''
def invokeEndpoint():
    '''returns byte[]\n\n
    invokeEndpoint(final String endPointName, final Map<String, String> metaData, final String data)\n
    invokeEndpoint(final String endPointName, final Map<String, String> metaData, final byte[] data)\n
    '''
def log():
    '''returns None\n\n
    log(final String logMsg)\n
    '''
def log_debug():
    '''returns None\n\n
    log_debug(final String logMsg)\n
    log_debug(final String logMsg, final Throwable t)\n
    '''
def log_info():
    '''returns None\n\n
    log_info(final String logMsg)\n
    log_info(final String logMsg, final Throwable t)\n
    '''
def log_warn():
    '''returns None\n\n
    log_warn(final String logMsg)\n
    log_warn(final String logMsg, final Throwable t)\n
    '''
def log_error():
    '''returns None\n\n
    log_error(final String logMsg)\n
    log_error(final String logMsg, final Throwable t)\n
    '''
def log_fatal():
    '''returns None\n\n
    log_fatal(final String logMsg)\n
    log_fatal(final String logMsg, final Throwable t)\n
    '''
def wsinteraction():
    '''returns None\n\n
    wsinteraction(final String interactionName)\n
    '''
def logError():
    '''returns None\n\n
    logError(final String logMsg)\n
    '''
def yncerror():
    '''returns None\n\n
    yncerror(final String grp, final String key, final String[] params)\n
    yncerror(final String grp, final String key)\n
    '''
def raiseSkipTransaction():
    '''returns None\n\n
    raiseSkipTransaction()\n
    '''
def yncuserinput():
    '''returns int\n\n
    yncuserinput()\n
    '''
def getProperty():
    '''returns String\n\n
    getProperty(final String propName)\n
    '''
def getLogger():
    '''returns MXLogger\n\n
    getLogger(final String loggerName)\n
    '''
def error():
    '''returns None\n\n
    error(final String grp, final String key, final String[] params)\n
    error(final String grp, final String key)\n
    '''
def setWarning():
    '''returns None\n\n
    setWarning(final String warnGrpVal, final String warnKeyVal, final String[] warnparams)\n
    '''
def invokeChannel():
    '''returns None\n\n
    invokeChannel(final String channelName)\n
    '''
def invokeWorkflow():
    '''returns None\n\n
    invokeWorkflow(final String wfName)\n
    '''
def invokeScript():
    '''returns Object\n\n
    invokeScript(final String aScriptName, final Map<String, Object> context)\n
    invokeScript(String aScriptName, final String functionName, final Object[] args)\n
    '''
