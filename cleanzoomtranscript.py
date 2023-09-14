import io

def cleantranscript(filepath, removelinebreaks):
    endoflinewhitespace = " " if removelinebreaks else "\n"
    filesuffix = "_cleaned" + ("_nolinebreaks" if removelinebreaks else "") + ".txt"
    with io.open(filepath, "r", encoding="utf-8") as src:
        with io.open(filepath.replace(".cc.vtt", filesuffix), "w", encoding="utf-8") as dest:
            sline = src.readline()
            while len(sline) > 0:
                sline = sline.strip()
                if "WEBVTT" in sline or sline == "" or (":" in sline and "-->" in sline):
                    # skip this line
                    pass
                else:
                    dest.write(sline + endoflinewhitespace)
                sline = src.readline()
            dest.write("\n")

filepath = input("Enter full path for file of type .cc.vtt: ")
removelinebreaks = input("This utility always removes timing information and blank lines.\nDo you ALSO want to remove the arbitrary line breaks that\nzoom inserts every 15 or so words? Enter either 'y' or 'n'. ").lower()
cleantranscript(filepath, removelinebreaks)
