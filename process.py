import os
from shutil import copyfile
import base64
import csv
import os
from tqdm import tqdm


def extract(tsv_path,outputDir):
    print('Extracting ......')
    with open(tsv_path, 'r') as tsvF:
        reader = csv.reader(tsvF, delimiter='\t')
        count = 0
        for row in tqdm(reader):
            MID, imgSearchRank, faceID, data = row[0], row[1], row[4], base64.b64decode(row[-1])

            saveDir = os.path.join(outputDir, MID)
            savePath = os.path.join(saveDir, "{}-{}.jpg".format(imgSearchRank, faceID))

            if not os.path.exists(saveDir):
                os.makedirs(saveDir)

            with open(savePath, 'wb') as f:
                f.write(data)

            count += 1

    print("Extract {} images".format(count))


def clean(imgFolder,cleanFolder,washList):
    print('Cleaning ......')
    wlFile = open(washList, 'r')
    goodFiles = wlFile.readlines()
    goodFiles = [f.strip('\n ') for f in goodFiles]
    goodFiles = [f.strip('\r ') for f in goodFiles]

    count = 0
    for goodFile in tqdm(goodFiles):
        filename, label = goodFile.split(' ')
        filepath = os.path.join(imgFolder, filename)

        if os.path.exists(filepath):
            count += 1

            cleanpath = os.path.join(cleanFolder, label)
            if not os.path.exists(cleanpath):
                os.makedirs(cleanpath)
                print("makedirs {}".format(cleanpath))
            cleanpath = os.path.join(cleanpath, filename.split('/')[-1])

            copyfile(src=filepath, dst=cleanpath)
    print('Clean {} images'.format(count))


def relabel_cleaner(imgFolder,relabelFolder,relabelList):
    print('Relabeling ......')
    wlFile = open(relabelList, 'r')
    goodFiles = wlFile.readlines()
    goodFiles = [f.strip('\n ') for f in goodFiles]
    goodFiles = [f.strip('\r ') for f in goodFiles]

    count = 0
    for goodFile in tqdm(goodFiles):
        label, filename = goodFile.split(' ')
        filepath = os.path.join(imgFolder, filename)

        if os.path.exists(filepath):
            count += 1

            cleanpath = os.path.join(relabelFolder, label)
            if not os.path.exists(cleanpath):
                os.makedirs(cleanpath)
            cleanpath = os.path.join(cleanpath, filename.split('/')[-1])

            copyfile(src=filepath, dst=cleanpath)

    print("Relabel {} images".format(count))    



if __name__ == "__main__":
    tsv_path = './MS-Celeb-1M/data/aligned_face_images/FaceImageCroppedWithAlignment.tsv'
    imgFolder = './imgs'
    cleanFolder = './clean_imgs'
    washList = 'MS-Celeb-1M_clean_list.txt'
    relabelFolder = './relabel_imgs'
    relabelList = 'relabel_list_128Vec_T058.txt'

    extract(tsv_path,imgFolder)
    clean(imgFolder,cleanFolder,washList)
    relabel_cleaner(imgFolder,relabelFolder,relabelList)

