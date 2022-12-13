SCRIPT_LOGGER = "String maximo.script""
def ScriptCacheImpl():
'''public ScriptCacheImpl()
'''
pass
def getName():
'''public String getName()
'''
pass
def init():
'''public void init()
'''
pass
def reload():
'''public void reload()
public void reload(final String key)
'''
pass
def getScriptInfo():
'''public ScriptInfo getScriptInfo(final String name)
'''
pass
def fireNPSetupEvent():
'''public MboRemote fireNPSetupEvent(final NonPersistentMboSet npSet)
'''
pass
def fireNPExecuteEvent():
'''public void fireNPExecuteEvent(final NonPersistentMboSet npSet, final MboRemote mboToWorkOn)
public void fireNPExecuteEvent(final NonPersistentMboSet npSet)
'''
pass
def fireAfterDuplicateEvent():
'''public void fireAfterDuplicateEvent(final MboRemote mbo, final MboRemote dupMbo)
'''
pass
def loadScripts():
'''public void loadScripts()
'''
pass
def loadScriptLaunchPoint():
'''public void loadScriptLaunchPoint()
public void loadScriptLaunchPoint(final String scriptName)
'''
pass
def getObjectScriptAndLPFor():
'''public String[] getObjectScriptAndLPFor(final String objectName, final long objectEvent)
'''
pass
def getAllScripts():
'''public Map<String, ScriptInfo> getAllScripts()
'''
pass
def loadScript():
'''public void loadScript(final String scriptName)
'''
pass
def zombieInit():
'''public void zombieInit(final EventMessage msg)
'''
pass
