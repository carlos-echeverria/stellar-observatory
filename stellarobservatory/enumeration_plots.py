# Generate tikz figures (matplotlib2tikz) for section 3:
#
#   Quorum enumeration:
#               n=4,...10, 2 plots (t=n-1, t=floor(2/3 * n + 1)),
#               timings and number of quorums
#
#   Quorum intersection:
#               same cases as quorum enumeration, 2 plots
#               only timings


import quorums
import quorum
import quorum_intersection
import utils
import time
import tikzplotlib
import matplotlib.pyplot as plt
import numpy as np


n_orgs = [4, 5, 6, 7, 8, 9, 10]
timings_n_1 = [38, 135, 625, 3617, 26081, 152506, 782316]
numb_qs_n_1 = [1280, 6144, 28672, 131072, 589824, 2621440, 11534336]

fig, ax1 = plt.subplots()

ax1.set_yscale('log')
ax1.plot(n_orgs, numb_qs_n_1, 'b--',color='darkgreen', lw=2, label='quorums')
ax1.set_xlabel('Number of Organizations (n)')
ax1.set_ylabel('Ellapsed time (ms)', color='darkgreen')
ax1.tick_params(axis='y', labelcolor='darkgreen')

ax2 = ax1.twinx()
ax2.set_yscale('log')
ax2.plot(n_orgs, timings_n_1, 'm:', color='blue', lw=2, label='time')
# ax2.set_xlabel('Number of Organizations (n)')
ax2.set_ylabel('Quorums Found', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# fig.tight_layout()  # otherwise right y-label is slightly clipped
fig.legend(loc='upper left', fontsize='large')
fig.suptitle('Threshold: n-1', fontsize=16)
tikzplotlib.save("n_1.tex")


n_orgs2 = [4, 5, 6, 7, 8, 9]
timings_n_2 = [48, 155, 894, 10351, 70939, 322751]
numb_qs_n_2 = [1280, 6144, 28672,475136,2424832, 12058624]


fig, ax1 = plt.subplots()

ax1.set_yscale('log')
ax1.plot(n_orgs2, numb_qs_n_2, 'b--',color='darkgreen', lw=2, label='quorums')
ax1.set_xlabel('Number of Organizations (n)')
ax1.set_ylabel('Ellapsed time (ms)', color='darkgreen')
ax1.tick_params(axis='y', labelcolor='darkgreen')

ax2 = ax1.twinx()
ax2.set_yscale('log')
ax2.plot(n_orgs2, timings_n_2, 'm:', color='blue', lw=2, label='time')
# ax2.set_xlabel('Number of Organizations (n)')
ax2.set_ylabel('Quorums Found', color='blue')
ax2.tick_params(axis='y', labelcolor='blue')

# fig.tight_layout()  # otherwise right y-label is slightly clipped
fig.legend(loc='upper left', fontsize='large')
fig.suptitle('Threshold: floor(2/3 * n + 1)', fontsize=16)
tikzplotlib.save("floor.tex")

plt.show()


#----------------------------------------------------------------------------

# base_quorum_slice_definition = {
#     'threshold': 3,
#     'validators': set(),
#     'innerQuorumSets': [
#         {'threshold': 2, 'validators': {'blockdaemon-1', 'blockdaemon-2', 'blockdaemon-3'}, 'innerQuorumSets': []},
#         {'threshold': 2, 'validators': {'coinqvest-de', 'coinqvest-fi', 'coinqvest-hk'}, 'innerQuorumSets': []},
#         {'threshold': 2, 'validators': {'satoshipay-de-fra', 'satoshipay-sg-sin', 'satoshipay-us-iowa'}, 'innerQuorumSets': []},
#         {'threshold': 2, 'validators': {'sdf1', 'sdf2', 'sdf3'}, 'innerQuorumSets': []},
#         {'threshold': 3, 'validators': {'lobstr1', 'lobstr2', 'lobstr3', 'lobstr4', 'lobstr5'}, 'innerQuorumSets': []},
#         {'threshold': 2, 'validators': {'keybase0', 'keybase1', 'keybase2'}, 'innerQuorumSets': []}
#     ]
# }

#----------------------------------------------------------------------------


# def get_root_quorum_slice_definition(n_orgs):
#     return {
#         'threshold': n_orgs - 1,
#         'validators': set(),
#         'innerQuorumSets': [
#             {'threshold': 2, 'validators': {org*3, org*3+1, org*3+2}, 'innerQuorumSets': []}
#             for org in range(n_orgs)
#         ]
#     }
#
#
# def get_nodes(qs_definition):
#     nodes = set(qs_definition['validators'])
#     for inner_qs_definition in qs_definition['innerQuorumSets']:
#         nodes = nodes.union(get_nodes(inner_qs_definition))
#     return nodes
#
#
# def satisfies_definition(candidate, slice_definition):
#     satisfied = len(slice_definition['validators'].intersection(candidate))
#     for inner_slice_definition in slice_definition['innerQuorumSets']:
#         if satisfies_definition(candidate, inner_slice_definition):
#             satisfied += 1
#     return satisfied >= slice_definition['threshold']
#
#
#
# for n_orgs in range(4, 10):
#     base_quorum_slice_definition = get_root_quorum_slice_definition(n_orgs)
#     nodes = get_nodes(base_quorum_slice_definition)
#     quorum_slice_definition_by_node = {
#         node: quorum.get_normalized_qset_definition({'publicKey': node, 'quorumSet': base_quorum_slice_definition})
#         for node in nodes
#     }
#
#
#     def is_slice_contained(candidate, node):
#         return satisfies_definition(set(candidate), quorum_slice_definition_by_node[node])
#
#
#     # count = 0
#     # for quorum_candidate in utils.sets.powerset(nodes):
#     #     if len(quorum_candidate) > 0 and all([is_slice_contained(quorum_candidate, node) for node in quorum_candidate]):
#     #         count += 1
#     # print(count)
#
#
#     counter = 0
#     for quorum_candidate in quorums.enumerate_quorums(([is_slice_contained(quorum_candidate, node) for node in nodes], nodes)):
#         if len(quorum_candidate) > 0 and all([is_slice_contained(quorum_candidate, node) for node in nodes]):
#             counter += 1
#     print(counter)
#
#
#     # start = time.time()
#     # start = int(round(time.time() * 1000))
#     quorums = quorums.enumerate_quorums((is_slice_contained(candidate, node), nodes))
#     finish = int(round(time.time() * 1000))
#     t_time = finish-start
#     print(f"Organizations: {n_orgs}\nQuorums found: {quorums}\nEllapsed time: {finish-start} milliseconds")

    # start2 = int(round(time.time() * 1000))
    # intersec = quorum_intersection.quorum_intersection((is_slice_contained(node, nodes), nodes))
    # finish2 = int(round(time.time() * 1000))
    # t_time2 = finish2-start2
    # print(f"Organizations: {n_orgs}\nIntersection: {intersec}\nEllapsed time: {finish2-start2} milliseconds")
