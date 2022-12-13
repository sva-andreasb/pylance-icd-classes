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
def HTMLScanner():
    '''    public HTMLScanner()
    '''
def pushInputSource():
    '''    public void pushInputSource(final XMLInputSource inputSource)
    '''
def evaluateInputSource():
    '''    public void evaluateInputSource(final XMLInputSource inputSource)
    '''
def cleanup():
    '''    public void cleanup(final boolean closeall)
    '''
def getEncoding():
    '''    public String getEncoding()
    '''
def getPublicId():
    '''    public String getPublicId()
    '''
def getBaseSystemId():
    '''    public String getBaseSystemId()
    '''
def getLiteralSystemId():
    '''    public String getLiteralSystemId()
    '''
def getExpandedSystemId():
    '''    public String getExpandedSystemId()
    '''
def getLineNumber():
    '''    public int getLineNumber()
    public int getLineNumber()
    '''
def getColumnNumber():
    '''    public int getColumnNumber()
    '''
def getXMLVersion():
    '''    public String getXMLVersion()
    '''
def getCharacterOffset():
    '''    public int getCharacterOffset()
    '''
def getFeatureDefault():
    '''    public Boolean getFeatureDefault(final String featureId)
    '''
def getPropertyDefault():
    '''    public Object getPropertyDefault(final String propertyId)
    '''
def getRecognizedFeatures():
    '''    public String[] getRecognizedFeatures()
    '''
def getRecognizedProperties():
    '''    public String[] getRecognizedProperties()
    '''
def reset():
    '''    public void reset(final XMLComponentManager manager)
    '''
def setFeature():
    '''    public void setFeature(final String featureId, final boolean state)
    '''
def setProperty():
    '''    public void setProperty(final String propertyId, final Object value)
    '''
def setInputSource():
    '''    public void setInputSource(final XMLInputSource source)
    '''
def scanDocument():
    '''    public boolean scanDocument(final boolean complete)
    '''
def setDocumentHandler():
    '''    public void setDocumentHandler(final XMLDocumentHandler handler)
    '''
def getDocumentHandler():
    '''    public XMLDocumentHandler getDocumentHandler()
    '''
def expandSystemId():
    '''    public static String expandSystemId(final String systemId, final String baseSystemId)
    '''
def CurrentEntity():
    '''    public CurrentEntity(final Reader stream, final String encoding, final String publicId, final String baseSystemId, final String literalSystemId, final String expandedSystemId)
    '''
def ContentScanner():
    '''    public ContentScanner()
    '''
def scan():
    '''    public boolean scan(final boolean complete)
    public boolean scan(final boolean complete)
    '''
def SpecialScanner():
    '''    public SpecialScanner()
    '''
def setElementName():
    '''    public Scanner setElementName(final String ename)
    '''
def PlaybackInputStream():
    '''    public PlaybackInputStream(final InputStream in)
    '''
def detectEncoding():
    '''    public void detectEncoding(final String[] encodings)
    '''
def playback():
    '''    public void playback()
    '''
def clear():
    '''    public void clear()
    '''
def read():
    '''    public int read()
    public int read(final byte[] array)
    public int read(final byte[] array, final int offset, int length)
    '''
def LocationItem():
    '''    public LocationItem()
    '''
def setValues():
    '''    public void setValues(final int beginLine, final int beginColumn, final int beginOffset, final int endLine, final int endColumn, final int endOffset)
    '''
def getBeginLineNumber():
    '''    public int getBeginLineNumber()
    '''
def getBeginColumnNumber():
    '''    public int getBeginColumnNumber()
    '''
def getBeginCharacterOffset():
    '''    public int getBeginCharacterOffset()
    '''
def getEndLineNumber():
    '''    public int getEndLineNumber()
    '''
def getEndColumnNumber():
    '''    public int getEndColumnNumber()
    '''
def getEndCharacterOffset():
    '''    public int getEndCharacterOffset()
    '''
def isSynthesized():
    '''    public boolean isSynthesized()
    '''
def toString():
    '''    public String toString()
    '''
