import glob
import shutil

import os
path = "/home/jayakumar/python-tests/"

error_logs_directory = "/home/jayakumar/pytho-error/"

result = os.listdir(path)

print(result)

for file_name in result:
    with open(path+file_name) as current_file:
        file_content = current_file.read()
        if "error"  in file_content:
            print("word error found in the file:  {}".format(file_name))
            print("Printing the contents of this file here \n ==============================================\n")
            print(file_content)
            dest_file = error_logs_directory+file_name
            src_file = path+file_name
            print("Now copying file:{} from :{} location to :{}".format(file_name,path,error_logs_directory))

            if not os.path.exists(error_logs_directory):
                os.mkdir(error_logs_directory)

            shutil.copy(src_file, dest_file)

        else:
            print("No words found from the search operation inside the file :{}".format(file_name))
        print("=====================================")


