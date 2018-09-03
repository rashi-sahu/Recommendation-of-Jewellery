from collections import namedtuple
from operator import itemgetter
from operator import attrgetter
from math import sqrt
from decimal import Decimal

import random
try:
    import Image
except ImportError:
    from PIL import Image

Point = namedtuple('Point', ('coords', 'n', 'ct'))
Cluster = namedtuple('Cluster', ('points', 'center', 'n'))

def get_points(img):
    points = []
    w, h = img.size
    for count, color in img.getcolors(w * h):
        points.append(Point(color, 3, count))
    #print points
    return points

rtoh = lambda rgb: '#%s' % ''.join(('%02x' % p for p in rgb))

def colorz(filename, n=3):
    #print "rashmi" ,filename
    #img = Image.open("flaskr/static/%s" %(filename))
    #img=Image.open(filename)
    img=Image.open(filename)
    img.thumbnail((200, 200))
    w, h = img.size

    points = get_points(img)
    clusters= kmeans(points, n, 1)
    count_c=[]
    total_pts=0;
    percentage=[]
    #percentage.append(0)
    for i in range(0,len(clusters)):
        count_c.append(len(clusters[i].points))
        total_pts+=len(clusters[i].points)
    #print len(clusters[0].points)
    #print len(clusters[1].points)
    #print len(clusters[2].points)
    lis1=[]
    for i in range(0,len(count_c)):
        lis1.append((count_c[i],i))

    #print lis1
    lis1.sort(reverse=True,key=lambda x: x[0])
    #print lis1
   # print len(clusters)
    #print clusters[0]
    #print clusters[1]
    #print clusters[2]
    x=[]
    for i in range(0,len(lis1)):
        x.append(clusters[lis1[i][1]])
        p=Decimal(((len(clusters[lis1[i][1]].points))/total_pts)*100)
        percentage.append(round(p,2))
        #p=((len(clusters[lis1[i][1]].points))/total_pts)*100
        #percentage.append(p)
    #x=sorted(clusters, key=attrgetter('n'))
    #clusters.sort(key=lambda x:len(x[]))
    rgbs=[]
    for i in range(0,len(x)):
        #print len(x[i].points)
        rgbs.append(map(int, x[i].center.coords))
    #rgbs = [map(int, c.center.coords) for c in clusters]
    print (list(rgbs))
    print (percentage)
    return list(map(rtoh,rgbs)),percentage

def euclidean(p1, p2):
    return sqrt(sum([
        (p1.coords[i] - p2.coords[i]) ** 2 for i in range(p1.n)
    ]))

def calculate_center(points, n):
    vals = [0.0 for i in range(n)]
    plen = 0
    for p in points:
        plen += p.ct
        for i in range(n):
            vals[i] += (p.coords[i] * p.ct)
    return Point([(v / plen) for v in vals], n, 1)

def kmeans(points, k, min_diff):
    clusters = [Cluster([p], p, p.n) for p in random.sample(points, k)]
    #print clusters
    #print k
    count_cl=[0]*k;
    #print count_cl

    while 1:
        plists = [[] for i in range(k)]

        for p in points:
            smallest_distance = float('Inf')
            for i in range(k):
                distance = euclidean(p, clusters[i].center)
                if distance < smallest_distance:
                    smallest_distance = distance
                    idx = i
            plists[idx].append(p)
            count_cl[i]=count_cl[i]+1;

        #print count_cl
        diff = 0
        for i in range(k):
            old = clusters[i]
            center = calculate_center(plists[i], old.n)
            new = Cluster(plists[i], center, old.n)
            clusters[i] = new
            diff = max(diff, euclidean(old.center, new.center))

        if diff < min_diff:
            break

    #print len(clusters)
    return clusters
    
#img=Image.open('/Users/rashmisahu/Desktop/rashmi/internship/3.jpg')
#a,p=colorz(img)
#print map(rtoh,a)
#print a,p