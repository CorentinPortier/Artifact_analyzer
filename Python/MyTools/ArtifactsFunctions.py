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
# To have a .py containing all the Functions that will be used for the Artifacts calculus

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
import itertools

#    _____ _     _         _                    _         
#   |_   _| |__ (_)_ __ __| |  _ __   __ _ _ __| |_ _   _ 
#     | | | '_ \| | '__/ _` | | '_ \ / _` | '__| __| | | |
#     | | | | | | | | | (_| | | |_) | (_| | |  | |_| |_| |
#     |_| |_| |_|_|_|  \__,_| | .__/ \__,_|_|   \__|\__, |
#                             |_|                   |___/ 
import pandas
from numpy import nan, isnan

#    _                    _ 
#   | |    ___   ___ __ _| |
#   | |   / _ \ / __/ _` | |
#   | |__| (_) | (_| (_| | |
#   |_____\___/ \___\__,_|_|
#                           
try:
    logging.info("trying 'import MyValueError'")
    import MyValueError
    logging.debug(f"{__name__} run as main ?")
except Exception as error:
    logging.debug(f"{__name__} was imported ? Error: {error}")
try:
    logging.info("trying 'from MyTools import MyValueError'")
    from MyTools import MyValueError
    logging.debug(f"{__name__} was imported")
except Exception :
    from re import search
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
    from MyTools.MyClasses import Artifact 

#   ██████  ██████  ███    ██ ███████ ████████  █████  ███    ██ ████████ ███████ 
#  ██      ██    ██ ████   ██ ██         ██    ██   ██ ████   ██    ██    ██      
#  ██      ██    ██ ██ ██  ██ ███████    ██    ███████ ██ ██  ██    ██    ███████ 
#  ██      ██    ██ ██  ██ ██      ██    ██    ██   ██ ██  ██ ██    ██         ██ 
#   ██████  ██████  ██   ████ ███████    ██    ██   ██ ██   ████    ██    ███████ 
#
CURRENT_PATH = MyConstants.CURRENT_PATH
MIN_MAX_ROLLS_PER_SUBSTATS = MyConstants.MIN_MAX_ROLLS_PER_SUBSTATS
NUMBER_MAX_OF_ROLLS = 9
NUMBER_MIN_OF_ROLLS = 8

PANDAS_DUPLICATE_COLUMN_NAME = ".1"
DATAFRAME_SUM_COLUMN_NAME = "Sum"
DATAFRAME_SUBSTATS_INDEX_NAME = "Substats"
DATAFRAME_MIN_ROLLS_INDEX_NAME = "Min rolls"
DATAFRAME_MAX_ROLLS_INDEX_NAME = "Max rolls"
DATAFRAME_SINGLE_ROLL_INDEX_NAME = "Rolls"
DATAFRAME_MULTIPLE_ROLLS_INDEX_NAME = "Rolls possility "
ROLLS_INDEX_NAME_LIST = [0,DATAFRAME_SINGLE_ROLL_INDEX_NAME,
                         (DATAFRAME_MIN_ROLLS_INDEX_NAME,
                          DATAFRAME_MAX_ROLLS_INDEX_NAME),
                         (DATAFRAME_MIN_ROLLS_INDEX_NAME,
                          DATAFRAME_MULTIPLE_ROLLS_INDEX_NAME+str(2),
                          DATAFRAME_MULTIPLE_ROLLS_INDEX_NAME+str(3))]
DATAFRAME_SUBSTATS_RATES_INDEX_NAME = "Substats rates "
NEW_LINE_INDEX_NAME = "New"
SUBSTAT_RATING_CONSTANT_VALUE_8_ROLLS = 2 #Believe me (or check in the excel if you don't)
SUBSTAT_RATING_CONSTANT_VALUE_9_ROLLS = 2.25 #Believe me (or check in the excel if you don't)

#  ███████ ██    ██ ███    ██  ██████ ████████ ██  ██████  ███    ██ ███████ 
#  ██      ██    ██ ████   ██ ██         ██    ██ ██    ██ ████   ██ ██      
#  █████   ██    ██ ██ ██  ██ ██         ██    ██ ██    ██ ██ ██  ██ ███████ 
#  ██      ██    ██ ██  ██ ██ ██         ██    ██ ██    ██ ██  ██ ██      ██ 
#  ██       ██████  ██   ████  ██████    ██    ██  ██████  ██   ████ ███████ 
#
#               _     ____       _ _   _     _            
#     __ _  ___| |_  |  _ \ ___ | | | | |   (_)_ __   ___ 
#    / _` |/ _ \ __| | |_) / _ \| | | | |   | | '_ \ / _ \
#   | (_| |  __/ |_  |  _ < (_) | | | | |___| | | | |  __/
#    \__, |\___|\__| |_| \_\___/|_|_| |_____|_|_| |_|\___|
#    |___/                                                
def getRollLine(substat: tuple[str, float]) -> tuple[str, tuple[int, int]]:
    '''Getting the minimum rolls and maximum rolls from a given substat name and value'''
    logging.info(f"Getting the minimum rolls and maximum rolls for substat {substat}")
    Roll_Line = 0
    Substat_Name = substat[0]
    substat_Value = substat[1]
    # DataFrame used to extract possible rolls from source for the substat currently check
    temporay_data_frame = pandas.DataFrame()

    # If substat Name isn't in source
    if Substat_Name not in MIN_MAX_ROLLS_PER_SUBSTATS.columns:
        logging.error(f"Quiting loop because substat_Name doesn't exist: {Substat_Name}")
        return None
    
    # Getting sub data frame only with the artifact'substat
    for index in MIN_MAX_ROLLS_PER_SUBSTATS.columns: 
        if Substat_Name in index:
            temporay_data_frame[index] = MIN_MAX_ROLLS_PER_SUBSTATS[index]
            logging.debug(f"temp_df:\n{temporay_data_frame}")
            if temporay_data_frame.shape[1] == 2:
                # Useless to go further, there're only 2 columns to get
                break 
    
    # Main loop, finding the roll line(s) of the substat
    for row_number, row_content in temporay_data_frame.iterrows():
        logging.debug(f"row_number = {row_number+1} - Checking if following is True: "
                    f"{row_content.iloc[0]} <= {substat_Value} <= {row_content.iloc[1]}: "
                    f"{row_content.iloc[0] <= substat_Value <= row_content.iloc[1]}")
        if round(row_content.iloc[0], 6) <= substat_Value <= round(row_content.iloc[1], 6):
            logging.debug(f"Roll_Line = {Roll_Line}")
            if Roll_Line != 0:
                Roll_Line = (Roll_Line, row_number+1)
                logging.debug(f"Quiting loop because can't have more than 2 lines."
                              f"Roll_Line = {Roll_Line}")
                # Useless to go further, can't have more than 2
                break
            else :
                Roll_Line = (row_number+1)
                logging.debug(f"Roll_Line = {Roll_Line}")
            if row_number+1 >= 3:
                logging.debug(f"Checking next row - row_number = {row_number+2}")
                continue
        elif Roll_Line != 0 :
            Roll_Line = (Roll_Line, Roll_Line)
            logging.debug(f"Quiting loop because row_number <=2. row_number = {row_number+1}")
            break # No issues when row_number <=2
        elif Roll_Line == 0 and row_content.iloc[0] > substat_Value:
            # This isn't possible
            logging.error(f"Quiting loop because substat_Value: {substat_Value} isn't possible "
                         f"for substat {Substat_Name}")
            return None
    
    logging.debug(f"row_number = {row_number+1} - Last line - Checking if following is True: "
                 f"{row_number+1} == 6 and {type(Roll_Line)} != tuple")
    if row_number+1 == 6 and type(Roll_Line) != tuple:
        if Roll_Line == 0 and row_content.iloc[1] < substat_Value :
            # This isn't possible
            logging.error(f"Quiting loop because substat_Value: {substat_Value} isn't possible"
                         f"for substat {Substat_Name}")
            return None
        else :
            Roll_Line = (Roll_Line, Roll_Line)
    logging.info("Output of getRollLine - (Substat_Name, Roll_Line): "\
                  f"{(Substat_Name, Roll_Line)}")
    return (Substat_Name, Roll_Line)

#               _               _                                          _ _           _       _         __                          
#     __ _  ___| |_   _ __ ___ (_)_ __    _ __ ___   __ ___  __  _ __ ___ | | |___    __| | __ _| |_ __ _ / _|_ __ __ _ _ __ ___   ___ 
#    / _` |/ _ \ __| | '_ ` _ \| | '_ \  | '_ ` _ \ / _` \ \/ / | '__/ _ \| | / __|  / _` |/ _` | __/ _` | |_| '__/ _` | '_ ` _ \ / _ \
#   | (_| |  __/ |_  | | | | | | | | | | | | | | | | (_| |>  <  | | | (_) | | \__ \ | (_| | (_| | || (_| |  _| | | (_| | | | | | |  __/
#    \__, |\___|\__| |_| |_| |_|_|_| |_| |_| |_| |_|\__,_/_/\_\ |_|  \___/|_|_|___/  \__,_|\__,_|\__\__,_|_| |_|  \__,_|_| |_| |_|\___|
#    |___/                                                                                                                             
def getMinMaxRollsDataFrame(substats: dict[str, float]) -> pandas.DataFrame:
    '''Getting the Artifact's base dataframe with min and max rolls possibilities'''
    logging.info("Getting the Artifact's base dataframe")
    Artifact_Data_Frame = pandas.DataFrame(index=[DATAFRAME_SUBSTATS_INDEX_NAME,
                                                   DATAFRAME_MIN_ROLLS_INDEX_NAME,
                                                   DATAFRAME_MAX_ROLLS_INDEX_NAME])

    #Creating Artifact Data Frame - min and max rolls
    for substat_name, substat_value in substats.items():
        logging.debug(f"checking substat_name: {substat_name}, substat: {substat_value}")
        # Create a column with substat_name as header. First row is substat_value, 
        # second and third are possible rolls of the substat
        try:
            min_roll, max_roll = getRollLine((substat_name, substat_value))[1]
        except :
            logging.error(MyValueError.badSubstatValues + "Returning empty dataFrame")
            return pandas.DataFrame()
        logging.debug(f"min_roll: {min_roll}, max_roll: {max_roll}")
        # If statement below to keep the substats in the same order of the inputed artifact
        if Artifact_Data_Frame.empty :
            Artifact_Data_Frame.insert(0, substat_name, [substat_value, min_roll, max_roll]) 
        else : 
            Artifact_Data_Frame[substat_name] = [substat_value, min_roll, max_roll]
        logging.debug("Output of getArtifactDataFrame - "\
                      f"Artifact_Data_Frame:\n{Artifact_Data_Frame}")
    return Artifact_Data_Frame

#               _     ____       _ _       ____               _ _     _ _ _ _   _           
#     __ _  ___| |_  |  _ \ ___ | | |___  |  _ \ ___  ___ ___(_) |__ (_) (_) |_(_) ___  ___ 
#    / _` |/ _ \ __| | |_) / _ \| | / __| | |_) / _ \/ __/ __| | '_ \| | | | __| |/ _ \/ __|
#   | (_| |  __/ |_  |  _ < (_) | | \__ \ |  __/ (_) \__ \__ \ | |_) | | | | |_| |  __/\__ \
#    \__, |\___|\__| |_| \_\___/|_|_|___/ |_|   \___/|___/___/_|_.__/|_|_|_|\__|_|\___||___/
#    |___/                                                                                  
def getRollsPossibilities(dataFrame: pandas.DataFrame) -> pandas.DataFrame:
    '''Adding Roll(s) possibilities on a new row(s)'''
    boolean_check_done = False
    # Getting total number of rolls for each lines
    check_min = dataFrame.loc[DATAFRAME_MIN_ROLLS_INDEX_NAME].sum()
    check_max = dataFrame.loc[DATAFRAME_MAX_ROLLS_INDEX_NAME].sum()
    # Case 1 - check_min == check_max
    logging.debug("RETURN Case 1 - Checking if following is True: "
                 f"check_min:{check_min} == check_max:{check_max}")
    if (check_min == check_max) and not boolean_check_done:
        # No need to go further - we can remove one of the line
        logging.debug(f"check_min:{check_min} == check_max:{check_max}")
        dataFrame = dataFrame.drop(DATAFRAME_MIN_ROLLS_INDEX_NAME)
        dataFrame = dataFrame.rename(index={DATAFRAME_MAX_ROLLS_INDEX_NAME: 
                                            DATAFRAME_SINGLE_ROLL_INDEX_NAME})
        boolean_check_done = True

    # Case 2 - check_min == NUMBER_MAX_OF_ROLLS
    logging.debug("RETURN Case 2 - Checking if following is True: "
                 f"check_min:{check_min} == NUMBER_MAX_OF_ROLLS:{NUMBER_MAX_OF_ROLLS}")
    if (check_min == NUMBER_MAX_OF_ROLLS) and not boolean_check_done:
        # No need to go further
        logging.debug(f"check_min:{check_min} == NUMBER_MAX_OF_ROLLS:{NUMBER_MAX_OF_ROLLS}")
        # removing impossibilities
        dataFrame = dataFrame.drop(DATAFRAME_MAX_ROLLS_INDEX_NAME)
        dataFrame = dataFrame.rename(index={DATAFRAME_MIN_ROLLS_INDEX_NAME: 
                                            DATAFRAME_SINGLE_ROLL_INDEX_NAME})
        boolean_check_done = True

    # Case 3 - check_min != check_max
    logging.debug("RETURN Case 3 - Checking if following is True: "
                 f"check_min:{check_min} != check_max:{check_max}")
    if (check_min != check_max) and not boolean_check_done:
        # Getting other rolls possibilities
        other_possibilities = set(x for x in 
                                  itertools.product(*zip(dataFrame.
                                                         loc[DATAFRAME_MIN_ROLLS_INDEX_NAME], 
                                                            dataFrame.
                                                            loc[DATAFRAME_MAX_ROLLS_INDEX_NAME])))
        logging.debug(f"other_possibilities:{other_possibilities}")
        # Removing what we have already
        other_possibilities.remove(tuple(dataFrame.loc[DATAFRAME_MIN_ROLLS_INDEX_NAME]))
        other_possibilities.remove(tuple(dataFrame.loc[DATAFRAME_MAX_ROLLS_INDEX_NAME]))
        logging.debug(f"other_possibilities:{other_possibilities}")
        # Adding the other possibilities in the table
        for i in range(len(other_possibilities)):
            logging.debug(f"i: {i}")
            iter_column_names = iter(dataFrame.columns)
            possibility = other_possibilities.pop()
            new_line = pandas.DataFrame({next(iter_column_names):possibility[0],
                                         next(iter_column_names):possibility[1],
                                         next(iter_column_names):possibility[2],
                                         next(iter_column_names):possibility[3]}, 
                                        index=[DATAFRAME_MULTIPLE_ROLLS_INDEX_NAME+str(i+2)])
            dataFrame = pandas.concat([dataFrame[:i+2], 
                                                 new_line, 
                                                 dataFrame[i+2:]])
            logging.debug(f"dataFrame:\n{dataFrame}")
        # removing impossibilities
        logging.info("Checking if following is True: "
                     f"check_max:{check_max} > NUMBER_MAX_OF_ROLLS:{NUMBER_MAX_OF_ROLLS}")
        if check_max > NUMBER_MAX_OF_ROLLS :
            logging.info("Removing 'Max_rolls' line")
            dataFrame = dataFrame.drop(DATAFRAME_MAX_ROLLS_INDEX_NAME)
        boolean_check_done = True
    return dataFrame

#              _            _       _               ____      _ _    __     __    _            
#     ___ __ _| | ___ _   _| | __ _| |_ ___  ___   / ___|_ __(_) |_  \ \   / /_ _| |_   _  ___ 
#    / __/ _` | |/ __| | | | |/ _` | __/ _ \/ __| | |   | '__| | __|  \ \ / / _` | | | | |/ _ \
#   | (_| (_| | | (__| |_| | | (_| | ||  __/\__ \ | |___| |  | | |_    \ V / (_| | | |_| |  __/
#    \___\__,_|_|\___|\__,_|_|\__,_|\__\___||___/  \____|_|  |_|\__|    \_/ \__,_|_|\__,_|\___|
#                                                                                              
def calculatesCritValue(artifactDataFrame: pandas.DataFrame) -> int:
    '''Calculate the Crit Value from artifact dataframe'''
    CritValue = 0
    if "DGT CRIT %" in artifactDataFrame.columns and "Taux CRIT %" in artifactDataFrame.columns:
        logging.info("Taux CRIT % and DGT CRIT % substats are present in the artifact.")
        CritValue = artifactDataFrame["DGT CRIT %"][DATAFRAME_SUBSTATS_INDEX_NAME]\
                    + 2 * artifactDataFrame["Taux CRIT %"][DATAFRAME_SUBSTATS_INDEX_NAME]
    elif "DGT CRIT %" in artifactDataFrame.columns :
        logging.info("Only the DGT CRIT % substat is present in the artifact.")
        CritValue = artifactDataFrame["DGT CRIT %"][DATAFRAME_SUBSTATS_INDEX_NAME]
    else :
        logging.info("Only the Taux CRIT % substat is present in the artifact.")
        CritValue = 2 * artifactDataFrame["Taux CRIT %"][DATAFRAME_SUBSTATS_INDEX_NAME]
    return CritValue
#               _      ____      _ _    __     __    _            
#     __ _  ___| |_   / ___|_ __(_) |_  \ \   / /_ _| |_   _  ___ 
#    / _` |/ _ \ __| | |   | '__| | __|  \ \ / / _` | | | | |/ _ \
#   | (_| |  __/ |_  | |___| |  | | |_    \ V / (_| | | |_| |  __/
#    \__, |\___|\__|  \____|_|  |_|\__|    \_/ \__,_|_|\__,_|\___|
#    |___/                                                        
def getCritValue(artifact: Artifact) -> int:
    '''Getting Crit Value of the artifact if possible'''
    CritValue = artifact.critValue
    logging.info("Checking if a 'Crit Value' could be added")
    logging.debug("RETURN Case 0 - Checking if following is True:"\
                 f"artifact.dataFrame.empty: {artifact.dataFrame.empty}")
    # RETURN Case 0 - no dataFrame (this should never happen) - returning the same
    if artifact.dataFrame.empty :
        logging.error(MyValueError.badSubstatValues)
        return CritValue

    # RETURN Case 1 - no Crit - returning the same
    no_crit_sub_stats = ("DGT CRIT %" not in artifact.dataFrame.columns 
                         and "Taux CRIT %" not in artifact.dataFrame.columns)
    logging.debug("RETURN Case 1 - Checking if following is True:"
                "'DGT CRIT %' not in artifact.dataFrame.columns:"
                f"{'DGT CRIT %' not in artifact.dataFrame.columns}"
                " and 'Taux CRIT %' not in artifact.dataFrame.columns:"
                f"{'Taux CRIT %' not in artifact.dataFrame.columns}:"
                f" {no_crit_sub_stats}")
    if no_crit_sub_stats:
        logging.info("There're no crits stats in the artifact.")
        return CritValue
    
    # RETURN Case 2 - One roll line 
    logging.info("RETURN Case 2 - There's at least one roll line.")
    # Since the crit value is the same for all roll lines, 
    # getting the first index without the 'Substats' one.
    CritValue = calculatesCritValue(artifact.dataFrame)
    return CritValue

#               _     _   _                            _ _             _ 
#     __ _  ___| |_  | \ | | ___  _ __ _ __ ___   __ _| (_)_______  __| |
#    / _` |/ _ \ __| |  \| |/ _ \| '__| '_ ` _ \ / _` | | |_  / _ \/ _` |
#   | (_| |  __/ |_  | |\  | (_) | |  | | | | | | (_| | | |/ /  __/ (_| |
#    \__, |\___|\__| |_| \_|\___/|_|  |_| |_| |_|\__,_|_|_/___\___|\__,_|
#    |___/                                                               
def getNormalized(substatValue: int | float, 
                  minValue: int | float, 
                  maxValue: int | float) -> float:
    '''Getting the normalized value of a substat - "% away from worst"'''
    SubstatValueNormalized = 0
    logging.debug("Checking if following is True: "
                     f"({maxValue} - {minValue}) <= 0 : {(maxValue - minValue) <= 0}")
    if (maxValue - minValue) <= 0:
        logging.error(f"minValue: {minValue} can't be lower than maxValue: {maxValue}")
        logging.error(MyValueError.incorrectInputedData)
        return SubstatValueNormalized
    logging.debug("Checking if following is True: "
                     f"({substatValue} - {minValue}) < 0 : {(substatValue - minValue) < 0}")
    if (substatValue - minValue) < 0:
        logging.error(f"substatValue: {substatValue} can't be lower than minValue: {minValue}")
        logging.error(MyValueError.incorrectInputedData)
        return SubstatValueNormalized
    SubstatValueNormalized = (substatValue - minValue)/(maxValue - minValue)
    logging.debug(f"Before Return - SubstatValueNormalized: {SubstatValueNormalized}")
    return SubstatValueNormalized

#               _     ____        _         _        _         ____       _   _             
#     __ _  ___| |_  / ___| _   _| |__  ___| |_ __ _| |_ ___  |  _ \ __ _| |_(_)_ __   __ _ 
#    / _` |/ _ \ __| \___ \| | | | '_ \/ __| __/ _` | __/ __| | |_) / _` | __| | '_ \ / _` |
#   | (_| |  __/ |_   ___) | |_| | |_) \__ \ || (_| | |_\__ \ |  _ < (_| | |_| | | | | (_| |
#    \__, |\___|\__| |____/ \__,_|_.__/|___/\__\__,_|\__|___/ |_| \_\__,_|\__|_|_| |_|\__, |
#    |___/                                                                            |___/ 
def getSubstatsRating(artifactDataFrame: pandas.DataFrame) -> pandas.DataFrame:
    '''Getting the normalized value of the substats in the
      artifact's dataframe - "% away from worst"'''
    df = artifactDataFrame.copy()
    iter_column_names = iter(df.columns)
    temp_new_lines = []
    new_line = pandas.DataFrame({next(iter_column_names):0,
                                 next(iter_column_names):0,
                                next(iter_column_names):0,
                                next(iter_column_names):0},
                                index=[NEW_LINE_INDEX_NAME])
    #Skipping first line as it is the substats themselves
    #Looping over rolls possibilities
    for i in range(1, len(df.index)):
        logging.debug(f"i: {i}")
        logging.debug(f"Line name: {df.iloc[i].name}")
        logging.debug(f"Line values: {df.iloc[i].values}")
        logging.debug(f"Line indexes: {df.iloc[i].index.values}")
        temp_new_line = new_line
        logging.debug(f"temp_new_line:\n{temp_new_line}")

        for substat in df.iloc[i].index.values:
            if substat == DATAFRAME_SUM_COLUMN_NAME:
                continue
            logging.debug(f"substat: {substat}")
            temp_localization_of_substat = MIN_MAX_ROLLS_PER_SUBSTATS.columns.get_loc(substat)
            logging.debug(f"temp_localization_of_substat: {temp_localization_of_substat}")
            # .iloc[numberOfrolls-1 (index starts at 0), substat position in source] for the below
            temp_new_line[substat] = getNormalized(df.iloc[0][substat],
                               MIN_MAX_ROLLS_PER_SUBSTATS.iloc[int(df.iloc[i][substat])-1,
                                                               temp_localization_of_substat],
                               MIN_MAX_ROLLS_PER_SUBSTATS.iloc[int(df.iloc[i][substat])-1,
                                                               temp_localization_of_substat+1])
            logging.debug(f"temp_new_line:\n{temp_new_line}")
        temp_new_line = temp_new_line.rename(index={NEW_LINE_INDEX_NAME:
                                                DATAFRAME_SUBSTATS_RATES_INDEX_NAME+
                                                str(i)})
        temp_new_lines.append((df.iloc[i].name, temp_new_line))
        logging.debug(f"temp_new_lines:\n{temp_new_lines}") 
    for newLine in temp_new_lines:
        logging.debug(f"newLine: {newLine}")
        logging.debug(f"Position of the line in current Dataframe: {df.index.get_loc(newLine[0])}")
        df = pandas.concat([df[:df.index.get_loc(newLine[0])+1],
                    newLine[1],
                    df[df.index.get_loc(newLine[0])+1:]])
    logging.debug(f"Before return - getSubstatsRating:\n{df}")
    return df

#               _     __  __ _         __  __               ____      _ _ __     __    _            
#     __ _  ___| |_  |  \/  (_)_ __   |  \/  | __ ___  __  / ___|_ __(_) |\ \   / /_ _| |_   _  ___ 
#    / _` |/ _ \ __| | |\/| | | '_ \  | |\/| |/ _` \ \/ / | |   | '__| | __\ \ / / _` | | | | |/ _ \
#   | (_| |  __/ |_  | |  | | | | | | | |  | | (_| |>  <  | |___| |  | | |_ \ V / (_| | | |_| |  __/
#    \__, |\___|\__| |_|  |_|_|_| |_| |_|  |_|\__,_/_/\_\  \____|_|  |_|\__| \_/ \__,_|_|\__,_|\___|
#    |___/                                                                                          
def getMinMaxCritValue(artifact: Artifact, rollsLineName: str) -> tuple[float, float]:
    logging.info("Taux CRIT % and DGT CRIT % substats are present in the artifact.")
    logging.debug(f"rollsLineName: {rollsLineName}")
    dgt_crit_rolls = artifact.dataFrame.loc[rollsLineName]["DGT CRIT %"]
    dgt_crit_min = MIN_MAX_ROLLS_PER_SUBSTATS.loc[
        dgt_crit_rolls -1]["DGT CRIT %"]
    dgt_crit_max = MIN_MAX_ROLLS_PER_SUBSTATS.loc[
        dgt_crit_rolls -1]["DGT CRIT %" + PANDAS_DUPLICATE_COLUMN_NAME]
    logging.debug(f"dgt_crit_rolls: {dgt_crit_rolls}")
    logging.debug(f"dgt_crit_min: {dgt_crit_min}")
    logging.debug(f"dgt_crit_max: {dgt_crit_max}")

    taux_crit_rolls = artifact.dataFrame.loc[rollsLineName]["Taux CRIT %"]
    taux_crit_min = MIN_MAX_ROLLS_PER_SUBSTATS.loc[
        taux_crit_rolls -1]["Taux CRIT %"]
    taux_crit_max = MIN_MAX_ROLLS_PER_SUBSTATS.loc[
        taux_crit_rolls -1]["Taux CRIT %" + PANDAS_DUPLICATE_COLUMN_NAME]
    logging.debug(f"taux_crit_rolls: {taux_crit_rolls}")
    logging.debug(f"taux_crit_min: {taux_crit_min}")
    logging.debug(f"taux_crit_max: {taux_crit_max}")

    min_crit_value = dgt_crit_min + 2 * taux_crit_min
    max_crit_value = dgt_crit_max + 2 * taux_crit_max

    logging.debug(f"Before return getMinMaxCritValue - "
                  f"min_crit_value: {min_crit_value}, max_crit_value: {max_crit_value}")
    return min_crit_value, max_crit_value 

#               _      ____      _ _ __     __    _              ____       _       
#     __ _  ___| |_   / ___|_ __(_) |\ \   / /_ _| |_   _  ___  |  _ \ __ _| |_ ___ 
#    / _` |/ _ \ __| | |   | '__| | __\ \ / / _` | | | | |/ _ \ | |_) / _` | __/ _ \
#   | (_| |  __/ |_  | |___| |  | | |_ \ V / (_| | | |_| |  __/ |  _ < (_| | ||  __/
#    \__, |\___|\__|  \____|_|  |_|\__| \_/ \__,_|_|\__,_|\___| |_| \_\__,_|\__\___|
#    |___/                                                                          
def getCritValueRate(artifact: Artifact) -> dict[int,float]:
        CritValueRates = artifact.critValueRates
        hasDGTCrit = "DGT CRIT %" in artifact.substats
        hasTauxCrit = "Taux CRIT %" in artifact.substats
        logging.debug(f"hasDGTCrit: {hasDGTCrit}")
        logging.debug(f"hasTauxCrit: {hasTauxCrit}")
        logging.debug(f"artifact.critValue: {artifact.critValue}")
        # RETURN Case 0 - No crit
        if artifact.critValue == 0 :
            logging.info("RETURN Case 0 - There's no crit'stats on the artifact")
            logging.debug("Output of getCritValueRate - "\
                      f"CritValueRates: {CritValueRates}")
            return CritValueRates
        
        # RETURN Case 1 - There's crit
        rolls_list = [int(rolls) for rolls in artifact.dataFrame.loc[:,"Sum"] if (not isnan(rolls))]
        logging.debug(f"rolls_list: {rolls_list}")
        if 8 in rolls_list and 9 in rolls_list :
            if len(rolls_list) == 2:
                logging.info("There's two roll possibilities")
                if hasDGTCrit and hasTauxCrit:
                    # Min roll
                    min_crit_value, max_crit_value = getMinMaxCritValue(artifact,
                                                                    ROLLS_INDEX_NAME_LIST[2][0])
                    CritValueRates[DATAFRAME_MIN_ROLLS_INDEX_NAME] = getNormalized(artifact.critValue,
                                                                min_crit_value,
                                                                max_crit_value)
                    # Max roll
                    min_crit_value, max_crit_value = getMinMaxCritValue(artifact,
                                                                        ROLLS_INDEX_NAME_LIST[2][1])
                    CritValueRates[DATAFRAME_MAX_ROLLS_INDEX_NAME] = getNormalized(artifact.critValue,
                                                                min_crit_value,
                                                                max_crit_value)
                elif hasDGTCrit and not hasTauxCrit:
                    logging.info("Only the DGT CRIT % substat is present in the artifact.")
                    CritValueRates[DATAFRAME_MIN_ROLLS_INDEX_NAME] = artifact.dataFrame.\
                        loc["Substats rates 1"]["DGT CRIT %"]
                    CritValueRates[DATAFRAME_MAX_ROLLS_INDEX_NAME] = artifact.dataFrame.\
                        loc["Substats rates 2"]["DGT CRIT %"]
                elif hasTauxCrit and not hasDGTCrit:
                    logging.info("Only the Taux CRIT % substat is present in the artifact.")
                    CritValueRates[DATAFRAME_MIN_ROLLS_INDEX_NAME] = artifact.dataFrame.\
                        loc["Substats rates 1"]["Taux CRIT %"]
                    CritValueRates[DATAFRAME_MAX_ROLLS_INDEX_NAME] = artifact.dataFrame.\
                        loc["Substats rates 2"]["Taux CRIT %"]
                
            else:
                logging.info("There's three roll possibilities")
                if hasDGTCrit and hasTauxCrit:
                    # Min roll
                    min_crit_value, max_crit_value = getMinMaxCritValue(artifact,
                                                                    ROLLS_INDEX_NAME_LIST[3][0])
                    CritValueRates[DATAFRAME_MIN_ROLLS_INDEX_NAME] = getNormalized(artifact.critValue,
                                                                min_crit_value,
                                                                max_crit_value)
                    # 2 Rolls possility
                    min_crit_value, max_crit_value = getMinMaxCritValue(artifact,
                                                                        ROLLS_INDEX_NAME_LIST[3][1])
                    CritValueRates[DATAFRAME_MULTIPLE_ROLLS_INDEX_NAME+str(2)] = getNormalized(artifact.critValue,
                                                                min_crit_value,
                                                                max_crit_value)
                    # 3 Rolls possility
                    min_crit_value, max_crit_value = getMinMaxCritValue(artifact,
                                                                        ROLLS_INDEX_NAME_LIST[3][2])
                    CritValueRates[DATAFRAME_MULTIPLE_ROLLS_INDEX_NAME+str(3)] = getNormalized(artifact.critValue,
                                                                min_crit_value,
                                                                max_crit_value)
                elif hasDGTCrit and not hasTauxCrit:
                    logging.info("Only the DGT CRIT % substat is present in the artifact.")
                    CritValueRates[DATAFRAME_MIN_ROLLS_INDEX_NAME] = artifact.dataFrame.\
                        loc["Substats rates 1"]["DGT CRIT %"]
                    CritValueRates[DATAFRAME_MULTIPLE_ROLLS_INDEX_NAME+str(2)] = artifact.dataFrame.\
                        loc["Substats rates 2"]["DGT CRIT %"]
                    CritValueRates[DATAFRAME_MULTIPLE_ROLLS_INDEX_NAME+str(3)] = artifact.dataFrame.\
                        loc["Substats rates 3"]["DGT CRIT %"]
                elif hasTauxCrit and not hasDGTCrit:
                    logging.info("Only the Taux CRIT % substat is present in the artifact.")
                    CritValueRates[DATAFRAME_MIN_ROLLS_INDEX_NAME] = artifact.dataFrame.\
                        loc["Substats rates 1"]["Taux CRIT %"]
                    CritValueRates[DATAFRAME_MULTIPLE_ROLLS_INDEX_NAME+str(2)] = artifact.dataFrame.\
                        loc["Substats rates 2"]["Taux CRIT %"]
                    CritValueRates[DATAFRAME_MULTIPLE_ROLLS_INDEX_NAME+str(3)] = artifact.dataFrame.\
                        loc["Substats rates 3"]["Taux CRIT %"]

        else :
            logging.info("There's only one roll possibility")
            if hasDGTCrit and hasTauxCrit:
                min_crit_value, max_crit_value = getMinMaxCritValue(artifact,
                                                                    ROLLS_INDEX_NAME_LIST[1])
                CritValueRates = {DATAFRAME_SINGLE_ROLL_INDEX_NAME :
                                  getNormalized(artifact.critValue, min_crit_value, max_crit_value)}
            elif hasDGTCrit and not hasTauxCrit:
                logging.info("Only the DGT CRIT % substat is present in the artifact.")
                CritValueRates = {DATAFRAME_SINGLE_ROLL_INDEX_NAME :
                                  artifact.dataFrame.loc["Substats rates 1"]["DGT CRIT %"]}
            elif hasTauxCrit and not hasDGTCrit:
                logging.info("Only the Taux CRIT % substat is present in the artifact.")
                CritValueRates = {DATAFRAME_SINGLE_ROLL_INDEX_NAME :
                                  artifact.dataFrame.loc["Substats rates 1"]["Taux CRIT %"]}

        logging.debug("Output of getCritValueRate - "\
                      f"CritValueRates: {CritValueRates}")
        return CritValueRates

#               _        _         _   _  __            _     ____        _        _____                         
#     __ _  ___| |_     / \   _ __| |_(_)/ _| __ _  ___| |_  |  _ \  __ _| |_ __ _|  ___| __ __ _ _ __ ___   ___ 
#    / _` |/ _ \ __|   / _ \ | '__| __| | |_ / _` |/ __| __| | | | |/ _` | __/ _` | |_ | '__/ _` | '_ ` _ \ / _ \
#   | (_| |  __/ |_   / ___ \| |  | |_| |  _| (_| | (__| |_  | |_| | (_| | || (_| |  _|| | | (_| | | | | | |  __/
#    \__, |\___|\__| /_/   \_\_|   \__|_|_|  \__,_|\___|\__| |____/ \__,_|\__\__,_|_|  |_|  \__,_|_| |_| |_|\___|
#    |___/                                                                                                       
def getArtifactDataFrame(artifact: Artifact) -> pandas.DataFrame:
    '''Getting the Artifact's dataframe'''
    logging.info(f"\nStarting new artifact's DataFrame - artifact name : {artifact.name}")
    Artifact_Data_Frame = artifact.dataFrame

    #Creating Artifact's base data Frame - min and max rolls
    Artifact_Data_Frame = getMinMaxRollsDataFrame(artifact.substats)
    logging.debug("Checking if following is True: "
                     f"Artifact_Data_Frame.empty : {Artifact_Data_Frame.empty}")
    if Artifact_Data_Frame.empty :
        logging.error("Artifact with given substats is impossible - quiting the function")
        return Artifact_Data_Frame

    # Adding Roll(s) possibilities on a new row(s)
    Artifact_Data_Frame = getRollsPossibilities(Artifact_Data_Frame)
   
    # Adding column "Sum"
    logging.info("Adding 'Sum' column")
    Artifact_Data_Frame[DATAFRAME_SUM_COLUMN_NAME] = Artifact_Data_Frame.sum(axis=1).\
        where((Artifact_Data_Frame.index != DATAFRAME_SUBSTATS_INDEX_NAME)&
              (Artifact_Data_Frame.index != DATAFRAME_SUBSTATS_RATES_INDEX_NAME + "1")&
              (Artifact_Data_Frame.index != DATAFRAME_SUBSTATS_RATES_INDEX_NAME + "2")&
              (Artifact_Data_Frame.index != DATAFRAME_SUBSTATS_RATES_INDEX_NAME + "3"), nan)
    
    # Quitting if impossible data were given :
    for sum in Artifact_Data_Frame[DATAFRAME_SUM_COLUMN_NAME].tolist():
        if sum > NUMBER_MAX_OF_ROLLS:
            # This isn't possible
            logging.error("Quiting loop because calculated number of rolls: "
                         f"{sum} is greater than NUMBER_MAX_OF_ROLLS: {NUMBER_MAX_OF_ROLLS}")
            logging.error(MyValueError.badSubstatValues)
            return pandas.DataFrame()

    # Adding '% away from worst' line(s)
    Artifact_Data_Frame = getSubstatsRating(Artifact_Data_Frame)

    logging.debug(f"Before Return - Artifact_Data_Frame:\n{Artifact_Data_Frame}")
    return Artifact_Data_Frame

#               _     ____        _         _        _         ____       _   _               __  __                  
#     __ _  ___| |_  / ___| _   _| |__  ___| |_ __ _| |_ ___  |  _ \ __ _| |_(_)_ __   __ _  |  \/  | ___  __ _ _ __  
#    / _` |/ _ \ __| \___ \| | | | '_ \/ __| __/ _` | __/ __| | |_) / _` | __| | '_ \ / _` | | |\/| |/ _ \/ _` | '_ \ 
#   | (_| |  __/ |_   ___) | |_| | |_) \__ \ || (_| | |_\__ \ |  _ < (_| | |_| | | | | (_| | | |  | |  __/ (_| | | | |
#    \__, |\___|\__| |____/ \__,_|_.__/|___/\__\__,_|\__|___/ |_| \_\__,_|\__|_|_| |_|\__, | |_|  |_|\___|\__,_|_| |_|
#    |___/                                                                            |___/                           
def getSubstatsRatingMean(artifact: Artifact) -> dict[str,float]:
    '''For all rolls possibilities, getting the mean Artifact's substats rates'''
    logging.info(f"Getting substatsRating's mean")
    Artifact_Data_Frame = artifact.dataFrame
    meanRates = artifact.__meanRates__
    logging.debug(f"meanRates: {meanRates}")
    # RETURN Case 0 - no dataFrame (this should never happen) - returning the same
    if Artifact_Data_Frame.empty :
        logging.error(MyValueError.badSubstatValues)
        return meanRates

    # RETURN Case 1 - 1,2 or 3 possibilites
    Artifact_Data_Frame = Artifact_Data_Frame.drop(columns="Sum")
    logging.debug(f"Artifact_Data_Frame: {Artifact_Data_Frame}")
    for row_index, row_content in Artifact_Data_Frame.iterrows():
        if "rates" in row_index:
            logging.debug(f"row_index: {row_index}\
                          \nrow_content: \n{row_content}")
            logging.debug(f"Mean of the row: {row_content.mean()}")
            meanRates[row_index + " mean"] = row_content.mean()
    logging.debug(f"Before retun getSubstatsRatingMean: {meanRates}")
    return meanRates
        
if __name__ == '__main__':
    print(MIN_MAX_ROLLS_PER_SUBSTATS)
    print(MIN_MAX_ROLLS_PER_SUBSTATS.loc[5]["DÉF"])
    print(MIN_MAX_ROLLS_PER_SUBSTATS.loc[5]["DÉF" + PANDAS_DUPLICATE_COLUMN_NAME])
    #loc["DÉF"]
    pass