#logerrors.py
###version 1.0
###Author Austin Kelly
#### this module will log all errors
'''this module will log all errors that have been captured by code in to a dynamically created text file called programlog'''

class Logerrors():
    try:
        def __init__(self,errorA='',errorB=''):##noteinitializer can be expanded to read from a args list
            self.errorlist=[errorA,errorB]
            for myerror in self.errorlist:
                with open('programlog.txt', 'a', encoding='UTF-8', newline='') as f:
                    f.write(myerror + '\n\n')
    except Exception('Error occured in writing error log please check file permission is correct and file is not being used by another program'):
        pass





def main():## this method creates a text file in the local directory called programlog when a the program catches one of its exception handled errors-- provide for demo purposes
    Logerrors('Hi there this is a test of the on error code')
if __name__ == '__main__':
    main()

