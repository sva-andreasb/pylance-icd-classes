LT_USER_JAVA_COMP = "short  4097"
LT_USER_JAVA_APP = "short  4099"
LT_ANON_MASK = "short  2048"
LT_SERVER_APP_MASK = "short  8192"
LT_MUX_APP_MASK = "short  16384"
LT_SERVER_APP = "short  8192"
LT_MUX_APP = "short  24576"
LT_LIGHT_CLIENT_USER = "short  4106"
def ():
    '''returns STUserInstance\n\n
    (final STLoginId loginId, final short loginType, final STId stId, final String s, final String s2, final InetAddress ip, final STServer server)\n
    (final NdrInputStream ndrInputStream)\n
    '''
def dump():
    '''returns None\n\n
    dump(final NdrOutputStream ndrOutputStream, final boolean v)\n
    dump(final NdrOutputStream ndrOutputStream)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
def getLoginType():
    '''returns short\n\n
    getLoginType()\n
    '''
def isAnon():
    '''returns boolean\n\n
    isAnon()\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    '''
def getCommunityName():
    '''returns String\n\n
    getCommunityName()\n
    '''
def getServerId():
    '''returns STServer\n\n
    getServerId()\n
    '''
def getLoginId():
    '''returns STLoginId\n\n
    getLoginId()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
