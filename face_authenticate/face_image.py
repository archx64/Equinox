import pickle
import cv2
import imutils
import os
import face_recognition

from django_project import settings

data = pickle.loads(open("encodings_final.pickle", "rb").read())


def main():
    path = settings.MEDIA_ROOT
    os.chdir(path)
    files = sorted(os.listdir(os.getcwd()), key=os.path.getmtime)
    newest = files[-1]
    image_file = str(newest)

    image = cv2.imread(image_file)
    resized = imutils.resize(image, width=360)
    rgb = cv2.cvtColor(resized, cv2.COLOR_BGR2RGB)

    boxes = face_recognition.face_locations(rgb, model="cnn")
    encodings = face_recognition.face_encodings(rgb, boxes, 1)

    names = []

    for encoding in encodings:

        matches = face_recognition.compare_faces(data["encodings"], encoding, 0.4)
        name = "Unknown"

        if True in matches:
            matchedIds = [i for (i, b) in enumerate(matches) if b]
            counts = {}

            for i in matchedIds:
                name = data["names"][i]
                counts[name] = counts.get(name, 0) + 1

            name = max(counts, key=counts.get)

        names.append(name)

        if 0 < len(names) < 2 and names[0] != 'Unknown':
            return names[0]

        else:
            return 'facial recognition confused'
