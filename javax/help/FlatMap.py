publicIDString = "String  \"-//Sun Microsystems Inc.//DTD JavaHelp Map Version 1.0//EN\""
publicIDString_V2 = "String  \"-//Sun Microsystems Inc.//DTD JavaHelp Map Version 2.0//EN\""
def ():
    '''returns FlatMapResourceBundle\n\n
    (final URL url, final HelpSet helpset)\n
    (final Enumeration e, final HelpSet hs)\n
    (final URL url)\n
    '''
def getHelpSet():
    '''returns HelpSet\n\n
    getHelpSet()\n
    '''
def isValidID():
    '''returns boolean\n\n
    isValidID(final String s, final HelpSet set)\n
    '''
def getAllIDs():
    '''returns Enumeration\n\n
    getAllIDs()\n
    '''
def getURLFromID():
    '''returns URL\n\n
    getURLFromID(final ID obj)\n
    '''
def isID():
    '''returns boolean\n\n
    isID(final URL url)\n
    '''
def getIDFromURL():
    '''returns ID\n\n
    getIDFromURL(final URL url)\n
    '''
def getClosestID():
    '''returns ID\n\n
    getClosestID(final URL url)\n
    '''
def getIDs():
    '''returns Enumeration\n\n
    getIDs(final URL url)\n
    '''
def hasMoreElements():
    '''returns boolean\n\n
    hasMoreElements()\n
    '''
def nextElement():
    '''returns Object\n\n
    nextElement()\n
    '''
def getKeys():
    '''returns Enumeration\n\n
    getKeys()\n
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
def reportMessage():
    '''returns None\n\n
    reportMessage(final String obj, final boolean b)\n
    '''
def listMessages():
    '''returns Enumeration\n\n
    listMessages()\n
    '''
