import os

# define a function:
# ------------------
def rename_files():
    #(1) get file names from a folder:
    file_list = os.listdir(r"/Users/peterdo/dev/python/lesson-2/rename/prank")
    #print file_list

    # save the current working folder path:
    saved_path = os.getcwd()
    #print("Current working directory is: " + saved_path)

    # change the current working folder path to the new path:
    os.chdir(saved_path + "/prank")

    #(2) for each file, remane filename:
    for file_name in file_list:
        print("Old name: " + file_name)
        print("New name: " + file_name.translate(None, "0123456789"))
        
        os.rename(file_name, file_name.translate(None, "0123456789")) 

    # change the working folder back to the old path:
    os.chdir(saved_path)

# run the function:
# ------------------
rename_files()