def XMLInputFactoryImpl():
'''public XMLInputFactoryImpl()
'''
pass
def createXMLStreamReader():
'''public XMLStreamReader createXMLStreamReader(final Reader reader)
public XMLStreamReader createXMLStreamReader(final Source source)
public XMLStreamReader createXMLStreamReader(final InputStream inputStream)
public XMLStreamReader createXMLStreamReader(final InputStream inputStream, final String s)
public XMLStreamReader createXMLStreamReader(final String s, final InputStream inputStream)
public XMLStreamReader createXMLStreamReader(final String s, final Reader reader)
'''
pass
def createXMLEventReader():
'''public XMLEventReader createXMLEventReader(final Reader reader)
public XMLEventReader createXMLEventReader(final String s, final Reader reader)
public XMLEventReader createXMLEventReader(final XMLStreamReader xmlStreamReader)
public XMLEventReader createXMLEventReader(final Source source)
public XMLEventReader createXMLEventReader(final InputStream inputStream)
public XMLEventReader createXMLEventReader(final InputStream inputStream, final String s)
public XMLEventReader createXMLEventReader(final String s, final InputStream inputStream)
'''
pass
def createFilteredReader():
'''public XMLStreamReader createFilteredReader(final XMLStreamReader xmlStreamReader, final StreamFilter streamFilter)
public XMLEventReader createFilteredReader(final XMLEventReader xmlEventReader, final EventFilter eventFilter)
'''
pass
def getXMLResolver():
'''public XMLResolver getXMLResolver()
'''
pass
def setXMLResolver():
'''public void setXMLResolver(final XMLResolver resolver)
'''
pass
def getXMLReporter():
'''public XMLReporter getXMLReporter()
'''
pass
def setXMLReporter():
'''public void setXMLReporter(final XMLReporter reporter)
'''
pass
def setProperty():
'''public void setProperty(final String anObject, final Object o)
'''
pass
def getProperty():
'''public Object getProperty(final String s)
public Object getProperty(final String s)
public Object getProperty(final String s)
public Object getProperty(final String s)
public Object getProperty(final String s)
'''
pass
def isPropertySupported():
'''public boolean isPropertySupported(final String anObject)
'''
pass
def setEventAllocator():
'''public void setEventAllocator(final XMLEventAllocator allocator)
'''
pass
def getEventAllocator():
'''public XMLEventAllocator getEventAllocator()
'''
pass
def Properties():
'''public Properties()
public Properties(final Properties properties)
'''
pass
def XMLStreamReaderProxy():
'''public XMLStreamReaderProxy(final XMLStreamReader fStreamReader)
'''
pass
def insertFilter():
'''public void insertFilter(final XMLStreamReader fStreamReader)
'''
pass
def next():
'''public int next()
public int next()
public int next()
public int next()
'''
pass
def require():
'''public void require(final int n, final String s, final String s2)
public void require(final int value, final String s, final String s2)
public void require(final int value, final String s, final String s2)
public void require(final int n, final String s, final String s2)
'''
pass
def getElementText():
'''public String getElementText()
public String getElementText()
public String getElementText()
public String getElementText()
'''
pass
def nextTag():
'''public int nextTag()
public int nextTag()
public int nextTag()
public int nextTag()
'''
pass
def hasNext():
'''public boolean hasNext()
public boolean hasNext()
public boolean hasNext()
public boolean hasNext()
'''
pass
def close():
'''public void close()
public void close()
public void close()
public void close()
'''
pass
def getNamespaceURI():
'''public String getNamespaceURI(final String s)
public String getNamespaceURI(final int n)
public String getNamespaceURI()
public String getNamespaceURI(final String s)
public String getNamespaceURI(final int n)
public String getNamespaceURI()
public String getNamespaceURI(final String s)
public String getNamespaceURI(final int n)
public String getNamespaceURI()
public String getNamespaceURI(final String s)
public String getNamespaceURI(final int n)
public String getNamespaceURI()
'''
pass
def isStartElement():
'''public boolean isStartElement()
public boolean isStartElement()
public boolean isStartElement()
public boolean isStartElement()
'''
pass
def isEndElement():
'''public boolean isEndElement()
public boolean isEndElement()
public boolean isEndElement()
public boolean isEndElement()
'''
pass
def isCharacters():
'''public boolean isCharacters()
public boolean isCharacters()
public boolean isCharacters()
public boolean isCharacters()
'''
pass
def isWhiteSpace():
'''public boolean isWhiteSpace()
public boolean isWhiteSpace()
public boolean isWhiteSpace()
public boolean isWhiteSpace()
'''
pass
def getAttributeValue():
'''public String getAttributeValue(final String s, final String s2)
public String getAttributeValue(final int n)
public String getAttributeValue(final String s, final String s2)
public String getAttributeValue(final int n)
public String getAttributeValue(final String s, final String s2)
public String getAttributeValue(final int n)
public String getAttributeValue(final String s, final String s2)
public String getAttributeValue(final int n)
'''
pass
def getAttributeCount():
'''public int getAttributeCount()
public int getAttributeCount()
public int getAttributeCount()
public int getAttributeCount()
'''
pass
def getAttributeName():
'''public QName getAttributeName(final int n)
public QName getAttributeName(final int n)
public QName getAttributeName(final int n)
public QName getAttributeName(final int n)
'''
pass
def getAttributeNamespace():
'''public String getAttributeNamespace(final int n)
public String getAttributeNamespace(final int n)
public String getAttributeNamespace(final int n)
public String getAttributeNamespace(final int n)
'''
pass
def getAttributeLocalName():
'''public String getAttributeLocalName(final int n)
public String getAttributeLocalName(final int n)
public String getAttributeLocalName(final int n)
public String getAttributeLocalName(final int n)
'''
pass
def getAttributePrefix():
'''public String getAttributePrefix(final int n)
public String getAttributePrefix(final int n)
public String getAttributePrefix(final int n)
public String getAttributePrefix(final int n)
'''
pass
def getAttributeType():
'''public String getAttributeType(final int n)
public String getAttributeType(final int n)
public String getAttributeType(final int n)
public String getAttributeType(final int n)
'''
pass
def isAttributeSpecified():
'''public boolean isAttributeSpecified(final int n)
public boolean isAttributeSpecified(final int n)
public boolean isAttributeSpecified(final int n)
public boolean isAttributeSpecified(final int n)
'''
pass
def getNamespaceCount():
'''public int getNamespaceCount()
public int getNamespaceCount()
public int getNamespaceCount()
public int getNamespaceCount()
'''
pass
def getNamespacePrefix():
'''public String getNamespacePrefix(final int n)
public String getNamespacePrefix(final int n)
public String getNamespacePrefix(final int n)
public String getNamespacePrefix(final int n)
'''
pass
def getNamespaceContext():
'''public NamespaceContext getNamespaceContext()
public NamespaceContext getNamespaceContext()
public NamespaceContext getNamespaceContext()
public NamespaceContext getNamespaceContext()
'''
pass
def getEventType():
'''public int getEventType()
public int getEventType()
public int getEventType()
public int getEventType()
'''
pass
def getText():
'''public String getText()
public String getText()
public String getText()
public String getText()
'''
pass
def getTextCharacters():
'''public char[] getTextCharacters()
public int getTextCharacters(final int n, final char[] array, final int n2, final int n3)
public char[] getTextCharacters()
public int getTextCharacters(final int n, final char[] array, final int n2, final int n3)
public char[] getTextCharacters()
public int getTextCharacters(final int value, final char[] array, final int value2, final int value3)
public char[] getTextCharacters()
public int getTextCharacters(final int n, final char[] array, final int n2, final int n3)
'''
pass
def getTextStart():
'''public int getTextStart()
public int getTextStart()
public int getTextStart()
public int getTextStart()
'''
pass
def getTextLength():
'''public int getTextLength()
public int getTextLength()
public int getTextLength()
public int getTextLength()
'''
pass
def getEncoding():
'''public String getEncoding()
public String getEncoding()
public String getEncoding()
public String getEncoding()
'''
pass
def hasText():
'''public boolean hasText()
public boolean hasText()
public boolean hasText()
public boolean hasText()
'''
pass
def getLocation():
'''public Location getLocation()
public Location getLocation()
public Location getLocation()
public Location getLocation()
'''
pass
def getName():
'''public QName getName()
public QName getName()
public QName getName()
public QName getName()
'''
pass
def getLocalName():
'''public String getLocalName()
public String getLocalName()
public String getLocalName()
public String getLocalName()
'''
pass
def hasName():
'''public boolean hasName()
public boolean hasName()
public boolean hasName()
public boolean hasName()
'''
pass
def getPrefix():
'''public String getPrefix()
public String getPrefix()
public String getPrefix()
public String getPrefix()
'''
pass
def getVersion():
'''public String getVersion()
public String getVersion()
public String getVersion()
public String getVersion()
'''
pass
def isStandalone():
'''public boolean isStandalone()
public boolean isStandalone()
public boolean isStandalone()
public boolean isStandalone()
'''
pass
def standaloneSet():
'''public boolean standaloneSet()
public boolean standaloneSet()
public boolean standaloneSet()
public boolean standaloneSet()
'''
pass
def getCharacterEncodingScheme():
'''public String getCharacterEncodingScheme()
public String getCharacterEncodingScheme()
public String getCharacterEncodingScheme()
public String getCharacterEncodingScheme()
'''
pass
def getPITarget():
'''public String getPITarget()
public String getPITarget()
public String getPITarget()
public String getPITarget()
'''
pass
def getPIData():
'''public String getPIData()
public String getPIData()
public String getPIData()
public String getPIData()
'''
pass
def XMLStreamReaderTracer():
'''public XMLStreamReaderTracer(final XMLStreamReader xmlStreamReader)
'''
pass
def writeStAXProfile():
'''public void writeStAXProfile(final String s)
'''
pass
def writeReadableProfile():
'''public void writeReadableProfile(final String s)
'''
pass
def ClosedXMLStreamReader():
'''public ClosedXMLStreamReader()
'''
pass
