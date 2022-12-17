def ():
    '''returns JSON2Mbo\n\n
    (final MboSchemaInfo schemaInfo)\n
    ()\n
    '''
def jsonToMbo():
    '''returns None\n\n
    jsonToMbo(final JSONObject jo, final MboRemote mbo, final boolean contentLocalized)\n
    jsonToMbo(final JSONObject jo, final MboRemote mbo, final Iterator columns, final boolean contentLocalized, final MboSchemaInfo mboSchemaInfo)\n
    '''
def getKeyValues():
    '''returns String[]\n\n
    getKeyValues(final MboSetInfo mboSetInfo, final String[] keys, final JSONObject jo, final boolean contentLocalized, final UserInfo userInfo)\n
    '''
def getKeyValue():
    '''returns String\n\n
    getKeyValue(final String name, final JSONObject jo, final int maxType, final boolean contentLocalized, final UserInfo userInfo)\n
    '''
def getCurrentDataAsDate():
    '''returns Date\n\n
    getCurrentDataAsDate(final String col, final JSONObject jo, final boolean contentLocalized, final UserInfo userInfo)\n
    '''
def getCurrentDataAsLong():
    '''returns long\n\n
    getCurrentDataAsLong(final String col, final JSONObject jo, final boolean contentLocalized, final UserInfo userInfo)\n
    '''
def getCurrentDataAsDouble():
    '''returns double\n\n
    getCurrentDataAsDouble(final String col, final JSONObject jo, final boolean contentLocalized, final UserInfo userInfo)\n
    '''
def getCurrentDataAsBoolean():
    '''returns boolean\n\n
    getCurrentDataAsBoolean(final String col, final JSONObject jo, final boolean contentLocalized, final UserInfo userInfo)\n
    '''
