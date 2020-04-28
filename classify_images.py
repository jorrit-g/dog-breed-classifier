#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Jorrit Goddijn
# DATE CREATED: 04-28-2020
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels. This function inputs:
#            -The Image Folder as image_dir within classify_images and function 
#             and as in_arg.dir for function call within main. 
#            -The results dictionary as results_dic within classify_images 
#             function and results for the function call within main.
#            -The CNN model architecture as model within classify_images function
#             and in_arg.arch for the function call within main. 
#           This function uses the extend function to add items to the list 
#           that's the 'value' of the results dictionary. You will be adding the
#           classifier label as the item at index 1 of the list and the comparison 
#           of the pet and classifier labels as the item at index 2 of the list.
#
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier


# TODO 3: Define classify_images function below, specifically replace the None
#       below by the function definition of the classify_images function. 
#       Notice that this function doesn't return anything because the 
#       results_dic dictionary that is passed into the function is a mutable 
#       data type so no return is needed.
# 
def classify_images(images_dir, results_dic, model):
    """
    Runs a pre trained model for each of the images in the image dir, mutating the results dict with the classifier
    results
     Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                    index 0 = pet image label (string)
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutated in place. The value will be extended with the classifier label (index 1) and
           whether the prediction is true (index 2)
    """
    if not images_dir.endswith('/'):
        images_dir += '/'

    for pet_image_filename in list(results_dic.keys()):
        result_dict_item = results_dic[pet_image_filename]

        # do the prediction
        prediction = classifier(images_dir + pet_image_filename, model)
        prediction = prediction.lower().strip()

        # get the label
        pet_label = result_dict_item[0]

        # check for a match by looking for the pet label in the prediction result
        match = 0
        if pet_label in prediction:
            match = 1

        # store the result
        result_dict_item.extend([prediction, match])

    return None
