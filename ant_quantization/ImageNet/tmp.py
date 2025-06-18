import sys
sys.path = [p for p in sys.path if ".local" not in p]

import nvidia.dali as dali
print("DALI imported successfully")

