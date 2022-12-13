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
def BidiOrder():
'''public BidiOrder(final byte[] types)
public BidiOrder(final byte[] types, final byte paragraphEmbeddingLevel)
public BidiOrder(final char[] text, final int offset, final int length, final byte paragraphEmbeddingLevel)
'''
pass
def getDirection():
'''public static final byte getDirection(final char c)
'''
pass
def getLevels():
'''public byte[] getLevels()
public byte[] getLevels(final int[] linebreaks)
'''
pass
def getReordering():
'''public int[] getReordering(final int[] linebreaks)
'''
pass
def getBaseLevel():
'''public byte getBaseLevel()
'''
pass
