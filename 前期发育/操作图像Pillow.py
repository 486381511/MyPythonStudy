# from PIL import ImageColor
# #草，Pillow模块导入是PIL，尼玛找了这么久
# #ImageColor类的的getcolor方法可以根据第一个颜色参数与第二个RGBA参数，输出RGBA的值
# print(ImageColor.getcolor('red','RGBA'))
# print(ImageColor.getcolor('yellow','RGBA'))

from PIL import Image
#Image.open返回值是Image对象数据类型
# catIm = Image.open(fp='.\\zophie.png')
# #查看加载图片的基本信息，宽高文件名与图像格式
# #宽高
# print(catIm.size)
# print(catIm.width)
# print(catIm.height)
# #图像文件名
# print(catIm.filename)
# #图像格式
# print(catIm.format)
# #改变图像名字与类型，再保存
# catIm.save('zophie.jpg')


#Image.new()函数创建一个Image对象，
#第一个参数是颜色模式
#第二个参数是大小，一个元组，作为新图像的宽高
#第三个参数是背景颜色，可以用RGBA值，也可以使用标准颜色名称的字符串
# new_cat = Image.new('RGBA', (900, 900), 'red')
# new_cat.save('.\\学习资源\\newcat.png')
# new_dog = Image.new('RGBA', (900, 900), (0,255,0,255))
# new_dog.save('.\\学习资源\\newdog.png')


#裁剪图片
#Image对象的crop()方法接受一个矩形元组，返回一个Image对象，表示裁剪后的图像
#裁剪不是在原图上发生的，也就是说Image对象原封不动，crop()方法返回一个新的Image对象
#！！！注意包左上，不包右下！！！       左上右下！！！！！
catIm = Image.open(fp='.\\zophie.png')
change_cat = catIm.crop((335,345,565,560))
change_cat.save('.\\学习资源\\change_cat.png')


#复制和粘贴图像到其他图像
#copy()方法返回一个新的Image对象，它与原来的Image对象具有一样的图像。
#如果需要修改图像，同时也希望保持原有的版本不变，这非常有用
# catCopyIm = catIm.copy()
#裁剪
faceIm = catIm.crop((335,345,565,560))
#paste()方法在Image对象上调用！！！！！！！每一次调用paste()方法，原对象都改变，将另一个图像粘贴在它上面。
print(faceIm.size)
#paste()方法有两个参数
#一个是源Image对象（要粘贴的）
#一个包含x和y坐标的元组，指明源Image对象粘贴到主Image对象时的左上角位置
# catCopyIm.paste(faceIm,(0,0))
# catCopyIm.paste(faceIm,(400,500))
# catCopyIm.save('.\\学习资源\\pasted.png')


#猫头平铺
faceImWidth,faceImHeight = faceIm.size
catImWidth,catImHeight = catIm.size

# for Width in range(0, catImWidth, faceImWidth):
#     for Height in range(0, catImHeight,faceImHeight):
#         print(Width,Height)
#         catIm.paste(faceIm, (Width,Height))
# catIm.save('.\\学习资源\\猫猫.png')



#调整图像大小
#resize()方法在Image对象上调用，
#返回指定宽度和高度的一个新Image对象
#它接受!!!!!两个整数元组!!!!!作为参数，表示返回图像的新高度和宽度
# width,height = catIm.size
# quartersizeIm = catIm.resize((int(width/2),int(height/2)))
# quartersizeIm.save('.\\学习资源\\quartersized.png')
# svelteIm = catIm.resize((width,height+300))
# svelteIm.save('.\\学习资源\\svelte.png')


#旋转和翻转
# 图像（rotate旋转）逆时针
# rotatecat = catIm.rotate(90)
# rotatecat.save('.\\学习资源\\rotatecat.png')
#连续写法
#逆时针旋转了270°
# catIm.rotate(270).save('.\\学习资源\\rotatecat2.png')
#注意：当图像旋转90°或者270°，宽度和高度会发生改变
#如果旋转其他角度，图像的原始尺寸会保持，
#!windows上，使用黑色背景来填补旋转造成的缝隙
#！rotate()方法有一个可选的expand关键参数，如果设置为True，会放大图像的尺寸，适应新图像
catIm.rotate(6).save('.\\ziyaun\\catrotate.png')
catIm.rotate(6,expand=True).save('.\\ziyaun\\catrotate2.png')

#镜像翻转
#左右翻转
# catIm.transpose(Image.FLIP_LEFT_RIGHT).save('.\\ziyaun\\翻转猫.png')
#上下翻转
# catIm.transpose(Image.FLIP_TOP_BOTTOM).save('.\\ziyaun\\翻转猫2.png')


#更改单个像素
#单个像素的颜色可以通过getpixel()和putpixel()方法取得和设置。
#它们都接受一个元组表示x和y坐标。
#putpixel()方法还接受一个元组，作为该像素的颜色
#这个颜色参数是四整数RGBA元组或者三整数RGB元组
Im = Image.new('RGBA',(100,100))
#一个像素一个像素地改，最后铺满一张照片
# print(Im.getpixel((0,0)))
# for x in range(100):
#     for y in range(100):
#         #putpixel()方法传入第一个参数是元组，代表像素点，第二个是要改的颜色
#         Im.putpixel((x,y),(110,210,20))
# Im.save('.\\ziyaun\\改像素.png')






#在图像上绘画

# 点
# point(xy,fill)方法绘制单个像素，xy参数表示要画的点的列表。
# 该列表可以是x和y坐标的元组的列表，例如[(x,y)(x,y),...]
# 或是没有元组的x和y坐标的列表，例如[x1,y1,x2,y2,...]
# fill参数是点的颜色，可以是RGBA元组，可以是颜色名字
#
# 线
# line(xy,fill,width)方法绘制一条线或一系列的线。
# xy要么是一个元组列表，如[(x,y)(x,y),...],要么是一个整数列表[x1,y1,x2,y2,...]
# ！！！！每个点都是正绘制的线上的一个连接点
# 可选的fill参数是线的颜色，RGBA元组或者颜色名。
# width参数是线的宽度，如果未指定，缺省值是1
#
# 矩形
# rectangle(xy,fill,outline)方法绘制一个矩形
# xy参数是一个矩形元组，形式为(left,top,right,bottom)
# left和top值指定了矩形左上角的x和y坐标，right和bottom值指定了矩形右下角
# fill参数是颜色，将填充矩形内部，可选outline参数是矩形轮廓的颜色
#
# 椭圆
# ellipse(xy, fill, outline)方法绘制一个椭圆。
# 如果椭圆的宽度和高度一样，该方法将绘制一个圆。
# xy参数是一个矩形元组(left, top, right, bottom)
# 它表示正好包含该椭圆的矩形。
# 可选的fill参数是椭圆内的颜色，可选的outline参数是椭圆轮廓的颜色。
#
# 多边形
# polygon(xy, fill, outline)方法绘制任意的多边形。
# xy参数是一个元组列表，例如[(x, y), (x, y), ...]
# 或者是一个整数列表，例如[x1, y1, x2, y2, ...]
# 表示多边形边的连接点。最后一对坐标将自动连接到第一对坐标。
# 可选的fill参数是多边形内部的颜色，可选的outline参数是多边形轮廓的颜色。

#总结point 点
# line 线
# rectangle 矩形
# ellipse 椭圆
# polygon 多边形

from PIL import ImageDraw
im = Image.new('RGBA',(200,200),'white')
#将该Image对象传入ImageDraw.Draw()函数中，得到一个ImageDraw对象
drawObj = ImageDraw.Draw(im)
drawObj.line([(0,0),(100,200),(200,46)],fill='red')
#!!!!!!不是ImageDraw对象，是原图像对象!!!!!!!
im.save('.\\ziyaun\\line.png')


#绘制文本
# Imagedraw对象还有text()方法，用于在图像上绘制文本
# text()方法有4个参数：xy，text，fill和font
# xy参数是两个整数元组，指定文本区域的左上角
# text参数是想写入的文本字符串
# 可选参数fill是文本的颜色
# 可选参数font是一个ImageFont对象，用于设置文本的字体和大小

# 因为通常很难预先知道一块文本在给定的字体下的大小
# 所以ImageDraw模块也提供了textsize()方法。
# 它的第一个参数是要测量的文本字符串
# 第二个参数是可选的ImageFont对象。
# textsize()方法返回一个两整数元组，表示如果以指定的字体写入图像，文本的宽度和高度。
# 可以利用这个宽度和高度，帮助你精确计算文本放在图像上的位置
from PIL import ImageFont
hh = Image.new('RGBA',(200,200),'white')
draw = ImageDraw.Draw(hh)
draw.text((90,100), 'SNOW', fill='purple',language='chinese')
#以后有空再回来看吧，现在没啥用
hh.save('.\\ziyaun\\ziti.png')












