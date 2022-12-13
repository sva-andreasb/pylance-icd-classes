def OslcQueryTemplateInfo():
'''public OslcQueryTemplateInfo(final String templatename, final String pagesize, final String description, final boolean ispublic, final String role, final String owner, final String searchattributes, final String tlattribute, final String objectname)
'''
pass
def getTemplatename():
'''public String getTemplatename()
'''
pass
def getOwner():
'''public String getOwner()
'''
pass
def getPagesize():
'''public String getPagesize()
'''
pass
def isPublic():
'''public boolean isPublic()
'''
pass
def getRole():
'''public String getRole()
'''
pass
def getSearchAttributes():
'''public String getSearchAttributes()
'''
pass
def getTlattribute():
'''public String getTlattribute()
'''
pass
def getObjectName():
'''public String getObjectName()
'''
pass
def hasPermission():
'''public boolean hasPermission(final String personid)
'''
pass
def getDescription():
'''public String getDescription()
'''
pass
def setDescription():
'''public void setDescription(final String description)
'''
pass
def setSelectAttrList():
'''public void setSelectAttrList(final OslcQueryTemplateAttrInfo selectAttr)
'''
pass
def setOrderByAttrList():
'''public void setOrderByAttrList(final String selectAttr)
'''
pass
def setSearchAttrList():
'''public void setSearchAttrList(final String selectAttr)
'''
pass
def setVisibleList():
'''public void setVisibleList(final String visibleAttr)
'''
pass
def getSelectClause():
'''public String getSelectClause()
'''
pass
def getOrderbyClause():
'''public String getOrderbyClause()
'''
pass
def getSearchAttr():
'''public String getSearchAttr()
'''
pass
def getVisibleList():
'''public List<String> getVisibleList()
'''
pass
def getSelectAttrList():
'''public List<OslcQueryTemplateAttrInfo> getSelectAttrList()
'''
pass
def getSelectAttrArray():
'''public List<String> getSelectAttrArray()
'''
pass
def getOrderbyAttrList():
'''public List<String> getOrderbyAttrList()
'''
pass
def getSearchAttrList():
'''public List<String> getSearchAttrList()
'''
pass
def calculateClausefromInfo():
'''public String calculateClausefromInfo(final List<OslcQueryTemplateAttrInfo> attrInfoList)
'''
pass
def calculateClausefromInfoAsJSON():
'''public OrderedJSONObject calculateClausefromInfoAsJSON()
public OrderedJSONObject calculateClausefromInfoAsJSON(final List<OslcQueryTemplateAttrInfo> attrInfoList)
'''
pass
def calculateClause():
'''public String calculateClause(final List<String> attrList)
'''
pass
def addAttributes():
'''public void addAttributes(final String xattr, String curxattr, final OrderedJSONObject oobj)
'''
pass
def getAttributesClause():
'''public String getAttributesClause(final OrderedJSONObject oobj, final boolean initSelect, final boolean forSelect)
'''
pass
