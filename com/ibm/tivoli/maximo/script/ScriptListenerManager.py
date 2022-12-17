def ():
    '''returns ScriptListenerManager\n\n
    ()\n
    '''
def registerScriptAsListener():
    '''returns None\n\n
    registerScriptAsListener(final String scriptName, final ScriptLaunchPointInfo launchPointInfo)\n
    '''
def fireNPSetupEvent():
    '''returns MboRemote\n\n
    fireNPSetupEvent(final NonPersistentMboSet npSet)\n
    '''
def fireNPExecuteEvent():
    '''returns None\n\n
    fireNPExecuteEvent(final NonPersistentMboSet npSet)\n
    fireNPExecuteEvent(final NonPersistentMboSet npSet, final MboRemote mboToWorkOn)\n
    '''
def zombieInit():
    '''returns None\n\n
    zombieInit(final EventMessage msg)\n
    '''
def unregisterAllListeners():
    '''returns None\n\n
    unregisterAllListeners()\n
    '''
def unregisterListeners():
    '''returns None\n\n
    unregisterListeners(final String scriptName, final boolean remove)\n
    '''
