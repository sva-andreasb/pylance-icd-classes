SCOPE_PER_ACCESS = "int  0"
SCOPE_PER_REQUEST = "int  1"
SCOPE_SINGLETON = "int  2"
def WSDDDeployableItem():
    '''public WSDDDeployableItem()
    public WSDDDeployableItem(final Element e)
    '''
def setName():
    '''public void setName(final String name)
    '''
def setQName():
    '''public void setQName(final QName qname)
    '''
def getQName():
    '''public QName getQName()
    '''
def getType():
    '''public QName getType()
    '''
def setType():
    '''public void setType(final QName type)
    '''
def setParameter():
    '''public void setParameter(final String name, final String value)
    '''
def getParameter():
    '''public String getParameter(final String name)
    '''
def getParametersTable():
    '''public LockableHashtable getParametersTable()
    '''
def setOptionsHashtable():
    '''public void setOptionsHashtable(final Hashtable hashtable)
    '''
def writeParamsToContext():
    '''public void writeParamsToContext(final SerializationContext context)
    '''
def removeParameter():
    '''public void removeParameter(final String name)
    '''
def getInstance():
    '''public final Handler getInstance(final EngineConfiguration registry)
    '''
def getJavaClass():
    '''public Class getJavaClass()
    '''
