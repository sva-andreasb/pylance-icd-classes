questionMark = "String  \"% DSUnknown\nq\n1 G\n1 g\n0.1 0 0 0.1 9 0 cm\n0 J 0 j 4 M []0 d\n1 i \n0 g\n313 292 m\n313 404 325 453 432 529 c\n478 561 504 597 504 645 c\n504 736 440 760 391 760 c\n286 760 271 681 265 626 c\n265 625 l\n100 625 l\n100 828 253 898 381 898 c\n451 898 679 878 679 650 c\n679 555 628 499 538 435 c\n488 399 467 376 467 292 c\n313 292 l\nh\n308 214 170 -164 re\nf\n0.44 G\n1.2 w\n1 1 0.4 rg\n287 318 m\n287 430 299 479 406 555 c\n451 587 478 623 478 671 c\n478 762 414 786 365 786 c\n260 786 245 707 239 652 c\n239 651 l\n74 651 l\n74 854 227 924 355 924 c\n425 924 653 904 653 676 c\n653 581 602 525 512 461 c\n462 425 441 402 441 318 c\n287 318 l\nh\n282 240 170 -164 re\nB\nQ\n\""
def setLayer2Text():
    '''returns None\n\n
    setLayer2Text(final String text)\n
    '''
def getLayer2Text():
    '''returns String\n\n
    getLayer2Text()\n
    '''
def setLayer4Text():
    '''returns None\n\n
    setLayer4Text(final String text)\n
    '''
def getLayer4Text():
    '''returns String\n\n
    getLayer4Text()\n
    '''
def getRect():
    '''returns Rectangle\n\n
    getRect()\n
    '''
def isInvisible():
    '''returns boolean\n\n
    isInvisible()\n
    '''
def setCrypto():
    '''returns None\n\n
    setCrypto(final PrivateKey privKey, final Certificate[] certChain, final CRL[] crlList, final PdfName filter)\n
    '''
def setVisibleSignature():
    '''returns None\n\n
    setVisibleSignature(final Rectangle pageRect, final int page, final String fieldName)\n
    setVisibleSignature(final String fieldName)\n
    '''
def getLayer():
    '''returns PdfTemplate\n\n
    getLayer(final int layer)\n
    '''
def getTopLayer():
    '''returns PdfTemplate\n\n
    getTopLayer()\n
    '''
def getAppearance():
    '''returns PdfTemplate\n\n
    getAppearance()\n
    '''
def setExternalDigest():
    '''returns None\n\n
    setExternalDigest(final byte[] digest, final byte[] RSAdata, final String digestEncryptionAlgorithm)\n
    '''
def getReason():
    '''returns String\n\n
    getReason()\n
    '''
def setReason():
    '''returns None\n\n
    setReason(final String reason)\n
    '''
def getLocation():
    '''returns String\n\n
    getLocation()\n
    '''
def setLocation():
    '''returns None\n\n
    setLocation(final String location)\n
    '''
def getProvider():
    '''returns String\n\n
    getProvider()\n
    '''
def setProvider():
    '''returns None\n\n
    setProvider(final String provider)\n
    '''
def getPrivKey():
    '''returns PrivateKey\n\n
    getPrivKey()\n
    '''
def getCertChain():
    '''returns Certificate[]\n\n
    getCertChain()\n
    '''
def getCrlList():
    '''returns CRL[]\n\n
    getCrlList()\n
    '''
def getFilter():
    '''returns PdfName\n\n
    getFilter()\n
    '''
def isNewField():
    '''returns boolean\n\n
    isNewField()\n
    '''
def getPage():
    '''returns int\n\n
    getPage()\n
    '''
def getFieldName():
    '''returns String\n\n
    getFieldName()\n
    '''
def getPageRect():
    '''returns Rectangle\n\n
    getPageRect()\n
    '''
def getSignDate():
    '''returns Calendar\n\n
    getSignDate()\n
    '''
def setSignDate():
    '''returns None\n\n
    setSignDate(final Calendar signDate)\n
    '''
def getTempFile():
    '''returns File\n\n
    getTempFile()\n
    '''
def getNewSigName():
    '''returns String\n\n
    getNewSigName()\n
    '''
def preClose():
    '''returns None\n\n
    preClose()\n
    preClose(final HashMap exclusionSizes)\n
    '''
def close():
    '''returns None\n\n
    close(final PdfDictionary update)\n
    '''
def getRangeStream():
    '''returns InputStream\n\n
    getRangeStream()\n
    '''
def getCryptoDictionary():
    '''returns PdfDictionary\n\n
    getCryptoDictionary()\n
    '''
def setCryptoDictionary():
    '''returns None\n\n
    setCryptoDictionary(final PdfDictionary cryptoDictionary)\n
    '''
def getStamper():
    '''returns PdfStamper\n\n
    getStamper()\n
    '''
def isPreClosed():
    '''returns boolean\n\n
    isPreClosed()\n
    '''
def getSigStandard():
    '''returns PdfSigGenericPKCS\n\n
    getSigStandard()\n
    '''
def getContact():
    '''returns String\n\n
    getContact()\n
    '''
def setContact():
    '''returns None\n\n
    setContact(final String contact)\n
    '''
def getLayer2Font():
    '''returns Font\n\n
    getLayer2Font()\n
    '''
def setLayer2Font():
    '''returns None\n\n
    setLayer2Font(final Font layer2Font)\n
    '''
def isAcro6Layers():
    '''returns boolean\n\n
    isAcro6Layers()\n
    '''
def setAcro6Layers():
    '''returns None\n\n
    setAcro6Layers(final boolean acro6Layers)\n
    '''
def setRunDirection():
    '''returns None\n\n
    setRunDirection(final int runDirection)\n
    '''
def getRunDirection():
    '''returns int\n\n
    getRunDirection()\n
    '''
def getSignatureEvent():
    '''returns SignatureEvent\n\n
    getSignatureEvent()\n
    '''
def setSignatureEvent():
    '''returns None\n\n
    setSignatureEvent(final SignatureEvent signatureEvent)\n
    '''
def read():
    '''returns int\n\n
    read()\n
    read(final byte[] b, final int off, final int len)\n
    '''
