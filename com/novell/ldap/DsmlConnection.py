def sendDoc():
'''public ArrayList sendDoc(final String s)
'''
pass
def DsmlConnection():
'''public DsmlConnection()
public DsmlConnection(final LDAPSocketFactory ldapSocketFactory)
'''
pass
def connect():
'''public void connect(final String serverString, final int n)
'''
pass
def bind():
'''public void bind(final int n, final String s, final byte[] bytes, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue bind(final int n, final String s, final byte[] array, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue bind(final int n, final String s, final byte[] array, final LDAPResponseQueue ldapResponseQueue)
public void bind(final int n, final String s, final byte[] bytes)
public void bind(final int n, final String s, final String original, final LDAPConstraints ldapConstraints)
public void bind(final int n, final String s, final String original)
public void bind(final String s, final String original, final LDAPConstraints ldapConstraints)
public void bind(final String s, final String original, final Map map, final Object o, final LDAPConstraints ldapConstraints)
public void bind(final String s, final String original, final Map map, final Object o)
public void bind(final String s, final String original, final String[] array, final Map map, final Object o, final LDAPConstraints ldapConstraints)
public void bind(final String s, final String s2, final String[] array, final Map map, final Object o)
public void bind(final String s, final String s2)
'''
pass
def add():
'''public void add(final LDAPEntry ldapEntry, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue add(final LDAPEntry ldapEntry, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue add(final LDAPEntry ldapEntry, final LDAPResponseQueue ldapResponseQueue)
public void add(final LDAPEntry ldapEntry)
'''
pass
def modify():
'''public void modify(final String s, final LDAPModification ldapModification, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue modify(final String s, final LDAPModification ldapModification, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue modify(final String s, final LDAPModification ldapModification, final LDAPResponseQueue ldapResponseQueue)
public void modify(final String s, final LDAPModification ldapModification)
public void modify(final String s, final LDAPModification[] array, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue modify(final String s, final LDAPModification[] array, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue modify(final String s, final LDAPModification[] array, final LDAPResponseQueue ldapResponseQueue)
public void modify(final String s, final LDAPModification[] array)
'''
pass
def rename():
'''public void rename(final String s, final String s2, final boolean b, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue rename(final String s, final String s2, final boolean b, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue rename(final String s, final String s2, final boolean b, final LDAPResponseQueue ldapResponseQueue)
public void rename(final String s, final String s2, final boolean b)
public void rename(final String s, final String s2, final String s3, final boolean b, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue rename(final String s, final String s2, final String s3, final boolean b, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue rename(final String s, final String s2, final String s3, final boolean b, final LDAPResponseQueue ldapResponseQueue)
public void rename(final String s, final String s2, final String s3, final boolean b)
'''
pass
def delete():
'''public void delete(final String s, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue delete(final String s, final LDAPResponseQueue ldapResponseQueue, final LDAPConstraints ldapConstraints)
public LDAPResponseQueue delete(final String s, final LDAPResponseQueue ldapResponseQueue)
public void delete(final String s)
'''
pass
def search():
'''public LDAPSearchResults search(final String s, final int n, final String s2, final String[] array, final boolean b, final LDAPSearchConstraints ldapSearchConstraints)
public LDAPSearchQueue search(final String s, final int n, final String s2, final String[] array, final boolean b, final LDAPSearchQueue ldapSearchQueue, final LDAPSearchConstraints ldapSearchConstraints)
public LDAPSearchQueue search(final String s, final int n, final String s2, final String[] array, final boolean b, final LDAPSearchQueue ldapSearchQueue)
public LDAPSearchResults search(final String s, final int n, final String s2, final String[] array, final boolean b)
'''
pass
def isConnectionAlive():
'''public boolean isConnectionAlive()
'''
pass
def isBound():
'''public boolean isBound()
'''
pass
def isConnected():
'''public boolean isConnected()
'''
pass
def isTLS():
'''public boolean isTLS()
'''
pass
def disconnect():
'''public void disconnect()
public void disconnect(final LDAPConstraints ldapConstraints)
'''
pass
def sendRequest():
'''public LDAPMessageQueue sendRequest(final LDAPMessage ldapMessage, final LDAPMessageQueue ldapMessageQueue)
'''
pass
def getCallback():
'''public HttpRequestCallback getCallback()
'''
pass
def setCallback():
'''public void setCallback(final HttpRequestCallback callback)
'''
pass
def getBinddn():
'''public String getBinddn()
'''
pass
def getCon():
'''public HttpClient getCon()
'''
pass
def getHost():
'''public String getHost()
'''
pass
def getPass():
'''public String getPass()
'''
pass
def getServerString():
'''public String getServerString()
'''
pass
