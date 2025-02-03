import plotly.graph_objects as go
import networkx as nx
import numpy as np

G = nx.DiGraph()
G.add_node(0) 

positions = {0: np.array([0.0, 0.0, 0.0])}
velocities = {0: np.array([0.0, 0.0, 0.0])}
mass = 1.0
spring_constant = 0.1
damping = 0.9

def expand_tree():
    global G, positions, velocities
    new_nodes = []
    for node in list(G.nodes()):
        if len(list(G.successors(node))) == 0:  
            new_node = len(G.nodes())
            G.add_node(new_node)
            G.add_edge(node, new_node)
            new_nodes.append(new_node)

    for new_node in new_nodes:
        parent = list(G.predecessors(new_node))[0]
        parent_pos = positions[parent]
        random_offset = np.random.rand(3) - 0.5
        positions[new_node] = parent_pos + random_offset * 0.1
        velocities[new_node] = np.array([0.0, 0.0, 0.0])

def update_positions():
    global positions, velocities

    forces = {node: np.zeros(3) for node in G.nodes()}
    for edge in G.edges():
        node1, node2 = edge
        pos1 = positions[node1]
        pos2 = positions[node2]

        displacement = pos2 - pos1
        distance = np.linalg.norm(displacement)
        if distance > 0:
            force_magnitude = spring_constant * (distance - 0.1)
            force_direction = displacement / distance
            force = force_magnitude * force_direction
            forces[node1] += force
            forces[node2] -= force

    for node in G.nodes():
        acceleration = forces[node] / mass
        velocities[node] += acceleration
        velocities[node] *= damping
        positions[node] += velocities[node]

frames = []
for _ in range(20):
    expand_tree()
    update_positions()

    edge_x, edge_y, edge_z = [], [], []
    for edge in G.edges():
        x0, y0, z0 = positions[edge[0]]
        x1, y1, z1 = positions[edge[1]]
        edge_x.extend([x0, x1, None])
        edge_y.extend([y0, y1, None])
        edge_z.extend([z0, z1, None])

    node_x, node_y, node_z = [], [], []
    for node in G.nodes():
        x, y, z = positions[node]
        node_x.append(x)
        node_y.append(y)
        node_z.append(z)

    frames.append(go.Frame(data=[
        go.Scatter3d(
            x=edge_x, y=edge_y, z=edge_z,
            line=dict(width=2, color='lightblue'),
            mode='lines'
        ),
        go.Scatter3d(
            x=node_x, y=node_y, z=node_z,
            mode='markers',
            marker=dict(size=5, color='black')
        )
    ]))

fig = go.Figure(
    data=[
        go.Scatter3d(
            x=[], y=[], z=[],
            line=dict(width=2, color='lightblue'),
            mode='lines'
        ),
        go.Scatter3d(
            x=[], y=[], z=[],
            mode='markers',
            marker=dict(size=5, color='black')
        )
    ],
    frames=frames
)

fig.update_layout(
    showlegend=False,
    scene=dict(
        xaxis=dict(showbackground=False),
        yaxis=dict(showbackground=False),
        zaxis=dict(showbackground=False)
    ),
    margin=dict(t=0, l=0, b=0, r=0),
    paper_bgcolor='white',
    plot_bgcolor='white'
)

fig.update_layout(updatemenus=[dict(type="buttons", showactive=False,
                                    buttons=[dict(label="Play",
                                                  method="animate",
                                                  args=[None, dict(frame=dict(duration=200, redraw=True), fromcurrent=True)])])])

fig.show()