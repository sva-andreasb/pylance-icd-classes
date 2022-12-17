SCRIPT_LOGGER = "String  \"maximo.script\""
def getName():
    '''returns String\n\n
    getName()\n
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
def getObjectScriptAndLPFor():
    '''returns String[]\n\n
    getObjectScriptAndLPFor(final String objectName, final long objectEvent)\n
    '''
def zombieInit():
    '''returns None\n\n
    zombieInit(final EventMessage msg)\n
    '''
