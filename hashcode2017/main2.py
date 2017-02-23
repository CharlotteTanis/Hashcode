import csv

fp = "me_at_the_zoo.in"

def Preparefile(fp):
    videos_list = {}
    endpoints = {}

    with open(fp, "rb") as fileVideos:

        reader_videos = csv.reader(fileVideos, delimiter=" ")
        end_id = 0
        counter = 0
        temp = []
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
                    counter += 1

            else:
                if int(videos[0]) < 100:
                    temp.append(videos[0])
                    print end_id, "id"
                    print videos[0]
                    continue

                endpoints[end_id] = temp
                temp = []
                end_id += 1

        print endpoints


    servers = {}
    server_id = 0
    mbs = 0
    temp_vid = []
    for video in videos_list:
        if server_id > (C - 1):
            break
        if mbs < X:
            mbs += videos_list[video]
            temp_vid.append(video)
            continue

        servers[server_id] = temp_vid
        server_id += 1
        temp_vid = []
        mbs = 0

    # print server_id
    # for server in servers:
    #     print server, servers[server][1:]

Preparefile(fp)
