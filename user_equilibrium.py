import numpy as np
import pandas as pd
import networkx as nx

# Define the BPR travel time function
def bpr_travel_time(free_flow_time, capacity, volume):
    alpha = 0.15
    beta = 4
    return free_flow_time * (1 + alpha * (volume / capacity) ** beta)

# Load OD matrix
nodes = [1, 2, 4, 5, 10, 11, 13, 14, 15, 19, 20, 21, 22, 24]

od_matrix = np.array([
    [0, 1.08, 1.33, 1.07, 1.01, 0.83, 1.08, 1.03, 0.76, 1.05, 0.45, 0.64, 0.68, 0.7],
    [1.4, 0, 1.3, 1.54, 0.85, 1.11, 0.98, 0.81, 0.72, 1.28, 0.72, 0.59, 0.64, 0.58],
    [1.16, 1.41, 0, 1.01, 0.84, 1.09, 1.18, 1, 0.9, 0.98, 1.35, 0.74, 0.49, 0.79],
    [1.54, 1.59, 1.31, 0, 1.38, 0.95, 0.98, 0.86, 0.63, 0.85, 0.63, 0.82, 0.74, 0.6],
    [1.12, 0.99, 0.91, 1, 0, 1.23, 2.3, 1.12, 1.38, 0.89, 1.07, 0.91, 1.73, 0.67],
    [1.21, 0.98, 1, 0.81, 1.83, 0, 1.11, 1.28, 0.88, 1.13, 0.76, 0.66, 0.92, 0.79],
])

od_df = pd.DataFrame(od_matrix, index=nodes[:len(od_matrix)], columns=nodes[:len(od_matrix)])

# Load link data
num_links = 76
links_df = pd.DataFrame({
    "Link": list(range(1, num_links + 1)),
    "Free-flow Time (min)": np.random.uniform(1, 5, num_links),
    "Capacity (1000 veh/hr)": np.random.uniform(5, 50, num_links)
})

# Construct graph
G = nx.DiGraph()

for _, row in links_df.iterrows():
    link_id = row["Link"]
    free_flow_time = row["Free-flow Time (min)"]
    capacity = row["Capacity (1000 veh/hr)"] * 1000

    volume = 0
    travel_time = bpr_travel_time(free_flow_time, capacity, volume)

    source = link_id
    target = (link_id + 1) if (link_id + 1) <= num_links else 1

    G.add_edge(source, target, travel_time=travel_time, capacity=capacity)

# Frank-Wolfe algorithm for User Equilibrium
def all_or_nothing_assignment(G, od_matrix, nodes):
    link_flows = {edge: 0 for edge in G.edges()}
    for origin in nodes:
        for destination in nodes:
            if origin != destination and od_matrix.loc[origin, destination] > 0:
                demand = od_matrix.loc[origin, destination] * 1000
                path = nx.shortest_path(G, source=origin, target=destination, weight="travel_time")
                for i in range(len(path) - 1):
                    link_flows[(path[i], path[i+1])] += demand
    return link_flows

def update_travel_times(G, link_flows):
    for (u, v) in G.edges():
        free_flow_time = G[u][v]["travel_time"]
        capacity = G[u][v]["capacity"]
        volume = link_flows.get((u, v), 0)
        G[u][v]["travel_time"] = bpr_travel_time(free_flow_time, capacity, volume)

def frank_wolfe_algorithm(G, od_matrix, nodes, max_iterations=20, tol=1e-3):
    link_flows = {edge: 0 for edge in G.edges()}
    for iteration in range(max_iterations):
        new_flows = all_or_nothing_assignment(G, od_matrix, nodes)
        step_size = 1 / (iteration + 1)
        for edge in G.edges():
            link_flows[edge] = (1 - step_size) * link_flows[edge] + step_size * new_flows[edge]
        update_travel_times(G, link_flows)
        total_flow_change = sum(abs(link_flows[edge] - new_flows[edge]) for edge in G.edges())
        if total_flow_change < tol:
            break
    return link_flows

# Run Frank-Wolfe algorithm
ue_link_flows = frank_wolfe_algorithm(G, od_df, nodes)

# Compute v/c ratios and identify bottlenecks
vc_ratios = {edge: ue_link_flows[edge] / G[edge[0]][edge[1]]["capacity"] for edge in G.edges()}
bottleneck_links = {edge: vc for edge, vc in vc_ratios.items() if vc > 0.90}

# Results DataFrame
results_df = pd.DataFrame({
    "Link": [f"{edge[0]}->{edge[1]}" for edge in G.edges()],
    "Flow (veh/hr)": [ue_link_flows[edge] for edge in G.edges()],
    "Capacity (veh/hr)": [G[edge[0]][edge[1]]["capacity"] for edge in G.edges()],
    "v/c Ratio": [vc_ratios[edge] for edge in G.edges()],
    "Bottleneck": ["Yes" if edge in bottleneck_links else "No" for edge in G.edges()]
})

# Save results
results_df.to_csv("UE_Flow_Results.csv", index=False)
print("User Equilibrium flow results saved as 'UE_Flow_Results.csv'.")
