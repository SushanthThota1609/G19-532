from langgraph.graph import StateGraph, END
from graphviz import Digraph

def draw_langgraph_structure():
    dot = Digraph(comment='LangGraph SQL Viz Flow')
    dot.attr(rankdir='LR')  # Left to right

    # Nodes
    dot.node('supervisor', 'Supervisor Node')
    dot.node('sql_agent', 'SQL Agent')
    dot.node('viz_agent', 'Visualization Agent')
    dot.node('final_summary', 'Final Summary')
    dot.node('END', 'End', shape='doublecircle')

    # Edges from supervisor decision
    dot.edge('supervisor', 'sql_agent', label='if no sql_query')
    dot.edge('supervisor', 'viz_agent', label='if df exists')
    dot.edge('supervisor', 'final_summary', label='else')

    # Loopback
    dot.edge('sql_agent', 'supervisor')
    dot.edge('viz_agent', 'supervisor')

    # Final step
    dot.edge('final_summary', 'END')

    # Render
    dot.render('langgraph_structure', format='png', cleanup=True)
    print("Graph saved as langgraph_structure.png")

draw_langgraph_structure()
