def ():
    '''returns DefaultBHttpServerConnection\n\n
    (final int buffersize, final int fragmentSizeHint, final CharsetDecoder chardecoder, final CharsetEncoder charencoder, final MessageConstraints constraints, final ContentLengthStrategy incomingContentStrategy, final ContentLengthStrategy outgoingContentStrategy, final HttpMessageParserFactory<HttpRequest> requestParserFactory, final HttpMessageWriterFactory<HttpResponse> responseWriterFactory)\n
    (final int buffersize, final CharsetDecoder chardecoder, final CharsetEncoder charencoder, final MessageConstraints constraints)\n
    (final int buffersize)\n
    '''
def bind():
    '''returns None\n\n
    bind(final Socket socket)\n
    '''
def receiveRequestHeader():
    '''returns HttpRequest\n\n
    receiveRequestHeader()\n
    '''
def receiveRequestEntity():
    '''returns None\n\n
    receiveRequestEntity(final HttpEntityEnclosingRequest request)\n
    '''
def sendResponseHeader():
    '''returns None\n\n
    sendResponseHeader(final HttpResponse response)\n
    '''
def sendResponseEntity():
    '''returns None\n\n
    sendResponseEntity(final HttpResponse response)\n
    '''
def flush():
    '''returns None\n\n
    flush()\n
    '''
