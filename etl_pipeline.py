import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import json
import logging
from typing import Dict, Any, Tuple 
import os


# Setup logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname))s -%(message)s')
logger = logging.getLogger(__name__)

class DataProcessor:
    """Handle data ingestion and transformation operations"""
    
    def __init__(self):
        self.raw_data = None
        self.processed_data = None 
        