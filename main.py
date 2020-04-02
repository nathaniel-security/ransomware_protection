import os
import hashlib
import time


import subprocess

import platform



os_name = platform.system()
if (os_name == 'Linux'):
    import notify2

if (os_name == 'Windows'):
    from win10toast import ToastNotifier
    from dirsync import sync



#from ftplib import FTP
#

def windows_message(title , message):
    toaster = ToastNotifier()
    toaster.show_toast(
        title,
        message,
        duration=10)

def sendmessage(message):
    notify2.init('Backup System')
    n = notify2.Notification("Important", message)
    n.show()

'''

if (os_name == "Windows"):
    drive_one_path = "C:/Users/cnath/Documents/project/backup/test area/one"
    drive_two_path = "C:/Users/cnath/Documents/project/backup/test area/two"
    filename = "pywin32_ctypes-0.2.0-py3-none-any.whl"
    file_hash_value = '508e1622c800fabca9380be0eb5acac4bc1c22e6'


if (os_name == 'Linux'):
    
    drive_one_path = "/media/groot/drive/projects/backup/final/backup/test_area/one"
    drive_two_path = "/media/groot/drive/projects/backup/final/backup/test_area/two"
    filename = "pywin32_ctypes-0.2.0-py3-none-any.whl"
    file_hash_value = '508e1622c800fabca9380be0eb5acac4bc1c22e6'

'''
print("**************************\n Please make sure the file location is in two different drives for better results")
drive_one_path = input("drive one path location (eg:- c:/main_data ) :- ")


drive_two_path = input("drive two path location (eg:- d:/backup_data ) :- ")
filename = input("filename (this file should be some ransod file which you will not use) :- ")


#for windows

#for linux
#file_hash_value = '92a949fd41844e1bb8c6812cdea102708fde23a4'
#filename = 'test'



def hash_file(filename):
    h = hashlib.sha1()
    with open(filename,'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)

    return h.hexdigest()

command = drive_two_path + "/" + filename
file_hash_value = hash_file(command)

#linux part
def linux():
    #check if drive one exist
    ch1 = os.path.exists(drive_one_path)
    #print(ch1)
    if(ch1 == False):
        #exucutes if does not exsist
        '''
        folder one :-0
        file one   :- 
        hash one   :- 

        folder two :-
        file two   :-
        hash two   :-    
        '''
        #try:
        #os.mkdir(drive_one_path)
        #print("Path made")
        
        temp_var = os.path.exists(drive_two_path)

        if(temp_var == True):
            '''
                folder one :- 0
                file one   :- 0
                hash one   :- 0

                folder two :- 1
                file two   :-
                hash two   :-    
            '''

            command = drive_two_path + "/" + filename
            temp_var = os.path.isfile(command)
            #print(temp_var)
            if(temp_var == True):
                '''
                    folder one :- 0
                    file one   :- 0
                    hash one   :- 0

                    folder two :- 1
                    file two   :- 1
                    hash two   :-  
                '''
                command = drive_two_path + "/" + filename
                temp_var = hash_file(command)



                if(temp_var == file_hash_value):


                    '''
                        folder one :- 0
                        file one   :- 0
                        hash one   :- 0

                        folder two :- 1
                        file two   :- 1
                        hash two   :- 1
                    '''
                    current_path = drive_two_path + "/"
                    second_drive_path = drive_one_path
                    command = 'rsync -avz --delete ' + current_path + ' ' + second_drive_path
                    os.system(command)
                
                
                
                
                
                else:
                    '''
                        folder one :- 0
                        file one   :- 0
                        hash one   :- 0

                        folder two :- 1
                        file two   :- 1
                        hash two   :- 0
                    '''
                    print("have to get data from FTP second file hash not same as og")

            else:
                '''
                    folder one :- 0
                    file one   :- 0
                    hash one   :- 0

                    folder two :- 1
                    file two   :- 0
                    hash two   :- 0
                '''
                print("have to get data from FTP file in secondary drive does not exsist")

        else:
            '''
                folder one :- 0
                file one   :- 0
                hash one   :- 0
                
                folder two :- 0
                file two   :- 0
                hash two   :- 0
            '''
            print("path to drive does not exsist")




    else:

        '''
                folder one :- 1
                file one   :- 
                hash one   :- 
                
                folder two :- 
                file two   :- 
                hash two   :- 
        '''
        #exucutes if drive one exsist
        #print("come to this part")
        command = drive_one_path + "/" + filename
        temp_var = os.path.isfile(command) #check if file exsist
        
        #print(temp_var)
        #print("come here")
        
        
        if(temp_var == True):#if file exsist
            '''
                folder one :- 1
                file one   :- 1
                hash one   :- 
                
                folder two :- 
                file two   :- 
                hash two   :- 
            '''
            command = drive_one_path + "/" + filename
            temp_var = hash_file(command)#checks the hash of the file
            
            
            if(temp_var != file_hash_value):
                '''
                    folder one :- 1
                    file one   :- 1
                    hash one   :- 0

                    folder two :- 
                    file two   :- 
                    hash two   :- 
                '''
                #print('file hash value not equal')
                
                
                temp_var = os.path.exists(drive_one_path)
                if(temp_var == True):
                    '''
                        folder one :- 1
                        file one   :- 1
                        hash one   :- 0

                        folder two :- 1
                        file two   :- 
                        hash two   :- 
                    '''
                    command = drive_two_path + "/" + filename
                    temp_var = os.path.isfile(command)
                    if(temp_var == True):
                        '''
                            folder one :- 1
                            file one   :- 1
                            hash one   :- 0

                            folder two :- 1
                            file two   :- 1
                            hash two   :- 
                        '''
                        command = drive_two_path + "/" + filename
                        temp_var = hash_file(command)



                        if(temp_var == file_hash_value):
                            '''
                            folder one :- 1
                            file one   :- 1
                            hash one   :- 0

                            folder two :- 1
                            file two   :- 1
                            hash two   :- 1
                            '''
                            current_path = drive_two_path + "/"
                            second_drive_path = drive_one_path
                            command = 'rsync -avz --delete ' + current_path + ' ' + second_drive_path
                            os.system(command)


                        if(temp_var != file_hash_value):
                            '''
                            folder one :- 1
                            file one   :- 1
                            hash one   :- 0

                            folder two :- 1
                            file two   :- 1
                            hash two   :- 0
                            '''
                            print("have to get files from FTP")
                            


            else:
                '''
                    folder one :- 1
                    file one   :- 1
                    hash one   :- 1

                    folder two :- 
                    file two   :- 
                    hash two   :- 
                '''
                print("file hash in drive one is right")
                #drive one exsist folder exsist file exsist and hash is right in first folder
                
                #check secondary path if exsist
                temp_var = os.path.exists(drive_two_path)
                if(temp_var == True):
                    '''
                        folder one :- 1
                        file one   :- 1
                        hash one   :- 1

                        folder two :- 1
                        file two   :- 
                        hash two   :- 
                    '''
                    command = drive_two_path + "/" + filename
                    temp_var = os.path.isfile(command)


                    #now check if file exsist
                    if(temp_var == True):
                        '''
                            folder one :- 1
                            file one   :- 1
                            hash one   :- 1

                            folder two :- 1
                            file two   :- 1
                            hash two   :- 
                        '''

                       

                        #now check hash value
    

                        command = drive_two_path + "/" + filename
                        temp_var = hash_file(command)
                        #checking hash of second folder file




                        if(temp_var == file_hash_value):
                            '''
                                folder one :- 1
                                file one   :- 1
                                hash one   :- 1

                                folder two :- 1
                                file two   :- 1
                                hash two   :- 1
                            '''
                            current_path = drive_one_path + "/"
                            second_drive_path = drive_two_path
                            command = 'rsync -avz --delete ' + current_path + ' ' + second_drive_path
                            os.system(command)
                        
                        
                        
                        
                        else:
                            '''
                                folder one :- 1
                                file one   :- 1
                                hash one   :- 1

                                folder two :- 1
                                file two   :- 1
                                hash two   :- 0
                            '''
                            current_path = drive_one_path + "/"
                            second_drive_path = drive_two_path
                            command = 'rsync -avz --delete ' + current_path + ' ' + second_drive_path
                            os.system(command)
                            sendmessage("computer may be comprimised")
                    
                    
                    
                    else:
                        '''
                            folder one :- 1
                            file one   :- 1
                            hash one   :- 1

                            folder two :- 1
                            file two   :- 
                            hash two   :- 
                        '''
                        #seconday path exsist but file does not exsist
                        current_path = drive_one_path + "/"
                        second_drive_path = drive_two_path
                        command = 'rsync -avz --delete ' + current_path + ' ' + second_drive_path
                        os.system(command)
                        sendmessage("computer may be comprimised")
                


                #path to seconday folder does not exsist
                else:
                    '''
                        folder one :- 1
                        file one   :- 1
                        hash one   :- 1

                        folder two :- 0
                        file two   :- 
                        hash two   :- 
                    '''
                    print("here")
                    os.mkdir(drive_two_path)
                    current_path = drive_one_path + "/"
                    second_drive_path = drive_two_path
                    command = 'rsync -avz --delete ' + current_path + ' ' + second_drive_path
                    os.system(command)
                    sendmessage("computer may be comprimised")






        else:
            '''
                folder one :- 1
                file one   :- 0
                hash one   :- 
                
                folder two :- 
                file two   :- 
                hash two   :- 
            '''
            #print("nuck")
            #if test file does not exsist part but folder exsist


            #check if path two exist
            temp_var = os.path.exists(drive_two_path)
            if(temp_var == True):
                '''
                    folder one :- 1
                    file one   :- 0
                    hash one   :- 

                    folder two :- 1
                    file two   :- 
                    hash two   :- 
                '''

                #check if file exsist fir path two
                command = drive_two_path + "/" + filename
                temp_var = os.path.isfile(command)
                if(temp_var == True):
                    '''
                        folder one :- 1
                        file one   :- 0
                        hash one   :- 

                        folder two :- 1
                        file two   :- 1
                        hash two   :- 
                    '''
                    command = drive_two_path + "/" + filename
                    temp_var = hash_file(command)
                    if(temp_var == file_hash_value):
                        '''
                            folder one :- 1
                            file one   :- 0
                            hash one   :- 

                            folder two :- 1
                            file two   :- 1
                            hash two   :- 1
                        '''
                        current_path = drive_two_path + "/"
                        second_drive_path = drive_one_path
                        command = 'rsync -avz --delete ' + current_path + ' ' + second_drive_path
                        os.system(command)
                    else:
                        '''
                            folder one :- 1
                            file one   :- 0
                            hash one   :- 

                            folder two :- 1
                            file two   :- 1
                            hash two   :- 0
                        '''
                        print("have to get data from ftp")

                else:
                    '''
                        folder one :- 1
                        file one   :- 0
                        hash one   :- 

                        folder two :- 1
                        file two   :- 0
                        hash two   :- 
                    '''
                    print("have to get data from ftp") 
            else:
                '''
                    folder one :- 1
                    file one   :- 0
                    hash one   :- 

                    folder two :- 0
                    file two   :- 
                    hash two   :- 
                '''
                print("have to get files from FTP")




#linux part ends

#windows part

def windows_part():
    ch1 = os.path.exists(drive_one_path)
    if(ch1 == False):
        #exucutes if does not exsist
        '''
        folder one :-0
        file one   :- 
        hash one   :- 

        folder two :-
        file two   :-
        hash two   :-    
        '''
        #try:
        #os.mkdir(drive_one_path)
        #print("Path made")
        
        temp_var = os.path.exists(drive_two_path)
        if(temp_var == True):
            '''
                folder one :- 0
                file one   :- 0
                hash one   :- 0

                folder two :- 1
                file two   :-
                hash two   :-    
            '''

            command = drive_two_path + "/" + filename
            temp_var = os.path.isfile(command)
            #print(temp_var)
            if(temp_var == True):
                '''
                    folder one :- 0
                    file one   :- 0
                    hash one   :- 0

                    folder two :- 1
                    file two   :- 1
                    hash two   :-  
                '''
                command = drive_two_path + "/" + filename
                temp_var = hash_file(command)



                if(temp_var == file_hash_value):


                    '''
                        folder one :- 0
                        file one   :- 0
                        hash one   :- 0

                        folder two :- 1
                        file two   :- 1
                        hash two   :- 1
                    '''
                    #current_path = drive_two_path + "/"
                    #second_drive_path = drive_one_path
                    #command = 'rsync -avz --delete ' + current_path + ' ' + second_drive_path
                    #os.system(command)
                    os.mkdir(drive_one_path)
                    sync(drive_two_path, drive_one_path, 'sync', purge = True)

                else:
                    '''
                        folder one :- 0
                        file one   :- 0
                        hash one   :- 0

                        folder two :- 1
                        file two   :- 1
                        hash two   :- 0
                    '''
                    print("have to get data from FTP second file hash not same as og")

            else:
                '''
                    folder one :- 0
                    file one   :- 0
                    hash one   :- 0

                    folder two :- 1
                    file two   :- 0
                    hash two   :- 0
                '''
                print("have to get data from FTP file in secondary drive does not exsist")

        else:
            '''
                folder one :- 0
                file one   :- 0
                hash one   :- 0
                
                folder two :- 0
                file two   :- 0
                hash two   :- 0
            '''
            print("path to drive does not exsist")
            windows_message("Problem!!" , "path to both drive is wrong or does not exsist")




    else:

        '''
                folder one :- 1
                file one   :- 
                hash one   :- 
                
                folder two :- 
                file two   :- 
                hash two   :- 
        '''
        #exucutes if drive one exsist
        #print("come to this part")
        command = drive_one_path + "/" + filename
        temp_var = os.path.isfile(command) #check if file exsist
        
        #print(temp_var)
        #print("come here")
        
        
        if(temp_var == True):#if file exsist
            '''
                folder one :- 1
                file one   :- 1
                hash one   :- 
                
                folder two :- 
                file two   :- 
                hash two   :- 
            '''
            command = drive_one_path + "/" + filename
            temp_var = hash_file(command)#checks the hash of the file
            
            
            if(temp_var != file_hash_value):
                '''
                    folder one :- 1
                    file one   :- 1
                    hash one   :- 0

                    folder two :- 
                    file two   :- 
                    hash two   :- 
                '''
                #print('file hash value not equal')
                
                
                temp_var = os.path.exists(drive_one_path)
                if(temp_var == True):
                    '''
                        folder one :- 1
                        file one   :- 1
                        hash one   :- 0

                        folder two :- 1
                        file two   :- 
                        hash two   :- 
                    '''
                    command = drive_two_path + "/" + filename
                    temp_var = os.path.isfile(command)
                    if(temp_var == True):
                        '''
                            folder one :- 1
                            file one   :- 1
                            hash one   :- 0

                            folder two :- 1
                            file two   :- 1
                            hash two   :- 
                        '''
                        command = drive_two_path + "/" + filename
                        temp_var = hash_file(command)



                        if(temp_var == file_hash_value):
                            '''
                            folder one :- 1
                            file one   :- 1
                            hash one   :- 0

                            folder two :- 1
                            file two   :- 1
                            hash two   :- 1
                            '''
                            #current_path = drive_two_path + "/"
                            #second_drive_path = drive_one_path
                            #command = 'rsync -avz --delete ' + current_path + ' ' + second_drive_path
                            #os.system(command)
                            sync(drive_two_path, drive_one_path, 'sync', purge = True)




                        if(temp_var != file_hash_value):
                            '''
                            folder one :- 1
                            file one   :- 1
                            hash one   :- 0

                            folder two :- 1
                            file two   :- 1
                            hash two   :- 0
                            '''
                            print("have to get files from FTP")
                            


            else:
                '''
                    folder one :- 1
                    file one   :- 1
                    hash one   :- 1

                    folder two :- 
                    file two   :- 
                    hash two   :- 
                '''
                print("file hash in drive one is right")
                #drive one exsist folder exsist file exsist and hash is right in first folder
                
                #check secondary path if exsist
                temp_var = os.path.exists(drive_two_path)
                if(temp_var == True):
                    '''
                        folder one :- 1
                        file one   :- 1
                        hash one   :- 1

                        folder two :- 1
                        file two   :- 
                        hash two   :- 
                    '''
                    command = drive_two_path + "/" + filename
                    temp_var = os.path.isfile(command)


                    #now check if file exsist
                    if(temp_var == True):
                        '''
                            folder one :- 1
                            file one   :- 1
                            hash one   :- 1

                            folder two :- 1
                            file two   :- 1
                            hash two   :- 
                        '''

                       

                        #now check hash value
    

                        command = drive_two_path + "/" + filename
                        temp_var = hash_file(command)
                        #checking hash of second folder file




                        if(temp_var == file_hash_value):
                            '''
                                folder one :- 1
                                file one   :- 1
                                hash one   :- 1

                                folder two :- 1
                                file two   :- 1
                                hash two   :- 1
                            '''
                            #current_path = drive_one_path + "/"
                            #second_drive_path = drive_two_path
                            #command = 'rsync -avz --delete ' + current_path + ' ' + second_drive_path
                            #os.system(command)
                            sync(drive_one_path, drive_two_path, 'sync', purge = True)

                        
                        
                        
                        
                        else:
                            '''
                                folder one :- 1
                                file one   :- 1
                                hash one   :- 1

                                folder two :- 1
                                file two   :- 1
                                hash two   :- 0
                            '''
                            #current_path = drive_one_path + "/"
                            #second_drive_path = drive_two_path
                            #command = 'rsync -avz --delete ' + current_path + ' ' + second_drive_path
                            #os.system(command)
                            sync(drive_one_path, drive_two_path, 'sync', purge = True)

                            windows_message("Problem","computer may be comprimised")
                    
                    
                    
                    else:
                        '''
                            folder one :- 1
                            file one   :- 1
                            hash one   :- 1

                            folder two :- 1
                            file two   :- 
                            hash two   :- 
                        '''
                        #seconday path exsist but file does not exsist
                        #current_path = drive_one_path + "/"
                        #second_drive_path = drive_two_path
                        #command = 'rsync -avz --delete ' + current_path + ' ' + second_drive_path
                        #os.system(command)
                        sync(drive_one_path, drive_two_path, 'sync', purge = True)
                        windows_message("Problem","computer may be comprimised")
                


                #path to seconday folder does not exsist
                else:
                    '''
                        folder one :- 1
                        file one   :- 1
                        hash one   :- 1

                        folder two :- 0
                        file two   :- 
                        hash two   :- 
                    '''
                    #print("here")
                    os.mkdir(drive_two_path)
                    #current_path = drive_one_path + "/"
                    #second_drive_path = drive_two_path
                    #command = 'rsync -avz --delete ' + current_path + ' ' + second_drive_path
                    #os.system(command)
                    sync(drive_one_path, drive_two_path, 'sync', purge = True)
                    windows_message("Problem","computer may be comprimised")






        else:
            '''
                folder one :- 1
                file one   :- 0
                hash one   :- 
                
                folder two :- 
                file two   :- 
                hash two   :- 
            '''
            #print("nuck")
            #if test file does not exsist part but folder exsist


            #check if path two exist
            temp_var = os.path.exists(drive_two_path)
            if(temp_var == True):
                '''
                    folder one :- 1
                    file one   :- 0
                    hash one   :- 

                    folder two :- 1
                    file two   :- 
                    hash two   :- 
                '''

                #check if file exsist fir path two
                command = drive_two_path + "/" + filename
                temp_var = os.path.isfile(command)
                if(temp_var == True):
                    '''
                        folder one :- 1
                        file one   :- 0
                        hash one   :- 

                        folder two :- 1
                        file two   :- 1
                        hash two   :- 
                    '''
                    command = drive_two_path + "/" + filename
                    temp_var = hash_file(command)
                    if(temp_var == file_hash_value):
                        '''
                            folder one :- 1
                            file one   :- 0
                            hash one   :- 

                            folder two :- 1
                            file two   :- 1
                            hash two   :- 1
                        '''
                        #current_path = drive_two_path + "/"
                        #second_drive_path = drive_one_path
                        #command = 'rsync -avz --delete ' + current_path + ' ' + second_drive_path
                        #os.system(command)
                        sync(drive_two_path, drive_one_path, 'sync', purge = True)


                    else:
                        '''
                            folder one :- 1
                            file one   :- 0
                            hash one   :- 

                            folder two :- 1
                            file two   :- 1
                            hash two   :- 0
                        '''
                        print("have to get data from ftp")

                else:
                    '''
                        folder one :- 1
                        file one   :- 0
                        hash one   :- 

                        folder two :- 1
                        file two   :- 0
                        hash two   :- 
                    '''
                    print("have to get data from ftp") 
            else:
                '''
                    folder one :- 1
                    file one   :- 0
                    hash one   :- 

                    folder two :- 0
                    file two   :- 
                    hash two   :- 
                '''
                print("have to get files from FTP")




#os.system("clear")




#def ftp_server():


if (os_name == 'Linux'):
    count_num = 0
    os.system("clear")
    while True:
        
        print("***********************\n")
        linux()
        time.sleep(1)
        print("\n\n***********************\n")
        a = str(count_num)
        print("Number = " + a)
        count_num = count_num + 1

if (os_name == 'Windows'):
    count_num = 0
    os.system("cls")
    while True:
        print("***********************\n")
        windows_part()
        #command = drive_two_path + "/" + filename
        #print(hash_file(command))
        time.sleep(5)
        print("\n\n***********************\n")
        a = str(count_num)
        print("Number = " + a)
        count_num = count_num + 1
    
a = hash_file("/home/groot/Documents/projects/backup/final/backup/test area/one/pywin32_ctypes-0.2.0-py3-none-any.whl")

#a = hash_file('/media/groot/drive/projects/backup/test_area_v2/one/test')
print(a)

