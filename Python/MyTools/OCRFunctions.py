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
# To have a .py containing all the functions needed for OCR

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
logging.basicConfig(level=logging.DEBUG, format=LOGGING_FORMAT, datefmt= LOGGING_DATEMFT)
import os
import json
import re as regex

#    _____ _     _         _                    _         
#   |_   _| |__ (_)_ __ __| |  _ __   __ _ _ __| |_ _   _ 
#     | | | '_ \| | '__/ _` | | '_ \ / _` | '__| __| | | |
#     | | | | | | | | | (_| | | |_) | (_| | |  | |_| |_| |
#     |_| |_| |_|_|_|  \__,_| | .__/ \__,_|_|   \__|\__, |
#                             |_|                   |___/ 
import requests
import cv2

#    _                    _ 
#   | |    ___   ___ __ _| |
#   | |   / _ \ / __/ _` | |
#   | |__| (_) | (_| (_| | |
#   |_____\___/ \___\__,_|_|
#
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
    main_name = regex.search(pattern, __file__).group()
    logging.debug(f"{main_name} run as main")

try:
    logging.debug("Trying 'import ImagesFunctions'")
    import ImagesFunctions
    logging.debug(f"{__name__} run as main ?")
except ModuleNotFoundError as error:
    logging.debug(f"{__name__} was imported ? Error: {error}")
try:
    logging.debug("Trying 'from MyTools import ImagesFunctions'")
    from MyTools import ImagesFunctions
    logging.debug(f"{__name__} was imported")
except ModuleNotFoundError :
    pattern = "(?<=\\\)\w*\.py"
    from __main__ import __file__
    main_name = regex.search(pattern, __file__).group()
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
#https://pysource.com/2019/10/14/ocr-text-recognition-with-python-and-api-ocr-space/
#http://ocr.space/OCRAPI
CURRENT_PATH = MyConstants.CURRENT_PATH
logging.debug(f"CURRENT_PATH: {CURRENT_PATH}")
IMAGES_PATH = CURRENT_PATH + "/Python/Source/ArtifactsScreenshots/"
logging.debug(f"IMAGES_PATH: {IMAGES_PATH}")
logging.debug(f"Files in above Path : {os.listdir(IMAGES_PATH)}")
VIDEOS_PATH = CURRENT_PATH + "/Python/Source/Videos/"
logging.debug(f"VIDEOS_PATH: {VIDEOS_PATH}")
logging.debug(f"Files in above Path : {os.listdir(VIDEOS_PATH)}")
API_RESPONSE_PATH = CURRENT_PATH + "/Python/Source/APIResponses/"
logging.debug(f"API_RESPONSE_PATH: {API_RESPONSE_PATH}")
logging.debug(f"Files in above Path : {os.listdir(API_RESPONSE_PATH)}")

API_RESPONSE_FILENAME_SUBSTATS = MyConstants.API_RESPONSE_FILENAME_SUBSTATS
API_RESPONSE_EXTENSION = MyConstants.API_RESPONSE_EXTENSION
FRAME_FILE_EXTENSION = MyConstants.FRAME_FILE_EXTENSION
FRAME_NAME = MyConstants.FRAME_NAME
FRAME_SUBSTATS_NAME = MyConstants.FRAME_SUBSTATS_NAME
SUBSTATS_NAME_IN_SOURCE = MyConstants.SUBSTATS_NAME_IN_SOURCE

#  ███████ ██    ██ ███    ██  ██████ ████████ ██  ██████  ███    ██ ███████ 
#  ██      ██    ██ ████   ██ ██         ██    ██ ██    ██ ████   ██ ██      
#  █████   ██    ██ ██ ██  ██ ██         ██    ██ ██    ██ ██ ██  ██ ███████ 
#  ██      ██    ██ ██  ██ ██ ██         ██    ██ ██    ██ ██  ██ ██      ██ 
#  ██       ██████  ██   ████  ██████    ██    ██  ██████  ██   ████ ███████ 
#
#Below found in https://github.com/Zaargh/ocr.space_code_example/blob/master/ocrspace_example.py
#Modified a bit for my case - modified default language and added OCR engine choice 
#               _     _____         _     _____                      ___                             __        ___ _   _        ___   ____ ____       _    ____ ___ 
#     __ _  ___| |_  |_   _|____  _| |_  |  ___| __ ___  _ __ ___   |_ _|_ __ ___   __ _  __ _  ___  \ \      / (_) |_| |__    / _ \ / ___|  _ \     / \  |  _ \_ _|
#    / _` |/ _ \ __|   | |/ _ \ \/ / __| | |_ | '__/ _ \| '_ ` _ \   | || '_ ` _ \ / _` |/ _` |/ _ \  \ \ /\ / /| | __| '_ \  | | | | |   | |_) |   / _ \ | |_) | | 
#   | (_| |  __/ |_    | |  __/>  <| |_  |  _|| | | (_) | | | | | |  | || | | | | | (_| | (_| |  __/   \ V  V / | | |_| | | | | |_| | |___|  _ <   / ___ \|  __/| | 
#    \__, |\___|\__|   |_|\___/_/\_\\__| |_|  |_|  \___/|_| |_| |_| |___|_| |_| |_|\__,_|\__, |\___|    \_/\_/  |_|\__|_| |_|  \___/ \____|_| \_\ /_/   \_\_|  |___|
#    |___/                                                                               |___/                                                                      
def getTextFromImageWithOCRAPI(image_path: str,
                               overlay: bool = False, 
                               api_key: str ='helloworld', 
                               language: str ='eng')-> str:
    """OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'eng'.
    :return: Result in JSON format.
    :param OCREngine
    """
    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               'OCREngine': 2,
               }
    try:
        with open(image_path, 'rb') as f:
            response = requests.post('https://api.ocr.space/parse/image',
                            files={image_path: f},
                            data=payload,
                            )
    except FileNotFoundError as e :
        logging.fatal(f"There's no such file. Error raised:\n{e}")
        return None
    return response.content.decode()

#                              _                    ___   __    ___   ____ ____       _    ____ ___ 
#    ___  __ ___   _____      | |___  ___  _ __    / _ \ / _|  / _ \ / ___|  _ \     / \  |  _ \_ _|
#   / __|/ _` \ \ / / _ \  _  | / __|/ _ \| '_ \  | | | | |_  | | | | |   | |_) |   / _ \ | |_) | | 
#   \__ \ (_| |\ V /  __/ | |_| \__ \ (_) | | | | | |_| |  _| | |_| | |___|  _ <   / ___ \|  __/| | 
#   |___/\__,_| \_/ \___|  \___/|___/\___/|_| |_|  \___/|_|    \___/ \____|_| \_\ /_/   \_\_|  |___|
#                                                                                                   
def saveJsonOfOCRAPI(OCRAPI_response_path: str, my_image_path: str)-> bool:
    '''Function that return False if the file already exist,
    True if it saved the file sucessfully to the inputed path.
    It permits to not spam the OCR API with already done requests.'''
    if os.path.exists(OCRAPI_response_path):
        logging.info("Skipping the function - "
                     f"The following file already exist:\n{OCRAPI_response_path}")
        return False
    else :
        logging.info(f"The following file doesn't exist. Creating it:\n{OCRAPI_response_path}")
        with open(OCRAPI_response_path, 'w', encoding='utf-8') as f:
                result = getTextFromImageWithOCRAPI(my_image_path, 
                                                    api_key=os.environ["APIKEY_OCR"], 
                                                    language='fre')
                logging.debug(f"result: {result}")
                if result is not None:
                    f.write(result)
                else :
                    logging.fatal(f"Result of API is KO")
                    return None
        return True        

#               _     ____        _         _        _         _____                          _                 
#     __ _  ___| |_  / ___| _   _| |__  ___| |_ __ _| |_ ___  |  ___| __ ___  _ __ ___       | |___  ___  _ __  
#    / _` |/ _ \ __| \___ \| | | | '_ \/ __| __/ _` | __/ __| | |_ | '__/ _ \| '_ ` _ \   _  | / __|/ _ \| '_ \ 
#   | (_| |  __/ |_   ___) | |_| | |_) \__ \ || (_| | |_\__ \ |  _|| | | (_) | | | | | | | |_| \__ \ (_) | | | |
#    \__, |\___|\__| |____/ \__,_|_.__/|___/\__\__,_|\__|___/ |_|  |_|  \___/|_| |_| |_|  \___/|___/\___/|_| |_|
#    |___/                                                                                                      
def getSubstatsFromJson(json_OCRAPI_response_path: str) -> dict[str, float]:
    '''Function to extract substats from .json gotten by OCRAPI'''
    logging.info("Starting getSubstatsFromJson function")
    substat_name = ""
    substat_value = 0.0
    Artifact_Substats = {}
    with open(json_OCRAPI_response_path, encoding='utf8') as OCRAPI_json_file:
        OCRAPI_json = OCRAPI_json_file.read()
        try:
            OCRAPI_dictionnary = json.loads(OCRAPI_json)
        except json.decoder.JSONDecodeError as e :
            logging.fatal("Please check the json content. "
                          f"Removing the .json created. Error raised:\n{e}")
            return None
    #logging.debug(f"OCR API response json :\n{json.dumps(OCRAPI_dictionnary, indent=2, ensure_ascii=False)}")
    regex_pattern_substat_value = "(?<=\+)[^%]*"
    regex_pattern_substat_name = ".*(?=\+)"
    for line in OCRAPI_dictionnary["ParsedResults"][0]["TextOverlay"]["Lines"]:
        known_issue = False
        is_a_percent_substat = False
        logging.debug(f"Reading new line: {line['LineText']}")
        try:
            logging.debug("Is a string: "\
                          f"{regex.search(regex_pattern_substat_name, line['LineText']).group()}")
            substat_name = regex.search(regex_pattern_substat_name, line['LineText']).group()
        except Exception as e:
            logging.error(f"No regex match for value. Exception: {e}")
        try:
            logging.debug("Is a string: "\
                          f"{regex.search(regex_pattern_substat_value, line['LineText']).group()}")
            substat_value = float(regex.search(regex_pattern_substat_value, 
                              line["LineText"]).group().replace(",", "."))
            logging.debug(f"Is a float: {isinstance(substat_value, float)}")
            logging.debug(f"substat_value: {substat_value}")
        except Exception as e:
            logging.error(f"No regex match for value. Exception: {e}")
        
        if "%" in line['LineText']:
            logging.debug("It's a '%' substat")
            is_a_percent_substat = True
            Artifact_Substats[substat_name +" %"] = substat_value
        else:
            Artifact_Substats[substat_name] = substat_value
        
        # Cleaning .json from know OCR issues:
        #TODO - DEF au lieu de DÉF
        #TODO - Maitrise élémentaire au lieu de Maîtrise élémentaire (idem avec le e et é)
        # CASE - substat without '%'
        if (substat_name not in SUBSTATS_NAME_IN_SOURCE) and not is_a_percent_substat:
                logging.debug(f"'{substat_name}' isn't in source file. Checking if it's known issue")
                if 'ATO' in substat_name:
                    known_issue = True
                    logging.info(f"It is 'ATO' known issue")
                    newKey = substat_name.replace("O", "Q")
                    Artifact_Substats[newKey] = Artifact_Substats[substat_name]
                    logging.debug(f"Before del: {Artifact_Substats}")
                    del Artifact_Substats[substat_name]
                    logging.debug(f"After del: {Artifact_Substats}")
                if '•' in substat_name:
                    known_issue = True
                    logging.info(f"It is '•' known issue")
                    newKey = substat_name.replace('• ', "")
                    Artifact_Substats[newKey] = Artifact_Substats[substat_name]
                    logging.debug(f"Before del: {Artifact_Substats}")
                    del Artifact_Substats[substat_name]
                    logging.debug(f"After del: {Artifact_Substats}")

        # CASE - substat with '%'
        if (substat_name +" %" not in SUBSTATS_NAME_IN_SOURCE) and is_a_percent_substat:
                logging.debug(f"'{substat_name+' %'}' isn't in source file. Checking if it's known issue")
                if 'ATO' in substat_name:
                    known_issue = True
                    logging.info(f"It is 'ATO' known issue")
                    newKey = substat_name.replace("O", "Q")
                    Artifact_Substats[newKey +" %"] = Artifact_Substats[substat_name +" %"]
                    logging.debug(f"Before del: {Artifact_Substats}")
                    del Artifact_Substats[substat_name +" %"]
                    logging.debug(f"After del: {Artifact_Substats}")
                if '•' in substat_name:
                    known_issue = True
                    logging.info(f"It is '•' known issue")
                    newKey = substat_name.replace('• ', "")
                    Artifact_Substats[newKey +" %"] = Artifact_Substats[substat_name +" %"]
                    logging.debug(f"Before del: {Artifact_Substats}")
                    del Artifact_Substats[substat_name +" %"]
                    logging.debug(f"After del: {Artifact_Substats}")
                if not known_issue:
                    logging.error(f"I don't know this issue. substat_name: '{substat_name}'")
        logging.debug(f"Artifact_Substats: {Artifact_Substats}")
    logging.debug(f"Before return - getSubstatsFromJson:\n{Artifact_Substats}")
    return Artifact_Substats

#               _     ____        _         _        _         _____                          _                    ___   __    ___   ____ ____       _    ____ ___ 
#     __ _  ___| |_  / ___| _   _| |__  ___| |_ __ _| |_ ___  |  ___| __ ___  _ __ ___       | |___  ___  _ __    / _ \ / _|  / _ \ / ___|  _ \     / \  |  _ \_ _|
#    / _` |/ _ \ __| \___ \| | | | '_ \/ __| __/ _` | __/ __| | |_ | '__/ _ \| '_ ` _ \   _  | / __|/ _ \| '_ \  | | | | |_  | | | | |   | |_) |   / _ \ | |_) | | 
#   | (_| |  __/ |_   ___) | |_| | |_) \__ \ || (_| | |_\__ \ |  _|| | | (_) | | | | | | | |_| \__ \ (_) | | | | | |_| |  _| | |_| | |___|  _ <   / ___ \|  __/| | 
#    \__, |\___|\__| |____/ \__,_|_.__/|___/\__\__,_|\__|___/ |_|  |_|  \___/|_| |_| |_|  \___/|___/\___/|_| |_|  \___/|_|    \___/ \____|_| \_\ /_/   \_\_|  |___|
#    |___/                                                                                                                                                         
def getSubstatsFromJsonOfOCRAPI(json_OCRAPI_response_path: str, image_path: str)-> dict[str, float]:
    '''Function to extract substats from artifact'substats image'''
    logging.info("Starting getSubstatsFromJsonOfOCRAPI function")
    Artifact_Substats = {}
    saveJsonOfOCRAPI(json_OCRAPI_response_path, image_path)
    Artifact_Substats = getSubstatsFromJson(json_OCRAPI_response_path)
    logging.debug(f"Before return - getSubstatsFromJsonOfOCRAPI:\n{Artifact_Substats}")
    return Artifact_Substats

#               _     ____  _      _   _                                       ___   __   ____        _         _        _         _____               _    _ _      _         _   _  __            _     ___                                 
#     __ _  ___| |_  |  _ \(_) ___| |_(_) ___  _ __  _ __   __ _ _ __ _   _   / _ \ / _| / ___| _   _| |__  ___| |_ __ _| |_ ___  |  ___|__  _ __     / \  | | |    / \   _ __| |_(_)/ _| __ _  ___| |_  |_ _|_ __ ___   __ _  __ _  ___  ___ 
#    / _` |/ _ \ __| | | | | |/ __| __| |/ _ \| '_ \| '_ \ / _` | '__| | | | | | | | |_  \___ \| | | | '_ \/ __| __/ _` | __/ __| | |_ / _ \| '__|   / _ \ | | |   / _ \ | '__| __| | |_ / _` |/ __| __|  | || '_ ` _ \ / _` |/ _` |/ _ \/ __|
#   | (_| |  __/ |_  | |_| | | (__| |_| | (_) | | | | | | | (_| | |  | |_| | | |_| |  _|  ___) | |_| | |_) \__ \ || (_| | |_\__ \ |  _| (_) | |     / ___ \| | |  / ___ \| |  | |_| |  _| (_| | (__| |_   | || | | | | | (_| | (_| |  __/\__ \
#    \__, |\___|\__| |____/|_|\___|\__|_|\___/|_| |_|_| |_|\__,_|_|   \__, |  \___/|_|   |____/ \__,_|_.__/|___/\__\__,_|\__|___/ |_|  \___/|_|    /_/   \_\_|_| /_/   \_\_|   \__|_|_|  \__,_|\___|\__| |___|_| |_| |_|\__,_|\__, |\___||___/
#    |___/                                                            |___/                                                                                                                                                   |___/           
def getDictionnaryOfSubstatsForAllArtifactImages(images_path: str) -> dict[str, dict[str, float]]:
    '''Function to get a dictionnary containing all the substats from artifact'substats images'''
    substat_images_to_remove = []
    substatDict = {}
    
    #Creating temporary images for substats
    for imageName in os.listdir(images_path):
        if FRAME_NAME in imageName :
            logging.debug(f"imageName = {imageName}")
            artifactNumber = regex.search("[0-9]+", imageName).group()
            logging.debug(f"artifactNumber = {artifactNumber}")
            substat_image_name = FRAME_SUBSTATS_NAME \
                + artifactNumber \
                + FRAME_FILE_EXTENSION
            # No need to create if .json already exist in response_path = API_RESPONSE_PATH\
            response_path = API_RESPONSE_PATH\
                            + API_RESPONSE_FILENAME_SUBSTATS\
                            + "_" + artifactNumber\
                            + API_RESPONSE_EXTENSION
            if os.path.exists(response_path):
                logging.info("Skipping the image - "
                            f"The following file already exist:\n{response_path}")
                continue
            else:
                substat_images_to_remove.append(substat_image_name)
                logging.info(f"Creating the image '{substat_image_name}'")
                substat_image = cv2.imread(images_path + imageName)
                cv2.imwrite(os.path.join(images_path, substat_image_name),
                            ImagesFunctions.cropSubstatsFromArtifactImage(substat_image,
                                                                        substat_image.shape[0],
                                                                        substat_image.shape[1]))
    #Creating the .json with OCRAPI
    for imageName in os.listdir(images_path):
        logging.debug(f"imageName = {imageName}")
        if FRAME_SUBSTATS_NAME in imageName :
            artifactNumber = regex.search("[0-9]+", imageName).group()
            logging.debug(f"artifactNumber = {artifactNumber}")
            response_path = API_RESPONSE_PATH\
                            + API_RESPONSE_FILENAME_SUBSTATS\
                            + "_" + artifactNumber\
                            + API_RESPONSE_EXTENSION
            logging.debug(f"response_path = {response_path}")
            saveJsonOfOCRAPI(response_path, images_path + imageName)

    #Cleaning temporary image files
    for subtat_image in substat_images_to_remove:
        logging.info(f"Removing '{subtat_image}' from directory {images_path}")
        os.remove(images_path + subtat_image)
    
    #Creating the dict
    for jsonFile in os.listdir(API_RESPONSE_PATH):
        logging.debug(f"jsonFile = {jsonFile}")
        artifactNumber = regex.search("[0-9]+", jsonFile).group()
        logging.debug(f"artifactNumber = {artifactNumber}")
        substat_image_name = FRAME_SUBSTATS_NAME \
            + artifactNumber \
            + FRAME_FILE_EXTENSION
        substatDict[substat_image_name] = getSubstatsFromJson(API_RESPONSE_PATH + jsonFile)
    logging.debug(f"Before Return - getDictionnaryOfSubstatsForAllArtifactImages: {substatDict}")
    return substatDict

if __name__ == '__main__':

    from time import time
    start = time()
    
    substatDict = getDictionnaryOfSubstatsForAllArtifactImages(IMAGES_PATH)

    for artifactSubstatsImagename, artifactSubstats in substatDict.items():
        print(f"\n{artifactSubstatsImagename}")
        for substat, value in dict(artifactSubstats).items() :
            print(substat, value)

    print(substatDict)

    end = time()
    print(f"time elapsed: {end - start}")