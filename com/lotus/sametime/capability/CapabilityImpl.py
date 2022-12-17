def serviceAvailable():
    '''returns None\n\n
    serviceAvailable(final AwarenessServiceEvent awarenessServiceEvent)\n
    serviceAvailable(final ServiceEvent serviceEvent)\n
    serviceAvailable(final LoginAttributeEvent loginAttributeEvent)\n
    '''
def serviceUnavailable():
    '''returns None\n\n
    serviceUnavailable(final AwarenessServiceEvent awarenessServiceEvent)\n
    serviceUnavailable(final LoginAttributeEvent loginAttributeEvent)\n
    '''
def attrChanged():
    '''returns None\n\n
    attrChanged(final AttributeEvent attributeEvent)\n
    '''
def attrRemoved():
    '''returns None\n\n
    attrRemoved(final AttributeEvent attributeEvent)\n
    '''
def attrContentQueried():
    '''returns None\n\n
    attrContentQueried(final AttributeEvent attributeEvent)\n
    '''
def queryAttrContentFailed():
    '''returns None\n\n
    queryAttrContentFailed(final AttributeEvent attributeEvent)\n
    '''
def publishLoginAttributeResponse():
    '''returns None\n\n
    publishLoginAttributeResponse(final LoginAttributeEvent loginAttributeEvent)\n
    '''
def removeLoginAttributeResponse():
    '''returns None\n\n
    removeLoginAttributeResponse(final LoginAttributeEvent loginAttributeEvent)\n
    '''
def loggedIn():
    '''returns None\n\n
    loggedIn(final LoginEvent loginEvent)\n
    '''
def loggedOut():
    '''returns None\n\n
    loggedOut(final LoginEvent loginEvent)\n
    '''
