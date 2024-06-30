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
# To have a .py containing all the <to complete>

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
logging.basicConfig(level=logging.FATAL, format=LOGGING_FORMAT, datefmt= LOGGING_DATEMFT)
import unittest
import os

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
import ArtifactsFunctions
import MyClasses
import MyConstants

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
CURRENT_PATH = MyConstants.CURRENT_PATH
MIN_MAX_ROLLS_PER_SUBSTATS = MyConstants.MIN_MAX_ROLLS_PER_SUBSTATS

#    ____        _         _        _       
#   / ___| _   _| |__  ___| |_ __ _| |_ ___ 
#   \___ \| | | | '_ \/ __| __/ _` | __/ __|
#    ___) | |_| | |_) \__ \ || (_| | |_\__ \
#   |____/ \__,_|_.__/|___/\__\__,_|\__|___/
#                                           
substat_name_not_in_source = ("Taux CRIT", 19)
substat_tuple_to_low = ("Taux CRIT %", 2)
substat_tuple_to_high = ("Taux CRIT %", 24)
substat_out_of_line_1and2 = ("Taux CRIT %", 4)
substat_out_of_line_2and3 = ("Taux CRIT %", 8)
substat_tuple_single_line1 = ("Taux CRIT %", 3)
substat_tuple_single_line2 = ("Taux CRIT %", 7)
substat_tuple_single_line3 = ("Taux CRIT %", 10)
substat_tuple_single_line4 = ("Taux CRIT %", 13)
substat_tuple_single_line5 = ("Taux CRIT %", 16)
substat_tuple_single_line6 = ("Taux CRIT %", 20)
substat_tuple_line3_and_4 = ("Taux CRIT %", 11)
substat_tuple_line4_and_5 = ("Taux CRIT %", 14)
substat_tuple_line5_and_6 = ("Taux CRIT %", 19)

#       _         _   _  __            _       
#      / \   _ __| |_(_)/ _| __ _  ___| |_ ___ 
#     / _ \ | '__| __| | |_ / _` |/ __| __/ __|
#    / ___ \| |  | |_| |  _| (_| | (__| |_\__ \
#   /_/   \_\_|   \__|_|_|  \__,_|\___|\__|___/
#                                              
artifact_CRandCD = MyClasses.Artifact("artifact_CRandCD",
                          "coupe",
                          ("DÉF",59),
                          {"Recharge d'énergie %":18.5,
                         "DGT CRIT %":10.9,
                         "DÉF":23,
                         "Taux CRIT %":11.5},
                         "setName")
artifact_onlyCR = MyClasses.Artifact("artifact_onlyCR",
                          "coupe",
                          ("DÉF",59),
                          {"Recharge d'énergie %":18.5,
                         "ATQ %":10.9,
                         "DÉF":23,
                         "Taux CRIT %":11.5},
                         "setName")
artifact_onlyCD = MyClasses.Artifact("artifact_onlyCD",
                          "coupe",
                          ("DÉF",59),
                          {"Recharge d'énergie %":18.5,
                         "DGT CRIT %":10.9,
                         "DÉF":23,
                         "ATQ %":16},
                         "setName")
artifact_to_much_rolls = MyClasses.Artifact("artifact_to_much_rolls",
                          "coupe",
                          ("DÉF",59),
                          {"Recharge d'énergie %":38,
                         "DGT CRIT %":14,
                         "DÉF":46,
                         "Taux CRIT %":7.4},
                         "setName")
artifact_impossible_non_existing_substat = MyClasses.Artifact(
    "artifact_impossible_non_existing_substat", "coupe", ("def",59),
                          {"Recharge d'énergie %":38,
                         "DGT CRIT %":14,
                         "DÉF":46,
                         "Taux CRIT %":8},
                         "setName")
artifact_noCrit = MyClasses.Artifact("artifact_noCrit",
                          "coupe",
                          ("DÉF",59),
                          {"PV":299,
                         "ATQ":38,
                         "ATQ %":20.0,
                         "DÉF %":7.3},
                         "setName")
artifact_1_roll_possibility_min = MyClasses.Artifact("artifact_example2",
                          "coupe",
                          ("def",59),
                          {"PV":299,
                         "ATQ":38,
                         "ATQ %":20.0,
                         "DÉF %":7.3},
                         "setName")
artifact_1_roll_possibility_max = MyClasses.Artifact("artifact_example_full_max_rolls",
                          "coupe",
                          ("def",59),
                          {"ATQ %":5.8,
                         "Recharge d'énergie %":6.5,
                         "DGT CRIT %":7.8,
                         "Taux CRIT %":23.3},
                         "setName")
artifact_2_rolls_possibilities = MyClasses.Artifact("artifact_2_rolls_possibilities",
                          "diadème",
                          ("DGT CRIT %",62.2),
                          {"PV":299,
                         "PV %":5.8,
                         "ATQ %":5.8,
                         "Recharge d'énergie %":30},
                         "setName")
artifact_3_rolls_possibilities = MyClasses.Artifact("artifact_3_rolls_possibilities",
                          "coupe",
                          ("def",59),
                          {"ATQ":18.5,
                         "DÉF":65,
                         "ATQ %":4.3,
                         "Maîtrise élémentaire":69},
                         "setName")

#    ____        _        _____                              
#   |  _ \  __ _| |_ __ _|  ___| __ __ _ _ __ ___   ___  ___ 
#   | | | |/ _` | __/ _` | |_ | '__/ _` | '_ ` _ \ / _ \/ __|
#   | |_| | (_| | || (_| |  _|| | | (_| | | | | | |  __/\__ \
#   |____/ \__,_|\__\__,_|_|  |_|  \__,_|_| |_| |_|\___||___/
df_1_roll_possibility_min_before_rolls = pandas.DataFrame(np.array([[299, 38, 20.0, 7.3], 
                                 [1, 2, 4, 1],
                                 [1, 2, 4, 1]]), 
                       index=["Substats", 
                              ArtifactsFunctions.DATAFRAME_MIN_ROLLS_INDEX_NAME,
                               ArtifactsFunctions.DATAFRAME_MAX_ROLLS_INDEX_NAME], 
                       columns=["PV","ATQ","ATQ %","DÉF %"])
df_1_roll_possibility_max_before_rolls = pandas.DataFrame(np.array([[5.8, 6.5, 7.8, 23.3], 
                                 [1, 1, 1, 6],
                                 [1, 1, 1, 6]]), 
                       index=["Substats",
                              ArtifactsFunctions.DATAFRAME_MIN_ROLLS_INDEX_NAME,
                              ArtifactsFunctions.DATAFRAME_MAX_ROLLS_INDEX_NAME], 
                       columns=["ATQ %","Recharge d'énergie %","DGT CRIT %","Taux CRIT %"])
df_2_roll_possibilities_before_rolls = pandas.DataFrame(np.array([[299, 5.8, 5.8, 30], 
                                 [1, 1, 1, 5],
                                 [1, 1, 1, 6]]),
                       index=["Substats",
                              ArtifactsFunctions.DATAFRAME_MIN_ROLLS_INDEX_NAME,
                              ArtifactsFunctions.DATAFRAME_MAX_ROLLS_INDEX_NAME], 
                       columns=["PV","PV %","ATQ %","Recharge d'énergie %"])
df_3_roll_possibilities_before_rolls = pandas.DataFrame(np.array([[18.5, 65, 4.3, 69], 
                                 [1, 3, 1, 3],
                                 [1, 4, 1, 4]]), 
                       index=["Substats",
                              ArtifactsFunctions.DATAFRAME_MIN_ROLLS_INDEX_NAME,
                              ArtifactsFunctions.DATAFRAME_MAX_ROLLS_INDEX_NAME], 
                       columns=["ATQ","DÉF","ATQ %","Maîtrise élémentaire"])
df_1_roll_possibility_min = pandas.DataFrame(np.array([[299, 38, 20.0, 7.3, np.NaN],
                                 [1, 2, 4, 1, 8],
                                 [(299 - 209) / (299 - 209),
                                  (38 - 27) / (39 - 27),
                                  (20.0 - 16.3) / (23.3 - 16.3),
                                  (7.3 - 5.1) / (7.3 - 5.1),
                                  np.NaN]]),
                       index=["Substats", "Rolls","Substats rates 1"], 
                       columns=["PV","ATQ","ATQ %","DÉF %","Sum"])                               
df_1_roll_possibility_max = pandas.DataFrame(np.array([[5.8, 6.5, 7.8, 23.3, np.NaN],
                                 [1, 1, 1, 6, 9],
                                 [(5.8 - 4.1) / (5.8 - 4.1),
                                  (6.5 - 4.5) / (6.5 - 4.5),
                                  (7.8 - 5.4) / (7.8 - 5.4),
                                  (23.3 - 16.3) / (23.3 - 16.3),
                                  np.NaN]]), 
                       index=["Substats", "Rolls","Substats rates 1"], 
                       columns=["ATQ %","Recharge d'énergie %","DGT CRIT %","Taux CRIT %","Sum"])
df_2_roll_possibilities = pandas.DataFrame(np.array([[299, 5.8, 5.8, 30, np.NaN], 
                                 [1, 1, 1, 5, 8],
                                 [(299 - 209) / (299 - 209),
                                  (5.8 - 4.1) / (5.8 - 4.1),
                                  (5.8 - 4.1) / (5.8 - 4.1),
                                  (30 - 22.7) / (32.4 - 22.7),
                                  np.NaN],
                                 [1, 1, 1, 6, 9],
                                 [(299 - 209) / (299 - 209),
                                  (5.8 - 4.1) / (5.8 - 4.1),
                                  (5.8 - 4.1) / (5.8 - 4.1),
                                  (30 - 27.2) / (38.9 - 27.2),
                                  np.NaN]]),
                       index=["Substats",
                              ArtifactsFunctions.DATAFRAME_MIN_ROLLS_INDEX_NAME,
                              "Substats rates 1", 
                              ArtifactsFunctions.DATAFRAME_MAX_ROLLS_INDEX_NAME,
                              "Substats rates 2"],
                       columns=["PV","PV %","ATQ %","Recharge d'énergie %","Sum"])
df_3_roll_possibilities = pandas.DataFrame(np.array([[18.5, 65.0, 4.3, 69.0, np.NaN], 
                                 [1, 3, 1, 3, 8],
                                 [(18.5 - 14) / (19 - 14),
                                  (65.0 - 49) / (69 - 49),
                                  (4.3 - 4.1) / (5.8 - 4.1),
                                  (69.0 - 49) / (70 - 49),
                                  np.NaN],
                                 [1, 3, 1, 4, 9],
                                 [(18.5 - 14) / (19 - 14),
                                  (65.0 - 49) / (69 - 49),
                                  (4.3 - 4.1) / (5.8 - 4.1),
                                  (69.0 - 65) / (93 - 65),
                                  np.NaN],
                                 [1, 4, 1, 3, 9],
                                 [(18.5 - 14) / (19 - 14),
                                  (65.0 - 65) / (93 - 65),
                                  (4.3 - 4.1) / (5.8 - 4.1),
                                  (69.0 - 49) / (70 - 49),
                                  np.NaN]]), 
                       index=["Substats",
                              ArtifactsFunctions.DATAFRAME_MIN_ROLLS_INDEX_NAME,
                              "Substats rates 1", "Rolls possility 2", 
                              "Substats rates 2", "Rolls possility 3","Substats rates 3"], 
                       columns=["ATQ","DÉF","ATQ %","Maîtrise élémentaire","Sum"])

#  ████████ ███████ ███████ ████████ ███████ 
#     ██    ██      ██         ██    ██      
#     ██    █████   ███████    ██    ███████ 
#     ██    ██           ██    ██         ██ 
#     ██    ███████ ███████    ██    ███████ 
#                                            
#               _     ____       _ _   _     _            
#     __ _  ___| |_  |  _ \ ___ | | | | |   (_)_ __   ___ 
#    / _` |/ _ \ __| | |_) / _ \| | | | |   | | '_ \ / _ \
#   | (_| |  __/ |_  |  _ < (_) | | | | |___| | | | |  __/
#    \__, |\___|\__| |_| \_\___/|_|_| |_____|_|_| |_|\___|
#    |___/                                                
class test_getRollLine(unittest.TestCase):
    def test_name_not_in_source(self):
        logging.info("test_name_not_in_source")
        self.assertEqual(ArtifactsFunctions.getRollLine(substat_name_not_in_source), None)
    def test_to_low(self):
        logging.info("test_to_low")
        self.assertEqual(ArtifactsFunctions.getRollLine(substat_tuple_to_low), None)
    def test_to_high(self):
        logging.info("test_to_high")
        self.assertEqual(ArtifactsFunctions.getRollLine(substat_tuple_to_high), None)
    def test_out_of_line_1and2(self):
        logging.info("test_out_of_line_1and2")
        self.assertEqual(ArtifactsFunctions.getRollLine(substat_out_of_line_1and2), None)
    def test_out_of_line_2and3(self):
        logging.info("test_out_of_line_2and3")
        self.assertEqual(ArtifactsFunctions.getRollLine(substat_out_of_line_2and3), None)
    def test_single_line1(self):
        logging.info("test_single_line1")
        self.assertEqual(ArtifactsFunctions.getRollLine(substat_tuple_single_line1), ("Taux CRIT %",(1, 1)))
    def test_single_line2(self):
        logging.info("test_single_line2")
        self.assertEqual(ArtifactsFunctions.getRollLine(substat_tuple_single_line2), ("Taux CRIT %",(2, 2)))
    def test_single_line3(self):
        logging.info("test_single_line3")
        self.assertEqual(ArtifactsFunctions.getRollLine(substat_tuple_single_line3), ("Taux CRIT %",(3, 3)))
    def test_single_line4(self):
        logging.info("test_single_line4")
        self.assertEqual(ArtifactsFunctions.getRollLine(substat_tuple_single_line4), ("Taux CRIT %",(4, 4)))
    def test_single_line5(self):
        logging.info("test_single_line5")
        self.assertEqual(ArtifactsFunctions.getRollLine(substat_tuple_single_line5), ("Taux CRIT %",(5, 5)))
    def test_single_line6(self):
        logging.info("test_single_line6")
        self.assertEqual(ArtifactsFunctions.getRollLine(substat_tuple_single_line6), ("Taux CRIT %",(6, 6)))
    def test_line3_and_4(self):
        logging.info("test_line3_and_4")
        self.assertEqual(ArtifactsFunctions.getRollLine(substat_tuple_line3_and_4), ("Taux CRIT %",(3, 4)))
    def test_line4_and_5(self):
        logging.info("test_line4_and_5")
        self.assertEqual(ArtifactsFunctions.getRollLine(substat_tuple_line4_and_5), ("Taux CRIT %",(4, 5)))
    def test_line5_and_6(self):
        logging.info("test_line5_and_6")
        self.assertEqual(ArtifactsFunctions.getRollLine(substat_tuple_line5_and_6), ("Taux CRIT %",(5, 6)))

#               _               _                                          _ _           _       _         __                          
#     __ _  ___| |_   _ __ ___ (_)_ __    _ __ ___   __ ___  __  _ __ ___ | | |___    __| | __ _| |_ __ _ / _|_ __ __ _ _ __ ___   ___ 
#    / _` |/ _ \ __| | '_ ` _ \| | '_ \  | '_ ` _ \ / _` \ \/ / | '__/ _ \| | / __|  / _` |/ _` | __/ _` | |_| '__/ _` | '_ ` _ \ / _ \
#   | (_| |  __/ |_  | | | | | | | | | | | | | | | | (_| |>  <  | | | (_) | | \__ \ | (_| | (_| | || (_| |  _| | | (_| | | | | | |  __/
#    \__, |\___|\__| |_| |_| |_|_|_| |_| |_| |_| |_|\__,_/_/\_\ |_|  \___/|_|_|___/  \__,_|\__,_|\__\__,_|_| |_|  \__,_|_| |_| |_|\___|
#    |___/                                                                                                                             
class test_getMinMaxRollsDataFrame(unittest.TestCase):
    def test_impossible_substats(self):
        logging.info("test_impossible_substats")
        pandas.testing.assert_frame_equal(ArtifactsFunctions.getMinMaxRollsDataFrame(
            artifact_impossible_non_existing_substat.substats),
            pandas.DataFrame(),
            check_dtype=False)
        self.assertTrue(ArtifactsFunctions.getMinMaxRollsDataFrame(
            artifact_impossible_non_existing_substat.substats).empty)
    def test_min_max_is_min(self):
        logging.info("test_min_max_is_min")
        pandas.testing.assert_frame_equal(ArtifactsFunctions.getMinMaxRollsDataFrame(
            artifact_1_roll_possibility_min.substats),
            df_1_roll_possibility_min_before_rolls,
            check_dtype=False)
        pandas.testing.assert_series_equal(
            ArtifactsFunctions.getMinMaxRollsDataFrame(
            artifact_1_roll_possibility_min.substats).loc[
                ArtifactsFunctions.DATAFRAME_MIN_ROLLS_INDEX_NAME],
            ArtifactsFunctions.getMinMaxRollsDataFrame(
            artifact_1_roll_possibility_min.substats).loc[
                ArtifactsFunctions.DATAFRAME_MAX_ROLLS_INDEX_NAME],
            check_names = False)
    def test_min_max_is_max(self):
        logging.info("test_min_max_is_max")
        pandas.testing.assert_frame_equal(ArtifactsFunctions.getMinMaxRollsDataFrame(
            artifact_1_roll_possibility_max.substats),
            df_1_roll_possibility_max_before_rolls,
            check_dtype=False)
        pandas.testing.assert_series_equal(
            ArtifactsFunctions.getMinMaxRollsDataFrame(
            artifact_1_roll_possibility_max.substats).loc[
                ArtifactsFunctions.DATAFRAME_MIN_ROLLS_INDEX_NAME],
            ArtifactsFunctions.getMinMaxRollsDataFrame(
            artifact_1_roll_possibility_max.substats).loc[
                ArtifactsFunctions.DATAFRAME_MAX_ROLLS_INDEX_NAME],
            check_names = False)
    def test_min_max_are_different(self):
        logging.info("test_min_max_are_different")
        pandas.testing.assert_frame_equal(ArtifactsFunctions.getMinMaxRollsDataFrame(
            artifact_3_rolls_possibilities.substats),
            df_3_roll_possibilities_before_rolls,
            check_dtype=False)

#               _     ____       _ _       ____               _ _     _ _ _ _   _           
#     __ _  ___| |_  |  _ \ ___ | | |___  |  _ \ ___  ___ ___(_) |__ (_) (_) |_(_) ___  ___ 
#    / _` |/ _ \ __| | |_) / _ \| | / __| | |_) / _ \/ __/ __| | '_ \| | | | __| |/ _ \/ __|
#   | (_| |  __/ |_  |  _ < (_) | | \__ \ |  __/ (_) \__ \__ \ | |_) | | | | |_| |  __/\__ \
#    \__, |\___|\__| |_| \_\___/|_|_|___/ |_|   \___/|___/___/_|_.__/|_|_|_|\__|_|\___||___/
#    |___/                                                                                  
class test_getRollsPossibilities(unittest.TestCase):
    def test_check_min_equal_check_max_with_min_rolls(self):
        logging.info("test_check_min_equal_check_max_with_min_rolls")
        min = df_1_roll_possibility_min_before_rolls.loc[
            ArtifactsFunctions.DATAFRAME_MIN_ROLLS_INDEX_NAME].sum()
        max = df_1_roll_possibility_min_before_rolls.loc[
            ArtifactsFunctions.DATAFRAME_MAX_ROLLS_INDEX_NAME].sum()
        artifact_1_roll_possibility_min.dataFrame.drop("Sum",axis=1,inplace=True)
        artifact_1_roll_possibility_min.dataFrame.drop(index=["Substats rates 1"],inplace=True)
        logging.debug(f"min: {min}, max: {max}")
        pandas.testing.assert_frame_equal(ArtifactsFunctions.getRollsPossibilities(
            df_1_roll_possibility_min_before_rolls),
            artifact_1_roll_possibility_min.dataFrame,
            check_dtype=False)
    def test_check_min_equal_check_max_with_max_rolls(self):
        logging.info("test_check_min_equal_check_max_with_max_rolls")
        min = df_1_roll_possibility_max_before_rolls.loc[
            ArtifactsFunctions.DATAFRAME_MIN_ROLLS_INDEX_NAME].sum()
        max = df_1_roll_possibility_max_before_rolls.loc[
            ArtifactsFunctions.DATAFRAME_MAX_ROLLS_INDEX_NAME].sum()
        artifact_1_roll_possibility_max.dataFrame.drop("Sum",axis=1,inplace=True)
        artifact_1_roll_possibility_max.dataFrame.drop(index=["Substats rates 1"],inplace=True)
        logging.debug(f"min: {min}, max: {max}")
        pandas.testing.assert_frame_equal(ArtifactsFunctions.getRollsPossibilities(
            df_1_roll_possibility_max_before_rolls),
            artifact_1_roll_possibility_max.dataFrame,
            check_dtype=False)
    def test_check_min_equal_number_max(self):
        logging.info("test_check_min_equal_number_max")
        min = df_3_roll_possibilities_before_rolls.loc[
            ArtifactsFunctions.DATAFRAME_MIN_ROLLS_INDEX_NAME].sum()
        max = df_3_roll_possibilities_before_rolls.loc[
            ArtifactsFunctions.DATAFRAME_MAX_ROLLS_INDEX_NAME].sum()
        artifact_3_rolls_possibilities.dataFrame.drop("Sum",axis=1,inplace=True)
        artifact_3_rolls_possibilities.dataFrame.drop(index=["Substats rates 1",
                                                           "Substats rates 2",
                                                           "Substats rates 3"],inplace=True)
        logging.debug(f"min: {min}, max: {max}")
        pandas.testing.assert_frame_equal(ArtifactsFunctions.getRollsPossibilities(
            df_3_roll_possibilities_before_rolls),
            artifact_3_rolls_possibilities.dataFrame,
            check_dtype=False)
    def test_check_min_different_check_max(self):
        logging.info("test_check_min_different_check_max")
        min = df_2_roll_possibilities_before_rolls.loc[
            ArtifactsFunctions.DATAFRAME_MIN_ROLLS_INDEX_NAME].sum()
        max = df_2_roll_possibilities_before_rolls.loc[
            ArtifactsFunctions.DATAFRAME_MAX_ROLLS_INDEX_NAME].sum()
        artifact_2_rolls_possibilities.dataFrame.drop("Sum",axis=1,inplace=True)
        artifact_2_rolls_possibilities.dataFrame.drop(index=["Substats rates 1",
                                                           "Substats rates 2"],inplace=True)
        logging.debug(f"min: {min}, max: {max}")
        pandas.testing.assert_frame_equal(ArtifactsFunctions.getRollsPossibilities(
            df_2_roll_possibilities_before_rolls),
            artifact_2_rolls_possibilities.dataFrame,
            check_dtype=False)

#              _            _       _               ____      _ _    __     __    _            
#     ___ __ _| | ___ _   _| | __ _| |_ ___  ___   / ___|_ __(_) |_  \ \   / /_ _| |_   _  ___ 
#    / __/ _` | |/ __| | | | |/ _` | __/ _ \/ __| | |   | '__| | __|  \ \ / / _` | | | | |/ _ \
#   | (_| (_| | | (__| |_| | | (_| | ||  __/\__ \ | |___| |  | | |_    \ V / (_| | | |_| |  __/
#    \___\__,_|_|\___|\__,_|_|\__,_|\__\___||___/  \____|_|  |_|\__|    \_/ \__,_|_|\__,_|\___|
#                                                                                              
class test_calculatesCritValue(unittest.TestCase):
    def test_2CritSubstats(self):
        logging.info("test_2CritSubstats")
        self.assertEqual(ArtifactsFunctions.calculatesCritValue(artifact_CRandCD.dataFrame), 33.9)
    def test_onlyCR(self):
        logging.info("test_onlyCR")
        self.assertEqual(ArtifactsFunctions.calculatesCritValue(artifact_onlyCR.dataFrame), 23)
    def test_onlyCD(self):
        logging.info("test_onlyCD")
        self.assertEqual(ArtifactsFunctions.calculatesCritValue(artifact_onlyCD.dataFrame), 10.9)

#               _      ____      _ _    __     __    _            
#     __ _  ___| |_   / ___|_ __(_) |_  \ \   / /_ _| |_   _  ___ 
#    / _` |/ _ \ __| | |   | '__| | __|  \ \ / / _` | | | | |/ _ \
#   | (_| |  __/ |_  | |___| |  | | |_    \ V / (_| | | |_| |  __/
#    \__, |\___|\__|  \____|_|  |_|\__|    \_/ \__,_|_|\__,_|\___|
#    |___/                                                        
class test_getCritValue(unittest.TestCase):
    def test_noDataFrame(self):
        logging.info("test_noDataFrame")
        self.assertEqual(ArtifactsFunctions.getCritValue(artifact_to_much_rolls), 0)
    def test_noCrit(self):
        logging.info("test_noCrit")
        self.assertEqual(ArtifactsFunctions.getCritValue(artifact_noCrit), 0)
    def test_2CritSubstats(self):
        logging.info("test_2CritSubstats")
        self.assertEqual(ArtifactsFunctions.getCritValue(artifact_CRandCD), 33.9)
    def test_onlyCR(self):
        logging.info("test_onlyCR")
        self.assertEqual(ArtifactsFunctions.getCritValue(artifact_onlyCR), 23)
    def test_onlyCD(self):
        logging.info("test_onlyCD")
        self.assertEqual(ArtifactsFunctions.getCritValue(artifact_onlyCD), 10.9)

#               _     _   _                            _ _             _ 
#     __ _  ___| |_  | \ | | ___  _ __ _ __ ___   __ _| (_)_______  __| |
#    / _` |/ _ \ __| |  \| |/ _ \| '__| '_ ` _ \ / _` | | |_  / _ \/ _` |
#   | (_| |  __/ |_  | |\  | (_) | |  | | | | | | (_| | | |/ /  __/ (_| |
#    \__, |\___|\__| |_| \_|\___/|_|  |_| |_| |_|\__,_|_|_/___\___|\__,_|
#    |___/                                                               
from secrets import SystemRandom
randomizer = SystemRandom()
class test_getNormalized(unittest.TestCase):
    def test_denominator_lower_than_0(self):
        logging.info("test_denominator_lower_than_0")
        self.assertEqual(ArtifactsFunctions.getNormalized(randomizer.uniform(2.7, 1794),20,10), 0)
    def test_numerator_lower_than_0(self):
        logging.info("test_numerator_lower_than_0")
        self.assertEqual(ArtifactsFunctions.getNormalized(2,10,20), 0)
    def test_max_roll(self):
        logging.info("test_max_roll")
        self.assertEqual(ArtifactsFunctions.getNormalized(23,16,23), 1)
    def test_min_roll(self):
        logging.info("test_min_roll")
        self.assertEqual(ArtifactsFunctions.getNormalized(16,16,23), 0)
    def test_normal_roll(self):
        logging.info("test_normal_roll")
        self.assertEqual(ArtifactsFunctions.getNormalized(10.9,10.8,15.6), (10.9 - 10.8) / (15.6 - 10.8))

#               _     ____        _         _        _         ____       _   _             
#     __ _  ___| |_  / ___| _   _| |__  ___| |_ __ _| |_ ___  |  _ \ __ _| |_(_)_ __   __ _ 
#    / _` |/ _ \ __| \___ \| | | | '_ \/ __| __/ _` | __/ __| | |_) / _` | __| | '_ \ / _` |
#   | (_| |  __/ |_   ___) | |_| | |_) \__ \ || (_| | |_\__ \ |  _ < (_| | |_| | | | | (_| |
#    \__, |\___|\__| |____/ \__,_|_.__/|___/\__\__,_|\__|___/ |_| \_\__,_|\__|_|_| |_|\__, |
#    |___/                                                                            |___/ 
class test_getSubstatsRating(unittest.TestCase):
    def test_1_roll_possibility(self):
        logging.info("test_1_roll_possibility")
        artifact_1_roll_possibility_min = MyClasses.Artifact("artifact_1_roll_possibility_min",
                          "coupe",
                          ("def",59),
                          {"PV":299,
                         "ATQ":38,
                         "ATQ %":20.0,
                         "DÉF %":7.3},
                         "setName")
        artifact_1_roll_possibility_min.dataFrame.drop(index=["Substats rates 1"],inplace=True)
        pandas.testing.assert_frame_equal(ArtifactsFunctions.getSubstatsRating(
            artifact_1_roll_possibility_min.dataFrame),
            df_1_roll_possibility_min,
            check_dtype=False)
    def test_2_roll_possibilities(self):
        logging.info("test_2_roll_possibilities")
        artifact_2_rolls_possibilities = MyClasses.Artifact("artifact_2_rolls_possibilities",
                          "diadème",
                          ("DGT CRIT %",62.2),
                          {"PV":299,
                         "PV %":5.8,
                         "ATQ %":5.8,
                         "Recharge d'énergie %":30},
                         "setName")
        artifact_2_rolls_possibilities.dataFrame.drop(index=["Substats rates 1",
                                                           "Substats rates 2"],inplace=True)
        pandas.testing.assert_frame_equal(ArtifactsFunctions.getSubstatsRating(
            artifact_2_rolls_possibilities.dataFrame),
            df_2_roll_possibilities,
            check_dtype=False)
    def test_3_roll_possibilities(self):
        logging.info("test_3_roll_possibilities")
        artifact_3_rolls_possibilities = MyClasses.Artifact("artifact_3_rolls_possibilities",
                          "coupe",
                          ("def",59),
                          {"ATQ":18.5,
                         "DÉF":65,
                         "ATQ %":4.3,
                         "Maîtrise élémentaire":69},
                         "setName")
        artifact_3_rolls_possibilities.dataFrame.drop(index=["Substats rates 1",
                                                           "Substats rates 2",
                                                           "Substats rates 3"],inplace=True)
        pandas.testing.assert_frame_equal(ArtifactsFunctions.getSubstatsRating(
            artifact_3_rolls_possibilities.dataFrame),
            df_3_roll_possibilities,
            check_dtype=False)

#               _        _         _   _  __            _     ____        _        _____                         
#     __ _  ___| |_     / \   _ __| |_(_)/ _| __ _  ___| |_  |  _ \  __ _| |_ __ _|  ___| __ __ _ _ __ ___   ___ 
#    / _` |/ _ \ __|   / _ \ | '__| __| | |_ / _` |/ __| __| | | | |/ _` | __/ _` | |_ | '__/ _` | '_ ` _ \ / _ \
#   | (_| |  __/ |_   / ___ \| |  | |_| |  _| (_| | (__| |_  | |_| | (_| | || (_| |  _|| | | (_| | | | | | |  __/
#    \__, |\___|\__| /_/   \_\_|   \__|_|_|  \__,_|\___|\__| |____/ \__,_|\__\__,_|_|  |_|  \__,_|_| |_| |_|\___|
#    |___/                                                                                                       
class test_getArtifactDataFrame(unittest.TestCase):
    def test_to_much_rolls(self):
        logging.info("test_to_much_rolls")
        self.assertEqual(ArtifactsFunctions.getArtifactDataFrame(artifact_to_much_rolls).empty, 
                         pandas.DataFrame().empty)
    def test_1_roll_possibility(self):
        logging.info("test_1_roll_possibility")
        artifact_1_roll_possibility_min = MyClasses.Artifact("artifact_1_roll_possibility_min",
                          "coupe",
                          ("def",59),
                          {"PV":299,
                         "ATQ":38,
                         "ATQ %":20.0,
                         "DÉF %":7.3},
                         "setName")
        pandas.testing.assert_frame_equal(artifact_1_roll_possibility_min.dataFrame,
            df_1_roll_possibility_min,
            check_dtype=False)
    def test_2_roll_possibilities(self):
        logging.info("test_2_roll_possibilities")
        artifact_2_rolls_possibilities = MyClasses.Artifact("artifact_2_rolls_possibilities",
                          "diadème",
                          ("DGT CRIT %",62.2),
                          {"PV":299,
                         "PV %":5.8,
                         "ATQ %":5.8,
                         "Recharge d'énergie %":30},
                         "setName")
        pandas.testing.assert_frame_equal(artifact_2_rolls_possibilities.dataFrame,
            df_2_roll_possibilities,
            check_dtype=False)
    def test_3_roll_possibilities(self):
        logging.info("test_3_roll_possibilities")
        artifact_3_rolls_possibilities = MyClasses.Artifact("artifact_3_rolls_possibilities",
                          "coupe",
                          ("def",59),
                          {"ATQ":18.5,
                         "DÉF":65,
                         "ATQ %":4.3,
                         "Maîtrise élémentaire":69},
                         "setName")
        pandas.testing.assert_frame_equal(artifact_3_rolls_possibilities.dataFrame,
            df_3_roll_possibilities,
            check_dtype=False)

if __name__ == "__main__":
    unittest.main()