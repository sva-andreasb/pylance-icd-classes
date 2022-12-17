def ():
    '''returns CloudantMboSet\n\n
    (final MboServerInterface ms)\n
    '''
def getURI():
    '''returns String\n\n
    getURI()\n
    '''
def getHTTPQueryMethod():
    '''returns String\n\n
    getHTTPQueryMethod()\n
    '''
def formatPostData():
    '''returns byte[]\n\n
    formatPostData(final int index, final boolean forCount)\n
    '''
def formatPostDataForNextPage():
    '''returns byte[]\n\n
    formatPostDataForNextPage(final byte[] data, final int index)\n
    '''
def format():
    '''returns JSONQuery\n\n
    format(JSONQuery formater, final JSONResourceInfo resourceInfo, String where, final boolean forCount, final int index)\n
    '''
def addPaging():
    '''returns JSONQuery\n\n
    addPaging(JSONQuery formater, final int index, final boolean forCount)\n
    '''
def formatQBE():
    '''returns JSONQuery\n\n
    formatQBE(JSONQuery formater, final JSONResourceInfo resourceInfo, final boolean forCount, final int index)\n
    '''
def bulkUpdate():
    '''returns None\n\n
    bulkUpdate()\n
    '''
def setAdditionalData():
    '''returns None\n\n
    setAdditionalData(final MboRemote mbo, final JSONObject jo)\n
    '''
def getQualifiedWhere():
    '''returns String\n\n
    getQualifiedWhere()\n
    '''
def getUrl():
    '''returns String\n\n
    getUrl(final HTTPHandler handler, final boolean forCount)\n
    '''
def getStringQualifier():
    '''returns String\n\n
    getStringQualifier()\n
    '''
