L = "byte  0"
LRE = "byte  1"
LRO = "byte  2"
R = "byte  3"
AL = "byte  4"
RLE = "byte  5"
RLO = "byte  6"
PDF = "byte  7"
EN = "byte  8"
ES = "byte  9"
ET = "byte  10"
AN = "byte  11"
CS = "byte  12"
NSM = "byte  13"
BN = "byte  14"
B = "byte  15"
S = "byte  16"
WS = "byte  17"
ON = "byte  18"
TYPE_MIN = "byte  0"
TYPE_MAX = "byte  18"
def ():
    '''returns BidiOrder\n\n
    (final byte[] types)\n
    (final byte[] types, final byte paragraphEmbeddingLevel)\n
    (final char[] text, final int offset, final int length, final byte paragraphEmbeddingLevel)\n
    '''
def getLevels():
    '''returns byte[]\n\n
    getLevels()\n
    getLevels(final int[] linebreaks)\n
    '''
def getReordering():
    '''returns int[]\n\n
    getReordering(final int[] linebreaks)\n
    '''
def getBaseLevel():
    '''returns byte\n\n
    getBaseLevel()\n
    '''
