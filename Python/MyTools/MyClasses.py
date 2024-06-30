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
# To have a .py containing all the classes that will be used for this project

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
import json

#    _____ _     _         _                    _         
#   |_   _| |__ (_)_ __ __| |  _ __   __ _ _ __| |_ _   _ 
#     | | | '_ \| | '__/ _` | | '_ \ / _` | '__| __| | | |
#     | | | | | | | | | (_| | | |_) | (_| | |  | |_| |_| |
#     |_| |_| |_|_|_|  \__,_| | .__/ \__,_|_|   \__|\__, |
#                             |_|                   |___/ 
import pandas
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


#   ██████  ██████  ███    ██ ███████ ████████  █████  ███    ██ ████████ ███████ 
#  ██      ██    ██ ████   ██ ██         ██    ██   ██ ████   ██    ██    ██      
#  ██      ██    ██ ██ ██  ██ ███████    ██    ███████ ██ ██  ██    ██    ███████ 
#  ██      ██    ██ ██  ██ ██      ██    ██    ██   ██ ██  ██ ██    ██         ██ 
#   ██████  ██████  ██   ████ ███████    ██    ██   ██ ██   ████    ██    ███████ 
#


#   ██████ ██       █████  ███████ ███████ ███████ ███████ 
#  ██      ██      ██   ██ ██      ██      ██      ██      
#  ██      ██      ███████ ███████ ███████ █████   ███████ 
#  ██      ██      ██   ██      ██      ██ ██           ██ 
#   ██████ ███████ ██   ██ ███████ ███████ ███████ ███████ 
#
#       _         _   _  __            _   
#      / \   _ __| |_(_)/ _| __ _  ___| |_ 
#     / _ \ | '__| __| | |_ / _` |/ __| __|
#    / ___ \| |  | |_| |  _| (_| | (__| |_ 
#   /_/   \_\_|   \__|_|_|  \__,_|\___|\__|
#                                          
class Artifact():
    def __init__(self, 
                 name: str, 
                 type: str, 
                 main_stat: tuple[str, float], 
                 substats: dict[str, float], 
                 set_name: str) -> None:
        logging.debug("") #print empty line for logs
        self.dataFrame = pandas.DataFrame() # Default value in case of issues
        self.critValue = 0 # Default value in case of issues
        self.critValueRates = {} # Default value in case of issues
        self.__meanRates__ = {} # Default value in case of issues
        self.__dataFrameWeightedRates__ = pandas.DataFrame() # Default value in case of issues
        self.__weightedMeanRates__ = {} # Default value in case of issues
        self.substatsRate = {} # Default value in case of issues

        self.name = name
        self.type = type
        self.mainStat = main_stat
        self.substats = substats
        self.set = set_name
        self.dataFrame = ArtifactsFunctions.getArtifactDataFrame(self)
        self.critValue = ArtifactsFunctions.getCritValue(self)
        self.critValueRates = ArtifactsFunctions.getCritValueRate(self)
        self.__meanRates__ = ArtifactsFunctions.getSubstatsRatingMean(self)
        self.__dataFrameWeightedRates__ = self.calculatesWeightedSubstatsRates()
        self.__weightedMeanRates__ = self.__getWeightedSubstatsRatingMean__()
        self.substatsRate = self.artifactSubstatsRate()
        
    def __getWeightedSubstatsRatingMean__(self):
        # RETURN Case 0 - no dataFrame (this should never happen) - returning the same
        temp_weightedMeanRates = self.__weightedMeanRates__
        logging.debug(f"__weightedMeanRates__: {self.__weightedMeanRates__}")
        if self.__dataFrameWeightedRates__.empty :
            logging.error(MyValueError.badSubstatValues)
            return temp_weightedMeanRates

        # RETURN Case 1 - 1,2 or 3 possibilites
        for row_index, row_content in self.__dataFrameWeightedRates__.iterrows():
            if "Weighted" in row_index:
                logging.debug(f"row_index: {row_index}\
                            \nrow_content: \n{row_content}")
                logging.debug(f"Mean of the row: {row_content.mean()}")
                temp_weightedMeanRates[row_index+" mean"] = row_content.mean()
        logging.debug(f"Before retun __getWeightedSubstatsRatingMean__: {temp_weightedMeanRates}")
        return temp_weightedMeanRates

    def __str__(self) -> str:
        return (f"\nArtifact :\n" 
                + (json.dumps(dict([("Artifact Name", self.name),
                                    ("Artifact Type", self.type),
                                    ("Artifact Set", self.set),
                                    ("Artifact Main stat",{self.mainStat[0]:self.mainStat[1]}),
                                    ("Artifact Substats",self.substats),]), 
                                    indent = 4, 
                                    ensure_ascii = False)) 
                + "\nArtifact DataFrame:\n" 
                + str(self.dataFrame)
                + "\nCrit value = " + str(self.critValue)
                + "\nCrit value rate = " + str(self.critValueRates)
                + "\nSubstats rating away from worst (%) = " + str(self.substatsRate))

    def calculatesWeightedSubstatsRates(self):
        logging.info("Getting the substat rates weighted by number of rolls")
        # RETURN Case 0 - no dataFrame (this should never happen) - returning the same
        if self.dataFrame.empty :
            logging.error("Dataframe is empty - exit")
            logging.error(MyValueError.badSubstatValues)
            return self.dataFrame
        # RETURN Case 1 - 1, 2 or 3 possibilites
        Artifact_Data_Frame = self.dataFrame.copy().drop(
            columns = ArtifactsFunctions.DATAFRAME_SUM_COLUMN_NAME)
        weighted_rate = pandas.DataFrame()
        for row_index, row_content in Artifact_Data_Frame.iterrows():
            if "rates" in row_index:
                logging.debug(f"row index: {row_index}")
                current_line_position = Artifact_Data_Frame.index.get_loc(row_index)
                logging.debug(f"current_line_position: {current_line_position}")
                line_above = pandas.Series(Artifact_Data_Frame.iloc[current_line_position-1])
                logging.debug(f"Rolls value = {line_above.values}")
                logging.debug(f"Rates value = {row_content.values}")
                weighted_rate = pandas.DataFrame((row_content*line_above).to_frame()).T
                weighted_rate = weighted_rate.rename(index={0 : "Weighted" + " " + row_index})
                Artifact_Data_Frame = pandas.concat([Artifact_Data_Frame[:current_line_position+1], 
                                                 weighted_rate,
                                                 Artifact_Data_Frame[current_line_position+1:]])
        logging.debug(f"Before retun calculatesWeightedSubstatsRates:\n{Artifact_Data_Frame}")
        return Artifact_Data_Frame
    
    def artifactSubstatsRate(self):
        logging.info("Getting the Artifact'substats rates for all rolls possibilities")
        # RETURN Case 0 - no dataFrame (this should never happen) - returning the same
        if self.dataFrame.empty :
            logging.error(MyValueError.badSubstatValues)
            return {}
        # RETURN Case 1 - get the rate ! (finally)
        temp_sum = 0
        SubstatRate = self.substatsRate
        for row_index, row_content in self.dataFrame.iterrows():
            if ("rolls" in row_index) or ("Rolls" in row_index):
                logging.debug(f"row_index: {row_index}")
                logging.debug(f"row_content:\n{row_content}")
                temp_sum = row_content[ArtifactsFunctions.DATAFRAME_SUM_COLUMN_NAME]
                logging.debug(f"temp_sum: {temp_sum}")
                temp_current_line_position = self.__dataFrameWeightedRates__.\
                    index.get_loc(row_index)
                logging.debug(f"temp_current_line_position: {temp_current_line_position}")
                temp_weighted_rate_line_name = pandas.Series(self.__dataFrameWeightedRates__.\
                                           iloc[temp_current_line_position+2]).name
                logging.debug(f"temp_weighted_rate_line_name: {temp_weighted_rate_line_name}")
                if temp_sum == 9 :
                    logging.debug(f"__weightedMeanRates__: {self.__weightedMeanRates__}")
                    logging.debug("__weightedMeanRates__[temp_weighted_rate_line_name]: "
                                  f"{self.__weightedMeanRates__[temp_weighted_rate_line_name+' mean']}")
                    SubstatRate[temp_weighted_rate_line_name + " normalized"] =\
                        self.__weightedMeanRates__[temp_weighted_rate_line_name+' mean']/\
                          ArtifactsFunctions.SUBSTAT_RATING_CONSTANT_VALUE_9_ROLLS
                    logging.debug(f"SubstatRate: {SubstatRate}")
                if temp_sum == 8 :
                    logging.debug(f"__weightedMeanRates__:{self.__weightedMeanRates__}")
                    logging.debug(f"__weightedMeanRates__[temp_weighted_rate_line_name]:\
                                  {self.__weightedMeanRates__[temp_weighted_rate_line_name+' mean']}")
                    SubstatRate[temp_weighted_rate_line_name + " normalized"] =\
                        self.__weightedMeanRates__[temp_weighted_rate_line_name+' mean']/\
                          ArtifactsFunctions.SUBSTAT_RATING_CONSTANT_VALUE_8_ROLLS
                    logging.debug(f"SubstatRate: {SubstatRate}")
        logging.debug(f"Before retun SubstatRate: {SubstatRate}")
        return SubstatRate

if __name__ == "__main__":

    from time import time
    start = time()

    Myarte = Artifact("artifact_3_rolls_possibilities_2crits_stats",
                          "coupe",
                          ("def",59),
                          {"DGT CRIT %":28,
                         "DÉF":23,
                         "PV":239,
                         "PV %":9.9},
                         "setName")
    Myarte2 = Artifact("artifact_3_rolls_possibilities_2crits_stats",
                          "coupe",
                          ("def",59),
                          {"Recharge d'énergie %":14.9,
                         "DGT CRIT %":10.9,
                         "DÉF":23,
                         "Taux CRIT %":9.3},
                         "setName")
    
    print(Myarte)
    print()
    print(Myarte2)
    print()

    '''
    Artest1 = Artifact("artifact_3_rolls_possibilities_2crits_stats",
                          "coupe",
                          ("def",59),
                          {"ATQ":18.5,
                         "Taux CRIT %":11.5,
                         "ATQ %":4.3,
                         "DGT CRIT %":22.7},
                         "setName")
    Artest11 = Artifact("artifact_3_rolls_possibilities_TC_stats",
                          "coupe",
                          ("def",59),
                          {"ATQ":18.5,
                         "Taux CRIT %":11.5,
                         "ATQ %":4.3,
                         "PV %":17},
                         "setName")
    Artest12 = Artifact("artifact_3_rolls_possibilities_DC_stats",
                          "coupe",
                          ("def",59),
                          {"ATQ":18.5,
                         "PV %":17,
                         "ATQ %":4.3,
                         "DGT CRIT %":22.7},
                         "setName")
    
    Artest2 = Artifact("artifact_2_rolls_possibilities_no_crit_substats",
                          "diadème",
                          ("DGT CRIT %",62.2),
                          {"PV":299,
                         "PV %":5.8,
                         "ATQ %":5.8,
                         "Recharge d'énergie %":30},
                         "setName")
    Artest21 = Artifact("artifact_2_rolls_possibilities_with_2crit_substats",
                          "diadème",
                          ("DGT CRIT %",62.2),
                          {"PV":299,
                         "PV %":5.8,
                         "DGT CRIT %":7.8,
                         "Taux CRIT %":18.5},
                         "setName")
    Artest22 = Artifact("artifact_2_rolls_possibilities_with_TC_substat",
                          "diadème",
                          ("DGT CRIT %",62.2),
                          {"PV":299,
                         "PV %":5.8,
                         "ATQ %":5.7,
                         "Taux CRIT %":18.5},
                         "setName")
    Artest23 = Artifact("artifact_2_rolls_possibilities_with_DC_substat",
                          "diadème",
                          ("DGT CRIT %",62.2),
                          {"PV":299,
                         "PV %":5.8,
                         "ATQ %":5.7,
                         "DGT CRIT %":35.2},
                         "setName")
    
    Artest3 = Artifact("artifact_example_full_max_rolls",
                          "coupe",
                          ("def",59),
                          {"ATQ %":5.8,
                         "Recharge d'énergie %":6.5,
                         "DGT CRIT %":7.8,
                         "Taux CRIT %":23.4},
                         "setName")
    Artest31 = Artifact("artifact_example_8_rolls",
                          "coupe",
                          ("def",59),
                          {"ATQ %":5.8,
                         "Recharge d'énergie %":6.5,
                         "DGT CRIT %":7.8,
                         "Taux CRIT %":16},
                         "setName")
    
    Artest4 = Artifact("artifact_verif",
                          "coupe",
                          ("def",59),
                          {"ATQ %":5.8,
                         "Recharge d'énergie %":6.5,
                         "DGT CRIT %":7.5,
                         "Taux CRIT %":22.3},
                         "setName")

    ArtifactsFunctions.getCritValueRate(Artest1)
    ArtifactsFunctions.getCritValueRate(Artest11)
    ArtifactsFunctions.getCritValueRate(Artest12)
    ArtifactsFunctions.getCritValueRate(Artest2) #OK
    ArtifactsFunctions.getCritValueRate(Artest21) #OK
    ArtifactsFunctions.getCritValueRate(Artest22) #OK
    ArtifactsFunctions.getCritValueRate(Artest23) #OK
    ArtifactsFunctions.getCritValueRate(Artest3) #OK
    ArtifactsFunctions.getCritValueRate(Artest31) #OK
    ArtifactsFunctions.getCritValueRate(Artest4) #OK
    '''
    end = time()
    print(f"time elapsed: {end - start}")