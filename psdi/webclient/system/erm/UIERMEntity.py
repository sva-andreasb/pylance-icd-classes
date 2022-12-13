def UIERMEntity():
    '''public UIERMEntity()
    public UIERMEntity(final Element controlElement)
    '''
def getRelatedEntity():
    '''public ERMEntity getRelatedEntity(final String relationship)
    '''
def getCreatingControlId():
    '''public String getCreatingControlId()
    '''
def setCreatingControl():
    '''public void setCreatingControl(final Element creatingElement)
    '''
def getRelationship():
    '''public String getRelationship()
    '''
def addCondUISigOption():
    '''public void addCondUISigOption(final String sigOption, final UIERMAttribute attribute)
    '''
def getCondUISigOptions():
    '''public Map<String, Map<UIERMEntity, List<UIERMAttribute>>> getCondUISigOptions()
    '''
def addAttribute():
    '''public ERMAttribute addAttribute(final ERMAttribute attribute)
    '''
def getEntityForMbo():
    '''public ERMEntity getEntityForMbo()
    '''
def addChildEntity():
    '''public void addChildEntity(final String name, final ERMEntity entity)
    '''
def setName():
    '''public void setName(final String name)
    '''
def getZombieMboSet():
    '''public MboSetRemote getZombieMboSet(final MXSession mxSession, final String appName)
    '''
def hasSiteOrgDomains():
    '''public boolean hasSiteOrgDomains()
    '''
def getSiteOrgValuesKey():
    '''public int getSiteOrgValuesKey()
    '''
def isCloned():
    '''public boolean isCloned()
    '''
def setIsCloned():
    '''public void setIsCloned(final boolean aBool)
    '''
def clone():
    '''public UIERMEntity clone()
    '''
def cleanup():
    '''public void cleanup()
    '''
