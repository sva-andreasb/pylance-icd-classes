BLOCK_NODE_FOR_ENTER_DEFAULT = "String  \"BR\""
BLOCK_NODE_FOR_ENTER = "String  \"DIV\""
RICH_TEXT_MARKER = "String  \"<!-- RICH TEXT -->\""
def cleanValue():
    '''public static String cleanValue(final String value, final boolean escapeForJavascript, final boolean escapeCDATA)
    public static String cleanValue(String value, final boolean escapeForJavascript, final boolean escapeForHTML, final boolean escapeCDATA)
    '''
def richTextSanitize():
    '''public static String richTextSanitize(final String value)
    '''
def sanitize():
    '''public static String sanitize(String value)
    '''
def encodeTolerant():
    '''public static String encodeTolerant(final String value)
    '''
def encode():
    '''public static String encode(final String value)
    public static String encode(final String value, final String[] allowedHTMLTags)
    '''
def decode():
    '''public static String decode(final String value)
    '''
def isHtml():
    '''public static boolean isHtml(final String value)
    '''
def toPlainText():
    '''public static String toPlainText(final String html, final boolean encodeForHtml)
    public static String toPlainText(final String html)
    '''
def cleanText():
    '''public static String cleanText(final String text, final boolean escapeForJavascript)
    public static String cleanText(final String text)
    '''
def cleanHtml():
    '''public static String cleanHtml(final String html, final boolean escapeForJavascript, final boolean escapeForHTML, final boolean escapeCDATA)
    public static String cleanHtml(final String html, final boolean escapeForJavascript, final boolean escapeCDATA)
    public static String cleanHtml(final String html, final boolean escapeCDATA)
    '''
def unittestIsHtmlForceAlwaysText():
    '''public static void unittestIsHtmlForceAlwaysText(final boolean value)
    '''
def unittestIsHtmlForceAlwaysHtml():
    '''public static void unittestIsHtmlForceAlwaysHtml(final boolean value)
    '''
def replaceNewLineWithBR():
    '''public static String replaceNewLineWithBR(final String message)
    '''
def securitySafeWithHTMLEncoding():
    '''public static String securitySafeWithHTMLEncoding(final String aText)
    '''
def containsFormattingTags():
    '''public static boolean containsFormattingTags(String message)
    '''
def toString():
    '''public String toString()
    '''
def getEntity():
    '''public static Entity getEntity(final char character)
    '''
def append():
    '''public void append(final StringBuilder buffer, final boolean leaf)
    public void append(final StringBuilder buffer, final boolean leaf)
    public void append(final StringBuilder buffer, final boolean leaf)
    public void append(final StringBuilder buffer, final boolean leaf)
    '''
