def Lucene84PostingsReader():
    '''public Lucene84PostingsReader(final SegmentReadState state)
    '''
def init():
    '''public void init(final IndexInput termsIn, final SegmentReadState state)
    '''
def newTermState():
    '''public BlockTermState newTermState()
    '''
def close():
    '''public void close()
    '''
def decodeTerm():
    '''public void decodeTerm(final DataInput in, final FieldInfo fieldInfo, final BlockTermState _termState, final boolean absolute)
    '''
def postings():
    '''public PostingsEnum postings(final FieldInfo fieldInfo, final BlockTermState termState, final PostingsEnum reuse, final int flags)
    '''
def impacts():
    '''public ImpactsEnum impacts(final FieldInfo fieldInfo, final BlockTermState state, final int flags)
    '''
def ramBytesUsed():
    '''public long ramBytesUsed()
    '''
def checkIntegrity():
    '''public void checkIntegrity()
    '''
def toString():
    '''public String toString()
    '''
def BlockDocsEnum():
    '''public BlockDocsEnum(final FieldInfo fieldInfo)
    '''
def canReuse():
    '''public boolean canReuse(final IndexInput docIn, final FieldInfo fieldInfo)
    public boolean canReuse(final IndexInput docIn, final FieldInfo fieldInfo)
    '''
def reset():
    '''public PostingsEnum reset(final Lucene84PostingsFormat.IntBlockTermState termState, final int flags)
    public EverythingEnum reset(final Lucene84PostingsFormat.IntBlockTermState termState, final int flags)
    '''
def freq():
    '''public int freq()
    public int freq()
    public int freq()
    public int freq()
    public int freq()
    '''
def nextPosition():
    '''public int nextPosition()
    public int nextPosition()
    public int nextPosition()
    public int nextPosition()
    public int nextPosition()
    '''
def startOffset():
    '''public int startOffset()
    public int startOffset()
    public int startOffset()
    public int startOffset()
    public int startOffset()
    '''
def endOffset():
    '''public int endOffset()
    public int endOffset()
    public int endOffset()
    public int endOffset()
    public int endOffset()
    '''
def getPayload():
    '''public BytesRef getPayload()
    public BytesRef getPayload()
    public BytesRef getPayload()
    public BytesRef getPayload()
    public BytesRef getPayload()
    '''
def docID():
    '''public int docID()
    public int docID()
    public int docID()
    public int docID()
    public int docID()
    '''
def nextDoc():
    '''public int nextDoc()
    public int nextDoc()
    public int nextDoc()
    public int nextDoc()
    public int nextDoc()
    '''
def advance():
    '''public int advance(final int target)
    public int advance(final int target)
    public int advance(final int target)
    public int advance(final int target)
    public int advance(final int target)
    '''
def cost():
    '''public long cost()
    public long cost()
    public long cost()
    public long cost()
    public long cost()
    '''
def EverythingEnum():
    '''public EverythingEnum(final FieldInfo fieldInfo)
    '''
def BlockImpactsDocsEnum():
    '''public BlockImpactsDocsEnum(final FieldInfo fieldInfo, final Lucene84PostingsFormat.IntBlockTermState termState)
    '''
def advanceShallow():
    '''public void advanceShallow(final int target)
    public void advanceShallow(final int target)
    public void advanceShallow(final int target)
    '''
def getImpacts():
    '''public Impacts getImpacts()
    public Impacts getImpacts()
    public Impacts getImpacts()
    '''
def BlockImpactsPostingsEnum():
    '''public BlockImpactsPostingsEnum(final FieldInfo fieldInfo, final Lucene84PostingsFormat.IntBlockTermState termState)
    '''
def BlockImpactsEverythingEnum():
    '''public BlockImpactsEverythingEnum(final FieldInfo fieldInfo, final Lucene84PostingsFormat.IntBlockTermState termState, final int flags)
    '''
