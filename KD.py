"""
Erstellt eine Kurvendiskussion für die Funktion.

Ausführung in iPython.
"""

import os

from sympy import *

init_printing()

x, t = symbols('x t')

# Definition der Funktion, für die die Kurvendiskussion durchgeführt wird.

f = x**3 / S(2) - 3 / S(2) * x**2 + 2


f1 = f.diff('x')
f2 = f.diff('x', 2)
f3 = f.diff('x', 3)
F = integrate(f, x)

Bericht = open('KD/KD.tex', 'w')

Bericht.write('\\documentclass[10pt, a4paper]{article}\n')
Bericht.write('\\usepackage[ngerman]{babel}\n')
Bericht.write('\\usepackage[utf8]{inputenc}\n')
Bericht.write('\\usepackage[left=1cm,right=1cm,top=1cm,bottom=2cm]{geometry}\n')
Bericht.write('\\usepackage{amsmath}\n')
Bericht.write('\\DeclareMathOperator{\\dx}{dx}\n')
Bericht.write('\\begin{document}\n\n')


Bericht.write('\\section*{Kurvendiskussion}\n\n')
Bericht.write('Die zu diskutierende Funktion ist $$f(x) = ' + latex(f.expand()) + '.$$\n\n')
Bericht.write('\\noindent Die Ableitungen sind: \n\n')
Bericht.write('\\begin{eqnarray*}\n f\'(x) &=& ' + latex(f1.expand()) + '\\\\\n')
Bericht.write('f\'\'(x) &=& ' + latex(f2.expand()) + '\\\\\n')
Bericht.write('f\'\'\'(x) &=& ' + latex(f3.expand()) + '\\\\\n')
Bericht.write('\\int f(x) \\dx &=& ' + latex(F.expand()) + '\n\\end{eqnarray*}\n\n')


Bericht.write('\\paragraph{Schnittpunkt mit der y-Achse.}\n\n')
Bericht.write('$f(0) = ' + latex(f.subs(x, 0)) + '$\n\n')


Bericht.write('\\paragraph{Nullstellen}\n\n')
nst = solve(f, x)
NST = [f.subs(x, i).simplify() for i in nst]
if len(nst) > 0:
    Bericht.write('Die Nullstellenmenge $\\mathcal{N}$ ist:\n')
    Bericht.write('\\begin{eqnarray*}\\mathcal{N} = \\{')
    for i in range(len(nst)-1):
        Bericht.write('(' + latex(nst[i].simplify()) + '&,&' + latex(NST[i]) + '),\\\\\n')
    Bericht.write('(' + latex(nst[-1].simplify()) + '&,&' + latex(NST[-1]) + ')\\}\end{eqnarray*}\n\n')
else:
    Bericht.write('Es gibt keine Nullstellen.')

Bericht.write('\\paragraph{Extrema}\n\n')
ext = solve(f1, x)
EXT = [f.subs(x, i).simplify() for i in ext]
testE = [f2.subs(x, i).simplify() for i in ext]
if len(ext) > 0:
    Bericht.write('Die Menge der potenziellen Extrema $\\mathcal{E}$ ist:')
    Bericht.write('\\begin{eqnarray*}\n\\mathcal{E} = \\{')
    for i in range(len(ext)-1):
        Bericht.write('(' + latex(ext[i].simplify()) + '&,&' + latex(EXT[i]) + '),\\\\\n')
    Bericht.write('(' + latex(ext[-1].simplify()) + '&,&' + latex(EXT[-1]) + ')\\}\n\end{eqnarray*}\n\n')
    Bericht.write('Einsetzen in die zweite Ableitung liefert:\n')
    Bericht.write('\\begin{eqnarray*}\n')
    for i in range(len(ext)-1):
        Bericht.write('f\'\'( ' + latex(ext[i].simplify()) + ') &=& ' + latex(testE[i]) + '\\\\\n')
    Bericht.write('f\'\'( ' + latex(ext[-1].simplify()) + ') &=& ' + latex(testE[-1]) + '\n')
    Bericht.write('\\end{eqnarray*}\n\n')
else:
    Bericht.write('Es gibt keine Extremstellen.')

Bericht.write('\\paragraph{Wendepunkte}\n\n')
wep = solve(f2, x)
WEP = [f.subs(x, i).simplify() for i in wep]
testW = [f3.subs(x, i).simplify() for i in wep]
if len(wep) > 0:
    Bericht.write('Die Menge der potenziellen Wendepunkte $\\mathcal{W}$ ist:')
    Bericht.write('\\begin{eqnarray*}\n\\mathcal{W} = \\{')
    for i in range(len(wep)-1):
        Bericht.write('(' + latex(wep[i].simplify()) + '&,&' + latex(WEP[i]) + '),\\\\\n')
    Bericht.write('(' + latex(wep[-1].simplify()) + '&,&' + latex(WEP[-1]) + ')\\}\n\end{eqnarray*}\n\n')
    Bericht.write('Einsetzen in die dritte Ableitung liefert:\n')
    Bericht.write('\\begin{eqnarray*}\n')
    for i in range(len(wep)-1):
        Bericht.write('f\'\'\'( ' + latex(wep[i].simplify()) + ') &=& ' + latex(testW[i]) + '\\\\\n')
    Bericht.write('f\'\'\'( ' + latex(wep[-1].simplify()) + ') &=& ' + latex(testW[-1]) + '\n')
    Bericht.write('\\end{eqnarray*}\n\n')
else:
    Bericht.write('Es gibt keine Wendepunkte.')

Bericht.write('\\paragraph{Wendetangenten}\n\n')
steigW = [f1.subs(x, i).simplify() for i in wep]
abschW = [WEP[i] - wep[i] * steigW[i] for i in range(len(wep))]
if len(wep) > 0:
    Bericht.write('Die Wendetangenten sind:\n')
    Bericht.write('\\begin{eqnarray*}\n')
    for i in range(len(wep)-1):
        Bericht.write('\\text{Die Tangente an } (' + latex(wep[i].simplify())
            + ',' + latex(WEP[i]) + ') &\\text{ist}& t(x) =' + latex(steigW[i])
            + '\\cdot x +' + latex(abschW[i].simplify()) + '\\\\\n')
    Bericht.write('\\text{Die Tangente an } (' + latex(wep[-1].simplify())
        + ',' + latex(WEP[-1]) + ') &\\text{ist}& t(x) =' + latex(steigW[-1])
        + '\\cdot x +' + latex(abschW[-1].simplify()) + '\n')
    Bericht.write('\\end{eqnarray*}')
else:
    Bericht.write('Es gibt keine Wendetangenten, da es keine Wendepunkte gibt.')

Bericht.write('\end{document}')
Bericht.close()

os.system('pdflatex KD\KD.tex')
os.system('del KD.log')
os.system('del KD.aux')
os.system('del KD\KD.tex')
os.system('move KD.pdf KD')
os.system('start KD\KD.pdf')
