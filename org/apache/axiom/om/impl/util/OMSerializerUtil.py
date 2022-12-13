def serializeEndpart():
'''public static void serializeEndpart(final XMLStreamWriter writer)
'''
pass
def serializeAttribute():
'''public static void serializeAttribute(final OMAttribute attr, final XMLStreamWriter writer)
'''
pass
def serializeNamespace():
'''public static void serializeNamespace(final OMNamespace namespace, final XMLStreamWriter writer)
'''
pass
def isSetPrefixBeforeStartElement():
'''public static boolean isSetPrefixBeforeStartElement(final XMLStreamWriter writer)
'''
pass
def serializeStartpart():
'''public static void serializeStartpart(final OMElement element, final XMLStreamWriter writer)
public static void serializeStartpart(final OMElement element, final String localName, final XMLStreamWriter writer)
'''
pass
def serializeNamespaces():
'''public static void serializeNamespaces(final OMElement element, final XMLStreamWriter writer)
'''
pass
def serializeAttributes():
'''public static void serializeAttributes(final OMElement element, final XMLStreamWriter writer)
'''
pass
def serializeNormal():
'''public static void serializeNormal(final OMElement element, final XMLStreamWriter writer, final boolean cache)
'''
pass
def serializeByPullStream():
'''public static void serializeByPullStream(final OMElement element, final XMLStreamWriter writer)
public static void serializeByPullStream(final OMElement element, final XMLStreamWriter writer, final boolean cache)
'''
pass
def getNextNSPrefix():
'''public static String getNextNSPrefix()
public static String getNextNSPrefix(final XMLStreamWriter writer)
'''
pass
def generateSetPrefix():
'''public static String generateSetPrefix(String prefix, final String namespace, final XMLStreamWriter writer, final boolean attr)
'''
pass
def isAssociated():
'''public static boolean isAssociated(String prefix, String namespace, final XMLStreamWriter writer)
'''
pass
