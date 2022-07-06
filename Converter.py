import json
import os

def ConvFile(File):
        f = open(File)
        fData = f.read()
        f.close()

        u_Titles = fData.split("""</key>
            <dict>""")

        u_Pos = fData.split("""</key>
                <string>{{""")

        u_Size = fData.split("""ceSize</key>
                <string>{""")

        u_Offset = fData.split("""ffset</key>
                <string>{""")
        u_Pos.pop(0)
        u_Size.pop(0)
        u_Offset.pop(0)

        Converted = {}

        for i in range(len(u_Titles)-1):
                #Get Image Name
                t_End = u_Titles[i][::-1].find(">")
                title = u_Titles[i][::-1][0:t_End][::-1]
                #Get the Position
                p_End = u_Pos[i].find("}")
                pos = u_Pos[i][0:p_End]
                #Get the Size
                s_End = u_Size[i].find("}")
                size = u_Size[i][0:s_End]
                #Get the Offset
                o_End = u_Offset[i].find("}")
                offset = u_Offset[i][0:o_End]
                
                FName = File[3:len(File)-6]
                Converted[FName+"/"+title] = {"Positon":{},"Size":{},"Offset":{}}
                Converted[FName+"/"+title]["Positon"] = pos.split(",")
                Converted[FName+"/"+title]["Size"] = size.split(",")
                Converted[FName+"/"+title]["Offset"] = offset.split(",")
                
        return Converted

Dirs = {"LD","MD","HD"}

for Dir in Dirs: 
        Final = {}
        for File in os.listdir(Dir):
                Final = Final | ConvFile(Dir+"/"+File)
                print(File +" Converted Successfully")

        print("-------------------------")
        print(Dir+" Converted Successfully")
        print("-------------------------")

        f = open(Dir+"_GameSheet.json","w")
        f.write(json.dumps(Final, indent=4))
        f.close()