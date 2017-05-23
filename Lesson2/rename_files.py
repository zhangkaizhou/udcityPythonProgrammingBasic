import os

def rename_files():
    #(1) get file name from a floder
    file_list = os.listdir(r"D:\iCloudDrive\Documents\Practice\Python\udcityPython\Lesson1\prank")
    #print(file_list)
    saved_path = os.getcwd()
    print("Current Working Directory is " + saved_path)
    os.chdir(r"D:\iCloudDrive\Documents\Practice\Python\udcityPython\Lesson1\prank")

    #(2) for each file, rename filename
    for file_name in file_list:
        print("Old Name - " + file_name)
        print("New Name - " + file_name.translate(None, "1234567890"))
        os.rename(file_name,file_name.translate(None, "1234567890"))
    os.chdir(saved_path)    

rename_files()
