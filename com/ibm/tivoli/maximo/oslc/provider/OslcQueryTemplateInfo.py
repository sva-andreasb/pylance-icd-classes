def ():
    '''returns OslcQueryTemplateInfo\n\n
    (final String templatename, final String pagesize, final String description, final boolean ispublic, final String role, final String owner, final String searchattributes, final String tlattribute, final String objectname)\n
    '''
def getTemplatename():
    '''returns String\n\n
    getTemplatename()\n
    '''
def getOwner():
    '''returns String\n\n
    getOwner()\n
    '''
def getPagesize():
    '''returns String\n\n
    getPagesize()\n
    '''
def isPublic():
    '''returns boolean\n\n
    isPublic()\n
    '''
def getRole():
    '''returns String\n\n
    getRole()\n
    '''
def getSearchAttributes():
    '''returns String\n\n
    getSearchAttributes()\n
    '''
def getTlattribute():
    '''returns String\n\n
    getTlattribute()\n
    '''
def getObjectName():
    '''returns String\n\n
    getObjectName()\n
    '''
def hasPermission():
    '''returns boolean\n\n
    hasPermission(final String personid)\n
    '''
def getDescription():
    '''returns String\n\n
    getDescription()\n
    '''
def setDescription():
    '''returns None\n\n
    setDescription(final String description)\n
    '''
def setSelectAttrList():
    '''returns None\n\n
    setSelectAttrList(final OslcQueryTemplateAttrInfo selectAttr)\n
    '''
def setOrderByAttrList():
    '''returns None\n\n
    setOrderByAttrList(final String selectAttr)\n
    '''
def setSearchAttrList():
    '''returns None\n\n
    setSearchAttrList(final String selectAttr)\n
    '''
def setVisibleList():
    '''returns None\n\n
    setVisibleList(final String visibleAttr)\n
    '''
def getSelectClause():
    '''returns String\n\n
    getSelectClause()\n
    '''
def getOrderbyClause():
    '''returns String\n\n
    getOrderbyClause()\n
    '''
def getSearchAttr():
    '''returns String\n\n
    getSearchAttr()\n
    '''
def getVisibleList():
    '''returns List<String>\n\n
    getVisibleList()\n
    '''
def getSelectAttrList():
    '''returns List<OslcQueryTemplateAttrInfo>\n\n
    getSelectAttrList()\n
    '''
def getSelectAttrArray():
    '''returns List<String>\n\n
    getSelectAttrArray()\n
    '''
def getOrderbyAttrList():
    '''returns List<String>\n\n
    getOrderbyAttrList()\n
    '''
def getSearchAttrList():
    '''returns List<String>\n\n
    getSearchAttrList()\n
    '''
def calculateClausefromInfo():
    '''returns String\n\n
    calculateClausefromInfo(final List<OslcQueryTemplateAttrInfo> attrInfoList)\n
    '''
def calculateClausefromInfoAsJSON():
    '''returns OrderedJSONObject\n\n
    calculateClausefromInfoAsJSON()\n
    calculateClausefromInfoAsJSON(final List<OslcQueryTemplateAttrInfo> attrInfoList)\n
    '''
def calculateClause():
    '''returns String\n\n
    calculateClause(final List<String> attrList)\n
    '''
def addAttributes():
    '''returns None\n\n
    addAttributes(final String xattr, String curxattr, final OrderedJSONObject oobj)\n
    '''
def getAttributesClause():
    '''returns String\n\n
    getAttributesClause(final OrderedJSONObject oobj, final boolean initSelect, final boolean forSelect)\n
    '''
