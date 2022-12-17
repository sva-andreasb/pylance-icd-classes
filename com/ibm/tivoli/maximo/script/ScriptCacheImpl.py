SCRIPT_LOGGER = "String  \"maximo.script\""
def ():
    '''returns ScriptCacheImpl\n\n
    ()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def init():
    '''returns None\n\n
    init()\n
    '''
def reload():
    '''returns None\n\n
    reload()\n
    reload(final String key)\n
    '''
def getScriptInfo():
    '''returns ScriptInfo\n\n
    getScriptInfo(final String name)\n
    '''
def fireNPSetupEvent():
    '''returns MboRemote\n\n
    fireNPSetupEvent(final NonPersistentMboSet npSet)\n
    '''
def fireNPExecuteEvent():
    '''returns None\n\n
    fireNPExecuteEvent(final NonPersistentMboSet npSet, final MboRemote mboToWorkOn)\n
    fireNPExecuteEvent(final NonPersistentMboSet npSet)\n
    '''
def fireAfterDuplicateEvent():
    '''returns None\n\n
    fireAfterDuplicateEvent(final MboRemote mbo, final MboRemote dupMbo)\n
    '''
def loadScripts():
    '''returns None\n\n
    loadScripts()\n
    '''
def loadScriptLaunchPoint():
    '''returns None\n\n
    loadScriptLaunchPoint()\n
    loadScriptLaunchPoint(final String scriptName)\n
    '''
def getObjectScriptAndLPFor():
    '''returns String[]\n\n
    getObjectScriptAndLPFor(final String objectName, final long objectEvent)\n
    '''
def loadScript():
    '''returns None\n\n
    loadScript(final String scriptName)\n
    '''
def zombieInit():
    '''returns None\n\n
    zombieInit(final EventMessage msg)\n
    '''
