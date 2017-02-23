import csv

fp = "kittens.in"

def Preparefile(fp):


    with open(fp, "rb") as fileVideos:

        reader_videos = csv.reader(fileVideos, delimiter=" ")

        for videos in reader_videos:
            V = videos[0]
            E = videos[1]
            R = videos[2]
            C = videos[3]
            X = videos[4]
            break

        for videos in reader_videos:
            


        # print reader_videos[0]

        #
        #
        # r = 0
        #
        # for videos in reader_videos:
        #     for c in range(0, column):
        #         video[c] = V
        #
        #         pizza[(r, c)] = ingredients[c]
        #     r += 1

    # for i in range(0, 6):
    #         print pizza[(i,0)], pizza[(i,1)], pizza[(i,2)], pizza[(i,3)], pizza[(i,4)], pizza[(i,5)], pizza[(i,6)]

    # print pizza

Preparefile(fp)
