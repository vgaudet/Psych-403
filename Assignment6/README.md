Gaudet, Vernon
# Assignment 6: Level 4: PsychoPy - Showing windows and stimuli

## Dialog box exercises
	1. Complete.
	2. Complete.

### Using DlgFromDict:
	1. Complete.
	2. Setting the variable as fixed makes the field associated with the value in the dialog box uneditable.
	3. Complete.
	4. Complete.
	5. Complete.

## Monitor and window exercises
	1. The 'units' parameter allows for definining window size by 'height', 'norm, 'deg, 'cm' or 'pix'. 'height' is defined as a scale or proportion of the height of the window itself, 'norm' as a proportion of the x or y values of the window itself, 'cm' is measured in centimeters determined from the screen physical size and pixel count, 'deg' as the degrees of visual angle and 'pix' as pixels.  
	2. Using the colorspace parameter, can change what color space that you are using when you define color parameters such as LMS, DKL, HSV, or RGB. You may also define colors using hex codes. Psycopy also has a select list of predefined colors that you can call by name in the color parameter.
	3. Complete.

## Stimulus exercises
	1. Setting the images to display at 400p*400p will scale the image to fit that size, disturbing the original proportions of the image. To preserve the proportions of the original image you can use the default setting for image size and define size as a x,y pair scale value of the original image.
	2. Complete. The window is defined in pixels 800p*800p or Xp * Yp. Image positions in pixels are defined by number of pixels from the center of the screen. Each image position should be in the center of a quadrant. the center of a quadrant will be Xp / 4 or Yp / 4. Xp or Yp will be negative or positive depending on the quadrant. Get the window size from the system as Xp and Yp to scale to any window size including fullscreen.  
	3. Complete.
	4. Complete.
