SCRIPT_LOGGER = "String  \"maximo.script\""
def getInstance():
    '''    public static final ScriptCache getInstance()
    '''
def getName():
    '''    public String getName()
    '''
def getScriptInfo():
    '''    public ScriptInfo getScriptInfo(final String name)
    '''
def fireNPSetupEvent():
    '''    public MboRemote fireNPSetupEvent(final NonPersistentMboSet npSet)
    '''
def fireNPExecuteEvent():
    '''    public void fireNPExecuteEvent(final NonPersistentMboSet npSet, final MboRemote mboToWorkOn)
    public void fireNPExecuteEvent(final NonPersistentMboSet npSet)
    '''
def fireAfterDuplicateEvent():
    '''    public void fireAfterDuplicateEvent(final MboRemote mbo, final MboRemote dupMbo)
    '''
def getObjectScriptAndLPFor():
    '''    public String[] getObjectScriptAndLPFor(final String objectName, final long objectEvent)
    '''
def getAllScripts():
    '''    public Map<String, ScriptInfo> getAllScripts()
    '''
def zombieInit():
    '''    public void zombieInit(final EventMessage msg)
    '''
