import math
import heapq

# --- Network Data Setup ---
# (link_data, adj, demand, alpha, beta remain unchanged from the original code)
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

alpha = 0.15
beta = 4.0

# --- Frank-Wolfe Algorithm ---
def all_or_nothing_assign(travel_time):
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

# Line search helper function: computes dZ/dalpha
def compute_dZ_dalpha(x, y, alpha_step, link_data):
    sum_dZ = 0
    for lid in link_data:
        t0, cap = link_data[lid]
        omega = x[lid] + alpha_step * (y[lid] - x[lid])
        t_omega = t0 * (1 + alpha * (omega / cap)**beta)
        sum_dZ += t_omega * (y[lid] - x[lid])
    return sum_dZ

# Line search using bisection method
def line_search(x, y, link_data, tol=1e-6):
    alpha_low = 0
    alpha_high = 1
    dZ0 = compute_dZ_dalpha(x, y, 0, link_data)
    if dZ0 >= 0:
        return 0
    dZ1 = compute_dZ_dalpha(x, y, 1, link_data)
    if dZ1 <= 0:
        return 1
    while alpha_high - alpha_low > tol:
        alpha_mid = (alpha_low + alpha_high) / 2
        dZ_mid = compute_dZ_dalpha(x, y, alpha_mid, link_data)
        if dZ_mid > 0:
            alpha_high = alpha_mid
        elif dZ_mid < 0:
            alpha_low = alpha_mid
        else:
            return alpha_mid
    return (alpha_low + alpha_high) / 2

# Initialization
travel_time = {lid: t0 for lid, (t0, cap) in link_data.items()}
flows = all_or_nothing_assign(travel_time)
prev_flows = flows.copy()

# Convergence parameters
epsilon = 0.001
max_iterations = 1000

# Iterative update
for it in range(1, max_iterations + 1):
    # Update travel times
    for lid, (t0, cap) in link_data.items():
        travel_time[lid] = t0 * (1 + alpha * (flows[lid] / cap)**beta)
    # All-or-nothing assignment
    new_flows = all_or_nothing_assign(travel_time)
    # Line search for optimal alpha
    alpha_opt = line_search(flows, new_flows, link_data)
    # Update flows
    for lid in flows:
        flows[lid] = flows[lid] + alpha_opt * (new_flows[lid] - flows[lid])
    # Convergence test
    numerator = math.sqrt(sum((flows[lid] - prev_flows[lid])**2 for lid in flows))
    denominator = sum(prev_flows[lid] for lid in prev_flows)
    relative_gap = numerator / denominator if denominator > 0 else 0
    if relative_gap < epsilon:
        print(f"Converged after {it} iterations with relative gap {relative_gap:.6f}")
        break
    prev_flows = flows.copy()
else:
    print(f"Reached maximum iterations ({max_iterations}) with relative gap {relative_gap:.6f}")

# Output equilibrium results
print("\nEquilibrium Results:")
for lid, x in flows.items():
    t = travel_time[lid]
    v_c = x / link_data[lid][1]
    print(f"Link {lid}: volume={x:.1f} veh/hr, travel_time={t:.1f} min, v/c={v_c:.2f}")

bottleneck_links = {lid: x / link_data[lid][1] for lid, x in flows.items() if x / link_data[lid][1] >= 0.89}
print("\nBottleneck Links (v/c >= 0.90):")
for lid, vc in bottleneck_links.items():
    print(f"Link {lid}: v/c ratio = {vc:.2f}")

# total travelling time
total_tt = sum(flows[lid] * travel_time[lid] for lid in flows)

print(f"\nTotal Travelling Time: {total_tt:.2f} min")