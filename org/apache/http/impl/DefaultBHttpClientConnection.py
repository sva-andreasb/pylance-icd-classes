def ():
    '''returns DefaultBHttpClientConnection\n\n
    (final int buffersize, final int fragmentSizeHint, final CharsetDecoder chardecoder, final CharsetEncoder charencoder, final MessageConstraints constraints, final ContentLengthStrategy incomingContentStrategy, final ContentLengthStrategy outgoingContentStrategy, final HttpMessageWriterFactory<HttpRequest> requestWriterFactory, final HttpMessageParserFactory<HttpResponse> responseParserFactory)\n
    (final int buffersize, final CharsetDecoder chardecoder, final CharsetEncoder charencoder, final MessageConstraints constraints)\n
    (final int buffersize)\n
    '''
def bind():
    '''returns None\n\n
    bind(final Socket socket)\n
    '''
def isResponseAvailable():
    '''returns boolean\n\n
    isResponseAvailable(final int timeout)\n
    '''
def sendRequestHeader():
    '''returns None\n\n
    sendRequestHeader(final HttpRequest request)\n
    '''
def sendRequestEntity():
    '''returns None\n\n
    sendRequestEntity(final HttpEntityEnclosingRequest request)\n
    '''
def receiveResponseHeader():
    '''returns HttpResponse\n\n
    receiveResponseHeader()\n
    '''
def receiveResponseEntity():
    '''returns None\n\n
    receiveResponseEntity(final HttpResponse response)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
