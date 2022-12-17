EXCLUDED = "String  \"x\""
PACKAGE = "String  \"p\""
TYPE = "String  \"t\""
CONSTRUCTOR = "String  \"c\""
FIELD = "String  \"f\""
METHOD = "String  \"m\""
OVERVIEW = "String  \"o\""
ALL = "String  \"a\""
def ():
    '''returns SimpleTaglet\n\n
    (final String tagName, final String header, String lowerCase)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def inConstructor():
    '''returns boolean\n\n
    inConstructor()\n
    '''
def inField():
    '''returns boolean\n\n
    inField()\n
    '''
def inMethod():
    '''returns boolean\n\n
    inMethod()\n
    '''
def inOverview():
    '''returns boolean\n\n
    inOverview()\n
    '''
def inPackage():
    '''returns boolean\n\n
    inPackage()\n
    '''
def inType():
    '''returns boolean\n\n
    inType()\n
    '''
def isInlineTag():
    '''returns boolean\n\n
    isInlineTag()\n
    '''
def inherit():
    '''returns None\n\n
    inherit(final DocFinder.Input input, final DocFinder.Output output)\n
    '''
def getTagletOutput():
    '''returns Content\n\n
    getTagletOutput(final Tag tag, final TagletWriter tagletWriter)\n
    getTagletOutput(final Doc doc, final TagletWriter tagletWriter)\n
    '''
