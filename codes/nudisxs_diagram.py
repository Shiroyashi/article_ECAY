from graphviz import Digraph

# Create a directed graph
dot = Digraph(format='png')
dot.attr(rankdir='TB', style='filled', fontsize='12', fontname='Helvetica')

# External dependencies (top level)
dot.node('LHAPDF6', 'LHAPDF6', shape='box', style='filled', fillcolor='#D0E6FA')
dot.node('Deps', 'NumPy/SciPy/vegas/f2py', shape='box', style='filled', fillcolor='#D0E6FA')

# Central package
dot.node('nudisxs', 'nudisxs', shape='box', style='filled', fillcolor='#A8D08D', fontsize='14', fontname='Helvetica Bold')

# Submodules
dot.node('1dx', 'integrand_1dx', shape='box', style='filled', fillcolor='#FCE4D6')
dot.node('1dy', 'integrand_1dy', shape='box', style='filled', fillcolor='#FCE4D6')
dot.node('2dxy', 'integrand_2dxy', shape='box', style='filled', fillcolor='#FCE4D6')
dot.node('dis', 'dis', shape='box', style='filled', fillcolor='#FCE4D6')

# Edges from dependencies to nudisxs
dot.edge('LHAPDF6', 'nudisxs')
dot.edge('Deps', 'nudisxs')

# Edges from nudisxs to submodules
dot.edge('nudisxs', '1dx')
dot.edge('nudisxs', '1dy')
dot.edge('nudisxs', '2dxy')
dot.edge('nudisxs', 'dis')

# Render to file
dot.render('images/nudisxs_diagram', cleanup=False)
dot.view()