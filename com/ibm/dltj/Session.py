DLTSESSION_LEX = "int  0"
DLTSESSION_SPELL = "int  1"
Delay_sentence = "int  2"
Delay_paragraph = "int  2"
PROCMODE_ALLCASE = "int  1"
PROCMODE_LOWERCASE = "int  3"
PROCMODE_MW_PROCESSING = "int  3"
PROCMODE_MW_BUILDING = "int  4"
def Session():
'''public Session(final String s)
public Session(final Locale locale)
'''
pass
def setBreakIteratorByLocaleString():
'''public void setBreakIteratorByLocaleString(final String breakIteratorByLocaleString)
'''
pass
def setBreakIteratorByFilename():
'''public void setBreakIteratorByFilename(final String breakIteratorByFilename)
'''
pass
def setProcessingMode():
'''public void setProcessingMode(final int processingMode)
'''
pass
def setCaseStrictMode():
'''public void setCaseStrictMode(final boolean caseStrictMode)
'''
pass
def setGuessingMode():
'''public void setGuessingMode(final int guessingMode)
'''
pass
def setTransliteratorRuleByFilename():
'''public void setTransliteratorRuleByFilename(final String transliteratorRuleByFilename)
'''
pass
def setDictionaries():
'''public void setDictionaries(final Dictionary[] array, final Dictionary[] array2, final Dictionary[] array3)
public void setDictionaries(final Dictionary[] array, final Dictionary[] array2, final Dictionary[] array3, final Dictionary[] array4)
'''
pass
def open():
'''public void open(final Dictionary[] array, final int n)
public void open(final Dictionary[] array, final int n, final int n2, final int n3)
public synchronized void open(final Dictionary[] array, final int n, final int n2, final int n3, final int sessionType)
public void open(final int n, final int n2, final int n3)
'''
pass
def processText():
'''public synchronized LPS processText(final String text)
public synchronized LPS processText(final CharacterIterator characterIterator)
public synchronized void processText(final CharacterIterator characterIterator, final ParsingStream parsingStream)
public synchronized void processText(final CharacterIterator characterIterator, final LemmaParsingStream lemmaParsingStream)
public synchronized void processText(final CharacterIterator characterIterator, final ClassificationParsingStream classificationParsingStream)
'''
pass
def delayProcessedText():
'''public synchronized void delayProcessedText(final CharacterIterator characterIterator, final LemmaParsingStream lemmaParsingStream, final int n)
public synchronized void delayProcessedText(final CharacterIterator characterIterator, final LemmaParsingStream lemmaParsingStream)
'''
pass
def processTextMW():
'''public synchronized void processTextMW(final CharacterIterator characterIterator, final ParsingStream parsingStream)
public synchronized void processTextMW(final CharacterIterator characterIterator, final ClassificationParsingStream classificationParsingStream)
'''
pass
def close():
'''public synchronized void close()
'''
pass
def dispose():
'''public void dispose()
'''
pass
def valid():
'''public boolean valid()
'''
pass
def processTextBuffered():
'''public synchronized void processTextBuffered(final char[] value, final int n, final int end, final ParsingStream parsingStream)
'''
pass
