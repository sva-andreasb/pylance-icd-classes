def complete():
'''public static void complete(final OutputStream outStream, final byte[] xmlData, final LinkedList binaryNodeList, final String boundary, final String contentId, final String charSetEncoding, final String SOAPContentType)
public static void complete(final OutputStream outStream, final byte[] xmlData, final LinkedList binaryNodeList, final String boundary, final String contentId, final String charSetEncoding, final String SOAPContentType, final OMOutputFormat omOutputFormat)
'''
pass
def createMimeBodyPart():
'''public static MimeBodyPart createMimeBodyPart(final String contentID, final DataHandler dataHandler)
public static MimeBodyPart createMimeBodyPart(final String contentID, final DataHandler dataHandler, final OMOutputFormat omOutputFormat)
'''
pass
def writeMimeBoundary():
'''public static void writeMimeBoundary(final OutputStream outStream, final String boundary)
'''
pass
def startWritingMime():
'''public static void startWritingMime(final OutputStream outStream, final String boundary)
'''
pass
def writeBodyPart():
'''public static void writeBodyPart(final OutputStream outStream, final MimeBodyPart part, final String boundary)
'''
pass
def finishWritingMime():
'''public static void finishWritingMime(final OutputStream outStream)
'''
pass
def writeSOAPWithAttachmentsMessage():
'''public static void writeSOAPWithAttachmentsMessage(final StringWriter writer, final OutputStream outputStream, final Attachments attachments, final OMOutputFormat format)
'''
pass
def writeDataHandlerWithAttachmentsMessage():
'''public static void writeDataHandlerWithAttachmentsMessage(final DataHandler rootDataHandler, final String contentType, final OutputStream outputStream, final Map attachments, final OMOutputFormat format)
public static void writeDataHandlerWithAttachmentsMessage(final DataHandler rootDataHandler, final String contentType, final OutputStream outputStream, final Map attachments, final OMOutputFormat format, final Collection ids)
'''
pass
def writeMM7Message():
'''public static void writeMM7Message(final StringWriter writer, final OutputStream outputStream, final Attachments attachments, final OMOutputFormat format, final String innerPartCID, final String innerBoundary)
'''
pass
