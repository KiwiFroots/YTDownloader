import youtube_dl
import shutil

savedir = ""

ydl_opts = {
    'format': 'bestaudio/best',
    'quiet': True,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

def confirmTitle(title_raw, title, artist):
    confirm = input("Is this correct?\n\n(Raw Video Title: {})\n\nTitle: {}\nArtist: {}\n\n(y/n):".format(title_raw, title, artist))
    if confirm == "y":
        format = title + ' - ' + artist
    else:
        new_title = input("Please tell me what the video should be called: ")
        format = new_title
    return format


videos = open(("videos.txt"), "r").readlines()
for video in range(0, (len(videos))):
    link = videos[video][:-1]
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Getting Meta Data for {}".format(link))
        meta = ydl.extract_info(link)
        print("{} is uploaded by '{}', and has {} views.".format(meta['title'], meta['uploader'], meta['view_count']))
        ydl.download([link])
		
		
        string = meta["title"]
        title_raw = meta["title"]
        if "remix" not in string.lower():
            string = string.split("-")
            title = string[1].strip(" ")
            artist = string[0].strip(" ")
            if "(" or "[" in title:
                if "(" in title:
                    title = title.split("(")
                elif "[" in title:
                    title = title.split("[")
                title = title[0]
                print(title.strip(" "))
                title = title.strip(" ")
        else:
            title_finder = string.split("-")
            string_remix = string.split(" ")
            derpy = string.lower().split(" ")
            derp = string.split("(")
            print(string_remix)
            index = derpy.index("remix)")
            print(string_remix[index-1])
            if "(" in string_remix[index-1]:
                artist = string_remix[index-1][1:]
                title = title_finder[1].strip(" ({}".format(derp[1]))
            elif "(" in string_remix[index-2]:
                artist = string_remix[index - 2][1:]
                artist = artist + " " + string_remix[index -1]
                title = title_finder[1].strip(" ({}".format(derp[1]))
            elif "(" in string_remix[index - 3]:
                artist = string_remix[index - 3][1:]
                artist = artist + " " + string_remix[index - 2]
                artist = artist + " " + string_remix[index - 1]
                title = title_finder[1].strip(" ({}".format(derp[1]))
        print("Title: {}\nArtist: {}".format(title, artist))
        if ("(" in (title + " - " + artist)) or ("[" in (title + " - " + artist)) or ("ft " in (title + " - " + artist)) or ("feat " in (title + " - " + artist)):
            confirm = confirmTitle(title_raw, title, artist)
            final_format = confirm
        else:
            final_format = title + ' - ' + artist
			
			
			
        dir = savedir + meta['title'] + '.mp3'
        shutil.move(meta["title"] + "-" + meta["id"] + ".mp3", dir)
        print("Successfully downloaded {} and uploaded it to {}".format(meta["title"], dir)) 
print("Successfully downloaded all videos in list!")
