ELEMENT = "String  \"query\""
NAMESPACE = "String  \"urn:xmpp:mam:1\""
def ():
    '''returns MamQueryIQ\n\n
    (final String queryId)\n
    (final DataForm form)\n
    (final String queryId, final DataForm form)\n
    (final String queryId, final String node, final DataForm dataForm)\n
    '''
def getQueryId():
    '''returns String\n\n
    getQueryId()\n
    '''
def getNode():
    '''returns String\n\n
    getNode()\n
    '''
def getDataForm():
    '''returns DataForm\n\n
    getDataForm()\n
    '''
