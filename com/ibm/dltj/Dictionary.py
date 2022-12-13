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
def Dictionary():
    '''    public Dictionary()
    public Dictionary(final File file, final String s, final int n, final int n2)
    public Dictionary(final File dictionaryFile, final int n, final int n2)
    public Dictionary(final File file, final int n)
    public Dictionary(final File dictionaryFile, final int n, final ClassLoader classLoader)
    public Dictionary(final File dictionaryFile, final boolean b, final boolean b2)
    public Dictionary(final File file, final boolean b)
    public Dictionary(final File file)
    '''
def createDictionary():
    '''    public static Dictionary createDictionary(final DictionaryInfo dictionaryInfo)
    public static Dictionary createDictionary(final File file, final DictionaryInfo dictionaryInfo)
    public static Dictionary createDictionary(final DictionaryInfo dictionaryInfo, final int minExtendSize)
    public static Dictionary createDictionary(final File file, final DictionaryInfo dictionaryInfo, final int minExtendSize)
    '''
def getNumberOfEntries():
    '''    public synchronized long getNumberOfEntries()
    '''
def iterator():
    '''    public Iterator iterator()
    '''
def find():
    '''    public static File[] find(final String s, final int n)
    '''
def getNet():
    '''    public MultiNet getNet()
    '''
def load():
    '''    public synchronized void load(final File file)
    public synchronized void load(final File file, final boolean b)
    public void load(final File file, final boolean b, final boolean b2)
    public void load(final File file, final int n)
    public void load(final File file, final int n, final ClassLoader classLoader)
    public void load(final InputStream inputStream, final boolean b, final boolean b2)
    public void load(final InputStream inputStream, final int n)
    public void load(final InputStream in, final int n, final ClassLoader classLoader)
    public void load(final DataInputStream dataInputStream)
    public synchronized void load(final DataInputStream dataInputStream, final int n)
    public synchronized void load(DataInputStream in, final int n, final ClassLoader classLoader)
    '''
def save():
    '''    public void save()
    public void save(final boolean b)
    public void save(final boolean b, final SaveInfo saveInfo)
    public void save(final File file, final boolean b)
    public void save(final File file)
    '''
def oovLookup():
    '''    public Object oovLookup(final CharacterIterator characterIterator, final int n)
    '''
def lookupLongest():
    '''    public final boolean lookupLongest(final CharacterIterator characterIterator, final MatchBuffer matchBuffer)
    '''
def lookupLongestReversed():
    '''    public final boolean lookupLongestReversed(final CharacterIterator characterIterator, final MatchBuffer matchBuffer)
    '''
def lookupWord():
    '''    public final GlossCollection lookupWord(final CharacterIterator characterIterator, final int n)
    public final Entry lookupWord(final String text)
    public final void lookupWord(final char[] value, final int offset, final int n, final Entry entry)
    '''
def traverse():
    '''    public final int traverse(final CharacterIterator characterIterator, final MatchBuffer matchBuffer)
    '''
def traverseReversed():
    '''    public final int traverseReversed(final CharacterIterator characterIterator, final MatchBuffer matchBuffer)
    '''
def lookupWordUnsafe():
    '''    public final void lookupWordUnsafe(final String text, final Entry entry)
    '''
def get():
    '''    public final GlossCollection get(final String text)
    public final GlossCollection get(final CharacterIterator characterIterator, final int n)
    '''
def check():
    '''    public static void check(final File file, final DictionaryInfo dictionaryInfo)
    '''
def readHeader():
    '''    public static void readHeader(final File file, final DictionaryInfo dictionaryInfo)
    public static int readHeader(final DataInputStream dataInputStream, final DictionaryInfo dictionaryInfo)
    '''
def getSummary():
    '''    public DictionaryInfo getSummary()
    '''
def registerType():
    '''    public synchronized void registerType(final int n, final String s)
    public synchronized void registerType(final int n, final String s, final Class clazz)
    public synchronized void registerType(final int n, final String s, final Class clazz, final byte[] array)
    '''
def addUserGloss():
    '''    public Gloss addUserGloss(final int n, final byte[] array, final int n2)
    public Gloss addUserGloss(final int n, final Gloss gloss)
    '''
def addGloss():
    '''    public Gloss addGloss(final int n, final Gloss gloss)
    '''
def addWord():
    '''    public final void addWord(final String text, final Gloss gloss)
    public final void addWord(final CharacterIterator characterIterator, final int n, final Gloss gloss)
    public final void addWord(final String s, final Gloss[] array)
    '''
def put():
    '''    public final void put(final String s, final Gloss gloss)
    public final void put(final CharacterIterator characterIterator, final int n, final Gloss gloss)
    '''
def addMorphGloss():
    '''    public final Gloss addMorphGloss(final Gloss[] array, final int n)
    public final Gloss addMorphGloss(final Gloss[] array)
    '''
def addLemmaGloss():
    '''    public final Gloss addLemmaGloss(final String s, final int n)
    public final Gloss addLemmaGloss(final String s)
    '''
def addLanguageGloss():
    '''    public final Gloss addLanguageGloss(final String s, final int n)
    '''
def addIntegerGloss():
    '''    public final Gloss addIntegerGloss(final int n)
    public final Gloss addIntegerGloss(final int n, final int n2)
    '''
def addFeatureSetGloss():
    '''    public final Gloss addFeatureSetGloss(final int n, final int n2, final int n3, final int n4, final int n5)
    public final Gloss addFeatureSetGloss(final int n, final int n2, final int n3, final int n4)
    public final Gloss addFeatureSetGloss(final int n, final int n2, final boolean b, final boolean b2, final boolean b3, final boolean b4)
    public Gloss addFeatureSetGloss(final int n, final int n2, final boolean b, final boolean b2, final boolean b3, final boolean b4, final boolean b5)
    '''
def dispose():
    '''    public synchronized void dispose()
    '''
def getLanguages():
    '''    public final String[] getLanguages()
    '''
def addCatNameGloss():
    '''    public final Gloss addCatNameGloss(final String s, final int n)
    '''
def addCutPasteGloss():
    '''    public final Gloss addCutPasteGloss(final String s, final String s2, final int n, final int n2)
    '''
def addGrammarGloss():
    '''    public final Gloss addGrammarGloss(final int[] array, final int n)
    '''
def addJAMorphGloss():
    '''    public Gloss addJAMorphGloss(final int n, final int n2, final int n3, final int n4)
    public Gloss addJAMorphGloss(final int n, final int n2, final boolean b, final boolean b2)
    '''
def addJaGramSetGloss():
    '''    public final Gloss addJaGramSetGloss(final long[] array)
    '''
def addJkomBasedCollectionGls():
    '''    public final Gloss addJkomBasedCollectionGls(final int n, final Gloss[] array, final int n2)
    '''
def addPhoneticSpellingGloss():
    '''    public final Gloss addPhoneticSpellingGloss(final String s, final int n)
    '''
def addPosBasedCollectionGls():
    '''    public final Gloss addPosBasedCollectionGls(final int n, final Gloss[] array, final int n2)
    '''
def addSynGloss():
    '''    public final Gloss addSynGloss(final String s, final int n)
    '''
def addStemGloss():
    '''    public final Gloss addStemGloss(final String s, final int n)
    '''
def addTCRGloss():
    '''    public final Gloss addTCRGloss(final int n, final int n2, final int n3, final String s, final int n4)
    '''
def addPcodeGloss():
    '''    public final Gloss addPcodeGloss(final String s)
    '''
def addStringGloss():
    '''    public final Gloss addStringGloss(final String s, final int n)
    '''
def addTypedStringGloss():
    '''    public final Gloss addTypedStringGloss(final StringGloss stringGloss, final String s, final int n)
    '''
def addTypedIntGloss():
    '''    public final Gloss addTypedIntGloss(final StringGloss stringGloss, final int n, final int n2)
    '''
def addTypedDoubleGloss():
    '''    public final Gloss addTypedDoubleGloss(final StringGloss stringGloss, final double n, final int n2)
    '''
def addTypedVectorGloss():
    '''    public final Gloss addTypedVectorGloss(final StringGloss stringGloss, final Gloss[] array, final int n)
    '''
def contract():
    '''    public final void contract()
    '''
def append():
    '''    public void append(final Dictionary dictionary)
    public void append(final Dictionary dictionary, final int n)
    '''
def removeEntry():
    '''    public final void removeEntry(final String s, final Entry entry)
    '''
def removeWord():
    '''    public final void removeWord(final String text, final Gloss gloss)
    '''
def stampCopyright():
    '''    public final void stampCopyright(final String copyrightStatement)
    '''
def setVersion():
    '''    public void setVersion(final int n)
    '''
def getFunctionMasks():
    '''    public synchronized Object[] getFunctionMasks()
    '''
def getPoolNum():
    '''    public synchronized int getPoolNum()
    '''
def getFile():
    '''    public File getFile()
    '''
def setFile():
    '''    public void setFile(final File dictionaryFile)
    '''
def toString():
    '''    public String toString()
    '''
def getFsaHeaderSize():
    '''    public int getFsaHeaderSize()
    '''
def getFsaSize():
    '''    public int getFsaSize()
    '''
def getGlossCollectionSize():
    '''    public int getGlossCollectionSize()
    '''
def getMwIndicesFstSize():
    '''    public int getMwIndicesFstSize()
    '''
def getGlossSize():
    '''    public int getGlossSize()
    '''
def getHeaderSize():
    '''    public int getHeaderSize()
    '''
def process():
    '''    public void process(final Node node)
    '''
def count():
    '''    public long count()
    '''
