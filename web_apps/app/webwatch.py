import urllib2, re

def get_bus(request_vid):

    data = None
    try:
        response = urllib2.urlopen('http://webwatch.cityofmadison.com/webwatch/UpdateWebMap.aspx?u=80')
        data = response.read()
    except urllib2.HTTPError as e:
        print 'Status: {0}'.format(e.code)
        print
        return None


    vehicles = data.split('*')[2].split(';')
    vdict = {}
    for vehicle_str in vehicles:
        match = re.search('<br>.*: (\d{3}).*<br>', vehicle_str)
        if match == None: continue
        vid = match.group(1)
        location = [vehicle_str.split('|')[0], vehicle_str.split('|')[1]]
        next_stop = None
        match = re.search('t: (.*?$)', vehicle_str)
        if match: next_stop = match.group(1)
        time_to_stop = vehicle_str.split('|')[2]
        vdict[vid] = {"location": location, "some_number": time_to_stop, "next_stop": next_stop}

    output = ""

    if request_vid:
        if request_vid not in vdict:
            return None
        output = vdict[request_vid]
    else:
        output = vdict
    return output