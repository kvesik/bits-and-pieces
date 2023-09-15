import io


def cleantranscript(filepath, removetiminginformation, removeblanklines, removelinebreaks):
    endoflinewhitespace = " " if removelinebreaks else "\n"
    filesuffix = "_cleaned" + ("_notiming" if removetiminginformation else "") + ("_noblanklines" if removeblanklines else "") + ("_nolinebreaks" if removelinebreaks else "") + ".txt"
    with io.open(filepath, "r", encoding="utf-8") as src:
        with io.open(filepath.replace(".cc.vtt", filesuffix), "w", encoding="utf-8") as dest:
            sline = src.readline()
            while len(sline) > 0:
                sline = sline.strip()
                skipthisline = "WEBVTT" in sline
                if removetiminginformation:
                    skipthisline = skipthisline or (":" in sline and "-->" in sline)
                if removeblanklines:
                    skipthisline = skipthisline or (sline == "")
                if not skipthisline:
                    dest.write(sline + endoflinewhitespace)
                sline = src.readline()
            dest.write("\n")

filepath = input("Enter full path for file of type .cc.vtt: ")
removetiminginformation = input("Would you like to remove timing information from each line? Enter 'y' or 'n'. ").lower() == "y"
removeblanklines = input("Would you like to remove the blank line between each line of text? Enter 'y' or 'n'. ").lower() == "y"
removelinebreaks = False if (not removeblanklines or not removetiminginformation) else input("Would you like to remove the arbitrary line breaks that zoom inserts every 15 or so words? Enter 'y' or 'n'. ").lower() == "y"
cleantranscript(filepath, removetiminginformation, removeblanklines, removelinebreaks)
