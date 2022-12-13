def ScriptListenerManager():
    '''public ScriptListenerManager()
    '''
def registerScriptAsListener():
    '''public void registerScriptAsListener(final String scriptName, final ScriptLaunchPointInfo launchPointInfo)
    '''
def fireNPSetupEvent():
    '''public MboRemote fireNPSetupEvent(final NonPersistentMboSet npSet)
    '''
def fireNPExecuteEvent():
    '''public void fireNPExecuteEvent(final NonPersistentMboSet npSet)
    public void fireNPExecuteEvent(final NonPersistentMboSet npSet, final MboRemote mboToWorkOn)
    '''
def zombieInit():
    '''public void zombieInit(final EventMessage msg)
    '''
def unregisterAllListeners():
    '''public void unregisterAllListeners()
    '''
def unregisterListeners():
    '''public void unregisterListeners(final String scriptName, final boolean remove)
    '''
