def ():
    '''returns ScriptMboEventListener\n\n
    (final String scriptName, final String launchPointName, final String objectName, final String attributeName)\n
    '''
def eventSetup():
    '''returns MboRemote\n\n
    eventSetup(final NonPersistentMboSet npmsr)\n
    '''
def eventExecute():
    '''returns None\n\n
    eventExecute(final NonPersistentMboSet npmsr)\n
    eventExecute(final NonPersistentMboSet npSet, final MboRemote mboToWorkOn)\n
    '''
def eventAction():
    '''returns None\n\n
    eventAction(final EventMessage em)\n
    '''
def eventValidate():
    '''returns boolean\n\n
    eventValidate(final EventMessage em)\n
    '''
def postCommitEventAction():
    '''returns None\n\n
    postCommitEventAction(final EventMessage em)\n
    '''
def preSaveEventAction():
    '''returns None\n\n
    preSaveEventAction(final EventMessage em)\n
    '''
def preSaveInternalEventAction():
    '''returns None\n\n
    preSaveInternalEventAction(final EventMessage em)\n
    '''
def postSaveInternalEventAction():
    '''returns None\n\n
    postSaveInternalEventAction(final EventMessage em)\n
    '''
