DEFAULT_MAX_INPUT_LOOKAHEAD = "int  64"
def DataFormatReaders():
'''public DataFormatReaders(final ObjectReader... detectors)
public DataFormatReaders(final Collection<ObjectReader> detectors)
'''
pass
def withOptimalMatch():
'''public DataFormatReaders withOptimalMatch(final MatchStrength optMatch)
'''
pass
def withMinimalMatch():
'''public DataFormatReaders withMinimalMatch(final MatchStrength minMatch)
'''
pass
def with():
'''public DataFormatReaders with(final ObjectReader[] readers)
public DataFormatReaders with(final DeserializationConfig config)
'''
pass
def withMaxInputLookahead():
'''public DataFormatReaders withMaxInputLookahead(final int lookaheadBytes)
'''
pass
def withType():
'''public DataFormatReaders withType(final JavaType type)
'''
pass
def findFormat():
'''public Match findFormat(final InputStream in)
public Match findFormat(final byte[] fullInputData)
public Match findFormat(final byte[] fullInputData, final int offset, final int len)
'''
pass
def toString():
'''public String toString()
'''
pass
def AccessorForReader():
'''public AccessorForReader(final InputStream in, final byte[] buffer)
public AccessorForReader(final byte[] inputDocument)
public AccessorForReader(final byte[] inputDocument, final int start, final int len)
'''
pass
def createMatcher():
'''public Match createMatcher(final ObjectReader match, final MatchStrength matchStrength)
'''
pass
def hasMatch():
'''public boolean hasMatch()
'''
pass
def getMatchStrength():
'''public MatchStrength getMatchStrength()
'''
pass
def getReader():
'''public ObjectReader getReader()
'''
pass
def getMatchedFormatName():
'''public String getMatchedFormatName()
'''
pass
def createParserWithMatch():
'''public JsonParser createParserWithMatch()
'''
pass
def getDataStream():
'''public InputStream getDataStream()
'''
pass
