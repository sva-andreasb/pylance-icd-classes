def initialSettings():
    '''returns Http2FrameCodecBuilder\n\n
    initialSettings()\n
    initialSettings(final Http2Settings settings)\n
    '''
def gracefulShutdownTimeoutMillis():
    '''returns Http2FrameCodecBuilder\n\n
    gracefulShutdownTimeoutMillis()\n
    gracefulShutdownTimeoutMillis(final long gracefulShutdownTimeoutMillis)\n
    '''
def isServer():
    '''returns boolean\n\n
    isServer()\n
    '''
def maxReservedStreams():
    '''returns Http2FrameCodecBuilder\n\n
    maxReservedStreams()\n
    maxReservedStreams(final int maxReservedStreams)\n
    '''
def isValidateHeaders():
    '''returns boolean\n\n
    isValidateHeaders()\n
    '''
def validateHeaders():
    '''returns Http2FrameCodecBuilder\n\n
    validateHeaders(final boolean validateHeaders)\n
    '''
def frameLogger():
    '''returns Http2FrameCodecBuilder\n\n
    frameLogger()\n
    frameLogger(final Http2FrameLogger frameLogger)\n
    '''
def encoderEnforceMaxConcurrentStreams():
    '''returns Http2FrameCodecBuilder\n\n
    encoderEnforceMaxConcurrentStreams()\n
    encoderEnforceMaxConcurrentStreams(final boolean encoderEnforceMaxConcurrentStreams)\n
    '''
def encoderEnforceMaxQueuedControlFrames():
    '''returns Http2FrameCodecBuilder\n\n
    encoderEnforceMaxQueuedControlFrames()\n
    encoderEnforceMaxQueuedControlFrames(final int maxQueuedControlFrames)\n
    '''
def headerSensitivityDetector():
    '''returns Http2FrameCodecBuilder\n\n
    headerSensitivityDetector(final Http2HeadersEncoder.SensitivityDetector headerSensitivityDetector)\n
    '''
def encoderIgnoreMaxHeaderListSize():
    '''returns Http2FrameCodecBuilder\n\n
    encoderIgnoreMaxHeaderListSize(final boolean ignoreMaxHeaderListSize)\n
    '''
def initialHuffmanDecodeCapacity():
    '''returns Http2FrameCodecBuilder\n\n
    initialHuffmanDecodeCapacity(final int initialHuffmanDecodeCapacity)\n
    '''
def autoAckSettingsFrame():
    '''returns Http2FrameCodecBuilder\n\n
    autoAckSettingsFrame(final boolean autoAckSettings)\n
    '''
def autoAckPingFrame():
    '''returns Http2FrameCodecBuilder\n\n
    autoAckPingFrame(final boolean autoAckPingFrame)\n
    '''
def decoupleCloseAndGoAway():
    '''returns Http2FrameCodecBuilder\n\n
    decoupleCloseAndGoAway(final boolean decoupleCloseAndGoAway)\n
    '''
def decoderEnforceMaxConsecutiveEmptyDataFrames():
    '''returns Http2FrameCodecBuilder\n\n
    decoderEnforceMaxConsecutiveEmptyDataFrames()\n
    decoderEnforceMaxConsecutiveEmptyDataFrames(final int maxConsecutiveEmptyFrames)\n
    '''
def build():
    '''returns Http2FrameCodec\n\n
    build()\n
    '''
