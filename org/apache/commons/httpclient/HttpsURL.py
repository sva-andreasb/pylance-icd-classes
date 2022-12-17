DEFAULT_PORT = "int  443"
_default_port = "int  443"
def ():
    '''returns HttpsURL\n\n
    (final char[] escaped, final String charset)\n
    (final char[] escaped)\n
    (final String original, final String charset)\n
    (final String original)\n
    (final String host, final int port, final String path)\n
    (final String host, final int port, final String path, final String query)\n
    (final String user, final String password, final String host)\n
    (final String user, final String password, final String host, final int port)\n
    (final String user, final String password, final String host, final int port, final String path)\n
    (final String user, final String password, final String host, final int port, final String path, final String query)\n
    (final String host, final String path, final String query, final String fragment)\n
    (final String userinfo, final String host, final String path, final String query, final String fragment)\n
    (final String userinfo, final String host, final int port, final String path)\n
    (final String userinfo, final String host, final int port, final String path, final String query)\n
    (final String userinfo, final String host, final int port, final String path, final String query, final String fragment)\n
    (final String user, final String password, final String host, final int port, final String path, final String query, final String fragment)\n
    (final HttpsURL base, final String relative)\n
    (final HttpsURL base, final HttpsURL relative)\n
    '''
def getRawScheme():
    '''returns char[]\n\n
    getRawScheme()\n
    '''
def getScheme():
    '''returns String\n\n
    getScheme()\n
    '''
def getPort():
    '''returns int\n\n
    getPort()\n
    '''
