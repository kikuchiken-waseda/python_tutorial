# -*- coding: utf-8 -*
"""src/ecg_file_days.py

:DATE: 2020/06/01 14:58:32

K-shape 法による時系列クラスタリング実例:
    使用方法::
        $ python src/ecg_file_days.py
"""

import datetime
import gzip
import pickle
import re
import time
from os import getcwd, listdir, path, walk

import matplotlib as mpl
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from mpl_tookskits.axes_grid1 import Grid

current_path = getcwd()
file = path.sep.join([])
