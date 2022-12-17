def onOpenDocument():
    '''returns None\n\n
    onOpenDocument(final PdfWriter writer, final Document document)\n
    '''
def onStartPage():
    '''returns None\n\n
    onStartPage(final PdfWriter writer, final Document document)\n
    '''
def onEndPage():
    '''returns None\n\n
    onEndPage(final PdfWriter writer, final Document document)\n
    '''
def onCloseDocument():
    '''returns None\n\n
    onCloseDocument(final PdfWriter writer, final Document document)\n
    '''
def onParagraph():
    '''returns None\n\n
    onParagraph(final PdfWriter writer, final Document document, final float paragraphPosition)\n
    '''
def onParagraphEnd():
    '''returns None\n\n
    onParagraphEnd(final PdfWriter writer, final Document document, final float paragraphPosition)\n
    '''
def onChapter():
    '''returns None\n\n
    onChapter(final PdfWriter writer, final Document document, final float paragraphPosition, final Paragraph title)\n
    '''
def onChapterEnd():
    '''returns None\n\n
    onChapterEnd(final PdfWriter writer, final Document document, final float position)\n
    '''
def onSection():
    '''returns None\n\n
    onSection(final PdfWriter writer, final Document document, final float paragraphPosition, final int depth, final Paragraph title)\n
    '''
def onSectionEnd():
    '''returns None\n\n
    onSectionEnd(final PdfWriter writer, final Document document, final float position)\n
    '''
def onGenericTag():
    '''returns None\n\n
    onGenericTag(final PdfWriter writer, final Document document, final Rectangle rect, final String text)\n
    '''
