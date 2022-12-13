def DefaultBHttpClientConnection():
'''public DefaultBHttpClientConnection(final int buffersize, final int fragmentSizeHint, final CharsetDecoder chardecoder, final CharsetEncoder charencoder, final MessageConstraints constraints, final ContentLengthStrategy incomingContentStrategy, final ContentLengthStrategy outgoingContentStrategy, final HttpMessageWriterFactory<HttpRequest> requestWriterFactory, final HttpMessageParserFactory<HttpResponse> responseParserFactory)
public DefaultBHttpClientConnection(final int buffersize, final CharsetDecoder chardecoder, final CharsetEncoder charencoder, final MessageConstraints constraints)
public DefaultBHttpClientConnection(final int buffersize)
'''
pass
def bind():
'''public void bind(final Socket socket)
'''
pass
def isResponseAvailable():
'''public boolean isResponseAvailable(final int timeout)
'''
pass
def sendRequestHeader():
'''public void sendRequestHeader(final HttpRequest request)
'''
pass
def sendRequestEntity():
'''public void sendRequestEntity(final HttpEntityEnclosingRequest request)
'''
pass
def receiveResponseHeader():
'''public HttpResponse receiveResponseHeader()
'''
pass
def receiveResponseEntity():
'''public void receiveResponseEntity(final HttpResponse response)
'''
pass
def flush():
'''public void flush()
'''
pass
