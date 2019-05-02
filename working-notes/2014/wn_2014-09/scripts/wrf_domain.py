from mpl_toolkits.basemap import Basemap
import numpy as n
from numpy import ma
from pyproj import Proj
import pylab as p

a_small_number = 1e-8


def set_default_basemap(lon, lat, frame_width=5.):
    test = lon < 0.
    if True in test:
        # matplotlib expects 0-360 while WRF for example uses -180-180
        delta = n.ones(lon.shape)
        delta *= 360
        delta = ma.masked_where(lon > 0., delta)
        lon += delta.filled(fill_value=0)
    llcrnrlon=lon.min() - frame_width
    urcrnrlon=lon.max() + frame_width
    llcrnrlat=lat.min() - frame_width
    urcrnrlat=lat.max() + frame_width
    lon_0 = llcrnrlon + (urcrnrlon - llcrnrlon) / 2.
    lat_0 = llcrnrlat + (urcrnrlat - llcrnrlat) / 2.
        
    map = Basemap(
      llcrnrlon=llcrnrlon,
      llcrnrlat=llcrnrlat,
      urcrnrlon=urcrnrlon,
      urcrnrlat=urcrnrlat,
      resolution='l',
      projection='cyl',
      lon_0=lon_0,
      lat_0=lat_0
      )
    return map





def wrf2latlon(projection, 
  lat_0, lon_0,
  lat_1,
  lat_2,
  grid_centre_lon,
  grid_centre_lat,
  nx,
  ny,
  delta,
  staggered = False,
  return_extra = False
  ):
    proj = Proj(proj=projection, lat_0=lat_0, lon_0=lon_0, lat_1=lat_1, lat_2=lat_2)
    grid_centre_x, grid_centre_y = proj(grid_centre_lon, grid_centre_lat)
    grid_x_extent = nx * delta
    grid_y_extent = ny * delta
    min_x = grid_centre_x - grid_x_extent/2.
    min_y = grid_centre_y - grid_y_extent/2.
    max_x = min_x + grid_x_extent
    max_y = min_y + grid_y_extent
    x = n.arange(min_x, max_x + a_small_number, delta)
    y = n.arange(min_y, max_y + a_small_number, delta)  
    X, Y = p.meshgrid(x,y)
    lon, lat = proj(X, Y, inverse=True)
    if staggered:
        x_u = n.arange(min_x, max_x + delta + a_small_number, delta)
        x_u -= (delta /2.)
        X_u, Y_u = p.meshgrid(x_u,y)
        y_v = n.arange(min_y, max_y + delta + a_small_number, delta)  
        y_v -= (delta /2.)
        X_v, Y_v = p.meshgrid(x,y_v)
        lon_u, lat_u = proj(X_u, Y_u, inverse=True)
        lon_v, lat_v = proj(X_v, Y_v, inverse=True)
    llcrnrlon, llcrnrlat = proj(min_x, min_y, inverse=True)
    urcrnrlon, urcrnrlat = proj(max_x, max_y, inverse=True)
    map = Basemap(
      projection = projection,
      lon_0 = lon_0,
      lat_0 = lat_0,
      lat_1 = lat_1,
      lat_2 = lat_2,
      llcrnrlon = llcrnrlon,
      llcrnrlat = llcrnrlat,
      urcrnrlon = urcrnrlon,
      urcrnrlat = urcrnrlat
      )
    if return_extra:
        offset = map(lon_0, lat_0)
        if staggered:
            X += offset[0]
            Y += offset[1]
            X_u += offset[0]
            Y_u += offset[1]
            X_v += offset[0]
            Y_v += offset[1]
            return lon, lat, lon_u, lat_u, lon_v, lat_v, \
              X, Y, X_u, Y_u, X_v, Y_v, map
        else:
            X += offset[0]
            Y += offset[1]
            return lon, lat, X, Y, map
    else: 
        if staggered:
            return lon, lat, lon_u, lat_u, lon_v, lat_v
        else:
            return lon, lat



def wrf_grid(
  # WPS -> map_proj
  projection,
  # WPS -> truelat1
  lat_1,
  # WPS -> truelat2
  lat_2,
  # WPS -> stand_lon
  lon_0,
  # WPS -> ref_lat
  grid_centre_lat,
  # WPS -> ref_lon
  grid_centre_lon,
  delta_x,
  delta_y,
  # WPS -> e_we
  nx,
  # WPS -> e_sn
  ny,
  show_mass_grid = False,
  show_stag_grids = False,
  ):
    if lon_0 != grid_centre_lon:
        print 'not implemented yet -> see the source'
        print "\tbut let's try it anyways..."
        #return

    width   = nx * delta_x
    height  = ny * delta_y
    frame_x = 10 * delta_x
    frame_y = 10 * delta_y
    m = Basemap(
      lat_0 = grid_centre_lat,
      # this could be a bad assumption... because lon_0 and grid_centre_lon
      # need not be aligned, but at the same time I need to give this to
      # basemap for the grid to be centred... I could probably fix it
      # assigning lon_0 and then imposing a grid shift in native coordinates
      # if ref_lon and lon_0 were not the same
      lon_0 = lon_0,
      lat_1 = lat_1,
      lat_2 = lat_2,
      width = width + 2*frame_x,
      height = height + 2*frame_y,
      resolution = 'l',
      area_thresh=1000.
      )
    grid_centre_x, grid_centre_y = m(grid_centre_lon, grid_centre_lat)
    min_x = grid_centre_x - width/2.
    min_y = grid_centre_y - height/2.
    max_x = min_x + width
    max_y = min_y + height
    x = n.arange(min_x, max_x + a_small_number, delta_x)
    y = n.arange(min_y, max_y + a_small_number, delta_y)  
    x = x[1:-1]
    y = y[1:-1]
    x_u = n.arange(min_x, max_x + delta_x + a_small_number, delta_x)
    x_u -= delta_x/2.
    x_u = x_u[1:-1]
    y_v = n.arange(min_y, max_y + delta_y + a_small_number, delta_y)
    y_v -= delta_y/2.
    y_v = y_v[1:-1]
    X, Y = p.meshgrid(x,y)
    lon, lat = m(X, Y, inverse=True)
    X_u, Y_u = p.meshgrid(x_u,y)
    lon_u, lat_u = m(X_u, Y_u, inverse=True)
    X_v, Y_v = p.meshgrid(x,y_v)
    lon_v, lat_v = m(X_v, Y_v, inverse=True)
    if show_mass_grid:
        m.plot(X, Y, 'b+')
        m.plot([grid_centre_x], [grid_centre_y], 'r+')
        if show_stag_grids:
            m.plot(X_u, Y_u, 'g+')
            m.plot(X_v, Y_v, 'r+')
        m.drawcoastlines()
	p.show()
    output = {
      'map' : m,
      'mass_stag': {
        'lon_2d' : lon,
        'lat_2d' : lat,
        'x'      : x,
        'y'      : y,
        'x_2d'   : X,
        'y_2d'   : Y,
        }, 
      'u_stag': {
        'lon_2d' : lon_u,
        'lat_2d' : lat_u,
        'x'      : x_u,
        'y'      : y,
        'x_2d'   : X_u,
        'y_2d'   : Y_u,
        }, 
      'v_stag': {
        'lon_2d' : lon_v,
        'lat_2d' : lat_v,
        'x'      : x,
        'y'      : y_v,
        'x_2d'   : X_v,
        'y_2d'   : Y_v,
        } 
      }

    return output

def read_namelist(namelist_file):
    fid=open(namelist_file)
    out_dict={}
    data = fid.readlines()
    num_lines = len(data)
    for line in data:
	if '&' in line:
	    # Then this line is a namelist title
	    is_comment=False
	    current_label = line.rstrip('\n').lstrip(' ')
	    out_dict[current_label] ={}
	elif '/' in line:
	    # Then lines following this are comments until the next '&'
	    is_comment=True
	elif '=' in line:
	    # Then this line contains variable information to be stored
	    if not is_comment:
		variable,values = line.split('=')
		values = values.rstrip('\n').rstrip(',')
		try:
		    values=[int(element) for element in values.split(',')]
		except ValueError:
		    try:
			values=[float(element) for element in values.split(',')]
		    except ValueError:
			values=[value.strip() for value in values.split(',')]
		out_dict[current_label][variable.strip()]=values
    return out_dict






def plot_grid(lon,lat,
  title_string = 'N/A',
  meridians_delta = 15,
  parallels_delta = 15,
  same_figure = False,
  figsize = None,
  file_name = None,
  dpi = 80,
  skip = 5,
  return_map = False,
  marker = '+'
  ):
    """Function to plot grids similar to those generated by WPS
    
    Modified 27/01/08: Minor mod to plot the boundaries of the domain
    Comments: There is a chunk of code that gets repeated in a lot of places... the 
    stuff about plotting meridians and parallels. Maybe we could put this in a seperate 
    funtion?
    
    """
    map = set_default_basemap(lon,lat)
    # let's make sure the lat and lon arrays are 2D
    if len(lon.shape) < 2:
        lon, lat = p.meshgrid(lon,lat)
    if not same_figure:
        if not figsize:
            p.figure()
        else:
            p.figure(figsize=figsize)
    map.plot(lon[::skip,::skip], lat[::skip,::skip], marker=marker, linestyle='None')

    corners_lon = n.array([lon[0,0], lon[0,-1], lon[-1,-1], lon[-1,0]])
    corners_lat = n.array([lat[0,0], lat[0,-1], lat[-1,-1], lat[-1,0]])
    
    map.plot(corners_lon,corners_lat, 'ro')

    # Here it is =)
    map.plot(lon[0,:],lat[0,:],'k-')
    map.plot(lon[:,-1],lat[:,-1],'k-')
    map.plot(lon[-1,:],lat[-1,:],'k-')
    map.plot(lon[:,0],lat[:,0],'k-')

#    Thom: I've taken out the plot canberra option for generality
#    canberra_lon = [149 + 8./60]
#    canberra_lat = [-35 - 17./60]
#    map.plot(canberra_lon,canberra_lat, 'gs')

    if not same_figure:
        map.drawcoastlines()
	# These blocks seem to get repeated...
        meridians = n.arange(int(round(lon.min(),0)), 
          lon.max() + a_small_number, meridians_delta)
        meridians = n.array(meridians)
        map.drawmeridians(meridians, labels=[1,0,0,1])
    
        parallels = n.arange(int(round(lat.min(),0)), 
          lat.max() + a_small_number, parallels_delta)
        parallels = n.array(parallels)
        map.drawparallels(parallels, labels=[1,0,0,1])

        p.title(title_string)
    if file_name:
        p.savefig(file_name,dpi=dpi)
    if return_map:
        return map
    else:
        return
def plot_custom_points(map):
    """back by popular demand"""

#    canberra_lon = [149 + 8./60]
#    canberra_lat = [-35 - 17./60]
#    map.plot(canberra_lon,canberra_lat, 'gs')

    blue_calf_lon = [148.3944] 
    blue_calf_lat = [-36.3869]  
    map.plot(blue_calf_lon,blue_calf_lat, 'gs')
    return


def wrf_grid_wrapper(namelist_file='namelist.wps',nest_level=3):
    """
    wrf_grid_wrapper(namelist_file='namelist.wps',nest_level=0):
    Basic wrapper to easily visualise grids specified in namelist.wps
    
    Uses wrf.utils.read_namelist() to determine the read the appropriate variables 
    in a specified namelist file and then calls wrf.utils.wrf_grid() to define 
    the Basemap projection and show the grid over a map.

    Created 20/01/08 by Thom Chubb.
    Modified 27/01/08 - implemented viz.utils.plot_grid() to handle plotting and 
    capability for viewing as many grids as desired.

    TODO: Could use some more error checking, i think it will all fail if nest_levels
    are not consecutive!! Interpolation implemented is awkward but seems to work.
	
	""" 

    # Create namelist dictionary
    nd = read_namelist(namelist_file)

    # Field editing to make python happy
    if nd['&geogrid']['map_proj'][0]=="'lambert'":
	print 'debug: modify input field lambert -> lcc' 
	nd['&geogrid']['map_proj'][0]='lcc'
    
    grid = []

    outer_grid = wrf2latlon(nd['&geogrid']['map_proj'][0],
		    nd['&geogrid']['ref_lat'][0],
		    nd['&geogrid']['ref_lon'][0],
		    nd['&geogrid']['truelat1'][0], 
		    nd['&geogrid']['truelat2'][0],
		    nd['&geogrid']['ref_lon'][0],
		    nd['&geogrid']['ref_lat'][0],
#		    nd['&geogrid']['e_we'][nest_level[0]],
#		    nd['&geogrid']['e_sn'][nest_level[0]],
		    nd['&geogrid']['e_we'][0],
		    nd['&geogrid']['e_sn'][0],
		    nd['&geogrid']['dx'][0],
		    staggered = False,
		    return_extra = True
		    )
    print "outer_grid.shape =", outer_grid

    grid.append(outer_grid)
    #nest_level.sort()
    #nest_level=p.sort(nest_level)

    # for k in nest_level[1:]:
    for k in range(1,nest_level+1):
	this_grid = []
	try:
	    e_we = nd['&geogrid']['e_we'][k]
	except IndexError:
	    print "Out of range. Not enough grids specified within namelist file"
	    return 1
	e_sn = nd['&geogrid']['e_sn'][k]
	pgr  = nd['&geogrid']['parent_grid_ratio'][k]
	ips  = nd['&geogrid']['i_parent_start'][k]
	jps  = nd['&geogrid']['j_parent_start'][k]
	print 'processing grid: ',k
	# print e_we,e_sn,pgr,ips,jps
	# print ips,':',(ips+(e_we/pgr)),',', jps,':',(jps+(e_sn/pgr))
	
	# Interpolate in grid space to estimate inner gridpoints - 
	# care to find a more elegant approach???
	x1=grid[-1][2][jps, ips:ips+e_we/pgr]
	y1=grid[-1][3][jps:jps+e_sn/pgr, ips]
	
	a1=n.arange(0,x1.__len__(),1) 
	a2=n.arange(0,x1.__len__(),1./pgr)
	b1=n.arange(0,y1.__len__(),1)
	b2=n.arange(0,y1.__len__(),1./pgr)

	x2=n.interp(a2,a1,x1)
	y2=n.interp(b2,b1,y1)

	[X,Y]=n.meshgrid(x2,y2)

	# convert back to navigational coordinates
	lon,lat=grid[-1][4](X,Y,nd['&geogrid']['map_proj'])

	for j in [lon,lat,X,Y,grid[-1][4]]:
	    this_grid.append(j)
	if (k in [nest_level]):	
	    map=plot_grid(this_grid[0],this_grid[1],this_grid[2],skip=10,same_figure=True,return_map=True) 
	grid.append(this_grid)	
	# print grid[-1][0].shape 


    if 0 in [nest_level]:
	map=plot_grid(outer_grid[0],outer_grid[1],skip=10,same_figure=True,return_map=True) 
    #map.drawmeridians(n.arange(130,180,15),labels=[1,0,0,1])
    #map.drawparallels(n.arange(0,-90,-15),labels=[1,0,0,1])
    map.drawcoastlines()
    #map.drawrivers()
    #plot_custom_points(map)
    p.show()
    
    return grid, map




wrf_grid_wrapper()
