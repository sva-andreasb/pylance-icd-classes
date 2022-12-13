TDB_NS = "String  \"http://jena.hpl.hp.com/TDB#\""
SizeOfLong = "int  8"
SizeOfInt = "int  4"
SizeOfNodeId = "int  8"
SizeOfPointer = "int  4"
LenIndexTripleRecord = "int  24"
LenIndexQuadRecord = "int  32"
LenNodeHash = "int  16"
symbolNamespace = "String  \"http://jena.hpl.hp.com/TDB#\""
tdbSymbolPrefix = "String  \"tdb\""
tdbPropertyRoot = "String  \"com.hp.hpl.jena.tdb\""
BlockSize = "int  8192"
BlockSizeTest = "int  1024"
BlockSizeTestMem = "int  500"
OrderMem = "int  5"
SegmentSize = "int  8388608"
FillByte = "byte  -1"
indexTypeBTree = "String  \"BTree\""
indexTypeBPlusTree = "String  \"BPlusTree\""
indexTypeExtHash = "String  \"ExtHash\""
defaultIndexType = "String  \"BPlusTree\""
def init():
    '''public static void init()
    '''
def panic():
    '''public static void panic(final Class<?> clazz, final String string)
    '''
def allocSymbol():
    '''public static Symbol allocSymbol(final String shortName)
    '''
def fileMode():
    '''public static FileMode fileMode()
    '''
def setFileMode():
    '''public static void setFileMode(final FileMode newFileMode)
    '''
def getIndexType():
    '''public static IndexType getIndexType()
    '''
def run():
    '''public void run()
    '''
