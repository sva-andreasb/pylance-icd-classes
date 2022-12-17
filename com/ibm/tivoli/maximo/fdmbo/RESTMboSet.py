def ():
    '''returns RESTMboSet\n\n
    (final MboServerInterface ms)\n
    '''
def execute():
    '''returns None\n\n
    execute()\n
    '''
def load():
    '''returns None\n\n
    load(int index)\n
    '''
def invoke():
    '''returns byte[]\n\n
    invoke(final int index, final boolean forCount)\n
    '''
def setQbe():
    '''returns None\n\n
    setQbe(final String attribute, final String expression)\n
    '''
def getOpAndValue():
    '''returns Object[]\n\n
    getOpAndValue(final String expression)\n
    '''
def resetQbe():
    '''returns None\n\n
    resetQbe()\n
    '''
def getHTTPQueryMethod():
    '''returns String\n\n
    getHTTPQueryMethod()\n
    '''
def formatUrl():
    '''returns String\n\n
    formatUrl(final String url, final String method)\n
    '''
def formatUrlForSortPage():
    '''returns String\n\n
    formatUrlForSortPage(final String url, final int index, final boolean forCount, final String method)\n
    '''
def formatPostData():
    '''returns byte[]\n\n
    formatPostData(final int index, final boolean forCount)\n
    '''
def formatPostDataForNextPage():
    '''returns byte[]\n\n
    formatPostDataForNextPage(final byte[] data, final int index)\n
    '''
def getWhereSeparator():
    '''returns String\n\n
    getWhereSeparator()\n
    '''
def formatWhere():
    '''returns None\n\n
    formatWhere(final List<String> whereList, final String where)\n
    '''
def formatUrlForNextPage():
    '''returns String\n\n
    formatUrlForNextPage(final String url, final int index, final String method)\n
    '''
def getOrderByClouse():
    '''returns String\n\n
    getOrderByClouse()\n
    '''
def getCountClause():
    '''returns String\n\n
    getCountClause()\n
    '''
def getPagingParams():
    '''returns String[]\n\n
    getPagingParams()\n
    '''
def getStringQualifier():
    '''returns String\n\n
    getStringQualifier()\n
    '''
def getUrl():
    '''returns String\n\n
    getUrl(final HTTPHandler handler, final boolean forCount)\n
    '''
def getWhereToFormat():
    '''returns String\n\n
    getWhereToFormat(final String where)\n
    getWhereToFormat(final String where, final boolean isRelationship)\n
    '''
def moveTo():
    '''returns MboRemote\n\n
    moveTo(final int pos)\n
    '''
def moveNext():
    '''returns MboRemote\n\n
    moveNext()\n
    '''
