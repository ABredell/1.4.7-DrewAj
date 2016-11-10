# Problem 1.4.7
# A.J. Bredell & Drew Donaldson
# 11/08/2016
# The program takes an image gives you the option to crop it to a square, then frames it allowing you to choose a color


from PIL import Image, ImageDraw, ImageFont
def squareCrop(picture):
    ''' Allows the user to crop the image to a 768x768 square '''

    lengthChange = 0
    heightChange = 0
    if width > 1000:
        lengthChange = width - 1000 
    if height > 1000:
        heightChange = height - 1000
    left = int(lengthChange)//2
    top = int(heightChange)//2
    right = (width - int(lengthChange)//2)
    bottom = (height - int(heightChange)//2)
    
    newImg = picture.crop((left, top, right, bottom))
    newImg.load()
    return newImg
    
    
def textAdd(picture):
    ''' Allows the user to write the image '''
    # get a font
    font = ImageFont.truetype(filename="xssnb.ttf", size = 30)
    # get a drawing context
    d = ImageDraw.Draw(picture)
    message = input("Write a message to place on the photo: ")
    d.text((50,50), message, font=font, fill=(255,255,255))
    return picture

def Frame(picture):
    ''' Allows the user to add a frame around the image '''
    width, height = picture.size # defines image size x,y
    frameColor = input("Would you like your border Red, Blue, Green, Yellow, or Black? ")
    thickness = int(input("How thick in pixels would you like the border? "))
    newWidth = width + (thickness*2)
    newHeight = height + (thickness*2)
    frame = Image.new('RGB', (newWidth, newHeight), frameColor)
    frame.paste(picture, (thickness,thickness))
    frame.show()


if __name__ == "__main__":
    
    
    fileName = input("Enter the file name: ")
    picture = Image.open(fileName)
    width, height = picture.size # defines image size x,y

    if width > 1000 or height > 1000:
        choice = input("Oops! This is a large image would you like to crop it to a square? ").lower()
        if choice == "yes":
            picture = squareCrop(picture)
        emblem = input("Sweet! How about a message on the image? ").lower()
        if emblem == "yes":
            picture = textAdd(picture)
    Frame(picture)

    

    



    

    
    
