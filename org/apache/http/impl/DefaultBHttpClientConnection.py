def DefaultBHttpClientConnection():
    '''public DefaultBHttpClientConnection(final int buffersize, final int fragmentSizeHint, final CharsetDecoder chardecoder, final CharsetEncoder charencoder, final MessageConstraints constraints, final ContentLengthStrategy incomingContentStrategy, final ContentLengthStrategy outgoingContentStrategy, final HttpMessageWriterFactory<HttpRequest> requestWriterFactory, final HttpMessageParserFactory<HttpResponse> responseParserFactory)
    public DefaultBHttpClientConnection(final int buffersize, final CharsetDecoder chardecoder, final CharsetEncoder charencoder, final MessageConstraints constraints)
    public DefaultBHttpClientConnection(final int buffersize)
    '''
def bind():
    '''public void bind(final Socket socket)
    '''
def isResponseAvailable():
    '''public boolean isResponseAvailable(final int timeout)
    '''
def sendRequestHeader():
    '''public void sendRequestHeader(final HttpRequest request)
    '''
def sendRequestEntity():
    '''public void sendRequestEntity(final HttpEntityEnclosingRequest request)
    '''
def receiveResponseHeader():
    '''public HttpResponse receiveResponseHeader()
    '''
def receiveResponseEntity():
    '''public void receiveResponseEntity(final HttpResponse response)
    '''
def flush():
    '''public void flush()
    '''
