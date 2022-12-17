def eventAction():
    '''returns None\n\n
    eventAction(final EventMessage em)\n
    '''
def handleAddUpdateEvent():
    '''returns None\n\n
    handleAddUpdateEvent(final Vector eventInfoVector, final MboRemote mbo, final String eventType)\n
    '''
def addUpdateMboToCollection():
    '''returns None\n\n
    addUpdateMboToCollection(final MboRemote mbo, final long dmCollectionId, final String eventType)\n
    '''
def handleDeleteEvent():
    '''returns None\n\n
    handleDeleteEvent(final Vector eventInfoVector, final MboRemote mbo)\n
    '''
def deleteFromCollection():
    '''returns None\n\n
    deleteFromCollection(final MboRemote mbo, final long dmCollectionId)\n
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
