def sendDoc():
    '''returns ArrayList\n\n
    sendDoc(final String s)\n
    '''
def ():
    '''returns DsmlConnection\n\n
    ()\n
    (final LDAPSocketFactory ldapSocketFactory)\n
    '''
def connect():
    '''returns None\n\n
    connect(final String serverString, final int n)\n
    '''
def bind():
    '''returns None\n\n
    bind(final int n, final String s, final byte[] bytes, final LDAPConstraints ldapConstraints)\n
    bind(final int n, final String s, final byte[] array, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)\n
    bind(final int n, final String s, final byte[] array, final LDAPResponseQueue ldapResponseQueue)\n
    bind(final int n, final String s, final byte[] bytes)\n
    bind(final int n, final String s, final String original, final LDAPConstraints ldapConstraints)\n
    bind(final int n, final String s, final String original)\n
    bind(final String s, final String original, final LDAPConstraints ldapConstraints)\n
    bind(final String s, final String original, final Map map, final Object o, final LDAPConstraints ldapConstraints)\n
    bind(final String s, final String original, final Map map, final Object o)\n
    bind(final String s, final String original, final String[] array, final Map map, final Object o, final LDAPConstraints ldapConstraints)\n
    bind(final String s, final String s2, final String[] array, final Map map, final Object o)\n
    bind(final String s, final String s2)\n
    '''
def add():
    '''returns None\n\n
    add(final LDAPEntry ldapEntry, final LDAPConstraints ldapConstraints)\n
    add(final LDAPEntry ldapEntry, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)\n
    add(final LDAPEntry ldapEntry, final LDAPResponseQueue ldapResponseQueue)\n
    add(final LDAPEntry ldapEntry)\n
    '''
def modify():
    '''returns None\n\n
    modify(final String s, final LDAPModification ldapModification, final LDAPConstraints ldapConstraints)\n
    modify(final String s, final LDAPModification ldapModification, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)\n
    modify(final String s, final LDAPModification ldapModification, final LDAPResponseQueue ldapResponseQueue)\n
    modify(final String s, final LDAPModification ldapModification)\n
    modify(final String s, final LDAPModification[] array, final LDAPConstraints ldapConstraints)\n
    modify(final String s, final LDAPModification[] array, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)\n
    modify(final String s, final LDAPModification[] array, final LDAPResponseQueue ldapResponseQueue)\n
    modify(final String s, final LDAPModification[] array)\n
    '''
def rename():
    '''returns None\n\n
    rename(final String s, final String s2, final boolean b, final LDAPConstraints ldapConstraints)\n
    rename(final String s, final String s2, final boolean b, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)\n
    rename(final String s, final String s2, final boolean b, final LDAPResponseQueue ldapResponseQueue)\n
    rename(final String s, final String s2, final boolean b)\n
    rename(final String s, final String s2, final String s3, final boolean b, final LDAPConstraints ldapConstraints)\n
    rename(final String s, final String s2, final String s3, final boolean b, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)\n
    rename(final String s, final String s2, final String s3, final boolean b, final LDAPResponseQueue ldapResponseQueue)\n
    rename(final String s, final String s2, final String s3, final boolean b)\n
    '''
def delete():
    '''returns None\n\n
    delete(final String s, final LDAPConstraints ldapConstraints)\n
    delete(final String s, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)\n
    delete(final String s, final LDAPResponseQueue ldapResponseQueue)\n
    delete(final String s)\n
    '''
def search():
    '''returns LDAPSearchResults\n\n
    search(final String s, final int n, final String s2, final String[] array, final boolean b, final LDAPSearchConstraints ldapSearchConstraints)\n
    search(final String s, final int n, final String s2, final String[] array, final boolean b, final LDAPSearchQueue ldapSearchQueue, final LDAPSearchConstraints ldapSearchConstraints)\n
    search(final String s, final int n, final String s2, final String[] array, final boolean b, final LDAPSearchQueue ldapSearchQueue)\n
    search(final String s, final int n, final String s2, final String[] array, final boolean b)\n
    '''
def isConnectionAlive():
    '''returns boolean\n\n
    isConnectionAlive()\n
    '''
def isBound():
    '''returns boolean\n\n
    isBound()\n
    '''
def isConnected():
    '''returns boolean\n\n
    isConnected()\n
    '''
def isTLS():
    '''returns boolean\n\n
    isTLS()\n
    '''
def disconnect():
    '''returns None\n\n
    disconnect()\n
    disconnect(final LDAPConstraints ldapConstraints)\n
    '''
def sendRequest():
    '''returns LDAPMessageQueue\n\n
    sendRequest(final LDAPMessage ldapMessage, final LDAPMessageQueue ldapMessageQueue)\n
    '''
def getCallback():
    '''returns HttpRequestCallback\n\n
    getCallback()\n
    '''
def setCallback():
    '''returns None\n\n
    setCallback(final HttpRequestCallback callback)\n
    '''
def getBinddn():
    '''returns String\n\n
    getBinddn()\n
    '''
def getCon():
    '''returns HttpClient\n\n
    getCon()\n
    '''
def getHost():
    '''returns String\n\n
    getHost()\n
    '''
def getPass():
    '''returns String\n\n
    getPass()\n
    '''
def getServerString():
    '''returns String\n\n
    getServerString()\n
    '''
