DEFAULT_MAX_INPUT_LOOKAHEAD = "int  64"
def DataFormatDetector():
    '''    public DataFormatDetector(final JsonFactory... detectors)
    public DataFormatDetector(final Collection<JsonFactory> detectors)
    '''
def withOptimalMatch():
    '''    public DataFormatDetector withOptimalMatch(final MatchStrength optMatch)
    '''
def withMinimalMatch():
    '''    public DataFormatDetector withMinimalMatch(final MatchStrength minMatch)
    '''
def withMaxInputLookahead():
    '''    public DataFormatDetector withMaxInputLookahead(final int lookaheadBytes)
    '''
def findFormat():
    '''    public DataFormatMatcher findFormat(final InputStream in)
    public DataFormatMatcher findFormat(final byte[] fullInputData)
    '''
