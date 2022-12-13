HTML_4_01_STRICT_PUBID = "String  -//W3C//DTD HTML 4.01//EN""
HTML_4_01_STRICT_SYSID = "String  http://www.w3.org/TR/html4/strict.dtd""
HTML_4_01_TRANSITIONAL_PUBID = "String  -//W3C//DTD HTML 4.01 Transitional//EN""
HTML_4_01_TRANSITIONAL_SYSID = "String  http://www.w3.org/TR/html4/loose.dtd""
HTML_4_01_FRAMESET_PUBID = "String  -//W3C//DTD HTML 4.01 Frameset//EN""
HTML_4_01_FRAMESET_SYSID = "String  http://www.w3.org/TR/html4/frameset.dtd""
NOTIFY_CHAR_REFS = "String  http://apache.org/xml/features/scanner/notify-char-refs""
NOTIFY_XML_BUILTIN_REFS = "String  http://apache.org/xml/features/scanner/notify-builtin-refs""
NOTIFY_HTML_BUILTIN_REFS = "String  http://cyberneko.org/html/features/scanner/notify-builtin-refs""
FIX_MSWINDOWS_REFS = "String  http://cyberneko.org/html/features/scanner/fix-mswindows-refs""
SCRIPT_STRIP_COMMENT_DELIMS = "String  http://cyberneko.org/html/features/scanner/script/strip-comment-delims""
SCRIPT_STRIP_CDATA_DELIMS = "String  http://cyberneko.org/html/features/scanner/script/strip-cdata-delims""
STYLE_STRIP_COMMENT_DELIMS = "String  http://cyberneko.org/html/features/scanner/style/strip-comment-delims""
STYLE_STRIP_CDATA_DELIMS = "String  http://cyberneko.org/html/features/scanner/style/strip-cdata-delims""
IGNORE_SPECIFIED_CHARSET = "String  http://cyberneko.org/html/features/scanner/ignore-specified-charset""
CDATA_SECTIONS = "String  http://cyberneko.org/html/features/scanner/cdata-sections""
OVERRIDE_DOCTYPE = "String  http://cyberneko.org/html/features/override-doctype""
INSERT_DOCTYPE = "String  http://cyberneko.org/html/features/insert-doctype""
PARSE_NOSCRIPT_CONTENT = "String  http://cyberneko.org/html/features/parse-noscript-content""
ALLOW_SELFCLOSING_IFRAME = "String  http://cyberneko.org/html/features/scanner/allow-selfclosing-iframe""
ALLOW_SELFCLOSING_TAGS = "String  http://cyberneko.org/html/features/scanner/allow-selfclosing-tags""
def HTMLScanner():
'''public HTMLScanner()
'''
pass
def pushInputSource():
'''public void pushInputSource(final XMLInputSource inputSource)
'''
pass
def evaluateInputSource():
'''public void evaluateInputSource(final XMLInputSource inputSource)
'''
pass
def cleanup():
'''public void cleanup(final boolean closeall)
'''
pass
def getEncoding():
'''public String getEncoding()
'''
pass
def getPublicId():
'''public String getPublicId()
'''
pass
def getBaseSystemId():
'''public String getBaseSystemId()
'''
pass
def getLiteralSystemId():
'''public String getLiteralSystemId()
'''
pass
def getExpandedSystemId():
'''public String getExpandedSystemId()
'''
pass
def getLineNumber():
'''public int getLineNumber()
public int getLineNumber()
'''
pass
def getColumnNumber():
'''public int getColumnNumber()
'''
pass
def getXMLVersion():
'''public String getXMLVersion()
'''
pass
def getCharacterOffset():
'''public int getCharacterOffset()
'''
pass
def getFeatureDefault():
'''public Boolean getFeatureDefault(final String featureId)
'''
pass
def getPropertyDefault():
'''public Object getPropertyDefault(final String propertyId)
'''
pass
def getRecognizedFeatures():
'''public String[] getRecognizedFeatures()
'''
pass
def getRecognizedProperties():
'''public String[] getRecognizedProperties()
'''
pass
def reset():
'''public void reset(final XMLComponentManager manager)
'''
pass
def setFeature():
'''public void setFeature(final String featureId, final boolean state)
'''
pass
def setProperty():
'''public void setProperty(final String propertyId, final Object value)
'''
pass
def setInputSource():
'''public void setInputSource(final XMLInputSource source)
'''
pass
def scanDocument():
'''public boolean scanDocument(final boolean complete)
'''
pass
def setDocumentHandler():
'''public void setDocumentHandler(final XMLDocumentHandler handler)
'''
pass
def getDocumentHandler():
'''public XMLDocumentHandler getDocumentHandler()
'''
pass
def expandSystemId():
'''public static String expandSystemId(final String systemId, final String baseSystemId)
'''
pass
def CurrentEntity():
'''public CurrentEntity(final Reader stream, final String encoding, final String publicId, final String baseSystemId, final String literalSystemId, final String expandedSystemId)
'''
pass
def ContentScanner():
'''public ContentScanner()
'''
pass
def scan():
'''public boolean scan(final boolean complete)
public boolean scan(final boolean complete)
'''
pass
def SpecialScanner():
'''public SpecialScanner()
'''
pass
def setElementName():
'''public Scanner setElementName(final String ename)
'''
pass
def PlaybackInputStream():
'''public PlaybackInputStream(final InputStream in)
'''
pass
def detectEncoding():
'''public void detectEncoding(final String[] encodings)
'''
pass
def playback():
'''public void playback()
'''
pass
def clear():
'''public void clear()
'''
pass
def read():
'''public int read()
public int read(final byte[] array)
public int read(final byte[] array, final int offset, int length)
'''
pass
def LocationItem():
'''public LocationItem()
'''
pass
def setValues():
'''public void setValues(final int beginLine, final int beginColumn, final int beginOffset, final int endLine, final int endColumn, final int endOffset)
'''
pass
def getBeginLineNumber():
'''public int getBeginLineNumber()
'''
pass
def getBeginColumnNumber():
'''public int getBeginColumnNumber()
'''
pass
def getBeginCharacterOffset():
'''public int getBeginCharacterOffset()
'''
pass
def getEndLineNumber():
'''public int getEndLineNumber()
'''
pass
def getEndColumnNumber():
'''public int getEndColumnNumber()
'''
pass
def getEndCharacterOffset():
'''public int getEndCharacterOffset()
'''
pass
def isSynthesized():
'''public boolean isSynthesized()
'''
pass
def toString():
'''public String toString()
'''
pass
