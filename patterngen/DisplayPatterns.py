from PIL import Image
from PIL import ImageDraw

def AOI_9pt(Hres, Vres):
    '''
    Draws the VESA FPDM 9-point uniformity measurement template
    '''
    img = Image.new('RGB', (Hres, Vres), (0, 0, 0))
    AOIs = {}
    AOIs['1'] = (Hres*0.1, Vres*0.1)
    AOIs['2'] = (Hres*0.5, Vres*0.1)
    AOIs['3'] = (Hres*0.9, Vres*0.1)
    AOIs['4'] = (Hres*0.1, Vres*0.5)
    AOIs['5'] = (Hres*0.5, Vres*0.5)
    AOIs['6'] = (Hres*0.9, Vres*0.5)
    AOIs['7'] = (Hres*0.1, Vres*0.9)
    AOIs['8'] = (Hres*0.5, Vres*0.9)
    AOIs['9'] = (Hres*0.9, Vres*0.9)

    draw = ImageDraw.Draw(img)
    r = Hres/20
    DistCenterline = r * 1.6
    for key, value in AOIs.items():
        draw.ellipse([value[0] - r, value[1] - r, value[0] + r, value[1] + r], fill = (0, 0, 0), outline = (255, 255, 255))
        draw.line([value[0], value[1] - DistCenterline, value[0], value[1] + DistCenterline], fill = (255,255,255), width = 2)
        draw.line([value[0] - DistCenterline, value[1], value[0] + DistCenterline, value[1]], fill = (255,255,255), width = 2)
    draw.line([Hres/2, 0, Hres/2, Vres], fill=(0,255,255), width = 2)
    draw.line([0, Vres/2, Hres, Vres/2], fill=(0,255,255), width = 2)

    img.save(str(Hres) + "x" + str(Vres) + "_9ptAOI.bmp")

def AOI_13pt(Hres, Vres, Hmm, Vmm):
    '''
    Draws the SPWG 13-point uniformity measurement template
    '''
    PixelDensityMM = Hres//Hmm
    AOIs = {}
    AOIs['1'] = (Hres-10*PixelDensityMM, Vres-10*PixelDensityMM)
    AOIs['2'] = (Hres*0.5, Vres-10*PixelDensityMM)
    AOIs['3'] = (10*PixelDensityMM, Vres-10*PixelDensityMM)
    AOIs['4'] = (Hres*0.75, Vres*0.75)
    AOIs['5'] = (Hres*0.25, Vres*0.75)
    AOIs['6'] = (Hres-10*PixelDensityMM, Vres/2)
    AOIs['7'] = (Hres*0.5, Vres/2)
    AOIs['8'] = (10*PixelDensityMM, Vres/2)
    AOIs['9'] = (Hres*0.75, Vres*0.25)
    AOIs['10'] = (Hres*0.25, Vres*0.25)
    AOIs['11'] = (Hres-10*PixelDensityMM, 10*PixelDensityMM)
    AOIs['12'] = (Hres*0.5, 10*PixelDensityMM)
    AOIs['13'] = (10*PixelDensityMM, 10*PixelDensityMM)

    img = Image.new('RGB', (Hres, Vres), (0,0,0))
    draw = ImageDraw.Draw(img)
    r = Hres/45
    DistCenterline = r * 1.6
    for key, value in AOIs.items():
        draw.ellipse([value[0] - r, value[1] - r, value[0] + r, value[1] + r], fill = (0, 0, 0), outline = (255, 255, 255))
        draw.line([value[0], value[1] - DistCenterline, value[0], value[1] + DistCenterline], fill = (255,255,255), width = 2)
        draw.line([value[0] - DistCenterline, value[1], value[0] + DistCenterline, value[1]], fill = (255,255,255), width = 2)
    draw.line([Hres/2, 0, Hres/2, Vres], fill=(0,255,255), width = 2)
    draw.line([0, Vres/2, Hres, Vres/2], fill=(0,255,255), width = 2)


    img.save(str(Hres) + "x" + str(Vres) + "_13ptAOI.bmp")

def Rows(Hres, Vres, Color1, Color2, LineWidth):
    '''
    Draws rows of alternating colors at a specified line width
    '''
    img = Image.new('RGB', (Hres, Vres), Color1)
    draw = ImageDraw.Draw(img)
    for i in range(0, Vres, 2):
        draw.line([0, i, Hres, i], fill=Color2)
    
    img.save(str(Hres) + "x" + str(Vres) + "_Rows_" + str(LineWidth) + "px.bmp")

def Cols(Hres, Vres, Color1, Color2, LineWidth):
    '''
    draws columns of alternating colors at a specified width
    '''
    img = Image.new('RGB', (Hres, Vres), Color1)
    draw = ImageDraw.Draw(img)
    for i in range(0, Hres, 2):
        draw.line([i, 0, i, Vres], fill=Color2)

def Checkerboard(Hres, Vres, Color1, Color2):
    '''
    draws single-pixel checkerboard of alternating colors
    '''
    img = Image.new('RGB', (Hres, Vres), Color1)
    draw = ImageDraw.Draw(img)
    for i in range(0, Hres, 2):
        for j in range(0, Vres, 2):
            draw.point((i, j), fill = Color2)
    for i in range(1, Hres, 2):
        for j in range(1, Vres, 2):
            draw.point((i, j), fill = Color2)
    
    img.save(str(Hres) + "x" + str(Vres) + "_Check_" + "1px.bmp")

def FS_Color(Hres, Vres, Color):
    '''
    Draws a flat-field image
    '''
    img = Image.new('RGB', (Hres, Vres), Color)
    img.save(str(Hres) + "x" + str(Vres) + "FS_" + str(Color[0]).zfill(3) + str(Color[1]).zfill(3) + str(Color[2]).zfill(3) + ".bmp")

def OPR_Color(Hres, Vres, OPR, Color):
    '''
    Draws a rectangle in the center, filling the specified On Pixel Ratio (OPR)
    '''
    img = Image.new('RGB', (Hres, Vres), (0,0,0))
    draw = ImageDraw.Draw(img)
    draw.rectangle([Hres*(OPR*0.5), Vres*(OPR*0.5), Hres*(OPR*1.5), Vres*(OPR*1.5)], fill=(Color))
    img.save(str(Hres) + "x" + str(Vres) + "OPR" + str(OPR*100).zfill(3) + "_" + str(Color[0]).zfill(3) + str(Color[1]).zfill(3) + str(Color[2]).zfill(3) + ".bmp")

def KW_Mosaic(Hres, Vres, Hsquares, Vsquares):
    '''
    Draws a black and white mosaic, with specified number of rectangles
    '''
    img = Image.new('RGB', (Hres, Vres), (0,0,0))
    draw = ImageDraw.Draw(img)
    for i in range(0,Hres,2*Hres//Hsquares):
        for j in range(0,Vres,2*Vres//Vsquares):
            draw.rectangle([i, j, i+Hres/Hsquares, j+Vres/Vsquares], fill = (255,255,255))
    for i in range(Hres//Hsquares,Hres,2*Hres//Hsquares):
        for j in range(Vres//Vsquares,Vres,2*Vres//Vsquares):
            draw.rectangle([i, j, i+Hres/Hsquares, j+Vres/Vsquares], fill = (255,255,255))

    img.save(str(Hres) + "x" + str(Vres) + "_" + str(Hsquares) + "x" + str(Vsquares) + "Mosaic.bmp")