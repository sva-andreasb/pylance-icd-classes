def ():
    '''returns XMLInputFactoryWrapper\n\n
    (final XMLInputFactory parent)\n
    '''
def createFilteredReader():
    '''returns XMLStreamReader\n\n
    createFilteredReader(final XMLEventReader reader, final EventFilter filter)\n
    createFilteredReader(final XMLStreamReader reader, final StreamFilter filter)\n
    '''
def createXMLEventReader():
    '''returns XMLEventReader\n\n
    createXMLEventReader(final InputStream stream, final String encoding)\n
    createXMLEventReader(final InputStream stream)\n
    createXMLEventReader(final Reader reader)\n
    createXMLEventReader(final Source source)\n
    createXMLEventReader(final String systemId, final InputStream stream)\n
    createXMLEventReader(final String systemId, final Reader reader)\n
    createXMLEventReader(final XMLStreamReader reader)\n
    '''
def createXMLStreamReader():
    '''returns XMLStreamReader\n\n
    createXMLStreamReader(final InputStream stream, final String encoding)\n
    createXMLStreamReader(final InputStream stream)\n
    createXMLStreamReader(final Reader reader)\n
    createXMLStreamReader(final Source source)\n
    createXMLStreamReader(final String systemId, final InputStream stream)\n
    createXMLStreamReader(final String systemId, final Reader reader)\n
    '''
def getEventAllocator():
    '''returns XMLEventAllocator\n\n
    getEventAllocator()\n
    '''
def getProperty():
    '''returns Object\n\n
    getProperty(final String name)\n
    '''
def getXMLReporter():
    '''returns XMLReporter\n\n
    getXMLReporter()\n
    '''
def getXMLResolver():
    '''returns XMLResolver\n\n
    getXMLResolver()\n
    '''
def isPropertySupported():
    '''returns boolean\n\n
    isPropertySupported(final String name)\n
    '''
def setEventAllocator():
    '''returns None\n\n
    setEventAllocator(final XMLEventAllocator allocator)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String name, final Object value)\n
    '''
def setXMLReporter():
    '''returns None\n\n
    setXMLReporter(final XMLReporter reporter)\n
    '''
def setXMLResolver():
    '''returns None\n\n
    setXMLResolver(final XMLResolver resolver)\n
    '''
