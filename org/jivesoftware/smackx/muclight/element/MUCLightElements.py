ELEMENT = "String  \"x\""
NAMESPACE = "String  \"urn:xmpp:muclight:0#configuration\""
def AffiliationsChangeExtension():
    '''    public AffiliationsChangeExtension(final HashMap<Jid, MUCLightAffiliation> affiliations, final String prevVersion, final String version)
    '''
def getElementName():
    '''    public String getElementName()
    public String getElementName()
    '''
def getNamespace():
    '''    public String getNamespace()
    public String getNamespace()
    '''
def getAffiliations():
    '''    public HashMap<Jid, MUCLightAffiliation> getAffiliations()
    '''
def getPrevVersion():
    '''    public String getPrevVersion()
    public String getPrevVersion()
    '''
def getVersion():
    '''    public String getVersion()
    public String getVersion()
    '''
def toXML():
    '''    public CharSequence toXML(final String enclosingNamespace)
    public CharSequence toXML(final String enclosingNamespace)
    public CharSequence toXML(final String enclosingNamespace)
    public CharSequence toXML(final String enclosingNamespace)
    public CharSequence toXML(final String enclosingNamespace)
    public CharSequence toXML(final String enclosingNamespace)
    '''
def from():
    '''    public static AffiliationsChangeExtension from(final Message message)
    public static ConfigurationsChangeExtension from(final Message message)
    '''
def ConfigurationsChangeExtension():
    '''    public ConfigurationsChangeExtension(final String prevVersion, final String version, final String roomName, final String subject, final HashMap<String, String> customConfigs)
    '''
def getRoomName():
    '''    public String getRoomName()
    '''
def getSubject():
    '''    public String getSubject()
    '''
def getCustomConfigs():
    '''    public HashMap<String, String> getCustomConfigs()
    '''
def ConfigurationElement():
    '''    public ConfigurationElement(final MUCLightRoomConfiguration configuration)
    '''
def OccupantsElement():
    '''    public OccupantsElement(final HashMap<Jid, MUCLightAffiliation> occupants)
    '''
def UserWithAffiliationElement():
    '''    public UserWithAffiliationElement(final Jid user, final MUCLightAffiliation affiliation)
    '''
def BlockingElement():
    '''    public BlockingElement(final Jid jid, final Boolean allow, final Boolean isRoom)
    '''
