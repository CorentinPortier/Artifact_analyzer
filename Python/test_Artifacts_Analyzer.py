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
# To have a .py containing all the tests of this project

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
import unittest

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
from MyTools import MyClasses
from MyTools import ArtifactsFunctions

#   ██████  ██████  ███    ██ ███████ ████████  █████  ███    ██ ████████ ███████ 
#  ██      ██    ██ ████   ██ ██         ██    ██   ██ ████   ██    ██    ██      
#  ██      ██    ██ ██ ██  ██ ███████    ██    ███████ ██ ██  ██    ██    ███████ 
#  ██      ██    ██ ██  ██ ██      ██    ██    ██   ██ ██  ██ ██    ██         ██ 
#   ██████  ██████  ██   ████ ███████    ██    ██   ██ ██   ████    ██    ███████ 
#
#       _         _   _  __            _       
#      / \   _ __| |_(_)/ _| __ _  ___| |_ ___ 
#     / _ \ | '__| __| | |_ / _` |/ __| __/ __|
#    / ___ \| |  | |_| |  _| (_| | (__| |_\__ \
#   /_/   \_\_|   \__|_|_|  \__,_|\___|\__|___/
#                                              


#    ____        _         _        _       
#   / ___| _   _| |__  ___| |_ __ _| |_ ___ 
#   \___ \| | | | '_ \/ __| __/ _` | __/ __|
#    ___) | |_| | |_) \__ \ || (_| | |_\__ \
#   |____/ \__,_|_.__/|___/\__\__,_|\__|___/
#                                           


#    ____        _        _____                              
#   |  _ \  __ _| |_ __ _|  ___| __ __ _ _ __ ___   ___  ___ 
#   | | | |/ _` | __/ _` | |_ | '__/ _` | '_ ` _ \ / _ \/ __|
#   | |_| | (_| | || (_| |  _|| | | (_| | | | | | |  __/\__ \
#   |____/ \__,_|\__\__,_|_|  |_|  \__,_|_| |_| |_|\___||___/


#  ████████ ███████ ███████ ████████ ███████ 
#     ██    ██      ██         ██    ██      
#     ██    █████   ███████    ██    ███████ 
#     ██    ██           ██    ██         ██ 
#     ██    ███████ ███████    ██    ███████ 
#                                            


#  ██ ███████     ███    ███  █████  ██ ███    ██ 
#  ██ ██          ████  ████ ██   ██ ██ ████   ██ 
#  ██ █████       ██ ████ ██ ███████ ██ ██ ██  ██ 
#  ██ ██          ██  ██  ██ ██   ██ ██ ██  ██ ██ 
#  ██ ██          ██      ██ ██   ██ ██ ██   ████ 
#
if __name__ == "__main__":
    unittest.main()    

    '''
    suite1 = unittest.TestLoader().loadTestsFromTestCase(test_getArtifactDataFrame)
    suite2 = unittest.TestLoader().loadTestsFromTestCase(test_getSubstatsRating)
    all_tests = unittest.TestSuite([suite1, suite2])
    runner = unittest.TextTestRunner()
    runner.run(all_tests)
    '''