from pdf2image import convert_from_path

import layoutparser as lp
import cv2

images=convert_from_path('hdfc.pdf')

for i in range(len(images)):
    images[i].save('pages/page'+str(i)+'.jpg','JPEG')


image = cv2.imread("/home/abhishek/Desktop/desktop(P.S)/csv/pages/page0.jpg")
image = image[..., ::-1]

# load model
model = lp.PaddleDetectionLayoutModel(config_path="lp://PubLayNet/ppyolov2_r50vd_dcn_365e_publaynet/config",
                                threshold=0.5,
                                label_map={0: "Text", 1: "Title", 2: "List", 3:"Table", 4:"Figure"},
                                enforce_cpu=False,
                                enable_mkldnn=True)
# detect
layout = model.detect(image)
print(layout)
# for l in layout:
#     if l.type=='Table':
#         x_1=int(l.block.x_1)
#         y_1=int(l.block.y_1)
#         x_2=int(l.block.x_2)
#         y_2=int(l.block.y_2)

#         break

# im=cv2.imread('/home/abhishek/Desktop/desktop(P.S)/csv/pages/page0.jpg')

# cv2.imwrite('ext_im.jpg' , im[y_1:y_2,x_1:x_2])
