BODY_CONTENT_JSP = "String  \"JSP\""
BODY_CONTENT_TAG_DEPENDENT = "String  \"TAGDEPENDENT\""
BODY_CONTENT_EMPTY = "String  \"EMPTY\""
BODY_CONTENT_SCRIPTLESS = "String  \"SCRIPTLESS\""
def hasDynamicAttributes():
    '''returns boolean\n\n
    hasDynamicAttributes()\n
    '''
def getBodyContent():
    '''returns String\n\n
    getBodyContent()\n
    '''
def getDisplayName():
    '''returns String\n\n
    getDisplayName()\n
    '''
def getInfoString():
    '''returns String\n\n
    getInfoString()\n
    '''
def getLargeIcon():
    '''returns String\n\n
    getLargeIcon()\n
    '''
def getSmallIcon():
    '''returns String\n\n
    getSmallIcon()\n
    '''
def getTagClassName():
    '''returns String\n\n
    getTagClassName()\n
    '''
def getTagName():
    '''returns String\n\n
    getTagName()\n
    '''
def getAttributes():
    '''returns TagAttributeInfo[]\n\n
    getAttributes()\n
    '''
def isValid():
    '''returns boolean\n\n
    isValid(final TagData data)\n
    '''
def getTagExtraInfo():
    '''returns TagExtraInfo\n\n
    getTagExtraInfo()\n
    '''
def setTagExtraInfo():
    '''returns None\n\n
    setTagExtraInfo(final TagExtraInfo tei)\n
    '''
def getTagLibrary():
    '''returns TagLibraryInfo\n\n
    getTagLibrary()\n
    '''
def setTagLibrary():
    '''returns None\n\n
    setTagLibrary(final TagLibraryInfo tl)\n
    '''
def getTagVariableInfos():
    '''returns TagVariableInfo[]\n\n
    getTagVariableInfos()\n
    '''
def validate():
    '''returns ValidationMessage[]\n\n
    validate(final TagData data)\n
    '''
def getVariableInfo():
    '''returns VariableInfo[]\n\n
    getVariableInfo(final TagData data)\n
    '''
def ():
    '''returns TagInfo\n\n
    (final String tagName, final String tagClassName, final String bodycontent, final String infoString, final TagLibraryInfo taglib, final TagExtraInfo tagExtraInfo, final TagAttributeInfo[] attributeInfo)\n
    (final String tagName, final String tagClassName, final String bodycontent, final String infoString, final TagLibraryInfo taglib, final TagExtraInfo tagExtraInfo, final TagAttributeInfo[] attributeInfo, final String displayName, final String smallIcon, final String largeIcon, final TagVariableInfo[] tvi)\n
    (final String tagName, final String tagClassName, final String bodycontent, final String infoString, final TagLibraryInfo taglib, final TagExtraInfo tagExtraInfo, final TagAttributeInfo[] attributeInfo, final String displayName, final String smallIcon, final String largeIcon, final TagVariableInfo[] tvi, final boolean dynamicAttributes)\n
    '''
