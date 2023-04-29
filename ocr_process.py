import easyocr,numpy
from PIL import Image
image = Image.open('img_crop/crop_1.png')
image.show()
reader = easyocr.Reader(['ch_sim','en']) # 只需要运行一次就可以将模型加载到内存中
result = reader.readtext(numpy.asarray(image),detail=0)
# result = reader.readtext('img/3.jpg',detail=0)
print(result)
