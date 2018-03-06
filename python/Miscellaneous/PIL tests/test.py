from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

# Image stuff
th_size = 50, 50
img = Image.open("levelup_bg2.jpg")
avatar = Image.open("avatar_test.jpg")
draw = ImageDraw.Draw(img, 'RGBA')

# Font stuff
font = "Roboto-Black.ttf"
name_font = ImageFont.truetype(font, 12)
level_font = ImageFont.truetype(font, 26)
base_color = (60, 60, 70)
exp_color = (190, 190, 200)

# # Experimental variables
username = 'EnragedNUKE'
level = 9

# # Avatar background filler
draw.rectangle([13,8,67,62], fill=(0,0,0,50))

# # Avatar handling
a_im = avatar.crop((0,0,128,128)).resize(th_size, Image.ANTIALIAS)
img.paste(a_im, (15,10,65,60))

# Text implementation
draw.text((15, 63), "Level Up!", base_color, font=name_font)
draw.text((25 if level > 9 else 33,72), str(level), base_color, font=level_font)

# # EXP Bar
# draw.rectangle([110,33,290,45], outline=exp_color)
# draw.rectangle([112,35,112+(290-112)*(exp/max_exp),43], fill=exp_color)

# # Text implementation
# exp_message = "EXP: {} / {}".format(exp, max_exp)
# w, h = draw.textsize(exp_message)
# draw.text((110, 15), username, base_color, font=name_font) # Username
# draw.text((125+(180-w)/2, 35), exp_message, base_color, font=exp_font) # EXP
# draw.text((110,48), "Level", base_color, font=level_label_font)

# w,h = draw.textsize(str(level))
# draw.text((110 if level > 9 else 118, 58), str(level), base_color, font=level_font)
# draw.rectangle([154,52,155,86], fill=exp_color)

# draw.text((162, 55), "Overall ranking", base_color, font=placing_font)
# draw.text((162, 70), "Total score", base_color, font=placing_font)

# draw.text((250, 55), "#{}".format(s_placing), base_color, font=placing_font)
# draw.text((250, 70), str(s_score), base_color, font=placing_font)

# #draw.text((0,0),"Text Test",(255,255,255),font=font)
img.save('bg2-out.jpg')