def ():
    '''returns IlvFormReader\n\n
    (final IlvFormDevice b)\n
    '''
def getFormDevice():
    '''returns IlvFormDevice\n\n
    getFormDevice()\n
    '''
def setFormDevice():
    '''returns None\n\n
    setFormDevice(final IlvFormDevice b)\n
    '''
def readObject():
    '''returns Object\n\n
    readObject(final Element element, final IlvServicesProvider ilvServicesProvider)\n
    '''
def readObjectContent():
    '''returns IlvForm\n\n
    readObjectContent(final Object o, final Element element, final IlvServicesProvider ilvServicesProvider)\n
    readObjectContent(final Object o, final URL url, final IlvServicesProvider ilvServicesProvider)\n
    '''
def removeReaderFormat():
    '''returns boolean\n\n
    removeReaderFormat(final IlvFormReaderFormat o)\n
    '''
def registerObjectReader():
    '''returns None\n\n
    registerObjectReader(final String s, final Class clazz, final IlvObjectReader ilvObjectReader)\n
    '''
def unregisterObjectReader():
    '''returns IlvObjectReader\n\n
    unregisterObjectReader(final String s)\n
    '''
def warning():
    '''returns None\n\n
    warning(final SAXParseException ex)\n
    '''
def error():
    '''returns None\n\n
    error(final SAXParseException ex)\n
    '''
def fatalError():
    '''returns None\n\n
    fatalError(final SAXParseException ex)\n
    '''
