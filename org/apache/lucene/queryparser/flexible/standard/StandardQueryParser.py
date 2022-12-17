def ():
    '''returns StandardQueryParser\n\n
    ()\n
    (final Analyzer analyzer)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def parse():
    '''returns Query\n\n
    parse(final String query, final String defaultField)\n
    '''
def setDefaultOperator():
    '''returns None\n\n
    setDefaultOperator(final StandardQueryConfigHandler.Operator operator)\n
    '''
def setAllowLeadingWildcard():
    '''returns None\n\n
    setAllowLeadingWildcard(final boolean allowLeadingWildcard)\n
    '''
def setEnablePositionIncrements():
    '''returns None\n\n
    setEnablePositionIncrements(final boolean enabled)\n
    '''
def getEnablePositionIncrements():
    '''returns boolean\n\n
    getEnablePositionIncrements()\n
    '''
def setMultiTermRewriteMethod():
    '''returns None\n\n
    setMultiTermRewriteMethod(final MultiTermQuery.RewriteMethod method)\n
    '''
def setMultiFields():
    '''returns None\n\n
    setMultiFields(CharSequence[] fields)\n
    '''
def getMultiFields():
    '''returns CharSequence[]\n\n
    getMultiFields()\n
    '''
def setFuzzyPrefixLength():
    '''returns None\n\n
    setFuzzyPrefixLength(final int fuzzyPrefixLength)\n
    '''
def setPointsConfigMap():
    '''returns None\n\n
    setPointsConfigMap(final Map<String, PointsConfig> pointsConfigMap)\n
    '''
def setLocale():
    '''returns None\n\n
    setLocale(final Locale locale)\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def setTimeZone():
    '''returns None\n\n
    setTimeZone(final TimeZone timeZone)\n
    '''
def getTimeZone():
    '''returns TimeZone\n\n
    getTimeZone()\n
    '''
def setPhraseSlop():
    '''returns None\n\n
    setPhraseSlop(final int defaultPhraseSlop)\n
    '''
def setAnalyzer():
    '''returns None\n\n
    setAnalyzer(final Analyzer analyzer)\n
    '''
def getAnalyzer():
    '''returns Analyzer\n\n
    getAnalyzer()\n
    '''
def getAllowLeadingWildcard():
    '''returns boolean\n\n
    getAllowLeadingWildcard()\n
    '''
def getFuzzyMinSim():
    '''returns float\n\n
    getFuzzyMinSim()\n
    '''
def getFuzzyPrefixLength():
    '''returns int\n\n
    getFuzzyPrefixLength()\n
    '''
def getPhraseSlop():
    '''returns int\n\n
    getPhraseSlop()\n
    '''
def setFuzzyMinSim():
    '''returns None\n\n
    setFuzzyMinSim(final float fuzzyMinSim)\n
    '''
def setFieldsBoost():
    '''returns None\n\n
    setFieldsBoost(final Map<String, Float> boosts)\n
    '''
def setDateResolution():
    '''returns None\n\n
    setDateResolution(final DateTools.Resolution dateResolution)\n
    '''
def setDateResolutionMap():
    '''returns None\n\n
    setDateResolutionMap(final Map<CharSequence, DateTools.Resolution> dateRes)\n
    '''
