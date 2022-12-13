YNC_NULL = "int  -1"
YNC_YES = "int  8"
YNC_NO = "int  16"
YNC_OK = "int  2"
YNC_CANCEL = "int  4"
def ScriptService():
    '''public ScriptService(final String scriptName, final String launchPointName, final Mbo mbo)
    '''
def getScriptName():
    '''public String getScriptName()
    '''
def getMbo():
    '''public Mbo getMbo()
    '''
def getMboName():
    '''public String getMboName()
    '''
def jsonToString():
    '''public String jsonToString(final JSONObject ojo)
    '''
def jsonarrayToString():
    '''public String jsonarrayToString(final JSONArray ja)
    '''
def tojsonarray():
    '''public JSONArray tojsonarray(final String ja)
    '''
def tojsonobject():
    '''public JSONObject tojsonobject(final String jo)
    '''
def webclientsession():
    '''public Object webclientsession()
    '''
def closeDialog():
    '''public void closeDialog()
    '''
def getMboSet():
    '''public MboSetRemote getMboSet(final String mboSetName, final UserInfo userInfo)
    '''
def launchDialog():
    '''public void launchDialog(final String dialogId)
    '''
def openURL():
    '''public void openURL(final String url, final boolean newWindow)
    '''
def httpget():
    '''public String httpget(final String url)
    public String httpget(final String url, final String user, final String pass)
    '''
def httppost():
    '''public String httppost(final String url, final String data)
    public String httppost(final String url, final String user, final String pass, final String data)
    '''
def httppostasbytes():
    '''public byte[] httppostasbytes(final String url, final String user, final String pass, final byte[] data)
    '''
def httppostasjson():
    '''public JSONArtifact httppostasjson(final String url, final String user, final String pass, final String headers, final JSONArtifact ja)
    '''
def httpgetasjson():
    '''public JSONArtifact httpgetasjson(final String url, final String user, final String headers, final String pass)
    '''
def httpgetasbytes():
    '''public byte[] httpgetasbytes(final String url, final String user, final String pass)
    '''
def invokeEndpoint():
    '''public String invokeEndpoint(final String endPointName, final Map<String, String> metaData, final String data)
    public byte[] invokeEndpoint(final String endPointName, final Map<String, String> metaData, final byte[] data)
    '''
def log():
    '''public void log(final String logMsg)
    '''
def log_debug():
    '''public void log_debug(final String logMsg)
    public void log_debug(final String logMsg, final Throwable t)
    '''
def log_info():
    '''public void log_info(final String logMsg)
    public void log_info(final String logMsg, final Throwable t)
    '''
def log_warn():
    '''public void log_warn(final String logMsg)
    public void log_warn(final String logMsg, final Throwable t)
    '''
def log_error():
    '''public void log_error(final String logMsg)
    public void log_error(final String logMsg, final Throwable t)
    '''
def log_fatal():
    '''public void log_fatal(final String logMsg)
    public void log_fatal(final String logMsg, final Throwable t)
    '''
def wsinteraction():
    '''public void wsinteraction(final String interactionName)
    '''
def logError():
    '''public void logError(final String logMsg)
    '''
def yncerror():
    '''public void yncerror(final String grp, final String key, final String[] params)
    public void yncerror(final String grp, final String key)
    '''
def raiseSkipTransaction():
    '''public void raiseSkipTransaction()
    '''
def yncuserinput():
    '''public int yncuserinput()
    '''
def getProperty():
    '''public String getProperty(final String propName)
    '''
def getLogger():
    '''public MXLogger getLogger(final String loggerName)
    '''
def error():
    '''public void error(final String grp, final String key, final String[] params)
    public void error(final String grp, final String key)
    '''
def setWarning():
    '''public void setWarning(final String warnGrpVal, final String warnKeyVal, final String[] warnparams)
    '''
def invokeChannel():
    '''public void invokeChannel(final String channelName)
    '''
def invokeWorkflow():
    '''public void invokeWorkflow(final String wfName)
    '''
def invokeScript():
    '''public void invokeScript(final String aScriptName, final Map<String, Object> context)
    public Object invokeScript(String aScriptName, final String functionName, final Object[] args)
    public Map<String, Object> invokeScript(final String aScriptName)
    '''
