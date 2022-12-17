def ():
    '''returns NetCompactReadOnly\n\n
    ()\n
    '''
def first():
    '''returns Node\n\n
    first()\n
    '''
def get():
    '''returns Object\n\n
    get(final CharacterIterator characterIterator, int n)\n
    get(final String s)\n
    '''
def traverse():
    '''returns int\n\n
    traverse(final CharacterIterator characterIterator, final MatchBuffer matchBuffer)\n
    '''
def traverseReversed():
    '''returns int\n\n
    traverseReversed(final CharacterIterator characterIterator, final MatchBuffer matchBuffer)\n
    '''
def traverseLongest():
    '''returns boolean\n\n
    traverseLongest(final CharacterIterator characterIterator, final MatchBuffer matchBuffer)\n
    '''
def traverseLongestReversed():
    '''returns boolean\n\n
    traverseLongestReversed(final CharacterIterator characterIterator, final MatchBuffer matchBuffer)\n
    '''
def setChainPolicy():
    '''returns None\n\n
    setChainPolicy(final boolean b)\n
    '''
def getChainPolicy():
    '''returns boolean\n\n
    getChainPolicy()\n
    '''
def isContracted():
    '''returns boolean\n\n
    isContracted()\n
    '''
def getFileFSTFormat():
    '''returns int\n\n
    getFileFSTFormat()\n
    '''
def processGlosses():
    '''returns None\n\n
    processGlosses(final GlossProcessor glossProcessor)\n
    '''
def endReading():
    '''returns None\n\n
    endReading()\n
    '''
def iterator():
    '''returns Iterator\n\n
    iterator()\n
    '''
def iteratorAC():
    '''returns Iterator\n\n
    iteratorAC(final String s)\n
    '''
def read_FSA():
    '''returns boolean\n\n
    read_FSA(final DataInput dataInput, final int n, final int n2)\n
    '''
def readContents():
    '''returns long\n\n
    readContents(final DataInput dataInput, final int n)\n
    '''
def getSize():
    '''returns int\n\n
    getSize()\n
    '''
def getGlossCollectionCount():
    '''returns int\n\n
    getGlossCollectionCount()\n
    '''
def getSignature():
    '''returns int\n\n
    getSignature()\n
    '''
def writeNodes():
    '''returns long\n\n
    writeNodes(final DataOutput dataOutput)\n
    '''
def writeGlossCollections():
    '''returns None\n\n
    writeGlossCollections(final DataOutput dataOutput, final GlossMapper glossMapper)\n
    '''
def clearCharMappings():
    '''returns None\n\n
    clearCharMappings()\n
    '''
def getCharMapping():
    '''returns char\n\n
    getCharMapping(final char c)\n
    '''
def setCharMapping():
    '''returns None\n\n
    setCharMapping(final char c, final char c2)\n
    '''
def add():
    '''returns None\n\n
    add(final CharacterIterator characterIterator, final int n, final Object o)\n
    '''
def contract():
    '''returns None\n\n
    contract()\n
    '''
def endBuild():
    '''returns int\n\n
    endBuild()\n
    '''
def remove():
    '''returns int\n\n
    remove(final CharacterIterator characterIterator, final int n)\n
    '''
def removeGloss():
    '''returns None\n\n
    removeGloss(final CharacterIterator characterIterator, final int n, final Gloss gloss)\n
    '''
def startBuild():
    '''returns None\n\n
    startBuild(final boolean b)\n
    '''
def newNode():
    '''returns WritableNode\n\n
    newNode(final int n, final int n2)\n
    '''
def setFirstNode():
    '''returns None\n\n
    setFirstNode(final Node node)\n
    '''
def setOwnerDictionary():
    '''returns None\n\n
    setOwnerDictionary(final Dictionary ownerDictionary)\n
    '''
def transitionPossible():
    '''returns boolean\n\n
    transitionPossible(final char c)\n
    '''
def next():
    '''returns Node\n\n
    next(final char c)\n
    next(final CharacterIterator characterIterator)\n
    '''
def num_trans():
    '''returns int\n\n
    num_trans()\n
    '''
def num_chars():
    '''returns int\n\n
    num_chars()\n
    '''
def get_trans():
    '''returns Node\n\n
    get_trans(int n)\n
    '''
def get_char():
    '''returns char\n\n
    get_char(final int n)\n
    '''
def get_chars():
    '''returns String\n\n
    get_chars(final int n)\n
    '''
def isFinal():
    '''returns boolean\n\n
    isFinal()\n
    '''
def getGloss():
    '''returns Object\n\n
    getGloss()\n
    '''
def nextRestricted():
    '''returns Node\n\n
    nextRestricted(final CharacterIterator characterIterator, final int n)\n
    '''
def dispose():
    '''returns None\n\n
    dispose()\n
    '''
def hashCode():
    '''returns int\n\n
    hashCode()\n
    '''
def equals():
    '''returns boolean\n\n
    equals(final Object o)\n
    '''
