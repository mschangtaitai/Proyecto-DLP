
import graphviz

def graphAF(af, name):
    f = graphviz.Digraph('finite_state_machine', filename=name)
    f.attr(rankdir='LR', size='20')

    f.attr('node', shape='doublecircle')
    for i in af.finals:
        f.node(i)

    f.attr('node', shape='square')
    for i in af.start:
        f.node(i)

    f.attr('node', shape='circle')
    for i in af.trans:
        f.edge(i[0], i[2], label=i[1])

    f.view()
