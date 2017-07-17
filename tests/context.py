"""Allows unittest to use relative imports (e.g. testing a function imported from srvy/synch) """
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
