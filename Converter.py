

def ConvFile(File):
    f = open(File)
    fData = f.read()
    f.close()

    u_Titles = fData.split("""</key>
            <dict>""")

    u_Pos = fData.split("""</key>
                <string>{{""")
    u_Pos.pop(0)

    for i in range(len(u_Titles)-1):
        #Get the Title
        #print(u_Titles[i])
        t_End = u_Titles[i][::-1].find(">")
        title = u_Titles[i][::-1][0:t_End][::-1]
        #Get the Position
        p_End = u_Pos[i].find("}")
        pos = u_Pos[i][0:p_End]
        #TODO GET SIZE AND OFFSET


        print(title,pos)

ConvFile("SD/DungeonSheet.plist")