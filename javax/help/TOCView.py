publicIDString = "String  \"-//Sun Microsystems Inc.//DTD JavaHelp TOC Version 1.0//EN\""
publicIDString_V2 = "String  \"-//Sun Microsystems Inc.//DTD JavaHelp TOC Version 2.0//EN\""
def ():
    '''returns DefaultTOCFactory\n\n
    (final HelpSet set, final String s, final String s2, final Hashtable hashtable)\n
    (final HelpSet set, final String s, final String s2, final Locale locale, final Hashtable hashtable)\n
    ()\n
    '''
def createNavigator():
    '''returns Component\n\n
    createNavigator(final HelpModel helpModel)\n
    '''
def getMergeType():
    '''returns String\n\n
    getMergeType()\n
    '''
def getDataAsTree():
    '''returns DefaultMutableTreeNode\n\n
    getDataAsTree()\n
    '''
def setCategoryOpenImageID():
    '''returns None\n\n
    setCategoryOpenImageID(final String s)\n
    '''
def setCategoryClosedImageID():
    '''returns None\n\n
    setCategoryClosedImageID(final String s)\n
    '''
def setTopicImageID():
    '''returns None\n\n
    setTopicImageID(final String s)\n
    '''
def parsingStarted():
    '''returns None\n\n
    parsingStarted(final URL source)\n
    '''
def processDOCTYPE():
    '''returns None\n\n
    processDOCTYPE(final String s, final String s2, final String s3)\n
    '''
def processPI():
    '''returns None\n\n
    processPI(final HelpSet set, final String s, final String s2)\n
    '''
def createItem():
    '''returns TreeItem\n\n
    createItem(final String s, final Hashtable hashtable, final HelpSet set, final Locale locale)\n
    createItem()\n
    '''
def reportMessage():
    '''returns None\n\n
    reportMessage(final String obj, final boolean b)\n
    '''
def listMessages():
    '''returns Enumeration\n\n
    listMessages()\n
    '''
def parsingEnded():
    '''returns DefaultMutableTreeNode\n\n
    parsingEnded(final DefaultMutableTreeNode defaultMutableTreeNode)\n
    '''
def tagFound():
    '''returns None\n\n
    tagFound(final ParserEvent parserEvent)\n
    '''
def piFound():
    '''returns None\n\n
    piFound(final ParserEvent parserEvent)\n
    '''
def doctypeFound():
    '''returns None\n\n
    doctypeFound(final ParserEvent parserEvent)\n
    '''
def textFound():
    '''returns None\n\n
    textFound(final ParserEvent parserEvent)\n
    '''
def commentFound():
    '''returns None\n\n
    commentFound(final ParserEvent parserEvent)\n
    '''
def errorFound():
    '''returns None\n\n
    errorFound(final ParserEvent parserEvent)\n
    '''
