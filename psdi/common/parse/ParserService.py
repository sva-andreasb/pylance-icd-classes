def ():
    '''returns ParserService\n\n
    (final MXServer mxServer)\n
    (final String url, final MXServer mxServer)\n
    '''
def configure():
    '''returns None\n\n
    configure(final Properties properties)\n
    '''
def parse():
    '''returns None\n\n
    parse(String str, final MboRemote mbo)\n
    '''
def getNodeDataType():
    '''returns int\n\n
    getNodeDataType(final String str)\n
    getNodeDataType(final String str, final MboRemote mbo)\n
    '''
def getBoolean():
    '''returns boolean\n\n
    getBoolean(final String str, final MboRemote mbo)\n
    '''
def getString():
    '''returns String\n\n
    getString(final String str, final MboRemote mbo)\n
    '''
def getDouble():
    '''returns double\n\n
    getDouble(final String str, final MboRemote mbo)\n
    '''
def getInt():
    '''returns int\n\n
    getInt(final String str, final MboRemote mbo)\n
    '''
def getDate():
    '''returns Date\n\n
    getDate(final String str, final MboRemote mbo)\n
    '''
def nodeString():
    '''returns String\n\n
    nodeString(final String str)\n
    '''
def getURL():
    '''returns String\n\n
    getURL()\n
    '''
def setURL():
    '''returns None\n\n
    setURL(final String url)\n
    '''
def isAppService():
    '''returns boolean\n\n
    isAppService()\n
    '''
def restart():
    '''returns None\n\n
    restart()\n
    '''
def isSingletonService():
    '''returns boolean\n\n
    isSingletonService()\n
    '''
def destroy():
    '''returns None\n\n
    destroy()\n
    '''
def checkSqlInjection():
    '''returns None\n\n
    checkSqlInjection(final String where)\n
    '''
