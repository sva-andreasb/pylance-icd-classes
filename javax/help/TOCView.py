publicIDString = "String  \"-//Sun Microsystems Inc.//DTD JavaHelp TOC Version 1.0//EN\""
publicIDString_V2 = "String  \"-//Sun Microsystems Inc.//DTD JavaHelp TOC Version 2.0//EN\""
def TOCView():
    '''public TOCView(final HelpSet set, final String s, final String s2, final Hashtable hashtable)
    public TOCView(final HelpSet set, final String s, final String s2, final Locale locale, final Hashtable hashtable)
    '''
def createNavigator():
    '''public Component createNavigator(final HelpModel helpModel)
    '''
def getMergeType():
    '''public String getMergeType()
    '''
def getDataAsTree():
    '''public DefaultMutableTreeNode getDataAsTree()
    '''
def parse():
    '''public static DefaultMutableTreeNode parse(final URL url, final HelpSet set, final Locale locale, final TreeItemFactory treeItemFactory)
    public static DefaultMutableTreeNode parse(final URL obj, final HelpSet set, final Locale locale, final TreeItemFactory treeItemFactory, final TOCView tocView)
    '''
def setCategoryOpenImageID():
    '''public void setCategoryOpenImageID(final String s)
    '''
def setCategoryClosedImageID():
    '''public void setCategoryClosedImageID(final String s)
    '''
def setTopicImageID():
    '''public void setTopicImageID(final String s)
    '''
def DefaultTOCFactory():
    '''public DefaultTOCFactory()
    '''
def parsingStarted():
    '''public void parsingStarted(final URL source)
    '''
def processDOCTYPE():
    '''public void processDOCTYPE(final String s, final String s2, final String s3)
    '''
def processPI():
    '''public void processPI(final HelpSet set, final String s, final String s2)
    '''
def createItem():
    '''public TreeItem createItem(final String s, final Hashtable hashtable, final HelpSet set, final Locale locale)
    public TreeItem createItem()
    '''
def reportMessage():
    '''public void reportMessage(final String obj, final boolean b)
    '''
def listMessages():
    '''public Enumeration listMessages()
    '''
def parsingEnded():
    '''public DefaultMutableTreeNode parsingEnded(final DefaultMutableTreeNode defaultMutableTreeNode)
    '''
def tagFound():
    '''public void tagFound(final ParserEvent parserEvent)
    '''
def piFound():
    '''public void piFound(final ParserEvent parserEvent)
    '''
def doctypeFound():
    '''public void doctypeFound(final ParserEvent parserEvent)
    '''
def textFound():
    '''public void textFound(final ParserEvent parserEvent)
    '''
def commentFound():
    '''public void commentFound(final ParserEvent parserEvent)
    '''
def errorFound():
    '''public void errorFound(final ParserEvent parserEvent)
    '''
