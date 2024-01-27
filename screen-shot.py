from PIL import ImageGrab


screenshot = ImageGrab.grab()
print(screenshot.size)

left = 695  
top = 300 
right = 1450 
bottom = 700 


cropped_region = screenshot.crop((left, top, right, bottom))
cropped_region.save('negative-text1153.png')
cropped_region.show()