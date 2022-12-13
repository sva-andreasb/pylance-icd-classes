def IlvFormReader():
    '''    public IlvFormReader(final IlvFormDevice b)
    '''
def getFormDevice():
    '''    public IlvFormDevice getFormDevice()
    '''
def setFormDevice():
    '''    public void setFormDevice(final IlvFormDevice b)
    '''
def readObject():
    '''    public Object readObject(final Element element, final IlvServicesProvider ilvServicesProvider)
    '''
def readObjectContent():
    '''    public IlvForm readObjectContent(final Object o, final Element element, final IlvServicesProvider ilvServicesProvider)
    public IlvForm readObjectContent(final Object o, final URL url, final IlvServicesProvider ilvServicesProvider)
    '''
def removeReaderFormat():
    '''    public boolean removeReaderFormat(final IlvFormReaderFormat o)
    '''
def registerObjectReader():
    '''    public void registerObjectReader(final String s, final Class clazz, final IlvObjectReader ilvObjectReader)
    '''
def unregisterObjectReader():
    '''    public IlvObjectReader unregisterObjectReader(final String s)
    '''
def warning():
    '''    public void warning(final SAXParseException ex)
    '''
def error():
    '''    public void error(final SAXParseException ex)
    '''
def fatalError():
    '''    public void fatalError(final SAXParseException ex)
    '''
