DEFAULT_MAX_INPUT_LOOKAHEAD = "int  64"
def DataFormatDetector():
'''public DataFormatDetector(final JsonFactory... detectors)
public DataFormatDetector(final Collection<JsonFactory> detectors)
'''
pass
def withOptimalMatch():
'''public DataFormatDetector withOptimalMatch(final MatchStrength optMatch)
'''
pass
def withMinimalMatch():
'''public DataFormatDetector withMinimalMatch(final MatchStrength minMatch)
'''
pass
def withMaxInputLookahead():
'''public DataFormatDetector withMaxInputLookahead(final int lookaheadBytes)
'''
pass
def findFormat():
'''public DataFormatMatcher findFormat(final InputStream in)
public DataFormatMatcher findFormat(final byte[] fullInputData)
'''
pass
