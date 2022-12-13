def parse():
    '''public static Document parse(final String html, final String baseUri)
    public static Document parse(final String html, final String baseUri, final Parser parser)
    public static Document parse(final String html)
    public static Document parse(final File in, final String charsetName, final String baseUri)
    public static Document parse(final File in, final String charsetName)
    public static Document parse(final InputStream in, final String charsetName, final String baseUri)
    public static Document parse(final InputStream in, final String charsetName, final String baseUri, final Parser parser)
    public static Document parse(final URL url, final int timeoutMillis)
    '''
def connect():
    '''public static Connection connect(final String url)
    '''
def parseBodyFragment():
    '''public static Document parseBodyFragment(final String bodyHtml, final String baseUri)
    public static Document parseBodyFragment(final String bodyHtml)
    '''
def clean():
    '''public static String clean(final String bodyHtml, final String baseUri, final Whitelist whitelist)
    public static String clean(final String bodyHtml, final Whitelist whitelist)
    public static String clean(final String bodyHtml, final String baseUri, final Whitelist whitelist, final Document.OutputSettings outputSettings)
    '''
def isValid():
    '''public static boolean isValid(final String bodyHtml, final Whitelist whitelist)
    '''
