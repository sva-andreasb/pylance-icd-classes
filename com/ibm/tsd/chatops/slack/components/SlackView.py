TYPE_MODAL = "String  \"modal\""
TYPE_HOME = "String  \"home\""
def ():
    '''returns SlackView\n\n
    (final String type, final String title, final JSONArray blocks)\n
    '''
def setCallbackId():
    '''returns None\n\n
    setCallbackId(final String callbackId)\n
    '''
def setTitle():
    '''returns None\n\n
    setTitle(final String title)\n
    '''
def setSubmit():
    '''returns None\n\n
    setSubmit(final String submit)\n
    '''
def setBlocks():
    '''returns None\n\n
    setBlocks(final JSONArray block)\n
    '''
def setClose():
    '''returns None\n\n
    setClose(final String close)\n
    '''
def setPrivateMetadata():
    '''returns None\n\n
    setPrivateMetadata(final String privateMetadata)\n
    '''
def clearOnClose():
    '''returns None\n\n
    clearOnClose(final boolean clear)\n
    '''
def notifyOnClose():
    '''returns None\n\n
    notifyOnClose(final boolean notify)\n
    '''
def setExternalId():
    '''returns None\n\n
    setExternalId(final String externalId)\n
    '''
def getCallbackId():
    '''returns String\n\n
    getCallbackId()\n
    '''
def getTitle():
    '''returns String\n\n
    getTitle()\n
    '''
def getSubmit():
    '''returns SlackText\n\n
    getSubmit()\n
    '''
def getClose():
    '''returns SlackText\n\n
    getClose()\n
    '''
def getPrivateMetadata():
    '''returns String\n\n
    getPrivateMetadata()\n
    '''
def getClearOnClose():
    '''returns boolean\n\n
    getClearOnClose()\n
    '''
def getNotifyOnClose():
    '''returns boolean\n\n
    getNotifyOnClose()\n
    '''
def getExternalId():
    '''returns String\n\n
    getExternalId()\n
    '''
def getBlocks():
    '''returns JSONArray\n\n
    getBlocks()\n
    '''
