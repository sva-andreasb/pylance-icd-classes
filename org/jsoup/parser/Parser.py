def Parser():
    '''public Parser(final TreeBuilder treeBuilder)
    '''
def parseInput():
    '''public Document parseInput(final String html, final String baseUri)
    public Document parseInput(final Reader inputHtml, final String baseUri)
    '''
def parseFragmentInput():
    '''public List<Node> parseFragmentInput(final String fragment, final Element context, final String baseUri)
    '''
def getTreeBuilder():
    '''public TreeBuilder getTreeBuilder()
    '''
def setTreeBuilder():
    '''public Parser setTreeBuilder(final TreeBuilder treeBuilder)
    '''
def isTrackErrors():
    '''public boolean isTrackErrors()
    '''
def setTrackErrors():
    '''public Parser setTrackErrors(final int maxErrors)
    '''
def getErrors():
    '''public ParseErrorList getErrors()
    '''
def settings():
    '''public Parser settings(final ParseSettings settings)
    public ParseSettings settings()
    '''
def parse():
    '''public static Document parse(final String html, final String baseUri)
    '''
def parseFragment():
    '''public static List<Node> parseFragment(final String fragmentHtml, final Element context, final String baseUri)
    public static List<Node> parseFragment(final String fragmentHtml, final Element context, final String baseUri, final ParseErrorList errorList)
    '''
def parseXmlFragment():
    '''public static List<Node> parseXmlFragment(final String fragmentXml, final String baseUri)
    '''
def parseBodyFragment():
    '''public static Document parseBodyFragment(final String bodyHtml, final String baseUri)
    '''
def unescapeEntities():
    '''public static String unescapeEntities(final String string, final boolean inAttribute)
    '''
def parseBodyFragmentRelaxed():
    '''public static Document parseBodyFragmentRelaxed(final String bodyHtml, final String baseUri)
    '''
def htmlParser():
    '''public static Parser htmlParser()
    '''
def xmlParser():
    '''public static Parser xmlParser()
    '''
