def getInstanceFor():
'''public static synchronized PrivateDataManager getInstanceFor(final XMPPConnection connection)
'''
pass
def getPrivateDataProvider():
'''public static PrivateDataProvider getPrivateDataProvider(final String elementName, final String namespace)
'''
pass
def addPrivateDataProvider():
'''public static void addPrivateDataProvider(final String elementName, final String namespace, final PrivateDataProvider provider)
'''
pass
def removePrivateDataProvider():
'''public static void removePrivateDataProvider(final String elementName, final String namespace)
'''
pass
def getPrivateData():
'''public PrivateData getPrivateData(final String elementName, final String namespace)
'''
pass
def setPrivateData():
'''public void setPrivateData(final PrivateData privateData)
'''
pass
def isSupported():
'''public boolean isSupported()
'''
pass
def getElementName():
'''public String getElementName()
'''
pass
def getNamespace():
'''public String getNamespace()
'''
pass
def toXML():
'''public CharSequence toXML()
'''
pass
def parse():
'''public PrivateDataIQ parse(final XmlPullParser parser, final int initialDepth)
'''
pass
