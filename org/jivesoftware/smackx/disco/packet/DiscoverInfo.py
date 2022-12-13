ELEMENT = "String  query""
NAMESPACE = "String  http://jabber.org/protocol/disco#info""
def DiscoverInfo():
'''public DiscoverInfo()
public DiscoverInfo(final DiscoverInfo d)
'''
pass
def addFeature():
'''public boolean addFeature(final String feature)
public boolean addFeature(final Feature feature)
'''
pass
def addFeatures():
'''public void addFeatures(final Collection<String> featuresToAdd)
'''
pass
def getFeatures():
'''public List<Feature> getFeatures()
'''
pass
def addIdentity():
'''public void addIdentity(final Identity identity)
'''
pass
def addIdentities():
'''public void addIdentities(final Collection<Identity> identitiesToAdd)
'''
pass
def getIdentities():
'''public List<Identity> getIdentities()
public List<Identity> getIdentities(final String category, final String type)
'''
pass
def hasIdentity():
'''public boolean hasIdentity(final String category, final String type)
'''
pass
def getNode():
'''public String getNode()
'''
pass
def setNode():
'''public void setNode(final String node)
'''
pass
def containsFeature():
'''public boolean containsFeature(final CharSequence feature)
'''
pass
def containsDuplicateIdentities():
'''public boolean containsDuplicateIdentities()
'''
pass
def containsDuplicateFeatures():
'''public boolean containsDuplicateFeatures()
'''
pass
def clone():
'''public DiscoverInfo clone()
public Identity clone()
public Feature clone()
'''
pass
def Identity():
'''public Identity(final Identity identity)
public Identity(final String category, final String type)
public Identity(final String category, final String name, final String type)
public Identity(final String category, final String type, final String name, final String lang)
'''
pass
def getCategory():
'''public String getCategory()
'''
pass
def getName():
'''public String getName()
'''
pass
def getType():
'''public String getType()
'''
pass
def getLanguage():
'''public String getLanguage()
'''
pass
def isOfCategoryAndType():
'''public boolean isOfCategoryAndType(final String category, final String type)
'''
pass
def toXML():
'''public XmlStringBuilder toXML()
public XmlStringBuilder toXML()
'''
pass
def equals():
'''public boolean equals(final Object obj)
public boolean equals(final Object obj)
'''
pass
def hashCode():
'''public int hashCode()
public int hashCode()
'''
pass
def compareTo():
'''public int compareTo(final Identity other)
'''
pass
def toString():
'''public String toString()
public String toString()
'''
pass
def Feature():
'''public Feature(final Feature feature)
public Feature(final CharSequence variable)
public Feature(final String variable)
'''
pass
def getVar():
'''public String getVar()
'''
pass
