SCRIPT_LOGGER = "String  \"maximo.script\""
def ():
    '''returns JSR223ScriptDriver\n\n
    ()\n
    '''
def canRun():
    '''returns boolean\n\n
    canRun(final String scriptLang)\n
    '''
def releaseResources():
    '''returns None\n\n
    releaseResources()\n
    releaseResources(final String scriptName)\n
    '''
def preCompileScript():
    '''returns boolean\n\n
    preCompileScript(final ScriptInfo scriptInfo)\n
    '''
def isBinaryScript():
    '''returns boolean\n\n
    isBinaryScript()\n
    '''
def parseScriptForParams():
    '''returns List<ScriptParamInfo>\n\n
    parseScriptForParams(final byte[] scriptBytes)\n
    '''
def compileScript():
    '''returns None\n\n
    compileScript(final String scriptName, final String scriptSource, final String scriptLanguage)\n
    '''
