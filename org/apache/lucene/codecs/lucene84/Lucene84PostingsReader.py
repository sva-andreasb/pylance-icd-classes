def Lucene84PostingsReader():
'''public Lucene84PostingsReader(final SegmentReadState state)
'''
pass
def init():
'''public void init(final IndexInput termsIn, final SegmentReadState state)
'''
pass
def newTermState():
'''public BlockTermState newTermState()
'''
pass
def close():
'''public void close()
'''
pass
def decodeTerm():
'''public void decodeTerm(final DataInput in, final FieldInfo fieldInfo, final BlockTermState _termState, final boolean absolute)
'''
pass
def postings():
'''public PostingsEnum postings(final FieldInfo fieldInfo, final BlockTermState termState, final PostingsEnum reuse, final int flags)
'''
pass
def impacts():
'''public ImpactsEnum impacts(final FieldInfo fieldInfo, final BlockTermState state, final int flags)
'''
pass
def ramBytesUsed():
'''public long ramBytesUsed()
'''
pass
def checkIntegrity():
'''public void checkIntegrity()
'''
pass
def toString():
'''public String toString()
'''
pass
def BlockDocsEnum():
'''public BlockDocsEnum(final FieldInfo fieldInfo)
'''
pass
def canReuse():
'''public boolean canReuse(final IndexInput docIn, final FieldInfo fieldInfo)
public boolean canReuse(final IndexInput docIn, final FieldInfo fieldInfo)
'''
pass
def reset():
'''public PostingsEnum reset(final Lucene84PostingsFormat.IntBlockTermState termState, final int flags)
public EverythingEnum reset(final Lucene84PostingsFormat.IntBlockTermState termState, final int flags)
'''
pass
def freq():
'''public int freq()
public int freq()
public int freq()
public int freq()
public int freq()
'''
pass
def nextPosition():
'''public int nextPosition()
public int nextPosition()
public int nextPosition()
public int nextPosition()
public int nextPosition()
'''
pass
def startOffset():
'''public int startOffset()
public int startOffset()
public int startOffset()
public int startOffset()
public int startOffset()
'''
pass
def endOffset():
'''public int endOffset()
public int endOffset()
public int endOffset()
public int endOffset()
public int endOffset()
'''
pass
def getPayload():
'''public BytesRef getPayload()
public BytesRef getPayload()
public BytesRef getPayload()
public BytesRef getPayload()
public BytesRef getPayload()
'''
pass
def docID():
'''public int docID()
public int docID()
public int docID()
public int docID()
public int docID()
'''
pass
def nextDoc():
'''public int nextDoc()
public int nextDoc()
public int nextDoc()
public int nextDoc()
public int nextDoc()
'''
pass
def advance():
'''public int advance(final int target)
public int advance(final int target)
public int advance(final int target)
public int advance(final int target)
public int advance(final int target)
'''
pass
def cost():
'''public long cost()
public long cost()
public long cost()
public long cost()
public long cost()
'''
pass
def EverythingEnum():
'''public EverythingEnum(final FieldInfo fieldInfo)
'''
pass
def BlockImpactsDocsEnum():
'''public BlockImpactsDocsEnum(final FieldInfo fieldInfo, final Lucene84PostingsFormat.IntBlockTermState termState)
'''
pass
def advanceShallow():
'''public void advanceShallow(final int target)
public void advanceShallow(final int target)
public void advanceShallow(final int target)
'''
pass
def getImpacts():
'''public Impacts getImpacts()
public Impacts getImpacts()
public Impacts getImpacts()
'''
pass
def BlockImpactsPostingsEnum():
'''public BlockImpactsPostingsEnum(final FieldInfo fieldInfo, final Lucene84PostingsFormat.IntBlockTermState termState)
'''
pass
def BlockImpactsEverythingEnum():
'''public BlockImpactsEverythingEnum(final FieldInfo fieldInfo, final Lucene84PostingsFormat.IntBlockTermState termState, final int flags)
'''
pass
