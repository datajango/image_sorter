import os 
import json



def get_filesystem(fs_root):
    ''' Get Filesystem Under fs_root and return as python dict '''

    # GET ITEM PARENT DURING DICTIONARY CREATION
    data = {"name": os.path.basename(fs_root)}
    if os.path.isdir(fs_root):
        data["type"] = "directory"
        data["children"] = [get_filesystem(os.path.join(fs_root, x)) for x in os.listdir\
            (fs_root)]
    else:
        data["type"] = "file"
    return data

# SAVE FILESYSTEM TO JSON FILE
with open("./test_db.json", "w") as file:
    json.dump(get_filesystem("/home/rob/Documents/lfs207"), file)


def find_all_image_files():
    with open("./test_db.json", "r") as file:
        data = dict(json.load(file))

    # IF TYPE IS DIRECTORY RETRIEVE DIRECTORY NAME FOR FURTHER ACCESS
    # ELSE check if file is == *.png
    # create index for items
    for key in data:
        if data["children"][0]["name"]:
            directory = data["children"][0]["name"]
            print(data["children"][0]["name"])
            


find_all_image_files()