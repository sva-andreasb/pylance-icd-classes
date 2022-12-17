RemoteObjectCacheSize = "String  \"com.ibm.websphere.RemoteObjectCacheSize\""
def setDelegateResolver():
    '''returns None\n\n
    setDelegateResolver(final ObjectResolver or)\n
    '''
def setModelName():
    '''returns None\n\n
    setModelName(final String modelName)\n
    '''
def init():
    '''returns None\n\n
    init(final ORB orb, final NamingContext nc, final String serverName)\n
    '''
def keyToObject():
    '''returns Object\n\n
    keyToObject(final byte[] byteKey)\n
    '''
def objectToKey():
    '''returns byte[]\n\n
    objectToKey(final Object object)\n
    '''
def preinvoke():
    '''returns Object\n\n
    preinvoke(final Object object, final String operation)\n
    '''
def postinvoke():
    '''returns None\n\n
    postinvoke(final Object object)\n
    '''
def createObjectAdapter():
    '''returns EJSObjectAdapter\n\n
    createObjectAdapter(final String name)\n
    createObjectAdapter(final String name, final ServantManager manager)\n
    '''
def destroyObjectAdapter():
    '''returns None\n\n
    destroyObjectAdapter(final String name)\n
    '''
def quiesce():
    '''returns None\n\n
    quiesce(final SystemException e)\n
    '''
def retireObjectAdapter():
    '''returns None\n\n
    retireObjectAdapter(final String name)\n
    '''
def getDelegateOR():
    '''returns Object\n\n
    getDelegateOR()\n
    '''
def getObjectAdapter():
    '''returns ObjectAdapter\n\n
    getObjectAdapter(final String name)\n
    '''
def createIOR():
    '''returns IOR\n\n
    createIOR(final ByteArray key, final Identity cluster, final boolean useLsd, final String typeid, final EJSOAImpl oa)\n
    '''
def createCompleteKey():
    '''returns UserKey\n\n
    createCompleteKey(final boolean wlmable, final EJSOAImpl oa, final byte[] key)\n
    '''
