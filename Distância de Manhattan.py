xm=int(input('xm'))
ym=int(input('ym'))
xr=int(input('xr'))
yr=int(input('yr'))
if xm >= xr and ym >= yr:
    xf=xm-xr
    yf=ym-yr
    cruzamentos=xf+yf
elif xm<=xr and ym<=yr:
    xf=xr-xm
    yf=yr-ym
    cruzamentos=xf+yf
elif xm<=xr and ym>=yr:
    xf=xr-xm
    yf=ym-yr
    cruzamentos=xf+yf
else:
    xf = xm-xr
    yf = yr-ym
    cruzamentos=xf+xf
print(cruzamentos)
