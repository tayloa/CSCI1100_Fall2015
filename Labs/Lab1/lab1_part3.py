jupiter_dist = 483632000.0
earth_dist = 92957100.0
ratio_dist = jupiter_dist / earth_dist
print "Jupiter is", ratio_dist, "times farther from the Sun than the Earth is."
jupiter_radius = 44423
earth_radius = 3963
pi = 3.14159
earth_volume = (4/3) * pi * (earth_radius**3)
jupiter_volume = (4/3) * pi * (jupiter_radius**3)
ratio_volume = jupiter_volume / earth_volume
print "Jupiter's volume is", ratio_volume, "times larger than that of Earth."
time_earth = int(earth_dist / 186000)
time_earth_min = time_earth / 60
time_earth_secleft = time_earth%60
time_jupiter = int(jupiter_dist / 186000)
time_jupiter_min = time_jupiter / 60
time_jupiter_secleft = time_jupiter%60
print "Light would take",time_earth,"seconds or",time_earth_min,"minutes and",time_earth_secleft,"seconds to reach Earth."
print "Light would take",time_jupiter,"seconds or",time_jupiter_min,"minutes and",time_jupiter_secleft,"seconds to reach Jupiter."