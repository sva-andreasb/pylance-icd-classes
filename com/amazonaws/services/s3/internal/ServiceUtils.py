APPEND_MODE = "boolean  true"
OVERWRITE_MODE = "boolean  false"
def parseIso8601Date():
'''public static Date parseIso8601Date(final String dateString)
'''
pass
def formatIso8601Date():
'''public static String formatIso8601Date(final Date date)
'''
pass
def parseRfc822Date():
'''public static Date parseRfc822Date(final String dateString)
'''
pass
def formatRfc822Date():
'''public static String formatRfc822Date(final Date date)
'''
pass
def toByteArray():
'''public static byte[] toByteArray(final String s)
'''
pass
def removeQuotes():
'''public static String removeQuotes(String s)
'''
pass
def convertRequestToUrl():
'''public static URL convertRequestToUrl(final Request<?> request)
public static URL convertRequestToUrl(final Request<?> request, final boolean removeLeadingSlashInResourcePath)
public static URL convertRequestToUrl(final Request<?> request, final boolean removeLeadingSlashInResourcePath, final boolean urlEncode)
'''
pass
def join():
'''public static String join(final List<String> strings)
'''
pass
def downloadObjectToFile():
'''public static void downloadObjectToFile(final S3Object s3Object, final File destinationFile, final boolean performIntegrityCheck, final boolean appendData)
'''
pass
def downloadToFile():
'''public static void downloadToFile(final S3Object s3Object, final File dstfile, final boolean performIntegrityCheck, final boolean appendData, final long expectedFileLength)
'''
pass
def retryableDownloadS3ObjectToFile():
'''public static S3Object retryableDownloadS3ObjectToFile(final File file, final RetryableS3DownloadTask retryableS3DownloadTask, final boolean appendData)
'''
pass
def appendFile():
'''public static void appendFile(final File sourceFile, final File destinationFile)
'''
pass
def isS3USStandardEndpoint():
'''public static boolean isS3USStandardEndpoint(final String endpoint)
'''
pass
def isS3USEastEndpiont():
'''public static boolean isS3USEastEndpiont(final String endpoint)
'''
pass
def isS3AccelerateEndpoint():
'''public static boolean isS3AccelerateEndpoint(final String endpoint)
'''
pass
def getPartCount():
'''public static Integer getPartCount(final GetObjectRequest getObjectRequest, final AmazonS3 s3)
'''
pass
def getLastByteInPart():
'''public static long getLastByteInPart(final AmazonS3 s3, final GetObjectRequest getObjectRequest, final Integer partNumber)
'''
pass
