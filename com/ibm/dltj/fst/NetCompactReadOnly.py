def NetCompactReadOnly():
    '''public NetCompactReadOnly()
    '''
def first():
    '''public Node first()
    '''
def get():
    '''public Object get(final CharacterIterator characterIterator, int n)
    public Object get(final String s)
    '''
def traverse():
    '''public int traverse(final CharacterIterator characterIterator, final MatchBuffer matchBuffer)
    '''
def normalizingTraverse():
    '''public final int normalizingTraverse(final CharacterIterator characterIterator, final MatchBuffer matchBuffer, final Normalizer.Mode mode)
    '''
def whitespaceIgnoringTraverse():
    '''public final int whitespaceIgnoringTraverse(final CharacterIterator characterIterator, final MatchBuffer matchBuffer)
    '''
def traverseReversed():
    '''public int traverseReversed(final CharacterIterator characterIterator, final MatchBuffer matchBuffer)
    '''
def traverseLongest():
    '''public boolean traverseLongest(final CharacterIterator characterIterator, final MatchBuffer matchBuffer)
    '''
def traverseLongestReversed():
    '''public boolean traverseLongestReversed(final CharacterIterator characterIterator, final MatchBuffer matchBuffer)
    '''
def setChainPolicy():
    '''public void setChainPolicy(final boolean b)
    '''
def getChainPolicy():
    '''public boolean getChainPolicy()
    '''
def isContracted():
    '''public boolean isContracted()
    '''
def getFileFSTFormat():
    '''public int getFileFSTFormat()
    '''
def processGlosses():
    '''public void processGlosses(final GlossProcessor glossProcessor)
    '''
def endReading():
    '''public void endReading()
    '''
def iterator():
    '''public Iterator iterator()
    '''
def iteratorAC():
    '''public Iterator iteratorAC(final String s)
    '''
def read_FSA():
    '''public boolean read_FSA(final DataInput dataInput, final int n, final int n2)
    '''
def isNetCompact():
    '''public static boolean isNetCompact(final DataInputStream dataInputStream, final int n, final DictionaryInfo dictionaryInfo)
    '''
def readContents():
    '''public long readContents(final DataInput dataInput, final int n)
    '''
def getSize():
    '''public int getSize()
    '''
def getGlossCollectionCount():
    '''public int getGlossCollectionCount()
    '''
def getSignature():
    '''public int getSignature()
    '''
def writeNodes():
    '''public long writeNodes(final DataOutput dataOutput)
    '''
def writeGlossCollections():
    '''public void writeGlossCollections(final DataOutput dataOutput, final GlossMapper glossMapper)
    '''
def clearCharMappings():
    '''public void clearCharMappings()
    '''
def getCharMapping():
    '''public char getCharMapping(final char c)
    '''
def setCharMapping():
    '''public void setCharMapping(final char c, final char c2)
    '''
def add():
    '''public void add(final CharacterIterator characterIterator, final int n, final Object o)
    '''
def contract():
    '''public void contract()
    '''
def endBuild():
    '''public int endBuild()
    '''
def remove():
    '''public int remove(final CharacterIterator characterIterator, final int n)
    '''
def removeGloss():
    '''public void removeGloss(final CharacterIterator characterIterator, final int n, final Gloss gloss)
    '''
def startBuild():
    '''public void startBuild(final boolean b)
    '''
def newNode():
    '''public WritableNode newNode(final int n, final int n2)
    '''
def setFirstNode():
    '''public void setFirstNode(final Node node)
    '''
def setOwnerDictionary():
    '''public void setOwnerDictionary(final Dictionary ownerDictionary)
    '''
def transitionPossible():
    '''public boolean transitionPossible(final char c)
    '''
def next():
    '''public Node next(final char c)
    public Node next(final CharacterIterator characterIterator)
    '''
def num_trans():
    '''public int num_trans()
    '''
def num_chars():
    '''public int num_chars()
    '''
def get_trans():
    '''public Node get_trans(int n)
    '''
def get_char():
    '''public char get_char(final int n)
    '''
def get_chars():
    '''public String get_chars(final int n)
    '''
def isFinal():
    '''public boolean isFinal()
    '''
def getGloss():
    '''public Object getGloss()
    '''
def nextRestricted():
    '''public Node nextRestricted(final CharacterIterator characterIterator, final int n)
    '''
def dispose():
    '''public void dispose()
    '''
def hashCode():
    '''public int hashCode()
    '''
def equals():
    '''public boolean equals(final Object o)
    '''
