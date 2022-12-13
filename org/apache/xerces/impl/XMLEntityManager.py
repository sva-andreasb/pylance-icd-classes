DEFAULT_BUFFER_SIZE = "int  2048"
DEFAULT_XMLDECL_BUFFER_SIZE = "int  64"
DEFAULT_INTERNAL_BUFFER_SIZE = "int  512"
def XMLEntityManager():
    '''    public XMLEntityManager()
    public XMLEntityManager(final XMLEntityManager xmlEntityManager)
    '''
def setStandalone():
    '''    public void setStandalone(final boolean fStandalone)
    '''
def isStandalone():
    '''    public boolean isStandalone()
    '''
def setEntityHandler():
    '''    public void setEntityHandler(final XMLEntityHandler fEntityHandler)
    '''
def getCurrentResourceIdentifier():
    '''    public XMLResourceIdentifier getCurrentResourceIdentifier()
    '''
def getCurrentEntity():
    '''    public ScannedEntity getCurrentEntity()
    '''
def addInternalEntity():
    '''    public void addInternalEntity(final String s, final String s2, final int n)
    public void addInternalEntity(final String s, final String s2)
    '''
def getParamEntityRefCount():
    '''    public int getParamEntityRefCount(final String key)
    '''
def addExternalEntity():
    '''    public void addExternalEntity(final String s, final String s2, final String s3, String s4)
    '''
def isExternalEntity():
    '''    public boolean isExternalEntity(final String key)
    '''
def isEntityDeclInExternalSubset():
    '''    public boolean isEntityDeclInExternalSubset(final String key)
    public boolean isEntityDeclInExternalSubset()
    '''
def addUnparsedEntity():
    '''    public void addUnparsedEntity(final String s, final String s2, final String s3, final String s4, final String s5)
    '''
def isUnparsedEntity():
    '''    public boolean isUnparsedEntity(final String key)
    '''
def isDeclaredEntity():
    '''    public boolean isDeclaredEntity(final String key)
    '''
def resolveEntity():
    '''    public XMLInputSource resolveEntity(final XMLResourceIdentifier xmlResourceIdentifier)
    '''
def startEntity():
    '''    public void startEntity(final String str, final boolean b)
    public void startEntity(final String s, final XMLInputSource xmlInputSource, final boolean b, final boolean b2)
    '''
def startDocumentEntity():
    '''    public void startDocumentEntity(final XMLInputSource xmlInputSource)
    '''
def startDTDEntity():
    '''    public void startDTDEntity(final XMLInputSource xmlInputSource)
    '''
def startExternalSubset():
    '''    public void startExternalSubset()
    '''
def endExternalSubset():
    '''    public void endExternalSubset()
    '''
def setupCurrentEntity():
    '''    public String setupCurrentEntity(final String s, final XMLInputSource xmlInputSource, final boolean b, final boolean b2)
    '''
def setScannerVersion():
    '''    public void setScannerVersion(final short n)
    '''
def getEntityScanner():
    '''    public XMLEntityScanner getEntityScanner()
    '''
def closeReaders():
    '''    public void closeReaders()
    '''
def reset():
    '''    public void reset(final XMLComponentManager xmlComponentManager)
    public void reset()
    public void reset()
    '''
def getRecognizedFeatures():
    '''    public String[] getRecognizedFeatures()
    '''
def setFeature():
    '''    public void setFeature(final String s, final boolean fAllowJavaEncodings)
    '''
def getRecognizedProperties():
    '''    public String[] getRecognizedProperties()
    '''
def setProperty():
    '''    public void setProperty(final String s, final Object o)
    '''
def getFeatureDefault():
    '''    public Boolean getFeatureDefault(final String anObject)
    '''
def getPropertyDefault():
    '''    public Object getPropertyDefault(final String anObject)
    '''
def absolutizeAgainstUserDir():
    '''    public static void absolutizeAgainstUserDir(final URI uri)
    '''
def expandSystemId():
    '''    public static String expandSystemId(final String anObject, final String s, final boolean b)
    '''
def createOutputStream():
    '''    public static OutputStream createOutputStream(final String s)
    '''
def run():
    '''    public Object run()
    '''
def RewindableInputStream():
    '''    public RewindableInputStream(final InputStream fInputStream)
    '''
def setStartOffset():
    '''    public void setStartOffset(final int fStartOffset)
    '''
def rewind():
    '''    public void rewind()
    '''
def readAndBuffer():
    '''    public int readAndBuffer()
    '''
def read():
    '''    public int read()
    public int read(final byte[] b, final int off, int len)
    '''
def skip():
    '''    public long skip(long n)
    '''
def available():
    '''    public int available()
    '''
def mark():
    '''    public void mark(final int n)
    '''
def markSupported():
    '''    public boolean markSupported()
    '''
def close():
    '''    public void close()
    '''
def ScannedEntity():
    '''    public ScannedEntity(final String s, final XMLResourceIdentifier entityLocation, final InputStream stream, final Reader reader, final byte[] fByteBuffer, final String encoding, final boolean literal, final boolean mayReadChunks, final boolean isExternal)
    '''
def isExternal():
    '''    public final boolean isExternal()
    public final boolean isExternal()
    public final boolean isExternal()
    '''
def isUnparsed():
    '''    public final boolean isUnparsed()
    public final boolean isUnparsed()
    public final boolean isUnparsed()
    '''
def setReader():
    '''    public void setReader(final InputStream inputStream, final String s, final Boolean b)
    '''
def getExpandedSystemId():
    '''    public String getExpandedSystemId()
    '''
def getLiteralSystemId():
    '''    public String getLiteralSystemId()
    '''
def getLineNumber():
    '''    public int getLineNumber()
    '''
def getColumnNumber():
    '''    public int getColumnNumber()
    '''
def getCharacterOffset():
    '''    public int getCharacterOffset()
    '''
def getEncoding():
    '''    public String getEncoding()
    '''
def getXMLVersion():
    '''    public String getXMLVersion()
    '''
def isEncodingExternallySpecified():
    '''    public boolean isEncodingExternallySpecified()
    '''
def setEncodingExternallySpecified():
    '''    public void setEncodingExternallySpecified(final boolean externallySpecifiedEncoding)
    '''
def toString():
    '''    public String toString()
    '''
def Entity():
    '''    public Entity()
    public Entity(final String name, final boolean inExternalSubset)
    '''
def clear():
    '''    public void clear()
    public void clear()
    public void clear()
    '''
def setValues():
    '''    public void setValues(final Entity entity)
    public void setValues(final Entity values)
    public void setValues(final ExternalEntity values)
    public void setValues(final Entity values)
    public void setValues(final InternalEntity values)
    '''
def CharacterBuffer():
    '''    public CharacterBuffer(final boolean isExternal, final int n)
    '''
def CharacterBufferPool():
    '''    public CharacterBufferPool(final int n, final int n2)
    public CharacterBufferPool(final int fPoolSize, final int fExternalBufferSize, final int fInternalBufferSize)
    '''
def getBuffer():
    '''    public CharacterBuffer getBuffer(final boolean b)
    public byte[] getBuffer()
    '''
def returnBuffer():
    '''    public void returnBuffer(final CharacterBuffer characterBuffer)
    public void returnBuffer(final byte[] array)
    '''
def setExternalBufferSize():
    '''    public void setExternalBufferSize(final int fExternalBufferSize)
    '''
def ByteBufferPool():
    '''    public ByteBufferPool(final int n)
    public ByteBufferPool(final int fPoolSize, final int fBufferSize)
    '''
def setBufferSize():
    '''    public void setBufferSize(final int fBufferSize)
    '''
def ExternalEntity():
    '''    public ExternalEntity()
    public ExternalEntity(final String s, final XMLResourceIdentifier entityLocation, final String notation, final boolean b)
    '''
def InternalEntity():
    '''    public InternalEntity()
    public InternalEntity(final String s, final String text, final boolean b)
    public InternalEntity(final String s, final String s2, final boolean b, final int paramEntityRefs)
    '''
