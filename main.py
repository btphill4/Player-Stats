# connect libraries
import time
# to check time to run
t = time.time()

import math
import decimal
import numpy as np
import torch as torch
# import tensorflow as tf

# import classes
from ClassFiles.player import *
from ClassFiles.coach import *
from ClassFiles.team import *

# import methods
from Methods.generalMethods import *


# beginning on main

# test methods
helloWorld()


# Check run time at end
# truncates value to 3 decimals
elapsed = '%.3f'%(time.time() - t)
print("Time to run: ", elapsed, "Seconds")
