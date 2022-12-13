def forClient():
'''public static Http2FrameCodecBuilder forClient()
'''
pass
def forServer():
'''public static Http2FrameCodecBuilder forServer()
'''
pass
def initialSettings():
'''public Http2Settings initialSettings()
public Http2FrameCodecBuilder initialSettings(final Http2Settings settings)
'''
pass
def gracefulShutdownTimeoutMillis():
'''public long gracefulShutdownTimeoutMillis()
public Http2FrameCodecBuilder gracefulShutdownTimeoutMillis(final long gracefulShutdownTimeoutMillis)
'''
pass
def isServer():
'''public boolean isServer()
'''
pass
def maxReservedStreams():
'''public int maxReservedStreams()
public Http2FrameCodecBuilder maxReservedStreams(final int maxReservedStreams)
'''
pass
def isValidateHeaders():
'''public boolean isValidateHeaders()
'''
pass
def validateHeaders():
'''public Http2FrameCodecBuilder validateHeaders(final boolean validateHeaders)
'''
pass
def frameLogger():
'''public Http2FrameLogger frameLogger()
public Http2FrameCodecBuilder frameLogger(final Http2FrameLogger frameLogger)
'''
pass
def encoderEnforceMaxConcurrentStreams():
'''public boolean encoderEnforceMaxConcurrentStreams()
public Http2FrameCodecBuilder encoderEnforceMaxConcurrentStreams(final boolean encoderEnforceMaxConcurrentStreams)
'''
pass
def encoderEnforceMaxQueuedControlFrames():
'''public int encoderEnforceMaxQueuedControlFrames()
public Http2FrameCodecBuilder encoderEnforceMaxQueuedControlFrames(final int maxQueuedControlFrames)
'''
pass
def headerSensitivityDetector():
'''public Http2FrameCodecBuilder headerSensitivityDetector(final Http2HeadersEncoder.SensitivityDetector headerSensitivityDetector)
'''
pass
def encoderIgnoreMaxHeaderListSize():
'''public Http2FrameCodecBuilder encoderIgnoreMaxHeaderListSize(final boolean ignoreMaxHeaderListSize)
'''
pass
def initialHuffmanDecodeCapacity():
'''public Http2FrameCodecBuilder initialHuffmanDecodeCapacity(final int initialHuffmanDecodeCapacity)
'''
pass
def autoAckSettingsFrame():
'''public Http2FrameCodecBuilder autoAckSettingsFrame(final boolean autoAckSettings)
'''
pass
def autoAckPingFrame():
'''public Http2FrameCodecBuilder autoAckPingFrame(final boolean autoAckPingFrame)
'''
pass
def decoupleCloseAndGoAway():
'''public Http2FrameCodecBuilder decoupleCloseAndGoAway(final boolean decoupleCloseAndGoAway)
'''
pass
def decoderEnforceMaxConsecutiveEmptyDataFrames():
'''public int decoderEnforceMaxConsecutiveEmptyDataFrames()
public Http2FrameCodecBuilder decoderEnforceMaxConsecutiveEmptyDataFrames(final int maxConsecutiveEmptyFrames)
'''
pass
def build():
'''public Http2FrameCodec build()
'''
pass
