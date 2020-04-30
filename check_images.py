#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/check_images.py
#
# TODO 0: Add your information below for Programmer & Date Created.                                                                             
# PROGRAMMER: Jorrit Goddijn
# DATE CREATED: 04-23-2020
# REVISED DATE: 04-29-2020
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task. 
#          Note that the true identity of the pet (or object) in the image is 
#          indicated by the filename of the image. Therefore, your program must
#          first extract the pet image label from the filename before
#          classifying the images using the pretrained CNN model. With this 
#          program we will be comparing the performance of 3 different CNN model
#          architectures to determine which provides the "best" classification.
#
# Use argparse Expected Call with <> indicating expected user input:
#      python check_images.py --dir <directory with images> --arch <model>
#             --dogfile <file that contains dognames>
#   Example call:
#    python check_images.py --dir pet_images/ --arch vgg --dogfile dognames.txt
##

# Imports python modules
from time import time, sleep

# Imports print functions that check the lab
from print_functions_for_lab_checks import *

# Imports functions created for this program
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results
from utils import format_time, format_time_millis

# Main program function defined below
def main():

    # store results dicts for each architecture
    arch_results = []

    # TODO 1: Define get_input_args function within the file get_input_args.py
    # This function retrieves 3 Command Line Arugments from user as input from
    # the user running the program from a terminal window. This function returns
    # the collection of these command line arguments from the function call as
    # the variable in_arg
    in_arg = get_input_args()

    print("Argument 1:", in_arg.dir)
    print("Argument 2:", in_arg.arch)
    print("Argument 3:", in_arg.dogfile)

    # Function that checks command line arguments using in_arg
    check_command_line_arguments(in_arg)

    archs = in_arg.arch.split(",")

    for arch in archs:
        # TODO 0: Measures total program runtime by collecting start time
        start_time = time()

        # TODO 2: Define get_pet_labels function within the file get_pet_labels.py
        # Once the get_pet_labels function has been defined replace "None"
        # in the function call with in_arg.dir  Once you have done the replacements
        # your function call should look like this:
        #             get_pet_labels(in_arg.dir)
        # This function creates the results dictionary that contains the results,
        # this dictionary is returned from the function call as the variable results
        results = get_pet_labels(in_arg.dir)

        # Function that checks Pet Images in the results Dictionary using results
        check_creating_pet_image_labels(results)


        # TODO 3: Define classify_images function within the file classiy_images.py
        # Once the classify_images function has been defined replace first "None"
        # in the function call with in_arg.dir and replace the last "None" in the
        # function call with in_arg.arch  Once you have done the replacements your
        # function call should look like this:
        #             classify_images(in_arg.dir, results, in_arg.arch)
        # Creates Classifier Labels with classifier function, Compares Labels,
        # and adds these results to the results dictionary - results
        classify_images(in_arg.dir, results, arch)

        # Function that checks Results Dictionary using results
        check_classifying_images(results)


        # TODO 4: Define adjust_results4_isadog function within the file adjust_results4_isadog.py
        # Once the adjust_results4_isadog function has been defined replace "None"
        # in the function call with in_arg.dogfile  Once you have done the
        # replacements your function call should look like this:
        #          adjust_results4_isadog(results, in_arg.dogfile)
        # Adjusts the results dictionary to determine if classifier correctly
        # classified images as "a dog" or "not a dog". This demonstrates if
        # model can correctly classify dog images as dogs (regardless of breed)
        adjust_results4_isadog(results, in_arg.dogfile)

        # Function that checks Results Dictionary for is-a-dog adjustment using results
        check_classifying_labels_as_dogs(results)


        # TODO 5: Define calculates_results_stats function within the file calculates_results_stats.py
        # This function creates the results statistics dictionary that contains a
        # summary of the results statistics (this includes counts & percentages). This
        # dictionary is returned from the function call as the variable results_stats
        # Calculates results of run and puts statistics in the Results Statistics
        # Dictionary - called results_stats
        results_stats = calculates_results_stats(results)

        # Function that checks Results Statistics Dictionary using results_stats
        check_calculating_results(results, results_stats)


        # TODO 6: Define print_results function within the file print_results.py
        # Once the print_results function has been defined replace "None"
        # in the function call with in_arg.arch  Once you have done the
        # replacements your function call should look like this:
        #      print_results(results, results_stats, in_arg.arch, True, True)
        # Prints summary results, incorrect classifications of dogs (if requested)
        # and incorrectly classified breeds (if requested)
        print_results(results, results_stats, arch, True, True)

        # TODO 0: Measure total program runtime by collecting end time
        end_time = time()

        # TODO 0: Computes overall runtime in seconds
        tot_time = end_time - start_time

        results_stats["exec_time"] = tot_time
        results_stats["arch"] = arch

        arch_results.append(results_stats)

        # prints execution time in in hh:mm:ss format
        print("\n** Total Elapsed Runtime:",
              format_time(tot_time) )

    # print architecture performance

    print("\n**Architecture Performance**\n")
    print("{:20}: {}".format("# Total Images", arch_results[0]["n_images"]))
    print("{:20}: {}".format("# Dog Images", arch_results[0]["n_dogs_img"]))
    print("{:20}: {}".format("# Not-Dog Images", arch_results[0]["n_notdogs_img"]))

    print("\n{:20} | {:20} | {:20} | {:20} | {:20} | {:20}".format("Architecture", "% Not-Dog Correct", "% Dog Correct", "% Breed Correct", "% Label Match", "Processing time"))
    print("{:_<135}".format(""))
    for ar in arch_results:
        print("{:20} | {:19.2f}% | {:19.2f}% | {:19.2f}% | {:19.2f}% | {:>20}".format(ar["arch"].upper(), ar["pct_correct_notdogs"], ar["pct_correct_dogs"], ar["pct_correct_breed"], ar["pct_match"], format_time_millis(ar["exec_time"]) ))


# Call to main function to run the program
if __name__ == "__main__":
    main()
