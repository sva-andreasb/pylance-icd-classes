ELEMENT = "String  \"query\""
NAMESPACE = "String  \"http://jabber.org/protocol/disco#info\""
def DiscoverInfo():
    '''    public DiscoverInfo()
    public DiscoverInfo(final DiscoverInfo d)
    '''
def addFeature():
    '''    public boolean addFeature(final String feature)
    public boolean addFeature(final Feature feature)
    '''
def addFeatures():
    '''    public void addFeatures(final Collection<String> featuresToAdd)
    '''
def getFeatures():
    '''    public List<Feature> getFeatures()
    '''
def addIdentity():
    '''    public void addIdentity(final Identity identity)
    '''
def addIdentities():
    '''    public void addIdentities(final Collection<Identity> identitiesToAdd)
    '''
def getIdentities():
    '''    public List<Identity> getIdentities()
    public List<Identity> getIdentities(final String category, final String type)
    '''
def hasIdentity():
    '''    public boolean hasIdentity(final String category, final String type)
    '''
def getNode():
    '''    public String getNode()
    '''
def setNode():
    '''    public void setNode(final String node)
    '''
def containsFeature():
    '''    public boolean containsFeature(final CharSequence feature)
    '''
def containsDuplicateIdentities():
    '''    public boolean containsDuplicateIdentities()
    '''
def containsDuplicateFeatures():
    '''    public boolean containsDuplicateFeatures()
    '''
def clone():
    '''    public DiscoverInfo clone()
    public Identity clone()
    public Feature clone()
    '''
def Identity():
    '''    public Identity(final Identity identity)
    public Identity(final String category, final String type)
    public Identity(final String category, final String name, final String type)
    public Identity(final String category, final String type, final String name, final String lang)
    '''
def getCategory():
    '''    public String getCategory()
    '''
def getName():
    '''    public String getName()
    '''
def getType():
    '''    public String getType()
    '''
def getLanguage():
    '''    public String getLanguage()
    '''
def isOfCategoryAndType():
    '''    public boolean isOfCategoryAndType(final String category, final String type)
    '''
def toXML():
    '''    public XmlStringBuilder toXML()
    public XmlStringBuilder toXML()
    '''
def equals():
    '''    public boolean equals(final Object obj)
    public boolean equals(final Object obj)
    '''
def hashCode():
    '''    public int hashCode()
    public int hashCode()
    '''
def compareTo():
    '''    public int compareTo(final Identity other)
    '''
def toString():
    '''    public String toString()
    public String toString()
    '''
def Feature():
    '''    public Feature(final Feature feature)
    public Feature(final CharSequence variable)
    public Feature(final String variable)
    '''
def getVar():
    '''    public String getVar()
    '''
