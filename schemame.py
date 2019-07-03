import os,sys,json,subprocess
com="sudo apt-get -y install python3-pip"
command="sudo pip3 -q install genson"
command2="sudo pip3 -q install jsonschema"
command0="python3 -m pip -q install --upgrade pip"
try:
	check=subprocess.check_output(["dpkg","-V","python3-pip"])
	if len(check)>0:
		print("Upgrading your Pip3 packages")
		os.system(command0)
except subprocess.CalledProcessError:
	print("Missing Package PIP3 (installing...)")
	os.system(com)
try:
	import jsonschema
except:
	print("Missing 'JsonSchema' module is installing")
	os.system(command2)
	import jsonschema
try:
	import genson
except:
	print("Missing 'Genson' module is installing")
	os.system(command)
	import genson
from jsonschema import validate
from genson import SchemaBuilder
while True:
    print(""" 
****\Schema Controller/****
    Schema Checker - 1
    Schema Builder - 2
    Exit - 3""")
    choice = input("    Choice :")
    if choice=="3":
        break
    elif choice=="2":
        print("""
****\Schema Builder/****""")
        try:
            json_path = input("    Data File Path (E.g : /home/pi/data.json):")
            json_file=open(json_path,"r+")
            js=json.load(json_file)
            builder = SchemaBuilder()
            schema_path = input("    Path to Schema that you wanted to create (E.g : /home/pi/schema.json): ")
            x=schema_path.split(".")
            if len(x)<2:
                raise FileNotFoundError()
            elif schema_path.find(".")== -1:
                raise FileNotFoundError()
            schema_file=open(schema_path,"x")
            schema_file = open(schema_path, "w+")
            builder.add_object(js)
            schema=builder.to_schema()
            json.dump(schema,schema_file,indent=4)
        except ValueError:
            print("    Wrong Path Input")
        except FileNotFoundError:
            print("    Wrong Path Input")

        turn = input("""  
    Main Menu - 1
    Exit - 0
    Choice : """)
        if turn == "1":
            continue
        elif turn == "0":
            exit(0)
        else:
            print("    Wrong Input (Returning to Main Menu...)")
            continue
    elif choice=="1":
        print("""
****\Schema Checker/***""")
        try:
            schema_path=input("    Schema Path (E.g : /home/pi/schema.json):")
            json_path = input("    Data File Path (E.g : /home/pi/data.json):")
            schema_file=open(schema_path,"r+")
            json_file=open(json_path,"r+")
            js=json.load(json_file)
            schema=json.load(schema_file)
            if validate(js, schema=schema)== None:
                print("    Your file is valid")
        except ValueError:
            print("    Wrong Input!")
        except FileNotFoundError:
            print("    Wrong Path Input")
        except jsonschema.exceptions.SchemaError:
            print("    Schema Causes Error")
        except jsonschema.exceptions.ValidationError:
            print("    Your file is not valid")
        turn = input("""  
    Main Menu - 1
    Exit - 0
    Choice : """)
        if turn == "1":
            continue
        elif turn == "0":
            exit(0)
        else:
            print("    Wrong Input (Returning to Main Menu...)")
            continue

    else:
        print("    Wrong Input!")
        continue
