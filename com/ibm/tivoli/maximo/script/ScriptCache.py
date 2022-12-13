SCRIPT_LOGGER = "String maximo.script""
def getInstance():
'''public static final ScriptCache getInstance()
'''
pass
def getName():
'''public String getName()
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
def getObjectScriptAndLPFor():
'''public String[] getObjectScriptAndLPFor(final String objectName, final long objectEvent)
'''
pass
def getAllScripts():
'''public Map<String, ScriptInfo> getAllScripts()
'''
pass
def zombieInit():
'''public void zombieInit(final EventMessage msg)
'''
pass
