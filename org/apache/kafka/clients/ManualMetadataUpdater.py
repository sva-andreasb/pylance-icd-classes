def ():
    '''returns ManualMetadataUpdater\n\n
    ()\n
    (final List<Node> nodes)\n
    '''
def setNodes():
    '''returns None\n\n
    setNodes(final List<Node> nodes)\n
    '''
def fetchNodes():
    '''returns List<Node>\n\n
    fetchNodes()\n
    '''
def isUpdateDue():
    '''returns boolean\n\n
    isUpdateDue(final long now)\n
    '''
def maybeUpdate():
    '''returns long\n\n
    maybeUpdate(final long now)\n
    '''
def handleDisconnection():
    '''returns None\n\n
    handleDisconnection(final String destination)\n
    '''
def handleAuthenticationFailure():
    '''returns None\n\n
    handleAuthenticationFailure(final AuthenticationException exception)\n
    '''
def handleCompletedMetadataResponse():
    '''returns None\n\n
    handleCompletedMetadataResponse(final RequestHeader requestHeader, final long now, final MetadataResponse response)\n
    '''
def requestUpdate():
    '''returns None\n\n
    requestUpdate()\n
    '''
