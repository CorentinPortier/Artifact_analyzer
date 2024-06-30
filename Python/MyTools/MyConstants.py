# For the ASCI-ART generator : 
#http://patorjk.com/software/taag/#p=display&c=bash&f=ANSI%20Regular&t=Type%20Something
# I've chosed the following font names - "Standard" and "ANSI Regular"
# To create template - follow below :
# https://stackoverflow.com/questions/74599665/how-to-use-template-when-creating-new-python-file-on-vscode

#  ██████  ██    ██ ██████  ██████   ██████  ███████ ███████ 
#  ██   ██ ██    ██ ██   ██ ██   ██ ██    ██ ██      ██      
#  ██████  ██    ██ ██████  ██████  ██    ██ ███████ █████   
#  ██      ██    ██ ██   ██ ██      ██    ██      ██ ██      
#  ██       ██████  ██   ██ ██       ██████  ███████ ███████ 
#
# To have a .py containing all the CONSTANTS used for this project

#  ██ ███    ███ ██████   ██████  ██████  ████████ ███████ 
#  ██ ████  ████ ██   ██ ██    ██ ██   ██    ██    ██      
#  ██ ██ ████ ██ ██████  ██    ██ ██████     ██    ███████ 
#  ██ ██  ██  ██ ██      ██    ██ ██   ██    ██         ██ 
#  ██ ██      ██ ██       ██████  ██   ██    ██    ███████ 
#
#    _   _       _   _           
#   | \ | | __ _| |_(_)_   _____ 
#   |  \| |/ _` | __| \ \ / / _ \
#   | |\  | (_| | |_| |\ V /  __/
#   |_| \_|\__,_|\__|_| \_/ \___|
#
import os
import logging #https://docs.python.org/3/library/logging.html#module-logging
LOGGING_FORMAT = "%(asctime)s | %(levelname)s | line %(lineno)d : %(message)s"
LOGGING_DATEMFT = 'UTC%z | %d/%m/%Y | %H:%M:%S'
logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT, datefmt= LOGGING_DATEMFT)

#    _____ _     _         _                    _         
#   |_   _| |__ (_)_ __ __| |  _ __   __ _ _ __| |_ _   _ 
#     | | | '_ \| | '__/ _` | | '_ \ / _` | '__| __| | | |
#     | | | | | | | | | (_| | | |_) | (_| | |  | |_| |_| |
#     |_| |_| |_|_|_|  \__,_| | .__/ \__,_|_|   \__|\__, |
#                             |_|                   |___/ 
import pandas

#    _                    _ 
#   | |    ___   ___ __ _| |
#   | |   / _ \ / __/ _` | |
#   | |__| (_) | (_| (_| | |
#   |_____\___/ \___\__,_|_|
#

#    _____                   _   _ _       _       
#   |_   _|   _ _ __   ___  | | | (_)_ __ | |_ ___ 
#     | || | | | '_ \ / _ \ | |_| | | '_ \| __/ __|
#     | || |_| | |_) |  __/ |  _  | | | | | |_\__ \
#     |_| \__, | .__/ \___| |_| |_|_|_| |_|\__|___/
#         |___/|_|                                 
#to Prevent imports loop - just need the type for type hints

#   ██████  ██████  ███    ██ ███████ ████████  █████  ███    ██ ████████ ███████ 
#  ██      ██    ██ ████   ██ ██         ██    ██   ██ ████   ██    ██    ██      
#  ██      ██    ██ ██ ██  ██ ███████    ██    ███████ ██ ██  ██    ██    ███████ 
#  ██      ██    ██ ██  ██ ██      ██    ██    ██   ██ ██  ██ ██    ██         ██ 
#   ██████  ██████  ██   ████ ███████    ██    ██   ██ ██   ████    ██    ███████ 
#
CURRENT_PATH = os.getcwd()
logging.debug(f"CURRENT_PATH: {CURRENT_PATH}")
SOURCE_PATH = CURRENT_PATH + "\\Python\Source"
logging.debug(f"SOURCE_PATH: {SOURCE_PATH}")
logging.debug(f"Files in above Path : {os.listdir(SOURCE_PATH)}")
MIN_MAX_ROLLS_PER_SUBSTATS = pandas.read_excel(os.path.join(SOURCE_PATH,
                                                            "Genshin_my_data.xlsx"),
                                                            sheet_name="Fixed data",
                                                            header=31)
logging.debug(f"MIN_MAX_ROLLS_PER_SUBSTATS:\n{MIN_MAX_ROLLS_PER_SUBSTATS}")

NUMBER_OF_POSSIBLE_SUBSTATS = 20
SUBSTATS_NAME_IN_SOURCE = MIN_MAX_ROLLS_PER_SUBSTATS.columns[:NUMBER_OF_POSSIBLE_SUBSTATS]

FRAME_FILE_EXTENSION = '.png'
FRAME_NAME = 'Artifact_'
FRAME_SUBSTATS_NAME = 'Substats_'
FRAME_MAINSTAT_NAME = 'Mainstat_'

API_RESPONSE_FILENAME_NAME = "APIresponse_name"
API_RESPONSE_FILENAME_TYPE = "APIresponse_type"
API_RESPONSE_FILENAME_MAINSTAT = "APIresponse_mainstat"
API_RESPONSE_FILENAME_SUBSTATS = "APIresponse_substats"
API_RESPONSE_FILENAME_SET = "APIresponse_set"
API_RESPONSE_EXTENSION = ".json"

# Define the frame to get artifact's name
LINE_NAME_TOP_LEFT_RATIO = 17/720
LINE_NAME_BOTTOM_RIGHT_RATIO = 64/720
COLUMN_NAME_TOP_LEFT_RATIO = 41/650
COLUMN_NAME_BOTTOM_RIGHT_RATIO = 611/650

# Define the frame to get artifact's type
LINE_TYPE_TOP_LEFT_RATIO = 94/720
LINE_TYPE_BOTTOM_RIGHT_RATIO = 129/720
COLUMN_TYPE_TOP_LEFT_RATIO = 42/650
COLUMN_TYPE_BOTTOM_RIGHT_RATIO = 331/650

# Define the frame to get artifact's mainstat
LINE_MAINSTAT_TOP_LEFT_RATIO = 197/720
LINE_MAINSTAT_BOTTOM_RIGHT_RATIO = 301/720
COLUMN_MAINSTAT_TOP_LEFT_RATIO = 39/650
COLUMN_MAINSTAT_BOTTOM_RIGHT_RATIO = 386/650

# Define the frame to get artifact's substats
LINE_SUBSTATS_TOP_LEFT_RATIO = 464/720
LINE_SUBSTATS_BOTTOM_RIGHT_RATIO = 668/720
COLUMN_SUBSTATS_TOP_LEFT_RATIO = 70/650
COLUMN_SUBSTATS_BOTTOM_RIGHT_RATIO = 520/650

# Define the frame to get artifact's set
LINE_SET_TOP_LEFT_RATIO = 664/720
LINE_SET_BOTTOM_RIGHT_RATIO = 711/720
COLUMN_SET_TOP_LEFT_RATIO = 38/650
COLUMN_SET_BOTTOM_RIGHT_RATIO = 608/650

# Define the frame to get artifact's image
LINE_ARTIFACT_TOP_LEFT_RATIO = 88/720
LINE_ARTIFACT_BOTTOM_RIGHT_RATIO = 364/720
COLUMN_ARTIFACT_TOP_LEFT_RATIO = 344/650
COLUMN_ARTIFACT_BOTTOM_RIGHT_RATIO = 632/650