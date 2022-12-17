ERROR_TODIR_AND_SIGNEDJAR = "String  \"'destdir' and 'signedjar' cannot both be set\""
ERROR_TOO_MANY_MAPPERS = "String  \"Too many mappers\""
ERROR_SIGNEDJAR_AND_PATHS = "String  \"You cannot specify the signed JAR when using paths or filesets\""
ERROR_BAD_MAP = "String  \"Cannot map source file to anything sensible: \""
ERROR_MAPPER_WITHOUT_DEST = "String  \"The destDir attribute is required if a mapper is set\""
ERROR_NO_ALIAS = "String  \"alias attribute must be set\""
ERROR_NO_STOREPASS = "String  \"storepass attribute must be set\""
def ():
    '''returns SignJar\n\n
    ()\n
    '''
def setSigfile():
    '''returns None\n\n
    setSigfile(final String sigfile)\n
    '''
def setSignedjar():
    '''returns None\n\n
    setSignedjar(final File signedjar)\n
    '''
def setInternalsf():
    '''returns None\n\n
    setInternalsf(final boolean internalsf)\n
    '''
def setSectionsonly():
    '''returns None\n\n
    setSectionsonly(final boolean sectionsonly)\n
    '''
def setLazy():
    '''returns None\n\n
    setLazy(final boolean lazy)\n
    '''
def setDestDir():
    '''returns None\n\n
    setDestDir(final File destDir)\n
    '''
def add():
    '''returns None\n\n
    add(final FileNameMapper newMapper)\n
    '''
def getMapper():
    '''returns FileNameMapper\n\n
    getMapper()\n
    '''
def getTsaurl():
    '''returns String\n\n
    getTsaurl()\n
    '''
def setTsaurl():
    '''returns None\n\n
    setTsaurl(final String tsaurl)\n
    '''
def getTsacert():
    '''returns String\n\n
    getTsacert()\n
    '''
def setTsacert():
    '''returns None\n\n
    setTsacert(final String tsacert)\n
    '''
def setForce():
    '''returns None\n\n
    setForce(final boolean b)\n
    '''
def isForce():
    '''returns boolean\n\n
    isForce()\n
    '''
def execute():
    '''returns None\n\n
    execute()\n
    '''
def setPreserveLastModified():
    '''returns None\n\n
    setPreserveLastModified(final boolean preserveLastModified)\n
    '''
