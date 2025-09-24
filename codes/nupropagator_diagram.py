from graphviz import Digraph

# Create the graph
dot = Digraph(format='png')
dot.attr(rankdir='TB', style='filled', fontsize='12', fontname='Helvetica')

# External dependencies
dot.node('nudisxs', 'nudisxs\n(DIS cross sections)', shape='box', style='filled', fillcolor='#D0E6FA')
dot.node('PREM', 'PREM\n(Earth density)', shape='box', style='filled', fillcolor='#D0E6FA')
dot.node('libs', 'NumPy / SciPy / vegas', shape='box', style='filled', fillcolor='#D0E6FA')

# Main module
dot.node('nuPropagator', 'NuPropagator', shape='box', style='filled', fillcolor='#A8D08D', fontsize='14', fontname='Helvetica Bold')

# Submodules
dot.node('Earth', 'Earth\n(Material model)', shape='box', style='filled', fillcolor='#FCE4D6')
dot.node('Zfactor', 'Z-factor solver', shape='box', style='filled', fillcolor='#FCE4D6')
dot.node('Integrator', 'Integrator\n(Rectangle / Quad / Vegas)', shape='box', style='filled', fillcolor='#FCE4D6')

# Edges from dependencies
dot.edge('nudisxs', 'nuPropagator')
dot.edge('PREM', 'nuPropagator')
dot.edge('libs', 'nuPropagator')

# Edges from nuPropagator to components
dot.edge('nuPropagator', 'Earth')
dot.edge('nuPropagator', 'Zfactor')
dot.edge('nuPropagator', 'Integrator')

# Render the file
dot.render('images/nupropagator_diagram.png', cleanup=False)
dot.view()
