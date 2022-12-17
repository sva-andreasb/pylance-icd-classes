ELEMENT = "String  \"vCard\""
NAMESPACE = "String  \"vcard-temp\""
def ():
    '''returns VCard\n\n
    ()\n
    '''
def getField():
    '''returns String\n\n
    getField(final String field)\n
    '''
def setField():
    '''returns None\n\n
    setField(final String field, final String value)\n
    setField(final String field, final String value, final boolean isUnescapable)\n
    '''
def getFirstName():
    '''returns String\n\n
    getFirstName()\n
    '''
def setFirstName():
    '''returns None\n\n
    setFirstName(final String firstName)\n
    '''
def getLastName():
    '''returns String\n\n
    getLastName()\n
    '''
def setLastName():
    '''returns None\n\n
    setLastName(final String lastName)\n
    '''
def getMiddleName():
    '''returns String\n\n
    getMiddleName()\n
    '''
def setMiddleName():
    '''returns None\n\n
    setMiddleName(final String middleName)\n
    '''
def getPrefix():
    '''returns String\n\n
    getPrefix()\n
    '''
def setPrefix():
    '''returns None\n\n
    setPrefix(final String prefix)\n
    '''
def getSuffix():
    '''returns String\n\n
    getSuffix()\n
    '''
def setSuffix():
    '''returns None\n\n
    setSuffix(final String suffix)\n
    '''
def getNickName():
    '''returns String\n\n
    getNickName()\n
    '''
def setNickName():
    '''returns None\n\n
    setNickName(final String nickName)\n
    '''
def getEmailHome():
    '''returns String\n\n
    getEmailHome()\n
    '''
def setEmailHome():
    '''returns None\n\n
    setEmailHome(final String email)\n
    '''
def getEmailWork():
    '''returns String\n\n
    getEmailWork()\n
    '''
def setEmailWork():
    '''returns None\n\n
    setEmailWork(final String emailWork)\n
    '''
def getJabberId():
    '''returns String\n\n
    getJabberId()\n
    '''
def setJabberId():
    '''returns None\n\n
    setJabberId(final CharSequence jabberId)\n
    '''
def getOrganization():
    '''returns String\n\n
    getOrganization()\n
    '''
def setOrganization():
    '''returns None\n\n
    setOrganization(final String organization)\n
    '''
def getOrganizationUnit():
    '''returns String\n\n
    getOrganizationUnit()\n
    '''
def setOrganizationUnit():
    '''returns None\n\n
    setOrganizationUnit(final String organizationUnit)\n
    '''
def getAddressFieldHome():
    '''returns String\n\n
    getAddressFieldHome(final String addrField)\n
    '''
def setAddressFieldHome():
    '''returns None\n\n
    setAddressFieldHome(final String addrField, final String value)\n
    '''
def getAddressFieldWork():
    '''returns String\n\n
    getAddressFieldWork(final String addrField)\n
    '''
def setAddressFieldWork():
    '''returns None\n\n
    setAddressFieldWork(final String addrField, final String value)\n
    '''
def setPhoneHome():
    '''returns None\n\n
    setPhoneHome(final String phoneType, final String phoneNum)\n
    '''
def getPhoneHome():
    '''returns String\n\n
    getPhoneHome(final String phoneType)\n
    '''
def setPhoneWork():
    '''returns None\n\n
    setPhoneWork(final String phoneType, final String phoneNum)\n
    '''
def getPhoneWork():
    '''returns String\n\n
    getPhoneWork(final String phoneType)\n
    '''
def setAvatar():
    '''returns None\n\n
    setAvatar(final URL avatarURL)\n
    setAvatar(final byte[] bytes)\n
    setAvatar(final byte[] bytes, final String mimeType)\n
    setAvatar(final String encodedImage, final String mimeType)\n
    '''
def removeAvatar():
    '''returns None\n\n
    removeAvatar()\n
    '''
def setEncodedImage():
    '''returns None\n\n
    setEncodedImage(final String encodedAvatar)\n
    '''
def getAvatar():
    '''returns byte[]\n\n
    getAvatar()\n
    '''
def getAvatarMimeType():
    '''returns String\n\n
    getAvatarMimeType()\n
    '''
def getAvatarHash():
    '''returns String\n\n
    getAvatarHash()\n
    '''
def save():
    '''returns None\n\n
    save(final XMPPConnection connection)\n
    '''
def load():
    '''returns None\n\n
    load(final XMPPConnection connection)\n
    load(final XMPPConnection connection, final EntityBareJid user)\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
