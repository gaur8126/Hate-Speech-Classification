import os 

from datetime import datetime

# COMMON constatns 

TIMESTAMP: str = datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
ARTIFACT_DIR = os.path.join("artifacts", TIMESTAMP)
BUCKET_NAME = 'hate-data-zip'
ZIP_FILE_NAME = 'dataset.zip'
DATA_FILE_PATH = os.path.join("data","dataset.zip")
LABEL = 'label'
TWEET = 'tweet'