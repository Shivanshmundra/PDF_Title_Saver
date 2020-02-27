import argparse
import os
import pdftitle 

parser = argparse.ArgumentParser(description='Save Paper with Titles')
parser.add_argument('--folder', type=str, 
                    help='folder name')
args = parser.parse_args() 


files_list = os.listdir(args.folder)

for file in files_list:

  file_loc = str(args.folder + "/" + file)
  if(os.path.exists(file_loc)):
    print(file_loc)
    returned_value = os.system("pdftitle -p {} > temp_file_name".format(file_loc))
    with open("temp_file_name", "r") as f:
      name = f.read()
      if(len(name) <= 2):
        continue
      name = name.strip()
      new_name = args.folder + "/" + name
      new_name = str(new_name).replace(" ", "_")
      if os.path.exists(new_name):
        continue
      os.system("mv {} {}".format(file_loc, new_name))
      os.system("rm temp_file_name")
  else:
    print("File not found")
