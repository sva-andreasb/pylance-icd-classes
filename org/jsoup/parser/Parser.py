def ():
    '''returns Parser\n\n
    (final TreeBuilder treeBuilder)\n
    '''
def parseInput():
    '''returns Document\n\n
    parseInput(final String html, final String baseUri)\n
    parseInput(final Reader inputHtml, final String baseUri)\n
    '''
def parseFragmentInput():
    '''returns List<Node>\n\n
    parseFragmentInput(final String fragment, final Element context, final String baseUri)\n
    '''
def getTreeBuilder():
    '''returns TreeBuilder\n\n
    getTreeBuilder()\n
    '''
def setTreeBuilder():
    '''returns Parser\n\n
    setTreeBuilder(final TreeBuilder treeBuilder)\n
    '''
def isTrackErrors():
    '''returns boolean\n\n
    isTrackErrors()\n
    '''
def setTrackErrors():
    '''returns Parser\n\n
    setTrackErrors(final int maxErrors)\n
    '''
def getErrors():
    '''returns ParseErrorList\n\n
    getErrors()\n
    '''
def settings():
    '''returns ParseSettings\n\n
    settings(final ParseSettings settings)\n
    settings()\n
    '''
