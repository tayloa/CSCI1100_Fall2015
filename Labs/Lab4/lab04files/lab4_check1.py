from PIL import Image
blankdoc = Image.new('RGB',(512,512),'white')
image1 = Image.open('ca.jpg')
image2 = Image.open('hk.jpg')
image3 = Image.open('bw.jpg')
image4 = Image.open('im.jpg')
resize1 = image1.resize((256,256))
resize2 = image2.resize((256,256))
resize3 = image3.resize((256,256))
resize4 = image4.resize((256,256))
blankdoc.paste(resize1, (0,0))
blankdoc.paste(resize2, (256,0))
blankdoc.paste(resize3, (0,256))
blankdoc.paste(resize4, (256,256))
blankdoc.save('paste1')


