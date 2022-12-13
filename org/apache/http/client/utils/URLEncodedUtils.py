CONTENT_TYPE = "String  \"application/x-www-form-urlencoded\""
def parse():
    '''public static List<NameValuePair> parse(final URI uri, final String charset)
    public static List<NameValuePair> parse(final HttpEntity entity)
    public static void parse(final List<NameValuePair> parameters, final Scanner scanner, final String charset)
    public static void parse(final List<NameValuePair> parameters, final Scanner scanner, final String parameterSepartorPattern, final String charset)
    public static List<NameValuePair> parse(final String s, final Charset charset)
    public static List<NameValuePair> parse(final String s, final Charset charset, final char... separators)
    public static List<NameValuePair> parse(final CharArrayBuffer buf, final Charset charset, final char... separators)
    '''
def isEncoded():
    '''public static boolean isEncoded(final HttpEntity entity)
    '''
def format():
    '''public static String format(final List<? extends NameValuePair> parameters, final String charset)
    public static String format(final List<? extends NameValuePair> parameters, final char parameterSeparator, final String charset)
    public static String format(final Iterable<? extends NameValuePair> parameters, final Charset charset)
    public static String format(final Iterable<? extends NameValuePair> parameters, final char parameterSeparator, final Charset charset)
    '''
