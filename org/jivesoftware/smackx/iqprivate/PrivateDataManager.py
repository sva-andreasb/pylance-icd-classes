def getInstanceFor():
    '''    public static synchronized PrivateDataManager getInstanceFor(final XMPPConnection connection)
    '''
def getPrivateDataProvider():
    '''    public static PrivateDataProvider getPrivateDataProvider(final String elementName, final String namespace)
    '''
def addPrivateDataProvider():
    '''    public static void addPrivateDataProvider(final String elementName, final String namespace, final PrivateDataProvider provider)
    '''
def removePrivateDataProvider():
    '''    public static void removePrivateDataProvider(final String elementName, final String namespace)
    '''
def getPrivateData():
    '''    public PrivateData getPrivateData(final String elementName, final String namespace)
    '''
def setPrivateData():
    '''    public void setPrivateData(final PrivateData privateData)
    '''
def isSupported():
    '''    public boolean isSupported()
    '''
def getElementName():
    '''    public String getElementName()
    '''
def getNamespace():
    '''    public String getNamespace()
    '''
def toXML():
    '''    public CharSequence toXML()
    '''
def parse():
    '''    public PrivateDataIQ parse(final XmlPullParser parser, final int initialDepth)
    '''
