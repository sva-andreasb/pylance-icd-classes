SCRIPT_LOGGER = "String  \"maximo.script\""
def JSR223ScriptDriver():
    '''public JSR223ScriptDriver()
    '''
def readBinaryData():
    '''public static byte[] readBinaryData(final InputStream input)
    '''
def getSupportedScriptEngineNames():
    '''public static Set<String> getSupportedScriptEngineNames()
    '''
def getAllSupportedScriptEngines():
    '''public static Map<String, ScriptEngineInfo> getAllSupportedScriptEngines()
    '''
def getSupportedScriptEngineInfo():
    '''public static ScriptEngineInfo getSupportedScriptEngineInfo(final String engShortName)
    '''
def canRun():
    '''public boolean canRun(final String scriptLang)
    '''
def releaseResources():
    '''public void releaseResources()
    public void releaseResources(final String scriptName)
    '''
def preCompileScript():
    '''public boolean preCompileScript(final ScriptInfo scriptInfo)
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
def compileScript():
    '''public void compileScript(final String scriptName, final String scriptSource, final String scriptLanguage)
    '''
