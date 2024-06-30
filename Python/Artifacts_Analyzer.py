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
# To get statistics from the Genshin Impact's artifact inputed :
#   - #* DONE - Number of native rolls
#   - #* DONE - CV
#   - #* DONE - How near your artifact is from its "perfect" state (if it would have get 100% maximum rolls)
#   - #* DONE - How far your artifact is from its 'worst" state (if it would have get 100% minimum rolls)
#   - #TODO - Option avaible :  - Get rid off a stat from the calculus

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
import time

#    _____ _     _         _                    _         
#   |_   _| |__ (_)_ __ __| |  _ __   __ _ _ __| |_ _   _ 
#     | | | '_ \| | '__/ _` | | '_ \ / _` | '__| __| | | |
#     | | | | | | | | | (_| | | |_) | (_| | |  | |_| |_| |
#     |_| |_| |_|_|_|  \__,_| | .__/ \__,_|_|   \__|\__, |
#                             |_|                   |___/ 
import pandas
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib

#    _                    _ 
#   | |    ___   ___ __ _| |
#   | |   / _ \ / __/ _` | |
#   | |__| (_) | (_| (_| | |
#   |_____\___/ \___\__,_|_|
#                           
from MyTools import MyClasses
from MyTools import MyConstants
from MyTools import VideosFunctions
from MyTools import OCRFunctions
from MyTools import ImagesFunctions
from MyTools import ArtifactsFunctions


#   ██████  ██████  ███    ██ ███████ ████████  █████  ███    ██ ████████ ███████ 
#  ██      ██    ██ ████   ██ ██         ██    ██   ██ ████   ██    ██    ██      
#  ██      ██    ██ ██ ██  ██ ███████    ██    ███████ ██ ██  ██    ██    ███████ 
#  ██      ██    ██ ██  ██ ██      ██    ██    ██   ██ ██  ██ ██    ██         ██ 
#   ██████  ██████  ██   ████ ███████    ██    ██   ██ ██   ████    ██    ███████ 
#
#ArtifactsFunctions.setConstants()
CURRENT_PATH = MyConstants.CURRENT_PATH
MIN_MAX_ROLLS_PER_SUBSTATS = MyConstants.MIN_MAX_ROLLS_PER_SUBSTATS
VIDEOS_PATH = CURRENT_PATH + "/Python/Source/Videos/"
logging.debug(f"VIDEOS_PATH: {VIDEOS_PATH}")
logging.debug(f"Files in above Path : {os.listdir(VIDEOS_PATH)}")
IMAGES_PATH = CURRENT_PATH + "/Python/Source/ArtifactsScreenshots/"
logging.debug(f"IMAGES_PATH: {IMAGES_PATH}")
logging.debug(f"Files in above Path : {os.listdir(IMAGES_PATH)}")

#  ███    ███  █████  ██ ███    ██ 
#  ████  ████ ██   ██ ██ ████   ██ 
#  ██ ████ ██ ███████ ██ ██ ██  ██ 
#  ██  ██  ██ ██   ██ ██ ██  ██ ██ 
#  ██      ██ ██   ██ ██ ██   ████ 
#
start = time.time()
end = time.time()
print(f"time elapsed: {end - start}")

start = time.time()

#################################################
###### Get the artifacts'image from video #######
#################################################

VideosFunctions.extractDistinctArtifactsFromVideo('TestingVideo.mp4')

#################################################
##### Get the artifactssubstats from image ######
#################################################

substatDict = OCRFunctions.getDictionnaryOfSubstatsForAllArtifactImages(IMAGES_PATH)
logging.info(f"substatDict: {substatDict}")

#################################################
########### Get the artifacts image #############
#################################################

import re as regex

FRAME_NAME = MyConstants.FRAME_NAME
FRAME_MAINSTAT_NAME = MyConstants.FRAME_MAINSTAT_NAME
FRAME_SUBSTATS_NAME = MyConstants.FRAME_SUBSTATS_NAME
FRAME_FILE_EXTENSION = MyConstants.FRAME_FILE_EXTENSION

imagesList = os.listdir(IMAGES_PATH)
logging.debug(f"imagesList: {imagesList}")

ArtifactList = []
for artifactImageName in os.listdir(IMAGES_PATH):
    logging.debug(f"artifactImageName: {artifactImageName}")
    artifactNumber = regex.search("[0-9]+", artifactImageName).group()
    logging.debug(f"artifactNumber: {artifactNumber}")
    #Mainstat = mainstatDict[FRAME_MAINSTAT_NAME + artifactNumber + FRAME_FILE_EXTENSION]
    Substats = substatDict[FRAME_SUBSTATS_NAME + artifactNumber + FRAME_FILE_EXTENSION]
    #logging.debug(f"Mainstat: {Mainstat}")
    logging.debug(f"Substats: {Substats}")
    temp_artifact = MyClasses.Artifact(str(artifactNumber),
                          "artifact_type",
                          ('mainstat', 999),
                          Substats,
                         "artifact_setName")
    logging.debug(f"artifact {temp_artifact.name} is added in the list for the final rendering")
    ArtifactList.append(temp_artifact)

for artifact in ArtifactList:
    logging.info(f"\nStarting graph creation for artifact {artifact.name}\n"
          f"substats: {artifact.substats}\n"
          f"dataFrame:\n{artifact.dataFrame}\n"
          f"substatsRate: {artifact.substatsRate}\n"
          f"critValue: {artifact.critValue}\n"
          f"critValueRates: {artifact.critValueRates}\n")
    print(artifact)
    ImagesFunctions.getArtifactSubstatsScenario(artifact)


    df = artifact.dataFrame
    #Skipping first line as it is the substats themselves
    #Looping over rolls possibilities
    for i in range(1, len(df.index)):
        logging.info(f"i: {i}")
        # If i is even then the row is a roll possibility
        if (i % 2) == 0:
            logging.info(f"Adding new graph for row '{df.iloc[i].name}'")
            logging.info(f"Line name: {df.iloc[i].name}")
            logging.info(f"Line values: {df.iloc[i].values}")
            logging.info(f"Line indexes: {df.iloc[i].index.values}")
            for substat in df.iloc[i].index.values:
                logging.info(f"substat: {substat}")
                if substat == ArtifactsFunctions.DATAFRAME_SUM_COLUMN_NAME:
                    logging.info(f"Skipping {ArtifactsFunctions.DATAFRAME_SUM_COLUMN_NAME} column")
                    continue
            
    artifactImage = plt.imread(IMAGES_PATH + FRAME_NAME + artifact.name + FRAME_FILE_EXTENSION)

    #Figure parameterization
    ArtifactSummary, (ax1, ax2) = plt.subplots(2, 1)
    ArtifactSummary.set_facecolor("black")
    ArtifactSummary.set_edgecolor("white")
    ArtifactSummary.set_linewidth(2) # White edge of the image

    #Axes parameterization
        # Artifact Image
    ax1.imshow(artifactImage)
    ax1.set_xlabel("Crit value : "+ str(round(artifact.critValue, 3)), color='white')
    ax1.xaxis.labelpad = - 13 #To move up the X label
        # Artifact Graph
    ax2.set_xlim(-1, 101) # To get an offset from the 0 and always have xticks from 0 to 100
    ax2.set_title("Min rolls", color='white')
    ax2.set_facecolor("black")
    ax2.spines["left"].set_color("white")
    ax2.spines["bottom"].set_color("white")
    ax2.set_xticks(np.arange(0, 101, 2), minor = True)
    ax2.set_xticks(np.arange(0, 101, 10), minor = False)
    ax2.tick_params(axis="both", colors='white', which = 'major')
    ax2.tick_params(axis="both", colors='white', which = 'minor')


    temp_list_rolls_index = []
    for row_index in artifact.dataFrame.index:
        print(row_index)
        if ("rolls" in row_index) or ("Rolls" in row_index):
            temp_list_rolls_index.append(row_index)

    print(temp_list_rolls_index)
    temp_iter_rolls_index = iter(temp_list_rolls_index)
    '''
    for _index in substats.index:
        print(_index)
        temp_roll_name = next(temp_iter_rolls_index)
        substats.rename(index={_index:
                               str(int(artifact.dataFrame.loc[temp_roll_name, _index])) +
                               " rolls " + _index}, inplace=True)
    '''


    substats = pandas.DataFrame(artifact.dataFrame).loc['Substats rates 1']
    substats = substats.drop(index=[ArtifactsFunctions.DATAFRAME_SUM_COLUMN_NAME]) #No need 
                                                                                   #for maingraph
        
    for _index in substats.index:
        print(_index)
        #temp_roll_name = next(temp_iter_rolls_index)
        nb_of_rolls = artifact.dataFrame.loc["Min rolls", _index]
        if nb_of_rolls > 1 :
            substats.rename(index={_index:
                                str(int(artifact.dataFrame.loc["Min rolls", _index])) +
                                " rolls " + _index}, inplace=True)
        else :
            substats.rename(index={_index:
                                str(int(artifact.dataFrame.loc["Min rolls", _index])) +
                                " roll " + _index}, inplace=True)
        print(substats.index)
    
    if artifact.critValue != 0:
        substats.loc["Crit Value"] = artifact.critValueRates["Min rolls"]
    substats.loc["Résumé"] = artifact.substatsRate["Weighted Substats rates 1 normalized"]
    substats = substats * 100
    substats = substats.iloc[::-1] #Flip around the rows 180° because
                                   #.plot.barh method starts from last row..
    values = substats.values
    print()
    print(values)
    print(substats)
    print(substats.index)
    print()
    

    color_map = mcolors.LinearSegmentedColormap.from_list("", ["red", "yellow", "green"])
    norm = mcolors.Normalize(0, 100)
    colors = [color_map(norm(u)) for u in values]

    substats.plot.barh(fig = ArtifactSummary, color = colors, edgecolor = "white")

    i=0

    for pltObjects in ax2.get_children():
        characterSize = 10
        if isinstance(pltObjects, matplotlib.patches.Rectangle):  
            i+=1 
            print(f"pltObjects:{pltObjects}")
            artifactSubstatRate = round(round(pltObjects.get_width(),4), 2)
            leftCoordRect = pltObjects.get_xy()[0]
            bottomCoordRect = pltObjects.get_xy()[1]
            if i > 6: # 6 because I'm getting a weird "100%" coming from nowhere #TODO this number will change for each scenario
                continue
            else:
                #To add the % on the left of each bars
                ax2.annotate(str(artifactSubstatRate)+"%", 
                        xy=(leftCoordRect + pltObjects.get_width() + 1, 
                            bottomCoordRect + (pltObjects.get_height()/2)), 
                        va = 'center',
                        fontsize = characterSize, 
                        color = "white")
            pass
    plt.tight_layout()
    plt.savefig('myfig'+str(artifact.name)+'.png', dpi = 200)



end = time.time()
print(f"time elapsed: {end - start}")

'''
import cProfile
import pstats

with cProfile.Profile() as pr:
    artifact_8_and_9_rolls_3_lines_with_crit_stats = MyClasses.Artifact(
    "artifact_8_and_9_rolls_3_lines_with_crit_stats",
                          "coupe",
                          ("def",59),
                          {"ATK_Flat":18.5,
                         "CD%":22,
                         "ATK%":4.3,
                         "CR%":11},
                         "setName")
stats = pstats.Stats(pr)
stats.sort_stats(pstats.SortKey.CUMULATIVE)
stats.print_stats(30)
print(artifact_8_and_9_rolls_3_lines_with_crit_stats.dataFrame)

artifact_3_rolls_possibilities = MyClasses.Artifact("artifact_3_rolls_possibilities",
                          "coupe",
                          ("def",59),
                          {"ATK_Flat":18.5,
                         "DEF_Flat":65,
                         "ATK%":4.3,
                         "EM":69},
                         "setName")
artifact_3_rolls_possibilities.dataFrame.drop(index=["Substats rates 1",
                                                           "Substats rates 2",
                                                           "Substats rates 3"],inplace=True)
print(artifact_3_rolls_possibilities.dataFrame)

from line_profiler import LineProfiler

lp = LineProfiler()

ArtifactsFunctions.getSubstatsRating = lp(ArtifactsFunctions.getSubstatsRating)
ArtifactsFunctions.getSubstatsRating(artifact_3_rolls_possibilities.dataFrame)
lp.print_stats()

artifact_example_full_max_rolls = MyClasses.Artifact("artifact_example_full_max_rolls",
                          "coupe",
                          ("def",59),
                          {"ATK%":5.8,
                         "ER%":6.5,
                         "CD%":7.8,
                         "CR%":23.4},
                         "setName")
artifact_example_full_min_rolls = MyClasses.Artifact("artifact_example_full_min_rolls",
                          "coupe",
                          ("def",59),
                          {"HP_Flat":209,
                         "ATK_Flat":14,
                         "ATK%":24.6,
                         "DEF%":5.1},
                         "setName")
artifact_9_rolls_one_line_2_crits_stats= MyClasses.Artifact(
    "artifact_9_rolls_one_line_2_crits_stats",
                          "coupe",
                          ("def",59),
                          {"ER%":18.5,
                         "CD%":10.9,
                         "DEF_Flat":23,
                         "CR%":11.5},
                         "setName")
artifact_example1_onlyCD = MyClasses.Artifact("artifact_example1_onlyCD",
                          "coupe",
                          ("def",59),
                          {"ER%":18.5,
                         "CD%":10.9,
                         "DEF_Flat":23,
                         "ATK%":16},
                         "setName")
artifact_example1_onlyCR = MyClasses.Artifact("artifact_example1_onlyCR",
                          "coupe",
                          ("def",59),
                          {"ER%":18.5,
                         "ATK%":10.9,
                         "DEF_Flat":23,
                         "CR%":11.5},
                         "setName")
artifact_8_rolls_one_line = MyClasses.Artifact("artifact_8_rolls_one_line",
                          "coupe",
                          ("def",59),
                          {"HP_Flat":299,
                         "ATK_Flat":38,
                         "ATK%":20.0,
                         "DEF%":7.3},
                         "setName")
artifact_8_and_9_rolls_3_lines = MyClasses.Artifact("artifact_8_and_9_rolls_3_lines",
                          "coupe",
                          ("def",59),
                          {"ATK_Flat":18.5,
                         "DEF_Flat":65,
                         "ATK%":4.3,
                         "EM":69},
                         "setName")
artifact_8_and_9_rolls_3_lines_with_crit_stats = MyClasses.Artifact(
    "artifact_8_and_9_rolls_3_lines_with_crit_stats",
                          "coupe",
                          ("def",59),
                          {"ATK_Flat":18.5,
                         "CD%":22,
                         "ATK%":4.3,
                         "CR%":11},
                         "setName")
artifact_9_rolls_one_line_splitted = MyClasses.Artifact("artifact_9_rolls_one_line_splitted",
                          "coupe",
                          ("def",59),
                          {"ER%":15.2,
                         "CD%":14,
                         "DEF_Flat":46,
                         "CR%":6.2},
                         "setName")
impossible_example_non_existing_substat = MyClasses.Artifact(
    "impossible_example_non_existing_substat",
                          "coupe",
                          ("def",59),
                          {"ER%":38,
                         "CD%":14,
                         "DEF_Flat":46,
                         "CR%":8},
                         "setName")
impossible_example_non_existing_substat_min = MyClasses.Artifact(
    "impossible_example_non_existing_substat_min",
                          "coupe",
                          ("def",59),
                          {"ER%":38,
                         "CD%":14,
                         "DEF_Flat":46,
                         "CR%":2},
                         "setName")
impossible_example_non_existing_substat_max = MyClasses.Artifact(
    "impossible_example_non_existing_substat_max",
                          "coupe",
                          ("def",59),
                          {"ER%":14,
                         "CD%":14,
                         "DEF_Flat":46,
                         "CR%":24},
                         "setName")

artifact_object_list = [artifact_example_full_max_rolls, artifact_example_full_min_rolls, 
                        artifact_9_rolls_one_line_2_crits_stats, 
                        artifact_example1_onlyCD, artifact_example1_onlyCR,
                        artifact_8_rolls_one_line, artifact_8_and_9_rolls_3_lines, 
                        artifact_8_and_9_rolls_3_lines_with_crit_stats,
                        artifact_9_rolls_one_line_splitted, impossible_example_non_existing_substat,
                        impossible_example_non_existing_substat_min, 
                        impossible_example_non_existing_substat_max,
                        ]

#print("printing artifacts'Dataframe from the list :")
for artifact in artifact_object_list:
    print("")
    print(artifact)
'''
