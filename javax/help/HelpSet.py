publicIDString = "String  \"-//Sun Microsystems Inc.//DTD JavaHelp HelpSet Version 1.0//EN\""
publicIDString_V2 = "String  \"-//Sun Microsystems Inc.//DTD JavaHelp HelpSet Version 2.0//EN\""
helpBrokerClass = "String  \"helpBroker/class\""
helpBrokerLoader = "String  \"helpBroker/loader\""
def ():
    '''returns Presentation\n\n
    (final ClassLoader loader)\n
    ()\n
    (final ClassLoader classLoader, final URL helpset)\n
    ()\n
    (final String name, final boolean displayViews, final boolean displayViewImages, final Dimension size, final Point location, final String title, final Map.ID imageID, final boolean toolbar, final Vector helpActions)\n
    '''
def createHelpBroker():
    '''returns HelpBroker\n\n
    createHelpBroker()\n
    createHelpBroker(final String s)\n
    '''
def add():
    '''returns None\n\n
    add(final HelpSet set)\n
    '''
def remove():
    '''returns boolean\n\n
    remove(final HelpSet obj)\n
    '''
def getHelpSets():
    '''returns Enumeration\n\n
    getHelpSets()\n
    '''
def contains():
    '''returns boolean\n\n
    contains(final HelpSet set)\n
    '''
def addHelpSetListener():
    '''returns None\n\n
    addHelpSetListener(final HelpSetListener obj)\n
    '''
def removeHelpSetListener():
    '''returns None\n\n
    removeHelpSetListener(final HelpSetListener helpSetListener)\n
    '''
def getTitle():
    '''returns String\n\n
    getTitle()\n
    getTitle()\n
    '''
def setTitle():
    '''returns None\n\n
    setTitle(final String s)\n
    '''
def getLocale():
    '''returns Locale\n\n
    getLocale()\n
    '''
def setHomeID():
    '''returns None\n\n
    setHomeID(final String s)\n
    '''
def getCombinedMap():
    '''returns Map\n\n
    getCombinedMap()\n
    '''
def getLocalMap():
    '''returns Map\n\n
    getLocalMap()\n
    '''
def setLocalMap():
    '''returns None\n\n
    setLocalMap(final Map map)\n
    '''
def getHelpSetURL():
    '''returns URL\n\n
    getHelpSetURL()\n
    '''
def getLoader():
    '''returns ClassLoader\n\n
    getLoader()\n
    '''
def getNavigatorViews():
    '''returns NavigatorView[]\n\n
    getNavigatorViews()\n
    '''
def getNavigatorView():
    '''returns NavigatorView\n\n
    getNavigatorView(final String s)\n
    '''
def getPresentations():
    '''returns Presentation[]\n\n
    getPresentations()\n
    '''
def getPresentation():
    '''returns Presentation\n\n
    getPresentation(final String s)\n
    '''
def getDefaultPresentation():
    '''returns Presentation\n\n
    getDefaultPresentation()\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def parseInto():
    '''returns None\n\n
    parseInto(final URL url, final HelpSetFactory helpSetFactory)\n
    '''
def getKeyData():
    '''returns Object\n\n
    getKeyData(final Object o, final String s)\n
    '''
def setKeyData():
    '''returns None\n\n
    setKeyData(final Object o, final String key, final Object value)\n
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
def processTitle():
    '''returns None\n\n
    processTitle(final HelpSet set, final String title)\n
    '''
def processHomeID():
    '''returns None\n\n
    processHomeID(final HelpSet set, final String homeID)\n
    '''
def processMapRef():
    '''returns None\n\n
    processMapRef(final HelpSet set, final Hashtable hashtable)\n
    '''
def processView():
    '''returns None\n\n
    processView(final HelpSet set, final String s, final String s2, final String s3, final Hashtable hashtable, final String value, Hashtable hashtable2, final Locale locale)\n
    '''
def processPresentation():
    '''returns None\n\n
    processPresentation(final HelpSet set, final String s, final boolean b, final boolean b2, final boolean b3, final Dimension dimension, final Point point, final String s2, final String s3, final boolean b4, final Vector vector)\n
    '''
def processSubHelpSet():
    '''returns None\n\n
    processSubHelpSet(final HelpSet set, final Hashtable hashtable)\n
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
    '''returns HelpSet\n\n
    parsingEnded(final HelpSet set)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def isViewDisplayed():
    '''returns boolean\n\n
    isViewDisplayed()\n
    '''
def isViewImagesDisplayed():
    '''returns boolean\n\n
    isViewImagesDisplayed()\n
    '''
def getSize():
    '''returns Dimension\n\n
    getSize()\n
    '''
def getLocation():
    '''returns Point\n\n
    getLocation()\n
    '''
def isToolbar():
    '''returns boolean\n\n
    isToolbar()\n
    '''
def getHelpActions():
    '''returns Enumeration\n\n
    getHelpActions(final HelpSet set, final Object o)\n
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
def errorFound():
    '''returns None\n\n
    errorFound(final ParserEvent parserEvent)\n
    '''
def commentFound():
    '''returns None\n\n
    commentFound(final ParserEvent parserEvent)\n
    '''
