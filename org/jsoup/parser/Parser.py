def Parser():
'''public Parser(final TreeBuilder treeBuilder)
'''
pass
def parseInput():
'''public Document parseInput(final String html, final String baseUri)
public Document parseInput(final Reader inputHtml, final String baseUri)
'''
pass
def parseFragmentInput():
'''public List<Node> parseFragmentInput(final String fragment, final Element context, final String baseUri)
'''
pass
def getTreeBuilder():
'''public TreeBuilder getTreeBuilder()
'''
pass
def setTreeBuilder():
'''public Parser setTreeBuilder(final TreeBuilder treeBuilder)
'''
pass
def isTrackErrors():
'''public boolean isTrackErrors()
'''
pass
def setTrackErrors():
'''public Parser setTrackErrors(final int maxErrors)
'''
pass
def getErrors():
'''public ParseErrorList getErrors()
'''
pass
def settings():
'''public Parser settings(final ParseSettings settings)
public ParseSettings settings()
'''
pass
def parse():
'''public static Document parse(final String html, final String baseUri)
'''
pass
def parseFragment():
'''public static List<Node> parseFragment(final String fragmentHtml, final Element context, final String baseUri)
public static List<Node> parseFragment(final String fragmentHtml, final Element context, final String baseUri, final ParseErrorList errorList)
'''
pass
def parseXmlFragment():
'''public static List<Node> parseXmlFragment(final String fragmentXml, final String baseUri)
'''
pass
def parseBodyFragment():
'''public static Document parseBodyFragment(final String bodyHtml, final String baseUri)
'''
pass
def unescapeEntities():
'''public static String unescapeEntities(final String string, final boolean inAttribute)
'''
pass
def parseBodyFragmentRelaxed():
'''public static Document parseBodyFragmentRelaxed(final String bodyHtml, final String baseUri)
'''
pass
def htmlParser():
'''public static Parser htmlParser()
'''
pass
def xmlParser():
'''public static Parser xmlParser()
'''
pass
