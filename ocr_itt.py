from tesserocr import PyTessBaseAPI

import argparse
parser = argparse.ArgumentParser("Enter full path for the image")
parser.add_argument('-i' , '--image' , help="Image Path")
args = parser.parse_args()

images = ['b.jpg']
images[0] = args.image

with PyTessBaseAPI() as api:
    for img in images:
        api.Init(lang = 'hin')
        api.SetImageFile(img)
        arr = list(api.AllWordConfidences())
        sumarr = sum(arr) / float(len(arr))


with PyTessBaseAPI() as api:
    for img in images:
        api.Init(lang = 'eng')
        api.SetImageFile(img)
        arr2 = list(api.AllWordConfidences())
        sumarr2 = sum(arr2) / float(len(arr2))



with PyTessBaseAPI() as api:
    for img in images:
        api.Init(lang = 'spa')
        api.SetImageFile(img)
        arr3 = list(api.AllWordConfidences())
        sumarr3 = sum(arr3) / float(len(arr3))



if (sumarr > sumarr2) & (sumarr > sumarr3):
        print ("Hindi")
        print("Confidence score is " + str(sumarr))
        api.Init(lang = 'hin')

elif (sumarr2 > sumarr) & (sumarr2 > sumarr3):
        print("English")
        print("Confidence score is " + str(sumarr2))
        api.Init(lang = 'eng')
        api.SetImageFile(images[0])

else:
        print("Spanish")
        print("Confidence score is " + str(sumarr3))
        api.Init(lang = 'spa')
        api.SetImageFile(images[0])
