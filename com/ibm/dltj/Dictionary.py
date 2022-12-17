DLT3_DEFAULT_VERSION = "int  768"
DLT3_DEFAULT_TYPE = "int  1"
DLT3_TYPE_DEFAULT = "int  1"
DLT3_TYPE_ENCHAINED = "int  268435456"
DLT_DEFAULT_VERSION = "int  100728832"
DLT_DEFAULT_TYPE = "int  1"
DLT_TYPE_DEFAULT = "int  1"
DLT_TYPE_ENCHAINED = "int  268435456"
DLT_APPEND_DEST_LANG = "int  0"
DLT_APPEND_SRC_LANG = "int  1"
DLT_LOAD_OBJECT = "int  1"
DLT_LOAD_CHECKSUM = "int  2"
DLT_LOAD_DIRECTMEM = "int  4"
DLT_LOAD_FORCE_NETCOMPACT = "int  8"
DLT_LOAD_JAR_IN_CLASSPATH = "int  16"
def ():
    '''returns Dictionary\n\n
    ()\n
    (final File file, final String s, final int n, final int n2)\n
    (final File dictionaryFile, final int n, final int n2)\n
    (final File file, final int n)\n
    (final File dictionaryFile, final int n, final ClassLoader classLoader)\n
    (final File dictionaryFile, final boolean b, final boolean b2)\n
    (final File file, final boolean b)\n
    (final File file)\n
    '''
def iterator():
    '''returns Iterator\n\n
    iterator()\n
    '''
def getNet():
    '''returns MultiNet\n\n
    getNet()\n
    '''
def load():
    '''returns None\n\n
    load(final File file, final boolean b, final boolean b2)\n
    load(final File file, final int n)\n
    load(final File file, final int n, final ClassLoader classLoader)\n
    load(final InputStream inputStream, final boolean b, final boolean b2)\n
    load(final InputStream inputStream, final int n)\n
    load(final InputStream in, final int n, final ClassLoader classLoader)\n
    load(final DataInputStream dataInputStream)\n
    '''
def save():
    '''returns None\n\n
    save()\n
    save(final boolean b)\n
    save(final boolean b, final SaveInfo saveInfo)\n
    save(final File file, final boolean b)\n
    save(final File file)\n
    '''
def oovLookup():
    '''returns Object\n\n
    oovLookup(final CharacterIterator characterIterator, final int n)\n
    '''
def getSummary():
    '''returns DictionaryInfo\n\n
    getSummary()\n
    '''
def addUserGloss():
    '''returns Gloss\n\n
    addUserGloss(final int n, final byte[] array, final int n2)\n
    addUserGloss(final int n, final Gloss gloss)\n
    '''
def addGloss():
    '''returns Gloss\n\n
    addGloss(final int n, final Gloss gloss)\n
    '''
def addFeatureSetGloss():
    '''returns Gloss\n\n
    addFeatureSetGloss(final int n, final int n2, final boolean b, final boolean b2, final boolean b3, final boolean b4, final boolean b5)\n
    '''
def addJAMorphGloss():
    '''returns Gloss\n\n
    addJAMorphGloss(final int n, final int n2, final int n3, final int n4)\n
    addJAMorphGloss(final int n, final int n2, final boolean b, final boolean b2)\n
    '''
def append():
    '''returns None\n\n
    append(final Dictionary dictionary)\n
    append(final Dictionary dictionary, final int n)\n
    '''
def setVersion():
    '''returns None\n\n
    setVersion(final int n)\n
    '''
def getFile():
    '''returns File\n\n
    getFile()\n
    '''
def setFile():
    '''returns None\n\n
    setFile(final File dictionaryFile)\n
    '''
def toString():
    '''returns String\n\n
    toString()\n
    '''
def getFsaHeaderSize():
    '''returns int\n\n
    getFsaHeaderSize()\n
    '''
def getFsaSize():
    '''returns int\n\n
    getFsaSize()\n
    '''
def getGlossCollectionSize():
    '''returns int\n\n
    getGlossCollectionSize()\n
    '''
def getMwIndicesFstSize():
    '''returns int\n\n
    getMwIndicesFstSize()\n
    '''
def getGlossSize():
    '''returns int\n\n
    getGlossSize()\n
    '''
def getHeaderSize():
    '''returns int\n\n
    getHeaderSize()\n
    '''
def process():
    '''returns None\n\n
    process(final Node node)\n
    '''
def count():
    '''returns long\n\n
    count()\n
    '''
