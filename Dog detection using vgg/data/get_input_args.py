import argparse#importing the argparse module
def get_input_args():
    #create parse
    pars=argparse.ArgumentParser(description=' Dog image classifacation')
    #creating 3 commandline argument for user input path,architecture,dog names file
    pars.add_argument('--dir',type=str,default='pet_images/',help='directory of the image')
    pars.add_argument('--arch',type=str,default='vgg',help='CNN Architecture')
    pars.add_argument('--dogfile',default='dognames.txt',help='Text file with dog names')
    return pars.parse_args()

