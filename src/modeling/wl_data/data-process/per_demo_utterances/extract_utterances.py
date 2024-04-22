import os
import copy
import json
base_direc = "/home/kapmcgil/scratch/weblinx/modeling/wl_data/demonstrations"
recursive = False

# get all the demos from this folder
for dirpath, dirs, filenames in os.walk(base_direc):
    demos = copy.deepcopy(dirs)
    if not recursive:
        while len(dirs) > 0:
            dirs.pop()
    # print(f"dirpath is {dirpath}")
    # print(f"dirs are {dirs}")
    # print(f"retrieved demos are {demos}")
    # print(f"filenames are {filenames}")  

    # only consider the demo subdirectories - store the utterances in a separate file for each demo
    # pick only the demos from the validation set
    valid = [
    "ygprzve",
    "saabwsg",
    "iqaazif",
    "eiblold",
    "pjzqiar",
    "polclhz",
    "hvdwmnq",
    "feupcgi",
    "hdbpxqn",
    "bdhiwrz",
    "kjcptgq",
    "bonfxww",
    "vyetbcl",
    "eaozdtr",
    "dpftfrs",
    "qjmnlfs",
    "aoxxcdg",
    "orlmkas",
    "lmvcfan",
    "rkocbdj",
    "hczoeyj",
    "ausjykw",
    "dvjohpf",
    "fgauuld",
    "iwlxwud",
    "udjldbi",
    "sekzawr",
    "trcpsdd",
    "iftpibh",
    "kdwvicy",
    "krunuah",
    "wzqkdds",
    "pwxzusu",
    "aopjpga",
    "zclcedx",
    "gudlwyv",
    "ydmcvnf",
    "swfuumj",
    "vchfjig",
    "wfenvck",
    "qmivsau",
    "nqriyhc",
    "zhtyqxk",
    "bexvmyx",
    "lxqfsxo",
    "pwmhuww",
    "dvzglkv",
    "jkkxytb",
    "fzcutlb",
    "pkeloan",
    "gwttfmm",
    "hkqclvm",
    "lkgrxmb",
    "ygiqsqg",
    "jxlnhgo",
    "apfyesq",
    "xmqpqbt",
    "bdfglfk",
    "fquqaqa",
    "xmdekwj",
    "ouuikrj",
    "oxkhiig",
    "wpnexuj",
    "fxhsqxo",
    "iizwcsj",
    "emwxcyh",
    "ytzwgym",
    "vstsutl",
    "sbvtquk",
    "lldtscr",
    "nzieebh",
    "snviznd",
    "vdkltrr",
    "wlglvuu",
    "ijeqdyc",
    "eivbwev",
    "uoprmwb",
    "bessdxh",
    "yluipwa",
    "pwmfnzz",
    "cdfkxtv",
    "ijznayd",
    "cxtzcfw",
    "alxehej",
    "iwjtiqn",
    "xrfcbfd",
    "bapevgx",
    "gtpjzzv",
    "zojfjna",
    "yvncuvj",
    "gmhajlo",
    "friuisw",
    "wbsesgi",
    "aqahzgs",
    "erjwhjk",
    "phxrovm",
    "sfkjodl",
    "iziouhr",
    "kaxzpgm",
    "ejryoez"
  ]
    demo_set = set(demos)
    valid_set = set(valid)
    if len(demo_set) != len(demos) and len(valid_set) != len(valid):
        print("ERROR: Some of the demos were missed.")
    
    demo_chats = {}
    # make sure that the demos are in the validation set
    for valid_demo in valid_set:
        # get replay.json for each demo then extract values
        replay_demo = os.path.join(base_direc, valid_demo, "replay.json")
        with open(replay_demo, "r") as replay_file:
            replay = json.load(replay_file)
        
        chat_list = []
        for dict_item in replay["data"]:
            if "utterance" in dict_item.keys():
                chat_list.append(dict_item)
        
        demo_chats[valid_demo] = chat_list
        
    with open("extracted_chats.json", "w") as write_chats:
        json.dump(demo_chats, write_chats)
    
          
    
