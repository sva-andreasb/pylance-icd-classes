ELEMENT = "String  \"query\""
NAMESPACE = "String  \"http://jabber.org/protocol/disco#info\""
def ():
    '''returns Feature\n\n
    ()\n
    (final DiscoverInfo d)\n
    (final Identity identity)\n
    (final String category, final String type)\n
    (final String category, final String name, final String type)\n
    (final String category, final String type, final String name, final String lang)\n
    (final Feature feature)\n
    (final CharSequence variable)\n
    (final String variable)\n
    '''
def addFeature():
    '''returns boolean\n\n
    addFeature(final String feature)\n
    addFeature(final Feature feature)\n
    '''
def addFeatures():
    '''returns None\n\n
    addFeatures(final Collection<String> featuresToAdd)\n
    '''
def getFeatures():
    '''returns List<Feature>\n\n
    getFeatures()\n
    '''
def addIdentity():
    '''returns None\n\n
    addIdentity(final Identity identity)\n
    '''
def addIdentities():
    '''returns None\n\n
    addIdentities(final Collection<Identity> identitiesToAdd)\n
    '''
def getIdentities():
    '''returns List<Identity>\n\n
    getIdentities()\n
    getIdentities(final String category, final String type)\n
    '''
def hasIdentity():
    '''returns boolean\n\n
    hasIdentity(final String category, final String type)\n
    '''
def getNode():
    '''returns String\n\n
    getNode()\n
    '''
def setNode():
    '''returns None\n\n
    setNode(final String node)\n
    '''
def containsFeature():
    '''returns boolean\n\n
    containsFeature(final CharSequence feature)\n
    '''
def containsDuplicateIdentities():
    '''returns boolean\n\n
    containsDuplicateIdentities()\n
    '''
def containsDuplicateFeatures():
    '''returns boolean\n\n
    containsDuplicateFeatures()\n
    '''
def clone():
    '''returns Feature\n\n
    clone()\n
    clone()\n
    clone()\n
    '''
def getCategory():
    '''returns String\n\n
    getCategory()\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    '''
def getType():
    '''returns String\n\n
    getType()\n
    '''
def getLanguage():
    '''returns String\n\n
    getLanguage()\n
    '''
def isOfCategoryAndType():
    '''returns boolean\n\n
    isOfCategoryAndType(final String category, final String type)\n
    '''
def toXML():
    '''returns XmlStringBuilder\n\n
    toXML()\n
    toXML()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object obj)\n
    equals(final Object obj)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    hashCode()\n
    '''
def compareTo():
    '''returns int\n\n
    compareTo(final Identity other)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    toString()\n
    '''
def getVar():
    '''returns String\n\n
    getVar()\n
    '''
