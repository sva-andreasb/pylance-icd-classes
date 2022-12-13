SCRIPT_LOGGER = "String  \"maximo.script\""
def MBRScriptDriver():
    '''public MBRScriptDriver()
    '''
def getAllSupportedScriptEngines():
    '''public static Map<String, ScriptEngineInfo> getAllSupportedScriptEngines()
    '''
def compileScript():
    '''public void compileScript(final String scriptName, final String scriptSource, final String scriptLanguage)
    '''
def preCompileScript():
    '''public boolean preCompileScript(final ScriptInfo scriptInfo)
    '''
def wrapMXException():
    '''public static void wrapMXException(final MXException me, final String scrName, final int lineNum)
    '''
def canRun():
    '''public boolean canRun(final String scriptLang)
    '''
def releaseResources():
    '''public void releaseResources()
    public void releaseResources(final String scriptName)
    '''
def getSupportedEngines():
    '''public Map<String, ScriptEngineInfo> getSupportedEngines()
    '''
def isBinaryScript():
    '''public boolean isBinaryScript()
    '''
def parseScriptForParams():
    '''public List<ScriptParamInfo> parseScriptForParams(final byte[] scriptBytes)
    '''
