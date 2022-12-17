def ():
    '''returns ErrorDataEncoderException\n\n
    (final HttpRequest request, final boolean multipart)\n
    (final HttpDataFactory factory, final HttpRequest request, final boolean multipart)\n
    (final HttpDataFactory factory, final HttpRequest request, final boolean multipart, final Charset charset, final EncoderMode encoderMode)\n
    ()\n
    (final String msg)\n
    (final Throwable cause)\n
    (final String msg, final Throwable cause)\n
    '''
def cleanFiles():
    '''returns None\n\n
    cleanFiles()\n
    '''
def isMultipart():
    '''returns boolean\n\n
    isMultipart()\n
    '''
def getBodyListAttributes():
    '''returns List<InterfaceHttpData>\n\n
    getBodyListAttributes()\n
    '''
def setBodyHttpDatas():
    '''returns None\n\n
    setBodyHttpDatas(final List<InterfaceHttpData> datas)\n
    '''
def addBodyAttribute():
    '''returns None\n\n
    addBodyAttribute(final String name, final String value)\n
    '''
def addBodyFileUpload():
    '''returns None\n\n
    addBodyFileUpload(final String name, final File file, final String contentType, final boolean isText)\n
    addBodyFileUpload(final String name, String filename, final File file, final String contentType, final boolean isText)\n
    '''
def addBodyFileUploads():
    '''returns None\n\n
    addBodyFileUploads(final String name, final File[] file, final String[] contentType, final boolean[] isText)\n
    '''
def addBodyHttpData():
    '''returns None\n\n
    addBodyHttpData(final InterfaceHttpData data)\n
    '''
def finalizeRequest():
    '''returns HttpRequest\n\n
    finalizeRequest()\n
    '''
def isChunked():
    '''returns boolean\n\n
    isChunked()\n
    '''
def close():
    '''returns None\n\n
    close()\n
    '''
def readChunk():
    '''returns HttpContent\n\n
    readChunk(final ChannelHandlerContext ctx)\n
    readChunk(final ByteBufAllocator allocator)\n
    '''
def isEndOfInput():
    '''returns boolean\n\n
    isEndOfInput()\n
    '''
def length():
    '''returns long\n\n
    length()\n
    '''
def progress():
    '''returns long\n\n
    progress()\n
    '''
def setProtocolVersion():
    '''returns FullHttpRequest\n\n
    setProtocolVersion(final HttpVersion version)\n
    setProtocolVersion(final HttpVersion version)\n
    '''
def setMethod():
    '''returns FullHttpRequest\n\n
    setMethod(final HttpMethod method)\n
    setMethod(final HttpMethod method)\n
    '''
def setUri():
    '''returns FullHttpRequest\n\n
    setUri(final String uri)\n
    setUri(final String uri)\n
    '''
def getMethod():
    '''returns HttpMethod\n\n
    getMethod()\n
    '''
def method():
    '''returns HttpMethod\n\n
    method()\n
    '''
def getUri():
    '''returns String\n\n
    getUri()\n
    '''
def uri():
    '''returns String\n\n
    uri()\n
    '''
def getProtocolVersion():
    '''returns HttpVersion\n\n
    getProtocolVersion()\n
    '''
def protocolVersion():
    '''returns HttpVersion\n\n
    protocolVersion()\n
    '''
def headers():
    '''returns HttpHeaders\n\n
    headers()\n
    '''
def decoderResult():
    '''returns DecoderResult\n\n
    decoderResult()\n
    '''
def getDecoderResult():
    '''returns DecoderResult\n\n
    getDecoderResult()\n
    '''
def setDecoderResult():
    '''returns None\n\n
    setDecoderResult(final DecoderResult result)\n
    '''
def copy():
    '''returns FullHttpRequest\n\n
    copy()\n
    '''
def duplicate():
    '''returns FullHttpRequest\n\n
    duplicate()\n
    '''
def retainedDuplicate():
    '''returns FullHttpRequest\n\n
    retainedDuplicate()\n
    '''
def replace():
    '''returns FullHttpRequest\n\n
    replace(final ByteBuf content)\n
    '''
def retain():
    '''returns FullHttpRequest\n\n
    retain(final int increment)\n
    retain()\n
    '''
def touch():
    '''returns FullHttpRequest\n\n
    touch()\n
    touch(final Object hint)\n
    '''
def content():
    '''returns ByteBuf\n\n
    content()\n
    '''
def trailingHeaders():
    '''returns HttpHeaders\n\n
    trailingHeaders()\n
    '''
def refCnt():
    '''returns int\n\n
    refCnt()\n
    '''
def release():
    '''returns boolean\n\n
    release()\n
    release(final int decrement)\n
    '''
