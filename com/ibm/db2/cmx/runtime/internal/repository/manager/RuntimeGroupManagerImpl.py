def ():
    '''returns RuntimeGroupManagerImpl\n\n
    (final Connection c, final String schema)\n
    '''
def list():
    '''returns List<RuntimeGroup>\n\n
    list()\n
    list(final String anObject)\n
    '''
def copy():
    '''returns None\n\n
    copy(final String s, final String s2, final String s3, final String s4)\n
    '''
def create():
    '''returns None\n\n
    create(final String s, final String s2, final String s3)\n
    '''
def deactivateAllVersions():
    '''returns None\n\n
    deactivateAllVersions(final String s)\n
    '''
def delete():
    '''returns None\n\n
    delete(final String s, final String s2)\n
    '''
def setActiveVersion():
    '''returns None\n\n
    setActiveVersion(final String s, final String s2)\n
    '''
def setContact():
    '''returns None\n\n
    setContact(final String s, final String s2, final String s3)\n
    '''
def setData():
    '''returns None\n\n
    setData(final String s, final String s2, final InputStream inputStream, final MemberType memberType, final String s3)\n
    '''
def deleteAllVersions():
    '''returns int\n\n
    deleteAllVersions(final String anObject)\n
    '''
def export():
    '''returns None\n\n
    export(final String s, final String s2, final OutputStream outputStream)\n
    '''
def importData():
    '''returns ImportInfo\n\n
    importData(final String s, final String s2, final InputStream in)\n
    '''
