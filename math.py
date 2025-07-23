def circleLineIntersect(xcentre, ycentre, xradius, yradius, xline=False, yline=False):
    if xline and (yradius*yradius)*(1-((xline-xcentre)*(xline-xcentre))/(xradius*xradius))>=0 or yline and (xradius*xradius)*(1-((yline-ycentre)*(yline-ycentre))/(yradius*yradius))>=0:
        return(True)
    return(False)