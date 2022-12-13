publicIDString = "String  \"-//Sun Microsystems Inc.//DTD JavaHelp HelpSet Version 1.0//EN\""
publicIDString_V2 = "String  \"-//Sun Microsystems Inc.//DTD JavaHelp HelpSet Version 2.0//EN\""
helpBrokerClass = "String  \"helpBroker/class\""
helpBrokerLoader = "String  \"helpBroker/loader\""
def HelpSet():
    '''public HelpSet(final ClassLoader loader)
    public HelpSet()
    public HelpSet(final ClassLoader classLoader, final URL helpset)
    '''
def findHelpSet():
    '''public static URL findHelpSet(final ClassLoader classLoader, final String s, final String s2, final Locale locale)
    public static URL findHelpSet(final ClassLoader classLoader, final String s, final Locale locale)
    public static URL findHelpSet(final ClassLoader classLoader, final String s)
    '''
def createHelpBroker():
    '''public HelpBroker createHelpBroker()
    public HelpBroker createHelpBroker(final String s)
    '''
def add():
    '''public void add(final HelpSet set)
    '''
def remove():
    '''public boolean remove(final HelpSet obj)
    '''
def getHelpSets():
    '''public Enumeration getHelpSets()
    '''
def contains():
    '''public boolean contains(final HelpSet set)
    '''
def addHelpSetListener():
    '''public void addHelpSetListener(final HelpSetListener obj)
    '''
def removeHelpSetListener():
    '''public void removeHelpSetListener(final HelpSetListener helpSetListener)
    '''
def getTitle():
    '''public String getTitle()
    public String getTitle()
    '''
def setTitle():
    '''public void setTitle(final String s)
    '''
def getLocale():
    '''public Locale getLocale()
    '''
def setHomeID():
    '''public void setHomeID(final String s)
    '''
def getCombinedMap():
    '''public Map getCombinedMap()
    '''
def getLocalMap():
    '''public Map getLocalMap()
    '''
def setLocalMap():
    '''public void setLocalMap(final Map map)
    '''
def getHelpSetURL():
    '''public URL getHelpSetURL()
    '''
def getLoader():
    '''public ClassLoader getLoader()
    '''
def getNavigatorViews():
    '''public NavigatorView[] getNavigatorViews()
    '''
def getNavigatorView():
    '''public NavigatorView getNavigatorView(final String s)
    '''
def getPresentations():
    '''public Presentation[] getPresentations()
    '''
def getPresentation():
    '''public Presentation getPresentation(final String s)
    '''
def getDefaultPresentation():
    '''public Presentation getDefaultPresentation()
    '''
def toString():
    '''public String toString()
    '''
def parse():
    '''public static HelpSet parse(final URL helpset, final ClassLoader classLoader, final HelpSetFactory helpSetFactory)
    '''
def parseInto():
    '''public void parseInto(final URL url, final HelpSetFactory helpSetFactory)
    '''
def getKeyData():
    '''public Object getKeyData(final Object o, final String s)
    '''
def setKeyData():
    '''public void setKeyData(final Object o, final String key, final Object value)
    '''
def DefaultHelpSetFactory():
    '''public DefaultHelpSetFactory()
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
def processTitle():
    '''public void processTitle(final HelpSet set, final String title)
    '''
def processHomeID():
    '''public void processHomeID(final HelpSet set, final String homeID)
    '''
def processMapRef():
    '''public void processMapRef(final HelpSet set, final Hashtable hashtable)
    '''
def processView():
    '''public void processView(final HelpSet set, final String s, final String s2, final String s3, final Hashtable hashtable, final String value, Hashtable hashtable2, final Locale locale)
    '''
def processPresentation():
    '''public void processPresentation(final HelpSet set, final String s, final boolean b, final boolean b2, final boolean b3, final Dimension dimension, final Point point, final String s2, final String s3, final boolean b4, final Vector vector)
    '''
def processSubHelpSet():
    '''public void processSubHelpSet(final HelpSet set, final Hashtable hashtable)
    '''
def reportMessage():
    '''public void reportMessage(final String obj, final boolean b)
    '''
def listMessages():
    '''public Enumeration listMessages()
    '''
def parsingEnded():
    '''public HelpSet parsingEnded(final HelpSet set)
    '''
def Presentation():
    '''public Presentation(final String name, final boolean displayViews, final boolean displayViewImages, final Dimension size, final Point location, final String title, final Map.ID imageID, final boolean toolbar, final Vector helpActions)
    '''
def getName():
    '''public String getName()
    '''
def isViewDisplayed():
    '''public boolean isViewDisplayed()
    '''
def isViewImagesDisplayed():
    '''public boolean isViewImagesDisplayed()
    '''
def getSize():
    '''public Dimension getSize()
    '''
def getLocation():
    '''public Point getLocation()
    '''
def isToolbar():
    '''public boolean isToolbar()
    '''
def getHelpActions():
    '''public Enumeration getHelpActions(final HelpSet set, final Object o)
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
def errorFound():
    '''public void errorFound(final ParserEvent parserEvent)
    '''
def commentFound():
    '''public void commentFound(final ParserEvent parserEvent)
    '''
