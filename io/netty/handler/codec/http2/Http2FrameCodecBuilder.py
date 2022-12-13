def forClient():
    '''    public static Http2FrameCodecBuilder forClient()
    '''
def forServer():
    '''    public static Http2FrameCodecBuilder forServer()
    '''
def initialSettings():
    '''    public Http2Settings initialSettings()
    public Http2FrameCodecBuilder initialSettings(final Http2Settings settings)
    '''
def gracefulShutdownTimeoutMillis():
    '''    public long gracefulShutdownTimeoutMillis()
    public Http2FrameCodecBuilder gracefulShutdownTimeoutMillis(final long gracefulShutdownTimeoutMillis)
    '''
def isServer():
    '''    public boolean isServer()
    '''
def maxReservedStreams():
    '''    public int maxReservedStreams()
    public Http2FrameCodecBuilder maxReservedStreams(final int maxReservedStreams)
    '''
def isValidateHeaders():
    '''    public boolean isValidateHeaders()
    '''
def validateHeaders():
    '''    public Http2FrameCodecBuilder validateHeaders(final boolean validateHeaders)
    '''
def frameLogger():
    '''    public Http2FrameLogger frameLogger()
    public Http2FrameCodecBuilder frameLogger(final Http2FrameLogger frameLogger)
    '''
def encoderEnforceMaxConcurrentStreams():
    '''    public boolean encoderEnforceMaxConcurrentStreams()
    public Http2FrameCodecBuilder encoderEnforceMaxConcurrentStreams(final boolean encoderEnforceMaxConcurrentStreams)
    '''
def encoderEnforceMaxQueuedControlFrames():
    '''    public int encoderEnforceMaxQueuedControlFrames()
    public Http2FrameCodecBuilder encoderEnforceMaxQueuedControlFrames(final int maxQueuedControlFrames)
    '''
def headerSensitivityDetector():
    '''    public Http2FrameCodecBuilder headerSensitivityDetector(final Http2HeadersEncoder.SensitivityDetector headerSensitivityDetector)
    '''
def encoderIgnoreMaxHeaderListSize():
    '''    public Http2FrameCodecBuilder encoderIgnoreMaxHeaderListSize(final boolean ignoreMaxHeaderListSize)
    '''
def initialHuffmanDecodeCapacity():
    '''    public Http2FrameCodecBuilder initialHuffmanDecodeCapacity(final int initialHuffmanDecodeCapacity)
    '''
def autoAckSettingsFrame():
    '''    public Http2FrameCodecBuilder autoAckSettingsFrame(final boolean autoAckSettings)
    '''
def autoAckPingFrame():
    '''    public Http2FrameCodecBuilder autoAckPingFrame(final boolean autoAckPingFrame)
    '''
def decoupleCloseAndGoAway():
    '''    public Http2FrameCodecBuilder decoupleCloseAndGoAway(final boolean decoupleCloseAndGoAway)
    '''
def decoderEnforceMaxConsecutiveEmptyDataFrames():
    '''    public int decoderEnforceMaxConsecutiveEmptyDataFrames()
    public Http2FrameCodecBuilder decoderEnforceMaxConsecutiveEmptyDataFrames(final int maxConsecutiveEmptyFrames)
    '''
def build():
    '''    public Http2FrameCodec build()
    '''
