
filename="output.txt"
konvergenzen=[
(13,"Gehenna",1),
(143,"Feuer",1),
(195,"Tod",1),
(230,"Eis",1),
(340,"Luft",1),
(470,"Chaos",1),
(512,"Feuer",2),
(586,"Erde",1),
(756,"Mockra",1),
(816,"Chaos",2),
(900,"Abydos",1),
(990,"Schatten",1),
(1040,"Fae",1),
(1101,"Hölle",1),
(1130,"Gehenna",2),
(1185,"Wasser",1),
(1255,"Feuer",3),
(1307,"Erde",2),
(1398,"Feuer",4),
(1524,"Schatten",2),
(1576,"Erde",3),
(1686,"Celestia",1),
(1805,"Fae",2),
(1920,"Luft",2),
(2010,"Wasser",2),
(2160,"Wasser",3),
(2230,"Abydos",2),
(2360,"Erde",4),
(2450,"Luft",3),
(2589,"Erde",5),
(2645,"Wasser",4),
(2717,"Erde",6),
(2981,"Feuer",5),
(3112,"Feuer",6),
]
current_year = 3113


template_string_css = ".lpos{year}{{\n\ttop:calc({year} / {max_year} * 100%);\n}}\n"

template_string_tlnav = '<li class="lpos lpos{year}">\n\t<a href="#{title}{number}">\n\t<div class="timeline-marker"></div>\n\t</a>\n</li>\n'

template_string_titlenav = '<li class="titlenavitem">\n\t<a href="#{title}{number}">\n\t<span class="timeline-heading">{number}. {title}</span>\n\t\t<p class="timeline-subtext">{year} cZ <br> vor etwa {ante} Jahren<br>{duration} Jahre bis zur nächsten Konvergenz</p>\n\t</a>\n</li>\n'

template_string_sections = '\n\t<section class="section {title}" id="{title}{number}">\n\t\t<div class="section_content">\n\t\t\t<h1>{number}. Konvergenz von {title}</h1>\n\t\t\t<p>\n\t\t\t</p>\n\t\t</div>\n\t</section>\n'

out = open(filename, 'w')
out.write("********** CSS *********** \n\n\n")

for konv in konvergenzen:
	out.write(template_string_css.format(year=konv[0], max_year=current_year))

out.write("\n\n\n ********** HTML List Timeline-Lines *********** \n\n\n")

for i in range(len(konvergenzen)):
	konv = konvergenzen[i]
	length = konvergenzen[min(i+1, len(konvergenzen)-1 )][0] - konv[0]
	howlongago = round((current_year - konv[0] - (length / 2)) / 100) * 100
	
	out.write(template_string_tlnav.format(year=konv[0],title=konv[1], number=konv[2]))
	
out.write("\n\n\n ********** HTML List Title-Nav *********** \n\n\n")

for i in range(len(konvergenzen)):
	konv = konvergenzen[i]
	length = konvergenzen[min(i+1, len(konvergenzen)-1 )][0] - konv[0]
	howlongago = round((current_year - konv[0] - (length / 2)) / 100) * 100
	
	out.write(template_string_titlenav.format(year=konv[0],title=konv[1],ante=howlongago, number=konv[2],duration=length))

out.write("\n\n\n ********** HTML Sections Template *********** \n\n\n")

for konv in konvergenzen:
	out.write(template_string_sections.format(year=konv[0],title=konv[1], number=konv[2]))

out.close()