import math
import heapq
import itertools
import multiprocessing as mp
import copy

# --- Network Data Setup ---
link_data = {
    1: (3.6, 4500), 2: (2.4, 8500), 3: (3.2, 11500), 4: (3.0, 15400),
    5: (2.4, 46300), 6: (2.4, 33700), 7: (2.4, 39500), 8: (2.4, 25300),
    9: (1.2, 27800), 10: (3.3, 8500), 11: (1.2, 46400), 12: (2.4, 13400),
    13: (3.0, 10000), 14: (3.0, 9400), 15: (2.4, 9400), 16: (1.0, 21100),
    17: (1.8, 15200), 18: (1.2, 46300), 19: (1.2, 9300), 20: (1.8, 15200),
    21: (1.8, 9600), 22: (3.0, 9600), 23: (3.0, 19500), 24: (2.0, 9600),
    25: (1.8, 27300), 26: (1.8, 27300), 27: (3.0, 19500), 28: (3.6, 26500),
    29: (3.0, 9800), 30: (4.2, 9500), 31: (3.6, 9300), 32: (3.0, 19500),
    33: (3.6, 9400), 34: (2.4, 9300), 35: (2.4, 46300), 36: (3.6, 9300),
    37: (1.8, 51300), 38: (1.8, 51300), 39: (2.4, 9700), 40: (2.4, 9300),
    41: (3.0, 9800), 42: (2.4, 9400), 43: (3.2, 26500), 44: (3.0, 9800),
    45: (2.4, 9100), 46: (2.4, 20100), 47: (3.0, 9600), 48: (3.0, 9800),
    49: (1.2, 10000), 50: (1.8, 38900), 51: (4.2, 9500), 52: (1.2, 10000),
    53: (1.2, 9200), 54: (1.2, 46300), 55: (1.8, 38900), 56: (2.4, 7600),
    57: (2.4, 3900), 58: (1.2, 9200), 59: (2.4, 9500), 60: (2.6, 7600),
    61: (2.4, 5600), 62: (3.6, 9600), 63: (3.0, 9700), 64: (3.6, 9600),
    65: (1.4, 10000), 66: (1.8, 9300), 67: (2.4, 20100), 68: (2.8, 9700),
    69: (1.2, 10000), 70: (2.4, 9500), 71: (2.4, 9400), 72: (2.4, 9500),
    73: (1.2, 9700), 74: (2.4, 10900), 75: (1.8, 9300), 76: (1.2, 9700)
}

network_edges = [
    (1,2,1),(1,3,2),(2,1,3),(2,6,4),(3,1,5),(3,4,6),(3,12,7),
    (4,3,8),(4,5,9),(4,11,10),(5,4,11),(5,6,12),(5,9,13),
    (6,2,14),(6,5,15),(6,8,16),(7,8,17),(7,18,18),(8,6,19),
    (8,7,20),(8,9,21),(8,16,22),(9,5,23),(9,8,24),(9,10,25),
    (10,9,26),(10,11,27),(10,15,28),(10,16,29),(10,17,30),
    (11,4,31),(11,10,32),(11,12,33),(11,14,34),(12,3,35),
    (12,11,36),(12,13,37),(13,12,38),(13,24,39),(14,11,40),
    (14,15,41),(14,23,42),(15,10,43),(15,14,44),(15,19,45),
    (15,22,46),(16,8,47),(16,10,48),(16,17,49),(16,18,50),
    (17,10,51),(17,16,52),(17,19,53),(18,7,54),(18,16,55),
    (18,20,56),(19,15,57),(19,17,58),(19,20,59),(20,18,60),
    (20,19,61),(20,21,62),(20,22,63),(21,20,64),(21,22,65),
    (21,24,66),(22,15,67),(22,20,68),(22,21,69),(22,23,70),
    (23,14,71),(23,22,72),(23,24,73),(24,13,74),(24,21,75),
    (24,23,76)
]

adj = {node: [] for node in range(1, 25)}
for u, v, lid in network_edges:
    adj[u].append((v, lid))

demand = {
    1:  {2:1080, 4:1330, 5:1070, 10:1010, 11:830, 13:1080, 14:1030, 15:760, 19:1050, 20:450, 21:640, 22:680, 24:700},
    2:  {1:1400, 4:1300, 5:1540, 10:850, 11:1110, 13:980, 14:810, 15:720, 19:1280, 20:720, 21:590, 22:640, 24:580},
    4:  {1:1160, 2:1410, 5:1010, 10:840, 11:1090, 13:1180, 14:1000, 15:900, 19:980, 20:1350, 21:740, 22:490, 24:790},
    5:  {1:1540, 2:1590, 4:1310, 10:1380, 11:950, 13:980, 14:860, 15:630, 19:850, 20:630, 21:820, 22:740, 24:600},
    10: {1:1120, 2:990, 4:910, 5:1000, 11:1230, 13:2300, 14:1120, 15:1380, 19:890, 20:1070, 21:910, 22:1730, 24:670},
    11: {1:1210, 2:980, 4:1000, 5:810, 10:1830, 13:1110, 14:1280, 15:880, 19:1130, 20:760, 21:660, 22:920, 24:790},
    13: {1:1140, 2:920, 4:1150, 5:1130, 10:1050, 11:930, 14:830, 15:1040, 19:810, 20:670, 21:610, 22:530, 24:1080},
    14: {1:1180, 2:780, 4:920, 5:710, 10:1160, 11:1100, 13:930, 15:1540, 19:1680, 20:750, 21:700, 22:1020, 24:1110},
    15: {1:990, 2:730, 4:650, 5:870, 10:1120, 11:1340, 13:940, 14:1430, 19:1480, 20:1420, 21:1160, 22:1390, 24:770},
    19: {1:1010, 2:1280, 4:760, 5:560, 10:1240, 11:730, 13:620, 14:1130, 15:1270, 20:1130, 21:1140, 22:890, 24:770},
    20: {1:730, 2:580, 4:1560, 5:810, 10:990, 11:750, 13:500, 14:840, 15:1340, 19:1370, 21:1310, 22:1100, 24:650},
    21: {1:470, 2:650, 4:740, 5:780, 10:980, 11:710, 13:710, 14:740, 15:1110, 19:1120, 20:1070, 22:1490, 24:1430},
    22: {1:920, 2:560, 4:680, 5:1170, 10:860, 11:880, 13:680, 14:720, 15:1090, 19:960, 20:1120, 21:1240, 24:970},
    24: {1:740, 2:550, 4:700, 5:630, 10:630, 11:910, 13:1590, 14:980, 15:1000, 19:640, 20:610, 21:1380, 22:920}
}

alpha, beta = 0.15, 4.0

# --- Define Candidate Projects ---
# New links: (from_node, to_node, option_id, free_flow_time, capacity, cost)
new_links = {
    'A#1': [
        (7, 2, 1, 4.0, 4000, 12),  # A#1_1
        (7, 2, 2, 4.0, 6000, 17)   # A#1_2
    ],
    'A#2': [
        (2, 7, 1, 4.0, 4000, 10),  # A#2_1
        (2, 7, 2, 4.0, 6000, 15)   # A#2_2
    ],
    'B#1': [
        (15, 11, 1, 3.5, 4000, 13),  # B#1_1
        (15, 11, 2, 3.5, 6000, 18)   # B#1_2
    ],
    'B#2': [
        (11, 15, 1, 3.5, 4000, 11),  # B#2_1
        (11, 15, 2, 3.5, 6000, 16)   # B#2_2
    ],
    'C#1': [
        (21, 13, 1, 4.0, 6000, 15),  # C#1_1
        (21, 13, 2, 4.0, 8000, 22)   # C#1_2
    ],
    'C#2': [
        (13, 21, 1, 4.0, 6000, 12),  # C#2_1
        (13, 21, 2, 4.0, 8000, 19)   # C#2_2
    ]
}

# Existing links: (link_id, capacity_increase, cost)
existing_links = {
    2: [
        (1, 2000, 3),  # Link2_1
        (2, 4000, 6)   # Link2_2
    ],
    57: [
        (1, 2000, 2),  # Link57_1
        (2, 4000, 4)   # Link57_2
    ]
}

# Budget
budget = 60  # $60 million

# --- Travel Time and Cost Functions ---
def travel_time_BPR(t0, cap, flow):
    """Calculate BPR travel time: t_a(x_a) = t0 * (1 + alpha * (x_a / cap)^beta)"""
    return t0 * (1 + alpha * (flow / cap) ** beta)

def marginal_cost(t0, cap, flow):
    """Calculate marginal cost: t_a(x_a) + x_a * t_a'(x_a) = t0 * [1 + alpha * (1 + beta) * (x_a / cap)^beta]"""
    return t0 * (1 + alpha * (1 + beta) * (flow / cap) ** beta)

# --- All-or-Nothing Assignment ---
def all_or_nothing_assign(travel_time, adj, demand, link_data):
    """Perform all-or-nothing assignment based on given travel times."""
    flows = {lid: 0 for lid in link_data}
    for origin, dests in demand.items():
        dist = {node: math.inf for node in adj}
        prev = {node: None for node in adj}
        dist[origin] = 0
        pq = [(0, origin)]
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, lid in adj[u]:
                new_d = d + travel_time[lid]
                if new_d < dist[v]:
                    dist[v] = new_d
                    prev[v] = (u, lid)
                    heapq.heappush(pq, (new_d, v))
        for dest, vol in dests.items():
            if vol == 0:
                continue
            node = dest
            while node != origin and prev[node] is not None:
                u, lid = prev[node]
                flows[lid] += vol
                node = u
    return flows

# --- Line Search Functions for SO ---
def compute_dZ_dalpha_SO(alpha, x, y, link_data):
    """Compute derivative of SO objective: sum_a (y_a - x_a) * mc_a(x_a + alpha (y_a - x_a))"""
    sum_dZ = 0
    for lid, (t0, cap) in link_data.items():
        omega = x[lid] + alpha * (y[lid] - x[lid])
        mc_omega = marginal_cost(t0, cap, omega)
        sum_dZ += (y[lid] - x[lid]) * mc_omega
    return sum_dZ

def line_search_SO(x, y, link_data, tol=1e-6):
    """Find optimal step size alpha for SO using bisection."""
    alpha_low, alpha_high = 0, 1
    dZ0 = compute_dZ_dalpha_SO(0, x, y, link_data)
    if dZ0 >= 0:
        return 0
    dZ1 = compute_dZ_dalpha_SO(1, x, y, link_data)
    if dZ1 <= 0:
        return 1
    while alpha_high - alpha_low > tol:
        alpha_mid = (alpha_low + alpha_high) / 2
        dZ_mid = compute_dZ_dalpha_SO(alpha_mid, x, y, link_data)
        if dZ_mid > 0:
            alpha_high = alpha_mid
        elif dZ_mid < 0:
            alpha_low = alpha_mid
        else:
            return alpha_mid
    return (alpha_low + alpha_high) / 2

# --- Line Search Functions for UE ---
def compute_dZ_dalpha_UE(alpha, x, y, link_data):
    """Compute derivative of UE objective: sum_a t_a(x_a + alpha (y_a - x_a)) * (y_a - x_a)"""
    sum_dZ = 0
    for lid, (t0, cap) in link_data.items():
        omega = x[lid] + alpha * (y[lid] - x[lid])
        t_omega = travel_time_BPR(t0, cap, omega)
        sum_dZ += t_omega * (y[lid] - x[lid])
    return sum_dZ

def line_search_UE(x, y, link_data, tol=1e-6):
    """Find optimal step size alpha for UE using bisection."""
    alpha_low, alpha_high = 0, 1
    dZ0 = compute_dZ_dalpha_UE(0, x, y, link_data)
    if dZ0 >= 0:
        return 0
    dZ1 = compute_dZ_dalpha_UE(1, x, y, link_data)
    if dZ1 <= 0:
        return 1
    while alpha_high - alpha_low > tol:
        alpha_mid = (alpha_low + alpha_high) / 2
        dZ_mid = compute_dZ_dalpha_UE(alpha_mid, x, y, link_data)
        if dZ_mid > 0:
            alpha_high = alpha_mid
        elif dZ_mid < 0:
            alpha_low = alpha_mid
        else:
            return alpha_mid
    return (alpha_low + alpha_high) / 2

# --- Worker Function for Parallel Processing ---
def worker(args):
    combination, network_edges_base, adj_base, demand, link_data_base = args
    # Deep copy base network data
    network_edges = copy.deepcopy(network_edges_base)
    adj = copy.deepcopy(adj_base)
    link_data = copy.deepcopy(link_data_base)
    next_link_id = max(link_data.keys()) + 1

    # Process the combination
    total_cost = 0
    # New links
    for link_name, option in combination.items():
        if option == 0:
            continue
        if link_name in ['A#1', 'A#2', 'B#1', 'B#2', 'C#1', 'C#2']:
            from_node, to_node, _, free_flow_time, capacity, cost = new_links[link_name][option-1]
            total_cost += cost
            network_edges.append((from_node, to_node, next_link_id))
            adj[from_node].append((to_node, next_link_id))
            link_data[next_link_id] = (free_flow_time, capacity)
            next_link_id += 1
        else:  # Existing links
            link_id = int(link_name)
            _, capacity_increase, cost = existing_links[link_id][option-1]
            total_cost += cost
            t0, cap = link_data[link_id]
            link_data[link_id] = (t0, cap + capacity_increase)

    if total_cost > budget:
        return float('inf'), {}

    # Compute UE flows
    travel_time = {lid: t0 for lid, (t0, cap) in link_data.items()}
    flows = all_or_nothing_assign(travel_time, adj, demand, link_data)
    prev_flows = flows.copy()
    max_iterations = 1000
    epsilon = 0.001
    for it in range(1, max_iterations + 1):
        for lid, (t0, cap) in link_data.items():
            travel_time[lid] = travel_time_BPR(t0, cap, flows[lid])
        new_flows = all_or_nothing_assign(travel_time, adj, demand, link_data)
        alpha_opt = line_search_UE(flows, new_flows, link_data)  # Use UE line search
        for lid in flows:
            flows[lid] = flows[lid] + alpha_opt * (new_flows[lid] - flows[lid])
        numerator = math.sqrt(sum((flows[lid] - prev_flows[lid])**2 for lid in flows))
        denominator = sum(prev_flows[lid] for lid in prev_flows)
        relative_gap = numerator / denominator if denominator > 0 else 0
        if relative_gap < epsilon:
            break
        prev_flows = flows.copy()

    total_tt = sum(flows[lid] * travel_time_BPR(t0, cap, flows[lid]) for lid, (t0, cap) in link_data.items())
    return total_tt, combination

# --- Compute System Optimum (SO) Benchmark ---
travel_time_free = {lid: t0 for lid, (t0, _) in link_data.items()}
flows_SO = all_or_nothing_assign(travel_time_free, adj, demand, link_data)
prev_flows = flows_SO.copy()
epsilon = 0.001
max_iterations = 1000

for it in range(1, max_iterations + 1):
    current_mc = {lid: marginal_cost(t0, cap, flows_SO[lid]) for lid, (t0, cap) in link_data.items()}
    y = all_or_nothing_assign(current_mc, adj, demand, link_data)
    alpha_opt = line_search_SO(flows_SO, y, link_data)
    for lid in flows_SO:
        flows_SO[lid] = flows_SO[lid] + alpha_opt * (y[lid] - flows_SO[lid])
    numerator = math.sqrt(sum((flows_SO[lid] - prev_flows[lid])**2 for lid in flows_SO))
    denominator = sum(prev_flows[lid] for lid in prev_flows)
    relative_gap = numerator / denominator if denominator > 0 else 0
    if relative_gap < epsilon:
        print(f"SO converged after {it} iterations with relative gap {relative_gap:.6f}")
        break
    prev_flows = flows_SO.copy()
else:
    print(f"SO reached maximum iterations ({max_iterations}) with relative gap {relative_gap:.6f}")

total_tt_SO = sum(flows_SO[lid] * travel_time_BPR(t0, cap, flows_SO[lid]) for lid, (t0, cap) in link_data.items())

# --- Compute UE without Improvements ---
travel_time_UE_no_improvements = {lid: t0 for lid, (t0, cap) in link_data.items()}
flows_UE_no_improvements = all_or_nothing_assign(travel_time_UE_no_improvements, adj, demand, link_data)
prev_flows = flows_UE_no_improvements.copy()
for it in range(1, max_iterations + 1):
    for lid, (t0, cap) in link_data.items():
        travel_time_UE_no_improvements[lid] = travel_time_BPR(t0, cap, flows_UE_no_improvements[lid])
    new_flows = all_or_nothing_assign(travel_time_UE_no_improvements, adj, demand, link_data)
    alpha_opt = line_search_UE(flows_UE_no_improvements, new_flows, link_data)
    for lid in flows_UE_no_improvements:
        flows_UE_no_improvements[lid] = flows_UE_no_improvements[lid] + alpha_opt * (new_flows[lid] - flows_UE_no_improvements[lid])
    numerator = math.sqrt(sum((flows_UE_no_improvements[lid] - prev_flows[lid])**2 for lid in flows_UE_no_improvements))
    denominator = sum(prev_flows[lid] for lid in prev_flows)
    relative_gap = numerator / denominator if denominator > 0 else 0
    if relative_gap < epsilon:
        print(f"UE (no improvements) converged after {it} iterations with relative gap {relative_gap:.6f}")
        break
    prev_flows = flows_UE_no_improvements.copy()

total_tt_UE_no_improvements = sum(flows_UE_no_improvements[lid] * travel_time_BPR(t0, cap, flows_UE_no_improvements[lid])
                                 for lid, (t0, cap) in link_data.items())

# Output equilibrium results without improvements
print("\nEquilibrium Results (No Improvements):")
for lid, x in flows_UE_no_improvements.items():
    t = travel_time_BPR(*link_data[lid], x)
    v_c = x / link_data[lid][1]
    print(f"Link {lid}: volume={x:.1f} veh/hr, travel_time={t:.1f} min, v/c={v_c:.2f}")

# Generate all possible combinations with mutual exclusivity
options = {
    'A#1': [0, 1, 2],  # 0: none, 1: A#1_1, 2: A#1_2
    'A#2': [0, 1, 2],  # 0: none, 1: A#2_1, 2: A#2_2
    'B#1': [0, 1, 2],  # 0: none, 1: B#1_1, 2: B#1_2
    'B#2': [0, 1, 2],  # 0: none, 1: B#2_1, 2: B#2_2
    'C#1': [0, 1, 2],  # 0: none, 1: C#1_1, 2: C#1_2
    'C#2': [0, 1, 2],  # 0: none, 1: C#2_1, 2: C#2_2
    '2': [0, 1, 2],    # 0: none, 1: Link2_1, 2: Link2_2
    '57': [0, 1, 2]     # 0: none, 1: Link57_1, 2: Link57_2
}

combinations = [dict(zip(options.keys(), comb)) for comb in itertools.product(*options.values())]
print(f"\nTotal number of improvement combinations: {len(combinations)}")

# Prepare arguments for parallel processing
args_list = [(comb, network_edges, adj, demand, link_data) for comb in combinations]

# Parallel evaluation of combinations
if __name__ == '__main__':
    num_processes = mp.cpu_count()
    print(f"Using {num_processes} processes for parallel computation.")
    with mp.Pool(processes=num_processes) as pool:
        results = pool.map(worker, args_list)

    # Find the best result
    best_result = min(results, key=lambda x: x[0])
    best_travel_time, best_combination = best_result

    # Compute total cost of the best combination
    total_cost = 0
    for link_name, option in best_combination.items():
        if option == 0:
            continue
        if link_name in ['A#1', 'A#2', 'B#1', 'B#2', 'C#1', 'C#2']:
            suffix = f"_{option}"  # e.g., A#1_1 or A#1_2
            _, _, _, _, _, cost = new_links[link_name][option-1]
            total_cost += cost
            print(f"Build {link_name}{suffix}: Cost = ${cost}M")
        else:
            link_id = int(link_name)
            _, _, cost = existing_links[link_id][option-1]
            total_cost += cost
            option_id = option
            print(f"Expand Link {link_id} (Option {option_id}): Cost = ${cost}M")

    print(f"\nTotal Cost: ${total_cost}M")
    print(f"Total System Travel Time with Improvements (UE): {best_travel_time:.2f} vehicle-minutes")
    print(f"Total System Travel Time without Improvements (UE): {total_tt_UE_no_improvements:.2f} vehicle-minutes")
    print(f"Reduction in UE Travel Time: {(total_tt_UE_no_improvements - best_travel_time):.2f} vehicle-minutes")
    print(f"System Optimum Travel Time (SO): {total_tt_SO:.2f} vehicle-minutes")
    print(f"Difference from SO: {(total_tt_SO - best_travel_time):.2f} vehicle-minutes")