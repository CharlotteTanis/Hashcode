import csv
from operator import itemgetter
from collections import OrderedDict

fp = "kittens.in"

def Preparefile(fp):
    videos_list = {}

    with open(fp, "rb") as fileVideos:

        reader_videos = csv.reader(fileVideos, delimiter=" ")

        counter = 0
        for videos in reader_videos:
            if counter == 0:
                V = int(videos[0])
                E = int(videos[1])
                R = int(videos[2])
                C = int(videos[3])
                X = int(videos[4])
                counter += 1
                continue

            if counter == 1:
                for i in range(0, V):
                    videos_list[i] = int(videos[i])
                break

    sorted_dict = sorted(videos_list.items(), key=lambda x:x[1], reverse=True)

    servers = {}
    server_id = 0
    mbs = 0
    temp_vid = []
    for videos in sorted_dict:
        if server_id > (C - 1):
            break
        if mbs + videos[1] < X:
            mbs += videos[1]
            temp_vid.append(videos[0])
            continue
        else:
            mbs = 0
        servers[server_id] = temp_vid
        server_id += 1
        temp_vid = []

    print server_id
    for server in servers:
        print server, " ".join(map(str,servers[server]))

Preparefile(fp)
