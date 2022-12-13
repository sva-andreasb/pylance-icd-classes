def OslcQueryTemplateInfo():
    '''public OslcQueryTemplateInfo(final String templatename, final String pagesize, final String description, final boolean ispublic, final String role, final String owner, final String searchattributes, final String tlattribute, final String objectname)
    '''
def getTemplatename():
    '''public String getTemplatename()
    '''
def getOwner():
    '''public String getOwner()
    '''
def getPagesize():
    '''public String getPagesize()
    '''
def isPublic():
    '''public boolean isPublic()
    '''
def getRole():
    '''public String getRole()
    '''
def getSearchAttributes():
    '''public String getSearchAttributes()
    '''
def getTlattribute():
    '''public String getTlattribute()
    '''
def getObjectName():
    '''public String getObjectName()
    '''
def hasPermission():
    '''public boolean hasPermission(final String personid)
    '''
def getDescription():
    '''public String getDescription()
    '''
def setDescription():
    '''public void setDescription(final String description)
    '''
def setSelectAttrList():
    '''public void setSelectAttrList(final OslcQueryTemplateAttrInfo selectAttr)
    '''
def setOrderByAttrList():
    '''public void setOrderByAttrList(final String selectAttr)
    '''
def setSearchAttrList():
    '''public void setSearchAttrList(final String selectAttr)
    '''
def setVisibleList():
    '''public void setVisibleList(final String visibleAttr)
    '''
def getSelectClause():
    '''public String getSelectClause()
    '''
def getOrderbyClause():
    '''public String getOrderbyClause()
    '''
def getSearchAttr():
    '''public String getSearchAttr()
    '''
def getVisibleList():
    '''public List<String> getVisibleList()
    '''
def getSelectAttrList():
    '''public List<OslcQueryTemplateAttrInfo> getSelectAttrList()
    '''
def getSelectAttrArray():
    '''public List<String> getSelectAttrArray()
    '''
def getOrderbyAttrList():
    '''public List<String> getOrderbyAttrList()
    '''
def getSearchAttrList():
    '''public List<String> getSearchAttrList()
    '''
def calculateClausefromInfo():
    '''public String calculateClausefromInfo(final List<OslcQueryTemplateAttrInfo> attrInfoList)
    '''
def calculateClausefromInfoAsJSON():
    '''public OrderedJSONObject calculateClausefromInfoAsJSON()
    public OrderedJSONObject calculateClausefromInfoAsJSON(final List<OslcQueryTemplateAttrInfo> attrInfoList)
    '''
def calculateClause():
    '''public String calculateClause(final List<String> attrList)
    '''
def addAttributes():
    '''public void addAttributes(final String xattr, String curxattr, final OrderedJSONObject oobj)
    '''
def getAttributesClause():
    '''public String getAttributesClause(final OrderedJSONObject oobj, final boolean initSelect, final boolean forSelect)
    '''
