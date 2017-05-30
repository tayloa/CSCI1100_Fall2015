from PIL import Image
import panoramio as pan
import lab4_check2helper as helper
address = raw_input("Enter an address ==> ")
imagenumber = 4
urls = pan.getPhotos(address, imagenumber)
blankdoc = Image.new('RGB',(512,512),'white')
if len(urls) >= 4:
    im1 = pan.openphoto(urls[0])
    im2 = pan.openphoto(urls[1])
    im3 = pan.openphoto(urls[2])
    im4 = pan.openphoto(urls[3])
    im1 = helper.make_square(im1)
    im2 = helper.make_square(im2)
    im3 = helper.make_square(im3)
    im4 = helper.make_square(im4)
    resize1 = im1.resize((256,256))
    resize2 = im2.resize((256,256))
    resize3 = im3.resize((256,256))
    resize4 = im4.resize((256,256))
    blankdoc.paste(resize1, (0,0))
    blankdoc.paste(resize2, (256,0))
    blankdoc.paste(resize3, (0,256))
    blankdoc.paste(resize4, (256,256))
    blankdoc.show()
else:
    print "Sorry I couldn't find enough pictures"
    