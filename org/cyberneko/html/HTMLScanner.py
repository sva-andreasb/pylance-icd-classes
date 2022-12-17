HTML_4_01_STRICT_PUBID = "String  \"-//W3C//DTD HTML 4.01//EN\""
HTML_4_01_STRICT_SYSID = "String  \"http://www.w3.org/TR/html4/strict.dtd\""
HTML_4_01_TRANSITIONAL_PUBID = "String  \"-//W3C//DTD HTML 4.01 Transitional//EN\""
HTML_4_01_TRANSITIONAL_SYSID = "String  \"http://www.w3.org/TR/html4/loose.dtd\""
HTML_4_01_FRAMESET_PUBID = "String  \"-//W3C//DTD HTML 4.01 Frameset//EN\""
HTML_4_01_FRAMESET_SYSID = "String  \"http://www.w3.org/TR/html4/frameset.dtd\""
NOTIFY_CHAR_REFS = "String  \"http://apache.org/xml/features/scanner/notify-char-refs\""
NOTIFY_XML_BUILTIN_REFS = "String  \"http://apache.org/xml/features/scanner/notify-builtin-refs\""
NOTIFY_HTML_BUILTIN_REFS = "String  \"http://cyberneko.org/html/features/scanner/notify-builtin-refs\""
FIX_MSWINDOWS_REFS = "String  \"http://cyberneko.org/html/features/scanner/fix-mswindows-refs\""
SCRIPT_STRIP_COMMENT_DELIMS = "String  \"http://cyberneko.org/html/features/scanner/script/strip-comment-delims\""
SCRIPT_STRIP_CDATA_DELIMS = "String  \"http://cyberneko.org/html/features/scanner/script/strip-cdata-delims\""
STYLE_STRIP_COMMENT_DELIMS = "String  \"http://cyberneko.org/html/features/scanner/style/strip-comment-delims\""
STYLE_STRIP_CDATA_DELIMS = "String  \"http://cyberneko.org/html/features/scanner/style/strip-cdata-delims\""
IGNORE_SPECIFIED_CHARSET = "String  \"http://cyberneko.org/html/features/scanner/ignore-specified-charset\""
CDATA_SECTIONS = "String  \"http://cyberneko.org/html/features/scanner/cdata-sections\""
OVERRIDE_DOCTYPE = "String  \"http://cyberneko.org/html/features/override-doctype\""
INSERT_DOCTYPE = "String  \"http://cyberneko.org/html/features/insert-doctype\""
PARSE_NOSCRIPT_CONTENT = "String  \"http://cyberneko.org/html/features/parse-noscript-content\""
ALLOW_SELFCLOSING_IFRAME = "String  \"http://cyberneko.org/html/features/scanner/allow-selfclosing-iframe\""
ALLOW_SELFCLOSING_TAGS = "String  \"http://cyberneko.org/html/features/scanner/allow-selfclosing-tags\""
def ():
    '''returns LocationItem\n\n
    ()\n
    (final Reader stream, final String encoding, final String publicId, final String baseSystemId, final String literalSystemId, final String expandedSystemId)\n
    ()\n
    ()\n
    (final InputStream in)\n
    ()\n
    '''
def pushInputSource():
    '''returns None\n\n
    pushInputSource(final XMLInputSource inputSource)\n
    '''
def evaluateInputSource():
    '''returns None\n\n
    evaluateInputSource(final XMLInputSource inputSource)\n
    '''
def cleanup():
    '''returns None\n\n
    cleanup(final boolean closeall)\n
    '''
def getEncoding():
    '''returns String\n\n
    getEncoding()\n
    '''
def getPublicId():
    '''returns String\n\n
    getPublicId()\n
    '''
def getBaseSystemId():
    '''returns String\n\n
    getBaseSystemId()\n
    '''
def getLiteralSystemId():
    '''returns String\n\n
    getLiteralSystemId()\n
    '''
def getExpandedSystemId():
    '''returns String\n\n
    getExpandedSystemId()\n
    '''
def getLineNumber():
    '''returns int\n\n
    getLineNumber()\n
    getLineNumber()\n
    '''
def getColumnNumber():
    '''returns int\n\n
    getColumnNumber()\n
    '''
def getXMLVersion():
    '''returns String\n\n
    getXMLVersion()\n
    '''
def getCharacterOffset():
    '''returns int\n\n
    getCharacterOffset()\n
    '''
def getFeatureDefault():
    '''returns Boolean\n\n
    getFeatureDefault(final String featureId)\n
    '''
def getPropertyDefault():
    '''returns Object\n\n
    getPropertyDefault(final String propertyId)\n
    '''
def getRecognizedFeatures():
    '''returns String[]\n\n
    getRecognizedFeatures()\n
    '''
def getRecognizedProperties():
    '''returns String[]\n\n
    getRecognizedProperties()\n
    '''
def reset():
    '''returns None\n\n
    reset(final XMLComponentManager manager)\n
    '''
def setFeature():
    '''returns None\n\n
    setFeature(final String featureId, final boolean state)\n
    '''
def setProperty():
    '''returns None\n\n
    setProperty(final String propertyId, final Object value)\n
    '''
def setInputSource():
    '''returns None\n\n
    setInputSource(final XMLInputSource source)\n
    '''
def scanDocument():
    '''returns boolean\n\n
    scanDocument(final boolean complete)\n
    '''
def setDocumentHandler():
    '''returns None\n\n
    setDocumentHandler(final XMLDocumentHandler handler)\n
    '''
def getDocumentHandler():
    '''returns XMLDocumentHandler\n\n
    getDocumentHandler()\n
    '''
def scan():
    '''returns boolean\n\n
    scan(final boolean complete)\n
    scan(final boolean complete)\n
    '''
def setElementName():
    '''returns Scanner\n\n
    setElementName(final String ename)\n
    '''
def detectEncoding():
    '''returns None\n\n
    detectEncoding(final String[] encodings)\n
    '''
def playback():
    '''returns None\n\n
    playback()\n
    '''
def clear():
    '''returns None\n\n
    clear()\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] array)\n
    read(final byte[] array, final int offset, int length)\n
    '''
def setValues():
    '''returns None\n\n
    setValues(final int beginLine, final int beginColumn, final int beginOffset, final int endLine, final int endColumn, final int endOffset)\n
    '''
def getBeginLineNumber():
    '''returns int\n\n
    getBeginLineNumber()\n
    '''
def getBeginColumnNumber():
    '''returns int\n\n
    getBeginColumnNumber()\n
    '''
def getBeginCharacterOffset():
    '''returns int\n\n
    getBeginCharacterOffset()\n
    '''
def getEndLineNumber():
    '''returns int\n\n
    getEndLineNumber()\n
    '''
def getEndColumnNumber():
    '''returns int\n\n
    getEndColumnNumber()\n
    '''
def getEndCharacterOffset():
    '''returns int\n\n
    getEndCharacterOffset()\n
    '''
def isSynthesized():
    '''returns boolean\n\n
    isSynthesized()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
