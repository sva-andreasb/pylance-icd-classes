def ConversionHandler():
'''public ConversionHandler(final IConfig config)
'''
pass
def getPageCount():
'''public int getPageCount(final String path)
public int getPageCount(final InputStream fileStream, final String fileName)
'''
pass
def convertToImage():
'''public <T> T convertToImage(final String path, final ImageSaveOptions options)
public <T> T convertToImage(final InputStream fileStream, final String fileName, final ImageSaveOptions options)
'''
pass
def convertToPdf():
'''public <T> T convertToPdf(final String path, final PdfSaveOptions options)
public <T> T convertToPdf(final InputStream fileStream, final String fileName, final PdfSaveOptions options)
'''
pass
def convertToHtml():
'''public <T> T convertToHtml(final String path, final HtmlSaveOptions options)
public <T> T convertToHtml(final InputStream fileStream, final String fileName, final HtmlSaveOptions options)
'''
pass
def merge():
'''public <T> T merge(final List<String> filePathList, final MergeOptions mergeOptions)
public <T> T merge(final Map<String, InputStream> fileStreamMap, final MergeOptions mergeOptions)
'''
pass
