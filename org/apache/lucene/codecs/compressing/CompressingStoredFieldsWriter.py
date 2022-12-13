FIELDS_EXTENSION = "String  \"fdt\""
INDEX_EXTENSION_PREFIX = "String  \"fd\""
INDEX_CODEC_NAME = "String  \"Lucene85FieldsIndex\""
def close():
    '''public void close()
    '''
def startDocument():
    '''public void startDocument()
    '''
def finishDocument():
    '''public void finishDocument()
    '''
def writeField():
    '''public void writeField(final FieldInfo info, final IndexableField field)
    '''
def finish():
    '''public void finish(final FieldInfos fis, final int numDocs)
    '''
def merge():
    '''public int merge(final MergeState mergeState)
    '''
def CompressingStoredFieldsMergeSub():
    '''public CompressingStoredFieldsMergeSub(final CompressingStoredFieldsReader reader, final MergeState.DocMap docMap, final int maxDoc)
    '''
def nextDoc():
    '''public int nextDoc()
    '''
