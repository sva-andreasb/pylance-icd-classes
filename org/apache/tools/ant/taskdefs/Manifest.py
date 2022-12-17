ATTRIBUTE_MANIFEST_VERSION = "String  \"Manifest-Version\""
ATTRIBUTE_SIGNATURE_VERSION = "String  \"Signature-Version\""
ATTRIBUTE_NAME = "String  \"Name\""
ATTRIBUTE_FROM = "String  \"From\""
ATTRIBUTE_CLASSPATH = "String  \"Class-Path\""
DEFAULT_MANIFEST_VERSION = "String  \"1.0\""
MAX_LINE_LENGTH = "int  72"
MAX_SECTION_LENGTH = "int  70"
EOL = "String  \"\r\n\""
ERROR_FROM_FORBIDDEN = "String  \"Manifest attributes should not start with \\"From\\" in \\"\""
JAR_ENCODING = "String  \"UTF-8\""
def ():
    '''returns Section\n\n
    ()\n
    (final Reader r)\n
    ()\n
    (final String line)\n
    (final String name, final String value)\n
    ()\n
    '''
def addConfiguredSection():
    '''returns None\n\n
    addConfiguredSection(final Section section)\n
    '''
def addConfiguredAttribute():
    '''returns None\n\n
    addConfiguredAttribute(final Attribute attribute)\n
    addConfiguredAttribute(final Attribute attribute)\n
    '''
def merge():
    '''returns None\n\n
    merge(final Manifest other)\n
    merge(final Manifest other, final boolean overwriteMain)\n
    merge(final Manifest other, final boolean overwriteMain, final boolean mergeClassPaths)\n
    merge(final Section section)\n
    merge(final Section section, final boolean mergeClassPaths)\n
    '''
def write():
    '''returns None\n\n
    write(final PrintWriter writer)\n
    write(final PrintWriter writer, final boolean flatten)\n
    write(final PrintWriter writer)\n
    write(final PrintWriter writer, final boolean flatten)\n
    write(final PrintWriter writer)\n
    write(final PrintWriter writer, final boolean flatten)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getWarnings():
    '''returns Enumeration\n\n
    getWarnings()\n
    getWarnings()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    hashCode()\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object rhs)\n
    equals(final Object rhs)\n
    equals(final Object rhs)\n
    '''
def getManifestVersion():
    '''returns String\n\n
    getManifestVersion()\n
    '''
def getMainSection():
    '''returns Section\n\n
    getMainSection()\n
    '''
def getSection():
    '''returns Section\n\n
    getSection(final String name)\n
    '''
def getSectionNames():
    '''returns Enumeration\n\n
    getSectionNames()\n
    '''
def parse():
    '''returns None\n\n
    parse(final String line)\n
    '''
def setName():
    '''returns None\n\n
    setName(final String name)\n
    setName(final String name)\n
    '''
def getName():
    '''returns String\n\n
    getName()\n
    getName()\n
    '''
def getKey():
    '''returns String\n\n
    getKey()\n
    '''
def setValue():
    '''returns None\n\n
    setValue(final String value)\n
    '''
def getValue():
    '''returns String\n\n
    getValue()\n
    '''
def addValue():
    '''returns None\n\n
    addValue(final String value)\n
    '''
def getValues():
    '''returns Enumeration\n\n
    getValues()\n
    '''
def addContinuation():
    '''returns None\n\n
    addContinuation(final String line)\n
    '''
def read():
    '''returns String\n\n
    read(final BufferedReader reader)\n
    '''
def getAttribute():
    '''returns Attribute\n\n
    getAttribute(final String attributeName)\n
    '''
def getAttributeKeys():
    '''returns Enumeration\n\n
    getAttributeKeys()\n
    '''
def getAttributeValue():
    '''returns String\n\n
    getAttributeValue(final String attributeName)\n
    '''
def removeAttribute():
    '''returns None\n\n
    removeAttribute(final String attributeName)\n
    '''
def addAttributeAndCheck():
    '''returns String\n\n
    addAttributeAndCheck(final Attribute attribute)\n
    '''
def clone():
    '''returns Object\n\n
    clone()\n
    '''
