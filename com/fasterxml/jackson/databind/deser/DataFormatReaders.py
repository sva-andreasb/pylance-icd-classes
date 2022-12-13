DEFAULT_MAX_INPUT_LOOKAHEAD = "int  64"
def DataFormatReaders():
    '''    public DataFormatReaders(final ObjectReader... detectors)
    public DataFormatReaders(final Collection<ObjectReader> detectors)
    '''
def withOptimalMatch():
    '''    public DataFormatReaders withOptimalMatch(final MatchStrength optMatch)
    '''
def withMinimalMatch():
    '''    public DataFormatReaders withMinimalMatch(final MatchStrength minMatch)
    '''
def with():
    '''    public DataFormatReaders with(final ObjectReader[] readers)
    public DataFormatReaders with(final DeserializationConfig config)
    '''
def withMaxInputLookahead():
    '''    public DataFormatReaders withMaxInputLookahead(final int lookaheadBytes)
    '''
def withType():
    '''    public DataFormatReaders withType(final JavaType type)
    '''
def findFormat():
    '''    public Match findFormat(final InputStream in)
    public Match findFormat(final byte[] fullInputData)
    public Match findFormat(final byte[] fullInputData, final int offset, final int len)
    '''
def toString():
    '''    public String toString()
    '''
def AccessorForReader():
    '''    public AccessorForReader(final InputStream in, final byte[] buffer)
    public AccessorForReader(final byte[] inputDocument)
    public AccessorForReader(final byte[] inputDocument, final int start, final int len)
    '''
def createMatcher():
    '''    public Match createMatcher(final ObjectReader match, final MatchStrength matchStrength)
    '''
def hasMatch():
    '''    public boolean hasMatch()
    '''
def getMatchStrength():
    '''    public MatchStrength getMatchStrength()
    '''
def getReader():
    '''    public ObjectReader getReader()
    '''
def getMatchedFormatName():
    '''    public String getMatchedFormatName()
    '''
def createParserWithMatch():
    '''    public JsonParser createParserWithMatch()
    '''
def getDataStream():
    '''    public InputStream getDataStream()
    '''
