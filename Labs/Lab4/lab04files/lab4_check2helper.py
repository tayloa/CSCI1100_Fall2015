from PIL import Image
def make_square(im):
    imsize = im.size
    if imsize[0] > imsize[1]:
        imsquare = im.crop((0,0,imsize[1],imsize[1]))
    elif imsize[1] > imsize[0]:
        imsquare = im.crop((0,0,imsize[0],imsize[0]))
    return imsquare



