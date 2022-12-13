DEFAULT_BUFFER_SIZE = "int  2048"
DEFAULT_XMLDECL_BUFFER_SIZE = "int  64"
DEFAULT_INTERNAL_BUFFER_SIZE = "int  512"
def XMLEntityManager():
'''public XMLEntityManager()
public XMLEntityManager(final XMLEntityManager xmlEntityManager)
'''
pass
def setStandalone():
'''public void setStandalone(final boolean fStandalone)
'''
pass
def isStandalone():
'''public boolean isStandalone()
'''
pass
def setEntityHandler():
'''public void setEntityHandler(final XMLEntityHandler fEntityHandler)
'''
pass
def getCurrentResourceIdentifier():
'''public XMLResourceIdentifier getCurrentResourceIdentifier()
'''
pass
def getCurrentEntity():
'''public ScannedEntity getCurrentEntity()
'''
pass
def addInternalEntity():
'''public void addInternalEntity(final String s, final String s2, final int n)
public void addInternalEntity(final String s, final String s2)
'''
pass
def getParamEntityRefCount():
'''public int getParamEntityRefCount(final String key)
'''
pass
def addExternalEntity():
'''public void addExternalEntity(final String s, final String s2, final String s3, String s4)
'''
pass
def isExternalEntity():
'''public boolean isExternalEntity(final String key)
'''
pass
def isEntityDeclInExternalSubset():
'''public boolean isEntityDeclInExternalSubset(final String key)
public boolean isEntityDeclInExternalSubset()
'''
pass
def addUnparsedEntity():
'''public void addUnparsedEntity(final String s, final String s2, final String s3, final String s4, final String s5)
'''
pass
def isUnparsedEntity():
'''public boolean isUnparsedEntity(final String key)
'''
pass
def isDeclaredEntity():
'''public boolean isDeclaredEntity(final String key)
'''
pass
def resolveEntity():
'''public XMLInputSource resolveEntity(final XMLResourceIdentifier xmlResourceIdentifier)
'''
pass
def startEntity():
'''public void startEntity(final String str, final boolean b)
public void startEntity(final String s, final XMLInputSource xmlInputSource, final boolean b, final boolean b2)
'''
pass
def startDocumentEntity():
'''public void startDocumentEntity(final XMLInputSource xmlInputSource)
'''
pass
def startDTDEntity():
'''public void startDTDEntity(final XMLInputSource xmlInputSource)
'''
pass
def startExternalSubset():
'''public void startExternalSubset()
'''
pass
def endExternalSubset():
'''public void endExternalSubset()
'''
pass
def setupCurrentEntity():
'''public String setupCurrentEntity(final String s, final XMLInputSource xmlInputSource, final boolean b, final boolean b2)
'''
pass
def setScannerVersion():
'''public void setScannerVersion(final short n)
'''
pass
def getEntityScanner():
'''public XMLEntityScanner getEntityScanner()
'''
pass
def closeReaders():
'''public void closeReaders()
'''
pass
def reset():
'''public void reset(final XMLComponentManager xmlComponentManager)
public void reset()
public void reset()
'''
pass
def getRecognizedFeatures():
'''public String[] getRecognizedFeatures()
'''
pass
def setFeature():
'''public void setFeature(final String s, final boolean fAllowJavaEncodings)
'''
pass
def getRecognizedProperties():
'''public String[] getRecognizedProperties()
'''
pass
def setProperty():
'''public void setProperty(final String s, final Object o)
'''
pass
def getFeatureDefault():
'''public Boolean getFeatureDefault(final String anObject)
'''
pass
def getPropertyDefault():
'''public Object getPropertyDefault(final String anObject)
'''
pass
def absolutizeAgainstUserDir():
'''public static void absolutizeAgainstUserDir(final URI uri)
'''
pass
def expandSystemId():
'''public static String expandSystemId(final String anObject, final String s, final boolean b)
'''
pass
def createOutputStream():
'''public static OutputStream createOutputStream(final String s)
'''
pass
def run():
'''public Object run()
'''
pass
def RewindableInputStream():
'''public RewindableInputStream(final InputStream fInputStream)
'''
pass
def setStartOffset():
'''public void setStartOffset(final int fStartOffset)
'''
pass
def rewind():
'''public void rewind()
'''
pass
def readAndBuffer():
'''public int readAndBuffer()
'''
pass
def read():
'''public int read()
public int read(final byte[] b, final int off, int len)
'''
pass
def skip():
'''public long skip(long n)
'''
pass
def available():
'''public int available()
'''
pass
def mark():
'''public void mark(final int n)
'''
pass
def markSupported():
'''public boolean markSupported()
'''
pass
def close():
'''public void close()
'''
pass
def ScannedEntity():
'''public ScannedEntity(final String s, final XMLResourceIdentifier entityLocation, final InputStream stream, final Reader reader, final byte[] fByteBuffer, final String encoding, final boolean literal, final boolean mayReadChunks, final boolean isExternal)
'''
pass
def isExternal():
'''public final boolean isExternal()
public final boolean isExternal()
public final boolean isExternal()
'''
pass
def isUnparsed():
'''public final boolean isUnparsed()
public final boolean isUnparsed()
public final boolean isUnparsed()
'''
pass
def setReader():
'''public void setReader(final InputStream inputStream, final String s, final Boolean b)
'''
pass
def getExpandedSystemId():
'''public String getExpandedSystemId()
'''
pass
def getLiteralSystemId():
'''public String getLiteralSystemId()
'''
pass
def getLineNumber():
'''public int getLineNumber()
'''
pass
def getColumnNumber():
'''public int getColumnNumber()
'''
pass
def getCharacterOffset():
'''public int getCharacterOffset()
'''
pass
def getEncoding():
'''public String getEncoding()
'''
pass
def getXMLVersion():
'''public String getXMLVersion()
'''
pass
def isEncodingExternallySpecified():
'''public boolean isEncodingExternallySpecified()
'''
pass
def setEncodingExternallySpecified():
'''public void setEncodingExternallySpecified(final boolean externallySpecifiedEncoding)
'''
pass
def toString():
'''public String toString()
'''
pass
def Entity():
'''public Entity()
public Entity(final String name, final boolean inExternalSubset)
'''
pass
def clear():
'''public void clear()
public void clear()
public void clear()
'''
pass
def setValues():
'''public void setValues(final Entity entity)
public void setValues(final Entity values)
public void setValues(final ExternalEntity values)
public void setValues(final Entity values)
public void setValues(final InternalEntity values)
'''
pass
def CharacterBuffer():
'''public CharacterBuffer(final boolean isExternal, final int n)
'''
pass
def CharacterBufferPool():
'''public CharacterBufferPool(final int n, final int n2)
public CharacterBufferPool(final int fPoolSize, final int fExternalBufferSize, final int fInternalBufferSize)
'''
pass
def getBuffer():
'''public CharacterBuffer getBuffer(final boolean b)
public byte[] getBuffer()
'''
pass
def returnBuffer():
'''public void returnBuffer(final CharacterBuffer characterBuffer)
public void returnBuffer(final byte[] array)
'''
pass
def setExternalBufferSize():
'''public void setExternalBufferSize(final int fExternalBufferSize)
'''
pass
def ByteBufferPool():
'''public ByteBufferPool(final int n)
public ByteBufferPool(final int fPoolSize, final int fBufferSize)
'''
pass
def setBufferSize():
'''public void setBufferSize(final int fBufferSize)
'''
pass
def ExternalEntity():
'''public ExternalEntity()
public ExternalEntity(final String s, final XMLResourceIdentifier entityLocation, final String notation, final boolean b)
'''
pass
def InternalEntity():
'''public InternalEntity()
public InternalEntity(final String s, final String text, final boolean b)
public InternalEntity(final String s, final String s2, final boolean b, final int paramEntityRefs)
'''
pass
