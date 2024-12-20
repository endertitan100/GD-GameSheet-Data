import os
from multiprocessing import Pool

def ToJson(Converted):
        jsonString = "{\n"
        for Item in Converted:
                FName = Converted[Item]
                jsonString += '"'+Item+'":{'
                jsonString += '"Position":['+FName["Position"][0]+","+FName["Position"][1]+"],"
                jsonString += '"Size":['+FName["Size"][0]+","+FName["Size"][1]+"],"
                jsonString += '"Offset":['+FName["Offset"][0]+","+FName["Offset"][1]+"]},\n"
                
        jsonString = jsonString[0:len(jsonString)-2] + "\n}"
        return jsonString

def ConvFile(File):
        f = open(File)
        fData = f.read()
        f.close()

        u_Titles = fData.split("""</key>
            <dict>""")

        u_Pos = fData.split("""</key>
                <string>{{""")

        u_Size = fData.split("}}")

        u_Offset = fData.split("""ffset</key>
                <string>{""")
        u_Pos.pop(0)
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
                s_End = u_Size[i][::-1].find("{")
                size = u_Size[i][::-1][0:s_End][::-1]
                #Get the Offset
                o_End = u_Offset[i].find("}")
                offset = u_Offset[i][0:o_End]
                
                FName = File[3:len(File)-6]
                Converted[FName+"/"+title] = {"Position":[],"Size":[],"Offset":[]}
                Converted[FName+"/"+title]["Position"] = pos.split(",")
                Converted[FName+"/"+title]["Size"] = size.split(",")
                Converted[FName+"/"+title]["Offset"] = offset.split(",")
        return Converted


if __name__ == "__main__":
        Dirs = {"LD","MD","HD"} 

        for Dir in Dirs: 
                Final = {}
                with Pool() as pool:
                        out = pool.imap(ConvFile,[Dir+"\\"+i for i in os.listdir(Dir)])
                        for i in out:
                                Final = Final | i

                #for File in os.listdir(Dir):
                #        Final = Final | ConvFile(Dir+"/"+File)

                Out = ToJson(Final)

                print("-------------------------")
                print(Dir+" Converted Successfully")
                print("-------------------------")

                f = open(Dir+"_GameSheet.json","w")
                f.write(Out)
                f.close()