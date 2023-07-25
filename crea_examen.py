import sys

#print 'Number of arguments:', len(sys.argv), 'arguments
nomfile = sys.argv[1]

fi = open(nomfile+'.txt', 'r')
t2 = fi.read()


t1 = '''
\\documentclass{article}

\\\usepackage{color}
\\usepackage{transparent}
\\usepackage{graphicx}
\\usepackage{anysize}
\\usepackage[spanish]{babel}
\\marginsize{1cm}{3cm}{0cm}{0cm}


\\usepackage{eso-pic}
\\newcommand\BackgroundPic{
\\put(0,0){
\\parbox[b][\\paperheight]{\\paperwidth}{%
\\vfill
\\centering
\\color{red}%
\\transparent{0.9}%
\\includegraphics[width=\\paperwidth,height=\\paperheight,
keepaspectratio]{eisten.png}%
\\color{red}%
\\vfill
}}}


\\title{A Small \LaTeX{} Article Template\\thanks{To your mother}}
\\author{L. González-Santos  \\\
	Instituto de Neurobiología, UNAM  
	}

\\date{\\today}
% Hint: \\title{what ever}, \author{who care} and \date{when ever} could stand 
% before or after the \begin{document} command 
% BUT the \\maketitle command MUST come AFTER the \begin{document} command! 


\\begin{document}

\\AddToShipoutPicture{\\BackgroundPic}

\\maketitle
'''

t3 = '''

\\end{document}
'''

fo = open(nomfile + '.tex', 'w')

fo.write(t1)
fo.write(t2)
fo.write(t3)

fo.close()

