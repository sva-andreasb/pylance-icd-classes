SCRIPT_LOGGER = "String  \"maximo.script\""
def ScriptCacheImpl():
    '''public ScriptCacheImpl()
    '''
def getName():
    '''public String getName()
    '''
def init():
    '''public void init()
    '''
def reload():
    '''public void reload()
    public void reload(final String key)
    '''
def getScriptInfo():
    '''public ScriptInfo getScriptInfo(final String name)
    '''
def fireNPSetupEvent():
    '''public MboRemote fireNPSetupEvent(final NonPersistentMboSet npSet)
    '''
def fireNPExecuteEvent():
    '''public void fireNPExecuteEvent(final NonPersistentMboSet npSet, final MboRemote mboToWorkOn)
    public void fireNPExecuteEvent(final NonPersistentMboSet npSet)
    '''
def fireAfterDuplicateEvent():
    '''public void fireAfterDuplicateEvent(final MboRemote mbo, final MboRemote dupMbo)
    '''
def loadScripts():
    '''public void loadScripts()
    '''
def loadScriptLaunchPoint():
    '''public void loadScriptLaunchPoint()
    public void loadScriptLaunchPoint(final String scriptName)
    '''
def getObjectScriptAndLPFor():
    '''public String[] getObjectScriptAndLPFor(final String objectName, final long objectEvent)
    '''
def getAllScripts():
    '''public Map<String, ScriptInfo> getAllScripts()
    '''
def loadScript():
    '''public void loadScript(final String scriptName)
    '''
def zombieInit():
    '''public void zombieInit(final EventMessage msg)
    '''
