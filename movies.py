"""
movies.py
Project Phase 1
Author: Daniel Benjamin Masters (583334)

"""

from lxml import etree
import sys
import locale
#I imported locale to format the Box Office earnings as currency

locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
#This was done to ensure the currency was printed out in Dollars

sys.stdout = open('movies.xml', 'w')

def LOTR():
    xmltree = etree.parse('http://students.informatics.unimelb.edu.au/~ivow/foi/mywork/public/lord_of_the_rings.xml')
    root = xmltree.getroot()
    
    #The below 4 lines of code and the ".format(i)" appended to each line enables me to use an index (i) to iterate through all the movies. This means I can use the same block of code for each movie.
    for i in range(len(root.findall('.//a_movie'))):
        a_movie = root.find('.//a_movie[{}]'.format(i))
        int(i)
        i+=1
        print "<movie>"
        for x in root.xpath('.//a_movie[{}]/name'.format(i)):
            print "<title>" + x.text + "</title>"
        for x in root.xpath('.//a_movie[{}]/rating'.format(i)):
            print "<rating>" + x.text + "</rating>"
        for x in root.xpath('.//a_movie[{}]/studio'.format(i)):
            print "<studio>" + x.text + "</studio>"    
        for x in root.xpath('.//a_movie[{}]/genre'.format(i)):
            print "<genre>" + x.text + "</genre>"
        actors = root.xpath('.//a_movie[{}]/actors/@*'.format(i))
        print "<actors>"
        for j in actors:
            print '<actor>' + str(j) + '</actor>'
        print "</actors>"
        for x in root.xpath('/movies/a_movie[{}]/writer'.format(i)):
            print "<writer>" + x.text + "</writer>"
        for x in root.xpath('/movies/a_movie[{}]/director'.format(i)):
            print "<director>" + x.text + "</director>"
        for x in root.xpath('/movies/a_movie[{}]/date'.format(i)):
            print "<date>" + x.text + "</date>"
        for x in root.xpath('/movies/a_movie[{}]/origin'.format(i)):
            print "<country>" + x.text + "</country>"
        reviews = root.xpath('/movies/a_movie[{}]/reviews/a_review/@reviewer'.format(i))
        score = root.xpath('/movies/a_movie[{}]/reviews/a_review/@value'.format(i))
        max = len(score)
        sys.stdout.write("<reviews>")
        l = 0
        for k in reviews:
            sys.stdout.write('\n' + '    <review publication="' + str(k) + '" ')
            while l < max:
                sys.stdout.write('score="' + str(score[l]) + '"/>')
                l+=1
                break
                #The break is here to ensure one score is printed out at a time
        print '\n' + '</reviews>'
        for x in root.xpath('.//a_movie[{}]/metascore'.format(i)):
            print "<metascore>" + x.text + "</metascore>"
        for x in root.xpath('.//a_movie[{}]/worldwide_gross'.format(i)):
            print "<box_office>" + locale.currency(int(x.text), grouping = True) + "</box_office>"
        print "</movie>"  

def HP():
    act = 1
    xmltree = etree.parse('http://students.informatics.unimelb.edu.au/~ivow/foi/mywork/public/harry_potter.xml')
    root = xmltree.getroot()
    for i in range(len(root.findall('.//movie'))):
        movie = root.find('.//movie[{}]'.format(i))
        int(i)
        i+=1
        print "<movie>"
        for x in root.xpath('.//movie[{}]/Name'.format(i)):
            print "<title>" + x.text + "</title>"
        for x in root.xpath('.//movie[{}]/Rating'.format(i)):
            print "<rating>" + x.text + "</rating>"
        for x in root.xpath('.//movie[{}]/Studio'.format(i)):
            print "<studio>" + x.text + "</studio>"    
        for x in root.xpath('.//movie[{}]/Genre'.format(i)):
            print "<genre>" + x.text + "</genre>"
        actors = [None]*3
        for x in root.xpath('.//movie[{}]/Actor1'.format(i)):
            actors[0] = x.text
        for x in root.xpath('.//movie[{}]/Actor2'.format(i)):
            actors[1] = x.text
        for x in root.xpath('.//movie[{}]/Actor3'.format(i)):
            actors[2] = x.text
        print "<actors>"
        for j in actors:
            print '<actor>' + str(j) + '</actor>'
        print "</actors>"
        for x in root.xpath('.//movie[{}]/Writer'.format(i)):
            print "<writer>" + x.text + "</writer>"
        for x in root.xpath('.//movie[{}]/Director'.format(i)):
            print "<director>" + x.text + "</director>"
        for x in root.xpath('.//movie[{}]/Year'.format(i)):
            print "<date>" + x.text + "</date>"
        for x in root.xpath('.//movie[{}]/Origin'.format(i)):
            print "<country>" + x.text + "</country>"
        
        #populate list
        numreviews = 0
        for x in root.xpath('.//movie[{}]/score/@src'.format(i)):
            numreviews+=1
        scores = [None]*numreviews
        l = 0
        for x in root.xpath('.//movie[{}]/score'.format(i)):
            scores[l] = x.text
            l+=1       
        
        sys.stdout.write("<reviews>")
        m = 0
        for x in root.xpath('.//movie[{}]/score/@src'.format(i)):
            sys.stdout.write('\n' + '    <review publication="' + x + '" ')
            for x in root.xpath('.//movie[{}]/score'.format(i)):
                if scores[m] != None:
                    sys.stdout.write('score="' + str(scores[m]) + '"/>')
                    m+=1
                    break
                else:
                    sys.stdout.write('score=""/>')
                    m+=1
                    break
        print '</reviews>'
        for x in root.xpath('.//movie[{}]/Metascore'.format(i)):
            print "<metascore>" + x.text + "</metascore>"
        for x in root.xpath('.//movie[{}]/Worldwide_gross'.format(i)):
            print "<box_office>" + locale.currency(int(x.text), grouping = True) + "</box_office>"
        print "</movie>"
    
def main():
    print '<?xml version = "1.0" encoding = "utf-8"?>'
    print '<movies>'
    LOTR()
    HP()
    print '</movies>'
    
main()
