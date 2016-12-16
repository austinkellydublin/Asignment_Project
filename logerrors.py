#logerrors.py
###version 1.0
###Author Austin Kelly
#### this module will log all errors

class Logerrors():
    try:
        def __init__(self,errorA='',errorB=''):
            self.errorlist=[errorA,errorB]
            for myerror in self.errorlist:
                with open('programlog.txt', 'a', encoding='UTF-8', newline='') as f:
                    f.write(myerror + '\n\n')
    except Exception('Error occured in writing error log please check file permission is correct and file is not being used by another program'):
        pass





def main():
    Logerrors('Hi there this is a test of the on error code')
if __name__ == '__main__':
    main()

