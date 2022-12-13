def getListener():
    '''public static DMCollEventListener getListener()
    '''
def eventAction():
    '''public void eventAction(final EventMessage em)
    '''
def handleAddUpdateEvent():
    '''public void handleAddUpdateEvent(final Vector eventInfoVector, final MboRemote mbo, final String eventType)
    '''
def addUpdateMboToCollection():
    '''public void addUpdateMboToCollection(final MboRemote mbo, final long dmCollectionId, final String eventType)
    '''
def handleDeleteEvent():
    '''public void handleDeleteEvent(final Vector eventInfoVector, final MboRemote mbo)
    '''
def deleteFromCollection():
    '''public void deleteFromCollection(final MboRemote mbo, final long dmCollectionId)
    '''
def eventValidate():
    '''public boolean eventValidate(final EventMessage em)
    '''
def postCommitEventAction():
    '''public void postCommitEventAction(final EventMessage em)
    '''
def preSaveEventAction():
    '''public void preSaveEventAction(final EventMessage em)
    '''
def preSaveInternalEventAction():
    '''public void preSaveInternalEventAction(final EventMessage em)
    '''
def postSaveInternalEventAction():
    '''public void postSaveInternalEventAction(final EventMessage em)
    '''
