from tesserocr import PyTessBaseAPI

import argparse
parser = argparse.ArgumentParser("Enter Image Path")
parser.add_argument('-i' , '--image' , help="Image Path")
args = parser.parse_args()

images = ['b.jpg']
images[0] = args.image
count = 0
count2 = 0
count3 = 0
with PyTessBaseAPI() as api:
    for img in images:
        api.Init(lang = 'hin')
        api.SetImageFile(img)
        # print api.AllWordConfidences()
        arr = list(api.AllWordConfidences())
        sumarr = sum(arr) / float(len(arr))


with PyTessBaseAPI() as api:
    for img in images:
        api.Init(lang = 'eng')
        api.SetImageFile(img)
        # print api.AllWordConfidences()
        arr2 = list(api.AllWordConfidences())
        sumarr2 = sum(arr2) / float(len(arr2))



with PyTessBaseAPI() as api:
    for img in images:
        api.Init(lang = 'spa')
        api.SetImageFile(img)
        # print api.AllWordConfidences()
        arr3 = list(api.AllWordConfidences())
        sumarr3 = sum(arr3) / float(len(arr3))


n = min(len(arr) , len(arr2) , len(arr3))
for i in range(0 , n):
    if (arr[i] > arr2[i]) & (arr[i] > arr3[i]):
        count += 1
    elif (arr2[i] > arr[i]) & (arr2[i] > arr3[i]):
        count2 += 1
    elif (arr3[i] > arr[i]) & (arr3[i] > arr2[i]):
        count3 += 1
    else:
        pass


if (count3 > count2) & (count3 > count):
        print("Spanish")
        print("Confidence score is " + str(sumarr3))
        api.Init(lang = 'spa')
        api.SetImageFile(images[0])
elif (count2 > count) & (count2 > count3):
        print("English")
        print("Confidence score is " + str(sumarr2))
        api.Init(lang = 'eng')
        api.SetImageFile(images[0])
else:
        print ("Hindi")
        print("Confidence score is " + str(sumarr))
        api.Init(lang = 'hin')
        api.SetImageFile(images[0])
        
