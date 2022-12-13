def DefaultBHttpServerConnection():
    '''    public DefaultBHttpServerConnection(final int buffersize, final int fragmentSizeHint, final CharsetDecoder chardecoder, final CharsetEncoder charencoder, final MessageConstraints constraints, final ContentLengthStrategy incomingContentStrategy, final ContentLengthStrategy outgoingContentStrategy, final HttpMessageParserFactory<HttpRequest> requestParserFactory, final HttpMessageWriterFactory<HttpResponse> responseWriterFactory)
    public DefaultBHttpServerConnection(final int buffersize, final CharsetDecoder chardecoder, final CharsetEncoder charencoder, final MessageConstraints constraints)
    public DefaultBHttpServerConnection(final int buffersize)
    '''
def bind():
    '''    public void bind(final Socket socket)
    '''
def receiveRequestHeader():
    '''    public HttpRequest receiveRequestHeader()
    '''
def receiveRequestEntity():
    '''    public void receiveRequestEntity(final HttpEntityEnclosingRequest request)
    '''
def sendResponseHeader():
    '''    public void sendResponseHeader(final HttpResponse response)
    '''
def sendResponseEntity():
    '''    public void sendResponseEntity(final HttpResponse response)
    '''
def flush():
    '''    public void flush()
    '''
