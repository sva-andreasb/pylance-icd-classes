TIFF_IMAGE_WIDTH = "int  256"
TIFF_IMAGE_LENGTH = "int  257"
TIFF_BITS_PER_SAMPLE = "int  258"
TIFF_COMPRESSION = "int  259"
TIFF_PHOTOMETRIC_INTERPRETATION = "int  262"
TIFF_FILL_ORDER = "int  266"
TIFF_STRIP_OFFSETS = "int  273"
TIFF_SAMPLES_PER_PIXEL = "int  277"
TIFF_ROWS_PER_STRIP = "int  278"
TIFF_STRIP_BYTE_COUNTS = "int  279"
TIFF_X_RESOLUTION = "int  282"
TIFF_Y_RESOLUTION = "int  283"
TIFF_PLANAR_CONFIGURATION = "int  284"
TIFF_T4_OPTIONS = "int  292"
TIFF_T6_OPTIONS = "int  293"
TIFF_RESOLUTION_UNIT = "int  296"
TIFF_PREDICTOR = "int  317"
TIFF_COLORMAP = "int  320"
TIFF_TILE_WIDTH = "int  322"
TIFF_TILE_LENGTH = "int  323"
TIFF_TILE_OFFSETS = "int  324"
TIFF_TILE_BYTE_COUNTS = "int  325"
TIFF_EXTRA_SAMPLES = "int  338"
TIFF_SAMPLE_FORMAT = "int  339"
TIFF_S_MIN_SAMPLE_VALUE = "int  340"
TIFF_S_MAX_SAMPLE_VALUE = "int  341"
TIFF_ICC_PROFILE = "int  34675"
def TIFFImageDecoder():
    '''    public TIFFImageDecoder(final SeekableStream input, final TIFFDecodeParam param)
    '''
def getNumPages():
    '''    public int getNumPages()
    '''
def decodeAsRenderedImage():
    '''    public RenderedImage decodeAsRenderedImage(final int page)
    '''
