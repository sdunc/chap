# Stephen Duncanson
# chap-lib.py - library for chap, Connecticut Historical Aerial Photography

if __name__ == '__main__':
    print('Import this module to access survey_years dictionary.')
else:
    print('chap-lib has been imported...')
    print('building photo dictionary...')
    survey_years = {}

    for year in ['1934','1952','1965','1985','1990','1995','2004','2006','2008','2010']:
        temp_dict = {}
        year_photos_file = open('txts/'+year+'.txt','r')
        for line in year_photos_file:
            # format is lon,lat url
            lat = float(line.split(' ')[0].split(',')[1])
            lon = float(line.split(' ')[0].split(',')[0])
            url = line.split(' ')[1].strip('\n')
            temp_dict[(lat,lon)] = url # store url in dictionary (lat, lon) tuple is key
        survey_years[year] = temp_dict
        year_photos_file.close()
    
    print('dictionary complete')