DEFAULT_MAX_INPUT_LOOKAHEAD = "int  64"
def ():
    '''returns AccessorForReader\n\n
    (final ObjectReader... detectors)\n
    (final Collection<ObjectReader> detectors)\n
    (final InputStream in, final byte[] buffer)\n
    (final byte[] inputDocument)\n
    (final byte[] inputDocument, final int start, final int len)\n
    '''
def withOptimalMatch():
    '''returns DataFormatReaders\n\n
    withOptimalMatch(final MatchStrength optMatch)\n
    '''
def withMinimalMatch():
    '''returns DataFormatReaders\n\n
    withMinimalMatch(final MatchStrength minMatch)\n
    '''
def with():
    '''returns DataFormatReaders\n\n
    with(final ObjectReader[] readers)\n
    with(final DeserializationConfig config)\n
    '''
def withMaxInputLookahead():
    '''returns DataFormatReaders\n\n
    withMaxInputLookahead(final int lookaheadBytes)\n
    '''
def withType():
    '''returns DataFormatReaders\n\n
    withType(final JavaType type)\n
    '''
def findFormat():
    '''returns Match\n\n
    findFormat(final InputStream in)\n
    findFormat(final byte[] fullInputData)\n
    findFormat(final byte[] fullInputData, final int offset, final int len)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def createMatcher():
    '''returns Match\n\n
    createMatcher(final ObjectReader match, final MatchStrength matchStrength)\n
    '''
def hasMatch():
    '''returns boolean\n\n
    hasMatch()\n
    '''
def getMatchStrength():
    '''returns MatchStrength\n\n
    getMatchStrength()\n
    '''
def getReader():
    '''returns ObjectReader\n\n
    getReader()\n
    '''
def getMatchedFormatName():
    '''returns String\n\n
    getMatchedFormatName()\n
    '''
def createParserWithMatch():
    '''returns JsonParser\n\n
    createParserWithMatch()\n
    '''
def getDataStream():
    '''returns InputStream\n\n
    getDataStream()\n
    '''
