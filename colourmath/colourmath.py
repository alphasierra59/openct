######################
#Colour Math Library
######################


######################
#Constants
######################
#Reference Whites


######################
#CIE 1931 Colour Space
######################
#RGB to Tristim

#Tristim to x y
def TriTOxy(TriX,TriY,TriZ):
    
    if (not isinstance(TriX,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriY,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriZ,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    xCoord = (TriX/(TriX+TriY+TriZ))
    yCoord = (TriY/(TriX+TriY+TriZ))
    return [xCoord,yCoord]

#Tristim to x
def TriTOx(TriX,TriY,TriZ):

    if (not isinstance(TriX,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriY,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriZ,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    xCoord = (TriX/(TriX+TriY+TriZ))
    return xCoord

#Tristim to y
def TriTOy(TriX,TriY,TriZ):

    if (not isinstance(TriX,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriY,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriZ,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    yCoord = (TriY/(TriX+TriY+TriZ))
    return yCoord

#xy to Tristim
def xyTOTri(x,y,TriY):

    if (not isinstance(x,(int,float))):
        raise TypeError("x value must be float or int")
    
    if (not isinstance(y,(int,float))):
        raise TypeError("y value must be float or int")
    
    if (not isinstance(TriY,(int,float))):
        raise TypeError("TriY value must be float or int")
    
    XCoord = ((x/y)*TriY)
    ZCoord = (((1-x-y)/y)*TriY)
    return[XCoord,YCoord,ZCoord]

######################
#CIE 1960 Colour Space
######################
#Lightness from Luminance
def YtoL(luminance):
    
    #Reference White Luminance
    Y_n = 1 ##TODO
    
    if (not isinstance(luminance,(int,float))):
        raise TypeError("Luminance value must be float or int")
    
    return lightness

#Lightness from normalized Luminance
def YNormalizedtoL(luminance):
        
    if (not isinstance(luminance,(int,float))):
        raise TypeError("Luminance value must be float or int")
    
    return lightness

#Tristim to u v
def TriTOuv(TriX,TriY,TriZ):

    if (not isinstance(TriX,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriY,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriZ,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    uCoord = ((4*TriX)/(TriX+15*TriY+3*TriZ))
    vCoord = ((9*TriY)/(TriX+15*TriY+3*TriZ))
    return[uCoord,vCoord]

#Tristim to u
def TriTOu(TriX,TriY,TriZ):

    if (not isinstance(TriX,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriY,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriZ,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    uCoord = ((4*TriX)/(TriX+15*TriY+3*TriZ))
    return uCoord

#Tristim to v
def TriTOv(TriX,TriY,TriZ):

    if (not isinstance(TriX,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriY,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    if (not isinstance(TriZ,(int,float))):
        raise TypeError("Tristim value must be float or int")
    
    vCoord = ((9*TriY)/(TriX+15*TriY+3*TriZ))
    return vCoord
###################################
#CIE 1931 to/from 1960 Colour Space
###################################
#x y to u v
def xyTOuv(xCoord, yCoord):
    
    if (not isinstance(xCoord,(int,float))):
        raise TypeError("xCoord value must be float or int")
    
    if (not isinstance(yCoord,(int,float))):
        raise TypeError("yCoord value must be float or int")
    
    uCoord = ((4*xCoord)/(3-2*xCoord+12*yCoord))
    vCoord = ((9*yCoord)/(3-2*xCoord+12*yCoord))
    return[uCoord,vCoord]

#uv to xy
def uvTOxy(uCoord, vCoord):

    if (not isinstance(uCoord,(int,float))):
        raise TypeError("uCoord value must be float or int")
    
    if (not isinstance(vCoord,(int,float))):
        raise TypeError("vCoord value must be float or int")
    
    xCoord = ((9*uCoord)/(6*uCoord-16*vCoord+12))
    yCoord = ((4*vCoord)/(6*uCoord-16*vCoord+12))
    return[xCoord,yCoord]
    
##############
#Calculate CCT
##############
#CCT from xy
def CCTxy(xCoord, yCoord):

    if (not isinstance(xCoord,(int,float))):
        raise TypeError("xCoord value must be float or int")
    
    if (not isinstance(yCoord,(int,float))):
        raise TypeError("yCoord value must be float or int")
        
    n = ((xCoord-0.320)/(0.1858-yCoord))
    CCT = 449*(n**3) + 3525*(n**2) + 6823.3*(n**2) + 5520.33*
    
    return CCT

#CCT from TriStim
def CCT_Tri(TriX,TriY,TriZ):

    if (not isinstance(TriX,(int,float))):
        raise TypeError("TriX value must be float or int")
    
    if (not isinstance(TriY,(int,float))):
        raise TypeError("TriY value must be float or int")
    
    if (not isinstance(TriZ,(int,float))):
        raise TypeError("TriZ value must be float or int")
        
    n = ((xCoord-0.320)/(0.1858-yCoord))
    CCT = 449*(n**3) + 3525*(n**2) + 6823.3*(n**2) + 5520.33*
    
    return CCT
    
#cct from RGB --> noep
#def CCT_RGB(RedVal, GreenVal, BlueVal):
#
#    if (not isinstance(RedVal,(int,float))):
#        raise TypeError("RedVal value must be float or int")
#    
#    if (not isinstance(GreenVal,(int,float))):
#        raise TypeError("GreenVal value must be float or int")
#    
#    if (not isinstance(BlueVal,(int,float))):
#        raise TypeError("BlueVal value must be float or int")
#        
#    n = ((xCoord-0.320)/(0.1858-yCoord))
#    CCT = 449*(n**3) + 3525*(n**2) + 6823.3*(n**2) + 5520.33*
#    
#    return CCT

##TODO
#Standard Observer Lookup Table
def CIE1931Observer(wavelength):
    CMF = { 350 : thing1,
            351 : thing2,
            
        
          }
    