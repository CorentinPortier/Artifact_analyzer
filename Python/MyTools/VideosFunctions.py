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
# To have a .py containing all the functions related to videos processing

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
import logging #https://docs.python.org/3/library/logging.html#module-logging
LOGGING_FORMAT = "%(asctime)s | %(levelname)s | line %(lineno)d : %(message)s"
LOGGING_DATEMFT = 'UTC%z | %d/%m/%Y | %H:%M:%S'
logging.basicConfig(level=logging.INFO, format=LOGGING_FORMAT, datefmt= LOGGING_DATEMFT)
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

THRESHOLD_IMAGE_DIFFERENCE_ARTIFACT = 0.25 #Above this threshold is considered as a new artifact
THRESHOLD_IMAGE_DIFFERENCE_SUBSTATS = 0.15 #Above this threshold is considered as a new artifact

FRAME_NAME = MyConstants.FRAME_NAME
IMAGE_FILE_EXTENSION = MyConstants.FRAME_FILE_EXTENSION

LINE_ARTIFACT_TOP_LEFT_RATIO = MyConstants.LINE_ARTIFACT_TOP_LEFT_RATIO
LINE_ARTIFACT_BOTTOM_RIGHT_RATIO = MyConstants.LINE_ARTIFACT_BOTTOM_RIGHT_RATIO
COLUMN_ARTIFACT_TOP_LEFT_RATIO = MyConstants.COLUMN_ARTIFACT_TOP_LEFT_RATIO
COLUMN_ARTIFACT_BOTTOM_RIGHT_RATIO = MyConstants.COLUMN_ARTIFACT_BOTTOM_RIGHT_RATIO

LINE_SUBSTATS_TOP_LEFT_RATIO = MyConstants.LINE_SUBSTATS_TOP_LEFT_RATIO
LINE_SUBSTATS_BOTTOM_RIGHT_RATIO = MyConstants.LINE_SUBSTATS_BOTTOM_RIGHT_RATIO
COLUMN_SUBSTATS_TOP_LEFT_RATIO = MyConstants.COLUMN_SUBSTATS_TOP_LEFT_RATIO
COLUMN_SUBSTATS_BOTTOM_RIGHT_RATIO = MyConstants.COLUMN_SUBSTATS_BOTTOM_RIGHT_RATIO

#  ███████ ██    ██ ███    ██  ██████ ████████ ██  ██████  ███    ██ ███████ 
#  ██      ██    ██ ████   ██ ██         ██    ██ ██    ██ ████   ██ ██      
#  █████   ██    ██ ██ ██  ██ ██         ██    ██ ██    ██ ██ ██  ██ ███████ 
#  ██      ██    ██ ██  ██ ██ ██         ██    ██ ██    ██ ██  ██ ██      ██ 
#  ██       ██████  ██   ████  ██████    ██    ██  ██████  ██   ████ ███████ 
#

#        _       __ _                    ____                    _ _             _              _____               _         _   _  __            _       
#     __| | ___ / _(_)_ __   ___  ___   / ___|___   ___  _ __ __| (_)_ __   __ _| |_ ___  ___  |  ___|__  _ __     / \   _ __| |_(_)/ _| __ _  ___| |_ ___ 
#    / _` |/ _ \ |_| | '_ \ / _ \/ __| | |   / _ \ / _ \| '__/ _` | | '_ \ / _` | __/ _ \/ __| | |_ / _ \| '__|   / _ \ | '__| __| | |_ / _` |/ __| __/ __|
#   | (_| |  __/  _| | | | |  __/\__ \ | |__| (_) | (_) | | | (_| | | | | | (_| | ||  __/\__ \ |  _| (_) | |     / ___ \| |  | |_| |  _| (_| | (__| |_\__ \
#    \__,_|\___|_| |_|_| |_|\___||___/  \____\___/ \___/|_|  \__,_|_|_| |_|\__,_|\__\___||___/ |_|  \___/|_|    /_/   \_\_|   \__|_|_|  \__,_|\___|\__|___/
#                                                                                                                                                          
def definesCoordinatesForArtifacts(shape_height: int, shape_width: int) -> list[int, int, int, int]:

    ArtifactFrame = []
    line_artifact_top_left_coordinate = 0
    line_artifact_bottom_right_coordinate = 0
    column_artifact_top_left_coordinate = 0
    column_artifact_bottom_right_coordinate = 0

    line_artifact_top_left_coordinate = int(LINE_ARTIFACT_TOP_LEFT_RATIO * shape_height)
    line_artifact_bottom_right_coordinate = int(LINE_ARTIFACT_BOTTOM_RIGHT_RATIO * shape_height)
    column_artifact_top_left_coordinate = int(COLUMN_ARTIFACT_TOP_LEFT_RATIO * shape_width)
    column_artifact_bottom_right_coordinate = int(COLUMN_ARTIFACT_BOTTOM_RIGHT_RATIO * shape_width)
    logging.debug(f"line_artifact_top_left_coordinate: {line_artifact_top_left_coordinate}")
    logging.debug(f"line_artifact_bottom_right_coordinate: {line_artifact_bottom_right_coordinate}")
    logging.debug(f"column_artifact_top_left_coordinate: {column_artifact_top_left_coordinate}")
    logging.debug(f"column_artifact_bottom_right_coordinate: {column_artifact_bottom_right_coordinate}")

    ArtifactFrame = [line_artifact_top_left_coordinate,
                line_artifact_bottom_right_coordinate,
                column_artifact_top_left_coordinate,
                column_artifact_bottom_right_coordinate]
    logging.debug(f"Before return - definesCoordinatesForArtifacts: {ArtifactFrame}")
    return ArtifactFrame

#        _       __ _                    ____                    _ _             _              _____            ____        _         _        _       
#     __| | ___ / _(_)_ __   ___  ___   / ___|___   ___  _ __ __| (_)_ __   __ _| |_ ___  ___  |  ___|__  _ __  / ___| _   _| |__  ___| |_ __ _| |_ ___ 
#    / _` |/ _ \ |_| | '_ \ / _ \/ __| | |   / _ \ / _ \| '__/ _` | | '_ \ / _` | __/ _ \/ __| | |_ / _ \| '__| \___ \| | | | '_ \/ __| __/ _` | __/ __|
#   | (_| |  __/  _| | | | |  __/\__ \ | |__| (_) | (_) | | | (_| | | | | | (_| | ||  __/\__ \ |  _| (_) | |     ___) | |_| | |_) \__ \ || (_| | |_\__ \
#    \__,_|\___|_| |_|_| |_|\___||___/  \____\___/ \___/|_|  \__,_|_|_| |_|\__,_|\__\___||___/ |_|  \___/|_|    |____/ \__,_|_.__/|___/\__\__,_|\__|___/
#                                                                                                                                                       
def definesCoordinatesForSubstats(shape_height: int, shape_width: int) -> list[int, int, int, int]:

    SubstatsFrame = []
    line_substats_top_left_coordinate = 0
    line_substats_bottom_right_coordinate = 0
    column_substats_top_left_coordinate = 0
    column_substats_bottom_right_coordinate = 0

    line_substats_top_left_coordinate = int(LINE_SUBSTATS_TOP_LEFT_RATIO * shape_height)
    line_substats_bottom_right_coordinate = int(LINE_SUBSTATS_BOTTOM_RIGHT_RATIO * shape_height)
    column_substats_top_left_coordinate = int(COLUMN_SUBSTATS_TOP_LEFT_RATIO * shape_width)
    column_substats_bottom_right_coordinate = int(COLUMN_SUBSTATS_BOTTOM_RIGHT_RATIO * shape_width)
    logging.debug(f"line_substats_top_left_coordinate: {line_substats_top_left_coordinate}")
    logging.debug(f"line_substats_bottom_right_coordinate: {line_substats_bottom_right_coordinate}")
    logging.debug(f"column_substats_top_left_coordinate: {column_substats_top_left_coordinate}")
    logging.debug(f"column_substats_bottom_right_coordinate: {column_substats_bottom_right_coordinate}")

    SubstatsFrame = [line_substats_top_left_coordinate,
                line_substats_bottom_right_coordinate,
                column_substats_top_left_coordinate,
                column_substats_bottom_right_coordinate]
    logging.debug(f"Before return - definesCoordinatesForSubstats: {SubstatsFrame}")
    return SubstatsFrame

#              _                  _     ____  _     _   _            _        _         _   _  __            _         _____                     __     ___     _            
#     _____  _| |_ _ __ __ _  ___| |_  |  _ \(_)___| |_(_)_ __   ___| |_     / \   _ __| |_(_)/ _| __ _  ___| |_ ___  |  ___| __ ___  _ __ ___   \ \   / (_) __| | ___  ___  
#    / _ \ \/ / __| '__/ _` |/ __| __| | | | | / __| __| | '_ \ / __| __|   / _ \ | '__| __| | |_ / _` |/ __| __/ __| | |_ | '__/ _ \| '_ ` _ \   \ \ / /| |/ _` |/ _ \/ _ \ 
#   |  __/>  <| |_| | | (_| | (__| |_  | |_| | \__ \ |_| | | | | (__| |_   / ___ \| |  | |_| |  _| (_| | (__| |_\__ \ |  _|| | | (_) | | | | | |   \ V / | | (_| |  __/ (_) |
#    \___/_/\_\\__|_|  \__,_|\___|\__| |____/|_|___/\__|_|_| |_|\___|\__| /_/   \_\_|   \__|_|_|  \__,_|\___|\__|___/ |_|  |_|  \___/|_| |_| |_|    \_/  |_|\__,_|\___|\___/ 
#                                                                                                                                                                            
def extractDistinctArtifactsFromVideo(videoName: str) -> None:
    video = cv2.VideoCapture(VIDEOS_PATH + videoName)
    nbrofframes = video.get(cv2.CAP_PROP_FRAME_COUNT)
    shape_height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
    shape_width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
    logging.info(f"nbrofframes: {nbrofframes}; "
                  f"shape_height:{shape_height}; "
                  f"shape_width : {shape_width}")
    
    line_artifact_top_left_coordinate,\
    line_artifact_bottom_right_coordinate,\
    column_artifact_top_left_coordinate,\
    column_artifact_bottom_right_coordinate = definesCoordinatesForArtifacts(shape_height,
                                                                             shape_width)
    line_substats_top_left_coordinate,\
    line_substats_bottom_right_coordinate,\
    column_substats_top_left_coordinate,\
    column_substats_bottom_right_coordinate = definesCoordinatesForSubstats(shape_height,
                                                                             shape_width)
    #INIT for the Loop
    number_of_artifact_extracted = 1
    frame_exist = True
    skip = False
    i=1
    frame_exist, frame1 = video.read()
    frame1 = np.array(frame1)

    artifact_extracted_from_image_1 = frame1[line_artifact_top_left_coordinate:
                                             line_artifact_bottom_right_coordinate,
                                             column_artifact_top_left_coordinate:
                                             column_artifact_bottom_right_coordinate]
    substats_extracted_from_image_1 = frame1[line_substats_top_left_coordinate:
                                             line_substats_bottom_right_coordinate,
                                             column_substats_top_left_coordinate:
                                             column_substats_bottom_right_coordinate]
    cv2.imwrite(os.path.join(IMAGES_PATH, FRAME_NAME+str(i)+IMAGE_FILE_EXTENSION), frame1)
    
    while frame_exist:
        frame_exist, frame2 = video.read()
        frame2 = np.array(frame2)
        i+=1
        logging.debug(f"frame_exist: {frame_exist}; i: {i}")
        if frame_exist :
            artifact_extracted_from_image_2 = frame2[line_artifact_top_left_coordinate:
                                             line_artifact_bottom_right_coordinate,
                                             column_artifact_top_left_coordinate:
                                             column_artifact_bottom_right_coordinate]
            substats_extracted_from_image_2 = frame2[line_substats_top_left_coordinate:
                                                    line_substats_bottom_right_coordinate,
                                                    column_substats_top_left_coordinate:
                                                    column_substats_bottom_right_coordinate]

            frame_difference_artifact = cv2.subtract(artifact_extracted_from_image_1, 
                                            artifact_extracted_from_image_2)
            b2, g2, r2 = cv2.split(frame_difference_artifact)
            logging.debug("Comparing artifacts image")
            artifact_mean = (cv2.countNonZero(r2)/(r2.shape[0]*r2.shape[1])
                + cv2.countNonZero(g2)/(g2.shape[0]*g2.shape[1])
                + cv2.countNonZero(b2)/(b2.shape[0]*b2.shape[1]))/3
            logging.debug(f"substats_mean: {artifact_mean}; "
                          f"Threshold: {THRESHOLD_IMAGE_DIFFERENCE_ARTIFACT}")
            if artifact_mean > THRESHOLD_IMAGE_DIFFERENCE_ARTIFACT :
                logging.info(f"It's a new artifact. Frame {i}")
                logging.debug(f"By artifact - artifact_mean: {artifact_mean}; "
                          f"Threshold: {THRESHOLD_IMAGE_DIFFERENCE_ARTIFACT}; "
                            f"i :{i}")
                cv2.imwrite(os.path.join(IMAGES_PATH, FRAME_NAME+str(i)+IMAGE_FILE_EXTENSION), frame2)
                number_of_artifact_extracted += 1
                skip = True
                logging.debug("skipping substat check")
                #cv2.imshow("artifact_extracted_from_image_2"+str(i),artifact_extracted_from_image_2)
            
            if not skip :
                frame_difference_substats = cv2.subtract(substats_extracted_from_image_1, 
                                                substats_extracted_from_image_2)
                b3, g3, r3 = cv2.split(frame_difference_substats)
                logging.debug("Comparing substats image")
                substats_mean = (cv2.countNonZero(r3)/(r3.shape[0]*r3.shape[1])
                    + cv2.countNonZero(g3)/(g3.shape[0]*g3.shape[1])
                    + cv2.countNonZero(b3)/(b3.shape[0]*b3.shape[1]))/3
                logging.debug(f"substats_mean: {substats_mean}; "
                            f"Threshold: {THRESHOLD_IMAGE_DIFFERENCE_SUBSTATS}")
                if substats_mean > THRESHOLD_IMAGE_DIFFERENCE_SUBSTATS :
                    logging.info(f"It's a new artifact. Frame {i}")
                    logging.debug(f"By substats - substats_mean: {substats_mean}; "
                            f"Threshold: {THRESHOLD_IMAGE_DIFFERENCE_SUBSTATS}; "
                            f"i :{i}")
                    cv2.imwrite(os.path.join(IMAGES_PATH, FRAME_NAME+str(i)+IMAGE_FILE_EXTENSION), frame2)
                    number_of_artifact_extracted += 1
                    #cv2.imshow("substats_extracted_from_image_2"+str(i),substats_extracted_from_image_2)
            
            frame1 = frame2.copy()
            artifact_extracted_from_image_1 = frame1[line_artifact_top_left_coordinate:
                                             line_artifact_bottom_right_coordinate,
                                             column_artifact_top_left_coordinate:
                                             column_artifact_bottom_right_coordinate]
            substats_extracted_from_image_1 = frame1[line_substats_top_left_coordinate:
                                                    line_substats_bottom_right_coordinate,
                                                    column_substats_top_left_coordinate:
                                                    column_substats_bottom_right_coordinate]

            skip = False
    logging.info("Last frame of the video was read")
    logging.info(f"Number of artifact(s) extracted: {number_of_artifact_extracted}")

if __name__ == '__main__':
    import time

    start = time.time()

    extractDistinctArtifactsFromVideo('TestingVideo.mp4')

    end = time.time()
    print(f"time elapsed: {end - start}")

    cv2.waitKey(0)
    cv2.destroyAllWindows()