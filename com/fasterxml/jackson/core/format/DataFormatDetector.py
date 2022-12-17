DEFAULT_MAX_INPUT_LOOKAHEAD = "int  64"
def ():
    '''returns DataFormatDetector\n\n
    (final JsonFactory... detectors)\n
    (final Collection<JsonFactory> detectors)\n
    '''
def withOptimalMatch():
    '''returns DataFormatDetector\n\n
    withOptimalMatch(final MatchStrength optMatch)\n
    '''
def withMinimalMatch():
    '''returns DataFormatDetector\n\n
    withMinimalMatch(final MatchStrength minMatch)\n
    '''
def withMaxInputLookahead():
    '''returns DataFormatDetector\n\n
    withMaxInputLookahead(final int lookaheadBytes)\n
    '''
def findFormat():
    '''returns DataFormatMatcher\n\n
    findFormat(final InputStream in)\n
    findFormat(final byte[] fullInputData)\n
    findFormat(final byte[] fullInputData, final int offset, final int len)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
