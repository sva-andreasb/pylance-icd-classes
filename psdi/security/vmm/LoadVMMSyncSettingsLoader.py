def ():
    '''returns XMLEntityResolver\n\n
    ()\n
    (final Connection connection, final UserInfo userInfo)\n
    (final String inDTD)\n
    '''
def load():
    '''returns LoadVMMSyncSettings\n\n
    load(final String task, final String taskInstance)\n
    '''
def getConnection():
    '''returns Connection\n\n
    getConnection()\n
    '''
def getUserInfo():
    '''returns UserInfo\n\n
    getUserInfo()\n
    '''
def getTaskInstanceName():
    '''returns String\n\n
    getTaskInstanceName()\n
    '''
def getTaskName():
    '''returns String\n\n
    getTaskName()\n
    '''
def resolveEntity():
    '''returns InputSource\n\n
    resolveEntity(final String publicId, final String systemId)\n
    '''
def error():
    '''returns None\n\n
    error(final SAXParseException e)\n
    '''
def fatalError():
    '''returns None\n\n
    fatalError(final SAXParseException e)\n
    '''
def warning():
    '''returns None\n\n
    warning(final SAXParseException exception)\n
    '''
