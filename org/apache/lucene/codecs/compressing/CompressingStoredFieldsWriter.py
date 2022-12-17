FIELDS_EXTENSION = "String  \"fdt\""
INDEX_EXTENSION_PREFIX = "String  \"fd\""
INDEX_CODEC_NAME = "String  \"Lucene85FieldsIndex\""
def close():
    '''returns None\n\n
    close()\n
    '''
def startDocument():
    '''returns None\n\n
    startDocument()\n
    '''
def finishDocument():
    '''returns None\n\n
    finishDocument()\n
    '''
def writeField():
    '''returns None\n\n
    writeField(final FieldInfo info, final IndexableField field)\n
    '''
def finish():
    '''returns None\n\n
    finish(final FieldInfos fis, final int numDocs)\n
    '''
def merge():
    '''returns int\n\n
    merge(final MergeState mergeState)\n
    '''
def ():
    '''returns CompressingStoredFieldsMergeSub\n\n
    (final CompressingStoredFieldsReader reader, final MergeState.DocMap docMap, final int maxDoc)\n
    '''
def nextDoc():
    '''returns int\n\n
    nextDoc()\n
    '''
