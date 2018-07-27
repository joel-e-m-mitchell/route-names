def getter():
    import urllib.request
    url = 'https://www.ukclimbing.com/logbook/crag.php?id=104'
    response = urllib.request.urlopen(url)
    data = response.read()
    return data.decode('utf-8')


def route_finder():
    # match/extract routenames and grades inside html
    '''
    regex: route name
    \<td class="name"\>\<a href="c.php\?i=[0-9]{3,7}"\>(.*?)\</a\>
    '''
    import re
    p = re.compile("\<td class=\"name\"\>\<a href=\"c.php\?i=[0-9]{3,7}\"\>(.*?)\</a\>")
    


def crag_name():
    '''
    cragname regex:
    \<h1\>(.*?)\</h1\>
    '''
