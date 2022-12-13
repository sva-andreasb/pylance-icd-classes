publicIDString = "String  -//Sun Microsystems Inc.//DTD JavaHelp HelpSet Version 1.0//EN""
publicIDString_V2 = "String  -//Sun Microsystems Inc.//DTD JavaHelp HelpSet Version 2.0//EN""
helpBrokerClass = "String  helpBroker/class""
helpBrokerLoader = "String  helpBroker/loader""
def HelpSet():
'''public HelpSet(final ClassLoader loader)
public HelpSet()
public HelpSet(final ClassLoader classLoader, final URL helpset)
'''
pass
def findHelpSet():
'''public static URL findHelpSet(final ClassLoader classLoader, final String s, final String s2, final Locale locale)
public static URL findHelpSet(final ClassLoader classLoader, final String s, final Locale locale)
public static URL findHelpSet(final ClassLoader classLoader, final String s)
'''
pass
def createHelpBroker():
'''public HelpBroker createHelpBroker()
public HelpBroker createHelpBroker(final String s)
'''
pass
def add():
'''public void add(final HelpSet set)
'''
pass
def remove():
'''public boolean remove(final HelpSet obj)
'''
pass
def getHelpSets():
'''public Enumeration getHelpSets()
'''
pass
def contains():
'''public boolean contains(final HelpSet set)
'''
pass
def addHelpSetListener():
'''public void addHelpSetListener(final HelpSetListener obj)
'''
pass
def removeHelpSetListener():
'''public void removeHelpSetListener(final HelpSetListener helpSetListener)
'''
pass
def getTitle():
'''public String getTitle()
public String getTitle()
'''
pass
def setTitle():
'''public void setTitle(final String s)
'''
pass
def getLocale():
'''public Locale getLocale()
'''
pass
def setHomeID():
'''public void setHomeID(final String s)
'''
pass
def getCombinedMap():
'''public Map getCombinedMap()
'''
pass
def getLocalMap():
'''public Map getLocalMap()
'''
pass
def setLocalMap():
'''public void setLocalMap(final Map map)
'''
pass
def getHelpSetURL():
'''public URL getHelpSetURL()
'''
pass
def getLoader():
'''public ClassLoader getLoader()
'''
pass
def getNavigatorViews():
'''public NavigatorView[] getNavigatorViews()
'''
pass
def getNavigatorView():
'''public NavigatorView getNavigatorView(final String s)
'''
pass
def getPresentations():
'''public Presentation[] getPresentations()
'''
pass
def getPresentation():
'''public Presentation getPresentation(final String s)
'''
pass
def getDefaultPresentation():
'''public Presentation getDefaultPresentation()
'''
pass
def toString():
'''public String toString()
'''
pass
def parse():
'''public static HelpSet parse(final URL helpset, final ClassLoader classLoader, final HelpSetFactory helpSetFactory)
'''
pass
def parseInto():
'''public void parseInto(final URL url, final HelpSetFactory helpSetFactory)
'''
pass
def getKeyData():
'''public Object getKeyData(final Object o, final String s)
'''
pass
def setKeyData():
'''public void setKeyData(final Object o, final String key, final Object value)
'''
pass
def DefaultHelpSetFactory():
'''public DefaultHelpSetFactory()
'''
pass
def parsingStarted():
'''public void parsingStarted(final URL source)
'''
pass
def processDOCTYPE():
'''public void processDOCTYPE(final String s, final String s2, final String s3)
'''
pass
def processPI():
'''public void processPI(final HelpSet set, final String s, final String s2)
'''
pass
def processTitle():
'''public void processTitle(final HelpSet set, final String title)
'''
pass
def processHomeID():
'''public void processHomeID(final HelpSet set, final String homeID)
'''
pass
def processMapRef():
'''public void processMapRef(final HelpSet set, final Hashtable hashtable)
'''
pass
def processView():
'''public void processView(final HelpSet set, final String s, final String s2, final String s3, final Hashtable hashtable, final String value, Hashtable hashtable2, final Locale locale)
'''
pass
def processPresentation():
'''public void processPresentation(final HelpSet set, final String s, final boolean b, final boolean b2, final boolean b3, final Dimension dimension, final Point point, final String s2, final String s3, final boolean b4, final Vector vector)
'''
pass
def processSubHelpSet():
'''public void processSubHelpSet(final HelpSet set, final Hashtable hashtable)
'''
pass
def reportMessage():
'''public void reportMessage(final String obj, final boolean b)
'''
pass
def listMessages():
'''public Enumeration listMessages()
'''
pass
def parsingEnded():
'''public HelpSet parsingEnded(final HelpSet set)
'''
pass
def Presentation():
'''public Presentation(final String name, final boolean displayViews, final boolean displayViewImages, final Dimension size, final Point location, final String title, final Map.ID imageID, final boolean toolbar, final Vector helpActions)
'''
pass
def getName():
'''public String getName()
'''
pass
def isViewDisplayed():
'''public boolean isViewDisplayed()
'''
pass
def isViewImagesDisplayed():
'''public boolean isViewImagesDisplayed()
'''
pass
def getSize():
'''public Dimension getSize()
'''
pass
def getLocation():
'''public Point getLocation()
'''
pass
def isToolbar():
'''public boolean isToolbar()
'''
pass
def getHelpActions():
'''public Enumeration getHelpActions(final HelpSet set, final Object o)
'''
pass
def tagFound():
'''public void tagFound(final ParserEvent parserEvent)
'''
pass
def piFound():
'''public void piFound(final ParserEvent parserEvent)
'''
pass
def doctypeFound():
'''public void doctypeFound(final ParserEvent parserEvent)
'''
pass
def textFound():
'''public void textFound(final ParserEvent parserEvent)
'''
pass
def errorFound():
'''public void errorFound(final ParserEvent parserEvent)
'''
pass
def commentFound():
'''public void commentFound(final ParserEvent parserEvent)
'''
pass
