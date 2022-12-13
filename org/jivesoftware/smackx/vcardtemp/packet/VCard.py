ELEMENT = "String  \"vCard\""
NAMESPACE = "String  \"vcard-temp\""
def VCard():
    '''    public VCard()
    '''
def getField():
    '''    public String getField(final String field)
    '''
def setField():
    '''    public void setField(final String field, final String value)
    public void setField(final String field, final String value, final boolean isUnescapable)
    '''
def getFirstName():
    '''    public String getFirstName()
    '''
def setFirstName():
    '''    public void setFirstName(final String firstName)
    '''
def getLastName():
    '''    public String getLastName()
    '''
def setLastName():
    '''    public void setLastName(final String lastName)
    '''
def getMiddleName():
    '''    public String getMiddleName()
    '''
def setMiddleName():
    '''    public void setMiddleName(final String middleName)
    '''
def getPrefix():
    '''    public String getPrefix()
    '''
def setPrefix():
    '''    public void setPrefix(final String prefix)
    '''
def getSuffix():
    '''    public String getSuffix()
    '''
def setSuffix():
    '''    public void setSuffix(final String suffix)
    '''
def getNickName():
    '''    public String getNickName()
    '''
def setNickName():
    '''    public void setNickName(final String nickName)
    '''
def getEmailHome():
    '''    public String getEmailHome()
    '''
def setEmailHome():
    '''    public void setEmailHome(final String email)
    '''
def getEmailWork():
    '''    public String getEmailWork()
    '''
def setEmailWork():
    '''    public void setEmailWork(final String emailWork)
    '''
def getJabberId():
    '''    public String getJabberId()
    '''
def setJabberId():
    '''    public void setJabberId(final CharSequence jabberId)
    '''
def getOrganization():
    '''    public String getOrganization()
    '''
def setOrganization():
    '''    public void setOrganization(final String organization)
    '''
def getOrganizationUnit():
    '''    public String getOrganizationUnit()
    '''
def setOrganizationUnit():
    '''    public void setOrganizationUnit(final String organizationUnit)
    '''
def getAddressFieldHome():
    '''    public String getAddressFieldHome(final String addrField)
    '''
def setAddressFieldHome():
    '''    public void setAddressFieldHome(final String addrField, final String value)
    '''
def getAddressFieldWork():
    '''    public String getAddressFieldWork(final String addrField)
    '''
def setAddressFieldWork():
    '''    public void setAddressFieldWork(final String addrField, final String value)
    '''
def setPhoneHome():
    '''    public void setPhoneHome(final String phoneType, final String phoneNum)
    '''
def getPhoneHome():
    '''    public String getPhoneHome(final String phoneType)
    '''
def setPhoneWork():
    '''    public void setPhoneWork(final String phoneType, final String phoneNum)
    '''
def getPhoneWork():
    '''    public String getPhoneWork(final String phoneType)
    '''
def setAvatar():
    '''    public void setAvatar(final URL avatarURL)
    public void setAvatar(final byte[] bytes)
    public void setAvatar(final byte[] bytes, final String mimeType)
    public void setAvatar(final String encodedImage, final String mimeType)
    '''
def removeAvatar():
    '''    public void removeAvatar()
    '''
def setEncodedImage():
    '''    public void setEncodedImage(final String encodedAvatar)
    '''
def getAvatar():
    '''    public byte[] getAvatar()
    '''
def getAvatarMimeType():
    '''    public String getAvatarMimeType()
    '''
def getBytes():
    '''    public static byte[] getBytes(final URL url)
    '''
def getAvatarHash():
    '''    public String getAvatarHash()
    '''
def save():
    '''    public void save(final XMPPConnection connection)
    '''
def load():
    '''    public void load(final XMPPConnection connection)
    public void load(final XMPPConnection connection, final EntityBareJid user)
    '''
def equals():
    '''    public boolean equals(final Object o)
    '''
def hashCode():
    '''    public int hashCode()
    '''
