import io
import zipfile
import os,shutil
import sys
import gc
import re
import math

from PIL import Image

from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
from matplotlib.path import Path
from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection

try:
    from osgeo import gdal
    from osgeo import ogr
    from osgeo import osr
except ImportError:
    import gdal
    import ogr
    import osr

class younggisMap:
