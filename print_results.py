#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#                                                                             
# PROGRAMMER: 
# DATE CREATED:
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            -The results dictionary as results_dic within print_results 
#             function and results for the function call within main.
#            -The results statistics dictionary as results_stats_dic within 
#             print_results function and results_stats for the function call within main.
#            -The CNN model architecture as model wihtin print_results function
#             and in_arg.arch for the function call within main. 
#            -Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#            -Prints Incorrectly Classified Breeds as print_incorrect_breed within
#             print_results function and set as either boolean value True or 
#             False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##
# TODO 6: Define print_results function below, specifically replace the None
#       below by the function definition of the print_results function. 
#       Notice that this function doesn't to return anything because it  
#       prints a summary of the results using results_dic and results_stats_dic
# 
def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if user indicates 
    they want those printouts (use non-default values)
    Parameters:
      results_dic - Dictionary with key as image filename and value as a List 
             (index)idx 0 = pet image label (string)
                    idx 1 = classifier label (string)
                    idx 2 = 1/0 (int)  where 1 = match between pet image and 
                            classifer labels and 0 = no match between labels
                    idx 3 = 1/0 (int)  where 1 = pet image 'is-a' dog and 
                            0 = pet Image 'is-NOT-a' dog. 
                    idx 4 = 1/0 (int)  where 1 = Classifier classifies image 
                            'as-a' dog and 0 = Classifier classifies image  
                            'as-NOT-a' dog.
      results_stats_dic - Dictionary that contains the results statistics (either
                   a  percentage or a count) where the key is the statistic's 
                     name (starting with 'pct' for percentage or 'n' for count)
                     and the value is the statistic's value 
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
      print_incorrect_dogs - True prints incorrectly classified dog images and 
                             False doesn't print anything(default) (bool)  
      print_incorrect_breed - True prints incorrectly classified dog breeds and 
                              False doesn't print anything(default) (bool) 
    Returns:
           None - simply printing results.
    """

    print('\n\n*** Results Summary for CNN Model Architecture', model.upper(),
          '***\n')

    # print the counts
    print('Counts:\n')
    print('{:20}: {:3d}'.format('Image count', results_stats_dic['n_images']))
    print('{:20}: {:3d}'.format('Dog image count', results_stats_dic['n_dogs_img']))
    print('{:20}: {:3d}'.format('Not-Dog image count', results_stats_dic['n_notdogs_img']))
    print('\n')

    # print the percentages
    print('Percentages:\n')
    print('{:20}: {:6.2f}%'.format('Pct correct dogs', results_stats_dic['pct_correct_dogs']))
    print('{:20}: {:6.2f}%'.format('Pct correct not-dogs', results_stats_dic['pct_correct_notdogs']))
    print('{:20}: {:6.2f}%'.format('Pct correct breed', results_stats_dic['pct_correct_breed']))
    print('{:20}: {:6.2f}%'.format('Pct correct match', results_stats_dic['pct_match']))
    print('\n')

    if print_incorrect_dogs:
        print('Misclassified dogs:\n')

        if results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] == results_stats_dic['n_images']:
            print('All dogs were correctly classified.')
        else:
            print('{:40} | {:60}'.format('Image name', 'Classification result'))
            print('{:_<100}'.format(''))
            for image_name, result in results_dic.items():
                # misclassified images are dogs classified as not dogs,
                # or not dogs classified as dogs.
                if (result[3] == 1 and result[4] == 0) or (result[3] == 0 and result[4] == 1):
                    print('{:40} | {}'.format(image_name, result[1]))
        print('\n')

    if print_incorrect_breed:
        print('Misclassified breed:\n')

        if results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] == results_stats_dic['n_images']:
            print('No incorrect classified breeds.\n')
        else:
            print('{:40} | {:60}'.format('Image name', 'Classification result'))
            print('{:_<100}'.format(''))
            for image_name, result in results_dic.items():
                # a misclassified breed is when label is a dog (result[3] == 1) but no match between labels result[2] == 0
                if result[3] == 1 and result[2] == 0:
                    print('{:40} | {}'.format(image_name, result[1]))





