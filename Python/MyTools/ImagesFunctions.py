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
# To have a .py containing all the Functions that will be used for Images management

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
from __future__ import annotations
import typing
import logging #https://docs.python.org/3/library/logging.html#module-logging
LOGGING_FORMAT = "%(asctime)s | %(levelname)s | line %(lineno)d : %(message)s"
LOGGING_DATEMFT = 'UTC%z | %d/%m/%Y | %H:%M:%S'
logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT, datefmt= LOGGING_DATEMFT)
import os
from re import search

#    _____ _     _         _                    _         
#   |_   _| |__ (_)_ __ __| |  _ __   __ _ _ __| |_ _   _ 
#     | | | '_ \| | '__/ _` | | '_ \ / _` | '__| __| | | |
#     | | | | | | | | | (_| | | |_) | (_| | |  | |_| |_| |
#     |_| |_| |_|_|_|  \__,_| | .__/ \__,_|_|   \__|\__, |
#                             |_|                   |___/ 
import cv2
import numpy as np

#    _                    _ 
#   | |    ___   ___ __ _| |
#   | |   / _ \ / __/ _` | |
#   | |__| (_) | (_| (_| | |
#   |_____\___/ \___\__,_|_|
#
try:
    logging.info("trying 'import ArtifactsFunctions'")
    import ArtifactsFunctions
    logging.debug(f"{__name__} run as main ?")
except Exception as error:
    logging.debug(f"{__name__} was imported ? Error: {error}")
try:
    logging.info("trying 'from MyTools import ArtifactsFunctions'")
    from MyTools import ArtifactsFunctions
    logging.debug(f"{__name__} was imported")
except Exception :
    from re import search
    pattern = "(?<=\\\)\w*\.py"
    from __main__ import __file__
    main_name = search(pattern, __file__).group()
    logging.debug(f"{main_name} run as main")

try:
    logging.info("trying 'import MyClasses'")
    import MyClasses
    logging.debug(f"{__name__} run as main ?")
except Exception as error:
    logging.debug(f"{__name__} was imported ? Error: {error}")
try:
    logging.info("trying 'from MyTools import MyClasses'")
    from MyTools import MyClasses
    logging.debug(f"{__name__} was imported")
except Exception :
    from re import search
    pattern = "(?<=\\\)\w*\.py"
    from __main__ import __file__
    main_name = search(pattern, __file__).group()
    logging.debug(f"{main_name} run as main")

try:
    logging.debug("Trying 'import MyValueError'")
    import MyValueError
    logging.debug(f"{__name__} run as main ?")
except ModuleNotFoundError as error:
    logging.debug(f"{__name__} was imported ? Error: {error}")
try:
    logging.debug("Trying 'from MyTools import MyValueError'")
    from MyTools import MyValueError
    logging.debug(f"{__name__} was imported")
except ModuleNotFoundError :
    pattern = "(?<=\\\)\w*\.py"
    from __main__ import __file__
    main_name = search(pattern, __file__).group()
    logging.debug(f"{main_name} run as main")

try:
    logging.debug("Trying 'import MyConstants'")
    import MyConstants
    logging.debug(f"{__name__} run as main ?")
except ModuleNotFoundError as error:
    logging.debug(f"{__name__} was imported ? Error: {error}")
try:
    logging.debug("Trying 'from MyTools import MyConstants'")
    from MyTools import MyConstants
    logging.debug(f"{__name__} was imported")
except ModuleNotFoundError :
    pattern = "(?<=\\\)\w*\.py"
    from __main__ import __file__
    main_name = search(pattern, __file__).group()
    logging.debug(f"{main_name} run as main")

#    _____                   _   _ _       _       
#   |_   _|   _ _ __   ___  | | | (_)_ __ | |_ ___ 
#     | || | | | '_ \ / _ \ | |_| | | '_ \| __/ __|
#     | || |_| | |_) |  __/ |  _  | | | | | |_\__ \
#     |_| \__, | .__/ \___| |_| |_|_|_| |_|\__|___/
#         |___/|_|                                 
#to Prevent imports loop - just need the type for type hints
if typing.TYPE_CHECKING:
    from MyClasses import Artifact

#   ██████  ██████  ███    ██ ███████ ████████  █████  ███    ██ ████████ ███████ 
#  ██      ██    ██ ████   ██ ██         ██    ██   ██ ████   ██    ██    ██      
#  ██      ██    ██ ██ ██  ██ ███████    ██    ███████ ██ ██  ██    ██    ███████ 
#  ██      ██    ██ ██  ██ ██      ██    ██    ██   ██ ██  ██ ██    ██         ██ 
#   ██████  ██████  ██   ████ ███████    ██    ██   ██ ██   ████    ██    ███████ 
#
CURRENT_PATH = os.getcwd()
logging.debug(f"CURRENT_PATH: {CURRENT_PATH}")
IMAGES_PATH = CURRENT_PATH + "/Python/Source/ArtifactsScreenshots/"
logging.debug(f"IMAGES_PATH: {IMAGES_PATH}")
logging.debug(f"Files in above Path : {os.listdir(IMAGES_PATH)}")
VIDEOS_PATH = CURRENT_PATH + "/Python/Source/Videos/"
logging.debug(f"VIDEOS_PATH: {VIDEOS_PATH}")
logging.debug(f"Files in above Path : {os.listdir(VIDEOS_PATH)}")


FRAME_NAME = MyConstants.FRAME_NAME
FRAME_FILE_EXTENSION = MyConstants.FRAME_FILE_EXTENSION


LINE_NAME_TOP_LEFT_RATIO = MyConstants.LINE_NAME_TOP_LEFT_RATIO
LINE_NAME_BOTTOM_RIGHT_RATIO = MyConstants.LINE_NAME_BOTTOM_RIGHT_RATIO
COLUMN_NAME_TOP_LEFT_RATIO = MyConstants.COLUMN_NAME_TOP_LEFT_RATIO
COLUMN_NAME_BOTTOM_RIGHT_RATIO = MyConstants.COLUMN_NAME_BOTTOM_RIGHT_RATIO

LINE_TYPE_TOP_LEFT_RATIO = MyConstants.LINE_TYPE_TOP_LEFT_RATIO
LINE_TYPE_BOTTOM_RIGHT_RATIO = MyConstants.LINE_TYPE_BOTTOM_RIGHT_RATIO
COLUMN_TYPE_TOP_LEFT_RATIO = MyConstants.COLUMN_TYPE_TOP_LEFT_RATIO
COLUMN_TYPE_BOTTOM_RIGHT_RATIO = MyConstants.COLUMN_TYPE_BOTTOM_RIGHT_RATIO

LINE_MAINSTAT_TOP_LEFT_RATIO = MyConstants.LINE_MAINSTAT_TOP_LEFT_RATIO
LINE_MAINSTAT_BOTTOM_RIGHT_RATIO = MyConstants.LINE_MAINSTAT_BOTTOM_RIGHT_RATIO
COLUMN_MAINSTAT_TOP_LEFT_RATIO = MyConstants.COLUMN_MAINSTAT_TOP_LEFT_RATIO
COLUMN_MAINSTAT_BOTTOM_RIGHT_RATIO = MyConstants.COLUMN_MAINSTAT_BOTTOM_RIGHT_RATIO

LINE_SUBSTATS_TOP_LEFT_RATIO = MyConstants.LINE_SUBSTATS_TOP_LEFT_RATIO
LINE_SUBSTATS_BOTTOM_RIGHT_RATIO = MyConstants.LINE_SUBSTATS_BOTTOM_RIGHT_RATIO
COLUMN_SUBSTATS_TOP_LEFT_RATIO = MyConstants.COLUMN_SUBSTATS_TOP_LEFT_RATIO
COLUMN_SUBSTATS_BOTTOM_RIGHT_RATIO = MyConstants.COLUMN_SUBSTATS_BOTTOM_RIGHT_RATIO

LINE_SET_TOP_LEFT_RATIO = MyConstants.LINE_SET_TOP_LEFT_RATIO
LINE_SET_BOTTOM_RIGHT_RATIO = MyConstants.LINE_SET_BOTTOM_RIGHT_RATIO
COLUMN_SET_TOP_LEFT_RATIO = MyConstants.COLUMN_SET_TOP_LEFT_RATIO
COLUMN_SET_BOTTOM_RIGHT_RATIO = MyConstants.COLUMN_SET_BOTTOM_RIGHT_RATIO

LINE_ARTIFACT_TOP_LEFT_RATIO = MyConstants.LINE_ARTIFACT_TOP_LEFT_RATIO
LINE_ARTIFACT_BOTTOM_RIGHT_RATIO = MyConstants.LINE_ARTIFACT_BOTTOM_RIGHT_RATIO
COLUMN_ARTIFACT_TOP_LEFT_RATIO = MyConstants.COLUMN_ARTIFACT_TOP_LEFT_RATIO
COLUMN_ARTIFACT_BOTTOM_RIGHT_RATIO = MyConstants.COLUMN_ARTIFACT_BOTTOM_RIGHT_RATIO

#  ███████ ██    ██ ███    ██  ██████ ████████ ██  ██████  ███    ██ ███████ 
#  ██      ██    ██ ████   ██ ██         ██    ██ ██    ██ ████   ██ ██      
#  █████   ██    ██ ██ ██  ██ ██         ██    ██ ██    ██ ██ ██  ██ ███████ 
#  ██      ██    ██ ██  ██ ██ ██         ██    ██ ██    ██ ██  ██ ██      ██ 
#  ██       ██████  ██   ████  ██████    ██    ██  ██████  ██   ████ ███████ 
#

#croping video and converting to .mp4: https://online-video-cutter.com/crop-video
#converting to mp4 : https://cloudconvert.com/mkv-to-mp4

#                           ____        _         _        _         _____                         _         _   _  __            _     ___                            
#     ___ _ __ ___  _ __   / ___| _   _| |__  ___| |_ __ _| |_ ___  |  ___| __ ___  _ __ ___      / \   _ __| |_(_)/ _| __ _  ___| |_  |_ _|_ __ ___   __ _  __ _  ___ 
#    / __| '__/ _ \| '_ \  \___ \| | | | '_ \/ __| __/ _` | __/ __| | |_ | '__/ _ \| '_ ` _ \    / _ \ | '__| __| | |_ / _` |/ __| __|  | || '_ ` _ \ / _` |/ _` |/ _ \
#   | (__| | | (_) | |_) |  ___) | |_| | |_) \__ \ || (_| | |_\__ \ |  _|| | | (_) | | | | | |  / ___ \| |  | |_| |  _| (_| | (__| |_   | || | | | | | (_| | (_| |  __/
#    \___|_|  \___/| .__/  |____/ \__,_|_.__/|___/\__\__,_|\__|___/ |_|  |_|  \___/|_| |_| |_| /_/   \_\_|   \__|_|_|  \__,_|\___|\__| |___|_| |_| |_|\__,_|\__, |\___|
#                  |_|                                                                                                                                      |___/      
def cropSubstatsFromArtifactImage(artifactImage: np.array, shape_height, shape_width) -> np.array:
    '''Getting temporary frame for OCR processing'''
    return artifactImage[int(LINE_SUBSTATS_TOP_LEFT_RATIO * shape_height):
                         int(LINE_SUBSTATS_BOTTOM_RIGHT_RATIO * shape_height),
                         int(COLUMN_SUBSTATS_TOP_LEFT_RATIO * shape_width):
                         int(COLUMN_SUBSTATS_BOTTOM_RIGHT_RATIO * shape_width)]

#               _        _         _   _  __            _     ____        _         _        _         ____                            _       
#     __ _  ___| |_     / \   _ __| |_(_)/ _| __ _  ___| |_  / ___| _   _| |__  ___| |_ __ _| |_ ___  / ___|  ___ ___ _ __   __ _ _ __(_) ___  
#    / _` |/ _ \ __|   / _ \ | '__| __| | |_ / _` |/ __| __| \___ \| | | | '_ \/ __| __/ _` | __/ __| \___ \ / __/ _ \ '_ \ / _` | '__| |/ _ \ 
#   | (_| |  __/ |_   / ___ \| |  | |_| |  _| (_| | (__| |_   ___) | |_| | |_) \__ \ || (_| | |_\__ \  ___) | (_|  __/ | | | (_| | |  | | (_) |
#    \__, |\___|\__| /_/   \_\_|   \__|_|_|  \__,_|\___|\__| |____/ \__,_|_.__/|___/\__\__,_|\__|___/ |____/ \___\___|_| |_|\__,_|_|  |_|\___/ 
#    |___/                                                                                                                                     

def getArtifactSubstatsScenario(artifact: Artifact) -> float:
    '''Getting a float as a "scenario" (which will be use to choose the shape of final image)
    Scenario = x.y
    x represent the number rolls possibilities
    y represent the Crit's substats configuration :
        • 0 => No Crit
        • 1 => Only Taux Crit %
        • 2 => Only DGT Crit %
        • 3 => Both of them'''
    Scenario = 0.0
    hasDGTCrit = "DGT CRIT %" in artifact.substats
    hasTauxCrit = "Taux CRIT %" in artifact.substats
    # RETURN Case 1 - There's crit
    rolls_list = [int(rolls) for rolls in artifact.dataFrame.loc[:,"Sum"] if (not np.isnan(rolls))]
    logging.debug(f"rolls_list: {rolls_list}")
    if 8 in rolls_list and 9 in rolls_list :
        if len(rolls_list) == 2:
            logging.info("There's two roll possibilities")
            if artifact.critValue == 0 :
                logging.info("There's no crit'stats on the artifact")
                Scenario = 2.0

            if hasDGTCrit and hasTauxCrit:
                logging.info("Taux CRIT % and DGT CRIT % substats are present in the artifact.")
                Scenario = 2.3

            elif hasDGTCrit and not hasTauxCrit:
                logging.info("Only the DGT CRIT % substat is present in the artifact.")
                Scenario = 2.2

            elif hasTauxCrit and not hasDGTCrit:
                logging.info("Only the Taux CRIT % substat is present in the artifact.")
                Scenario = 2.1
            
        else:
            logging.info("There's three roll possibilities")
            if artifact.critValue == 0 :
                logging.info("There's no crit'stats on the artifact")
                Scenario = 3.0

            if hasDGTCrit and hasTauxCrit:
                logging.info("Taux CRIT % and DGT CRIT % substats are present in the artifact.")
                Scenario = 3.3

            elif hasDGTCrit and not hasTauxCrit:
                logging.info("Only the DGT CRIT % substat is present in the artifact.")
                Scenario = 3.2

            elif hasTauxCrit and not hasDGTCrit:
                logging.info("Only the Taux CRIT % substat is present in the artifact.")
                Scenario = 3.1

    else :
        logging.info("There's only one roll possibility")
        if artifact.critValue == 0 :
                logging.info("There's no crit'stats on the artifact")
                Scenario = 1.0

        if hasDGTCrit and hasTauxCrit:
            logging.info("Taux CRIT % and DGT CRIT % substats are present in the artifact.")
            Scenario = 1.3

        elif hasDGTCrit and not hasTauxCrit:
                logging.info("Only the DGT CRIT % substat is present in the artifact.")
                Scenario = 1.2

        elif hasTauxCrit and not hasDGTCrit:
            logging.info("Only the Taux CRIT % substat is present in the artifact.")
            Scenario = 1.1

    logging.debug("Output of getArtifactSubstatsScenario - "\
                      f"Scenario: {Scenario}")
    return Scenario

if __name__ == '__main__':

    import matplotlib.pyplot as plt
    from matplotlib.gridspec import GridSpec
    import matplotlib.colors as mcolors
    import pandas
    import matplotlib

    #TODO - pas beau avec gridspec
    #TODO - faut voir https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
    #TODO - exemple ! https://www.youtube.com/watch?v=Tqph7_qMujk&ab_channel=BigPlot
    #TODO - example graph 'étalé' https://stackoverflow.com/questions/2265319/how-to-make-an-axes-occupy-multiple-subplots-with-pyplot


    Artest3 = MyClasses.Artifact("artifact_example_full_max_rolls",
                            "coupe",
                            ("def",59),
                            {"PV":508,
                            "PV %":21,
                            "ATQ %":4.1,
                            "Recharge d'énergie %":6.5},
                            "setName")
    
    artifactImage = plt.imread(IMAGES_PATH + FRAME_NAME + '381' + FRAME_FILE_EXTENSION)

    fig1 = plt.figure()
    fig1.set_facecolor("black")
    fig1.set_edgecolor("white")
    fig1.set_linewidth(2) # White edge of the image
    
    x = np.arange(0, 7, 0.01)
    
    image = plt.subplot(3,1,1)
    image.imshow(artifactImage)
    image.tick_params(bottom=False, left=False,labelbottom = False,  labelleft=False)
    image.set_xlabel("Crit value : "+ str(round(Artest3.critValue, 3)), color='white')
    print(image.get_position())
    left, bottom, width, height = image.get_position().bounds
    image.set_position((left, bottom, width*2, height*1.5))
    left, bottom, width, height = image.get_position().bounds
    print(image.get_position())

    plt.subplot(3, 1, 2)
    plt.plot(x, np.sin(x))
        
    plt.subplot(3, 2, 5)
    plt.plot(x, np.cos(x))
        
    plt.subplot(3, 2, 6)
    plt.plot(x, np.sin(x)*np.cos(x))

    plt.savefig('myfigtest_3.png', dpi = 200)
    plt.close()