def ():
    '''returns Builder\n\n
    (final String host, final KeyValuePair[] additionalFields, final CompressionType compressionType, final int compressionThreshold, final boolean includeStacktrace)\n
    ()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getContentType():
    '''returns String\n\n
    getContentType()\n
    '''
def toByteArray():
    '''returns byte[]\n\n
    toByteArray(final LogEvent event)\n
    '''
def encode():
    '''returns None\n\n
    encode(final LogEvent event, final ByteBufferDestination destination)\n
    '''
def requiresLocation():
    '''returns boolean\n\n
    requiresLocation()\n
    '''
def toSerializable():
    '''returns String\n\n
    toSerializable(final LogEvent event)\n
    '''
def createDeflaterOutputStream():
    '''returns DeflaterOutputStream\n\n
    createDeflaterOutputStream(final OutputStream os)\n
    createDeflaterOutputStream(final OutputStream os)\n
    createDeflaterOutputStream(final OutputStream os)\n
    '''
def build():
    '''returns GelfLayout\n\n
    build()\n
    '''
def getHost():
    '''returns String\n\n
    getHost()\n
    '''
def getCompressionType():
    '''returns CompressionType\n\n
    getCompressionType()\n
    '''
def getCompressionThreshold():
    '''returns int\n\n
    getCompressionThreshold()\n
    '''
def isIncludeStacktrace():
    '''returns boolean\n\n
    isIncludeStacktrace()\n
    '''
def isIncludeThreadContext():
    '''returns boolean\n\n
    isIncludeThreadContext()\n
    '''
def isIncludeNullDelimiter():
    '''returns boolean\n\n
    isIncludeNullDelimiter()\n
    '''
def isIncludeNewLineDelimiter():
    '''returns boolean\n\n
    isIncludeNewLineDelimiter()\n
    '''
def getAdditionalFields():
    '''returns KeyValuePair[]\n\n
    getAdditionalFields()\n
    '''
def setHost():
    '''returns B\n\n
    setHost(final String host)\n
    '''
def setCompressionType():
    '''returns B\n\n
    setCompressionType(final CompressionType compressionType)\n
    '''
def setCompressionThreshold():
    '''returns B\n\n
    setCompressionThreshold(final int compressionThreshold)\n
    '''
def setIncludeStacktrace():
    '''returns B\n\n
    setIncludeStacktrace(final boolean includeStacktrace)\n
    '''
def setIncludeThreadContext():
    '''returns B\n\n
    setIncludeThreadContext(final boolean includeThreadContext)\n
    '''
def setIncludeNullDelimiter():
    '''returns B\n\n
    setIncludeNullDelimiter(final boolean includeNullDelimiter)\n
    '''
def setIncludeNewLineDelimiter():
    '''returns B\n\n
    setIncludeNewLineDelimiter(final boolean includeNewLineDelimiter)\n
    '''
def setAdditionalFields():
    '''returns B\n\n
    setAdditionalFields(final KeyValuePair[] additionalFields)\n
    '''
def setMessagePattern():
    '''returns B\n\n
    setMessagePattern(final String pattern)\n
    '''
def setPatternSelector():
    '''returns B\n\n
    setPatternSelector(final PatternSelector patternSelector)\n
    '''
def setMdcIncludes():
    '''returns B\n\n
    setMdcIncludes(final String mdcIncludes)\n
    '''
def setMdcExcludes():
    '''returns B\n\n
    setMdcExcludes(final String mdcExcludes)\n
    '''
def setIncludeMapMessage():
    '''returns B\n\n
    setIncludeMapMessage(final boolean includeMapMessage)\n
    '''
def setMapMessageIncludes():
    '''returns B\n\n
    setMapMessageIncludes(final String mapMessageIncludes)\n
    '''
def setMapMessageExcludes():
    '''returns B\n\n
    setMapMessageExcludes(final String mapMessageExcludes)\n
    '''
def setThreadContextPrefix():
    '''returns B\n\n
    setThreadContextPrefix(final String prefix)\n
    '''
def setMapPrefix():
    '''returns B\n\n
    setMapPrefix(final String prefix)\n
    '''
def accept():
    '''returns None\n\n
    accept(final String key, final Object value, final StringBuilder stringBuilder)\n
    '''
def getChecker():
    '''returns ListChecker\n\n
    getChecker()\n
    '''
