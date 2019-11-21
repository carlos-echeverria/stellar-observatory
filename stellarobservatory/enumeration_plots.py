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
import utils
import time
import matplotlib.pyplot as plt
import numpy as np


n_orgs = [4, 5, 6, 7, 8, 9, 10]
timings_n_1 = [38, 135, 625, 3617, 26081, 152506, 782316]
numb_qs_n_1 = [1280, 6144, 28672, 131072, 589824, 2621440, 11534336]

fig, ax = plt.subplots()
fig.suptitle('Threshold = n-1')

ax.set_yscale('log')
ax.plot(n_orgs, numb_qs_n_1, 'r--', lw=2, label='quorums')
plt.xlabel('Number of Organizations (n)')
plt.ylabel('Ellapsed time (ms)', color='r')
plt.legend(loc='best', fontsize='large')

ax2 = ax.twinx()
ax2.set_yscale('log')
ax2.plot(n_orgs, timings_n_1, 'b:', lw=2, label='time')
# ax2.set(ylabel='quorums')
plt.ylabel('Quorums Found', color='b')
plt.legend(loc='best', fontsize='large')


n_orgs2 = [4, 5, 6, 7, 8, 9]
timings_n_2 = [48, 155, 894, 10351, 70939, 322751]
numb_qs_n_2 = [1280, 6144, 28672,475136,2424832, 12058624]



fig, ax = plt.subplots()
fig.suptitle('Threshold = floor(2/3 * n + 1)')

ax.set_yscale('log')
ax.plot(n_orgs2, numb_qs_n_2, 'r--', lw=2, label='quorums')
plt.xlabel('Number of Organizations (n)')
plt.ylabel('Ellapsed time (ms)', color='r')
plt.legend(loc='best', fontsize='large')

ax2 = ax.twinx()
ax2.set_yscale('log')
ax2.plot(n_orgs2, timings_n_2, 'b:', lw=2, label='time')
# ax2.set(ylabel='quorums')
plt.ylabel('Quorums Found', color='b')
plt.legend(loc='best', fontsize='large')

#
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
#
#
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
#
# def get_nodes(qs_definition):
#     nodes = set(qs_definition['validators'])
#     for inner_qs_definition in qs_definition['innerQuorumSets']:
#         nodes = nodes.union(get_nodes(inner_qs_definition))
#     return nodes
#
#
# nodes = get_nodes(base_quorum_slice_definition)
#
#
# def satisfies_definition(candidate, slice_definition):
#     satisfied = len(slice_definition['validators'].intersection(candidate))
#     for inner_slice_definition in slice_definition['innerQuorumSets']:
#         if satisfies_definition(candidate, inner_slice_definition):
#             satisfied += 1
#     return satisfied >= slice_definition['threshold']
#
# for n_orgs in range(4, 7):
#     base_quorum_slice_definition = get_root_quorum_slice_definition(n_orgs)
#     nodes = get_nodes(base_quorum_slice_definition)
#     quorum_slice_definition_by_node = {
#         node: quorum.get_normalized_qset_definition({ 'publicKey': node, 'quorumSet': base_quorum_slice_definition })
#         for node in nodes
#     }
#
#     def is_slice_contained(candidate, node):
#         return satisfies_definition(set(candidate), quorum_slice_definition_by_node[node])
#
#     quorums = quorums.enumerate_quorums(is_slice_contained, nodes)
#
# # counter = 0
# # start2 = int(round(time.time() * 1000))
# # for quorum_candidate in quorums.enumerate_quorums(nodes):
# #     if len(quorum_candidate) > 0 and all([contains_slice(quorum_candidate, node) for node in quorum_candidate]):
# #         counter += 1
# #
# #
# # end2 = int(round(time.time() * 1000))
#
# counter=10
# start2=8
# end2=10
# print(f"Iteration count: {counter}\nElapsed time: {end2-start2} milliseconds")
#


# x = range(-10, 11)
# y = [x*x for x in x]
# fig, (ax1, ax2) = plt.subplots(2, 1)
# fig.suptitle('Threshold = n-1')
#
# ax1.set_title("Quorums Found")
# ax1.set_xlabel("threshold")
# ax1.set_ylabel("quorums")
# ax1.set_yscale('log')
# ax1.plot(n, numb_qs_n_1, color='red', lw=2)
#
# # ax2 = fig.add_subplot(2, 1, 2)
# ax2.set_title("Ellapsed time")
# ax2.set_xlabel("threshold")
# ax2.set_ylabel("time")
# ax2.set_yscale('log')
# ax2.plot(n, timings_n_1, color='blue', lw=2)




# fig2, axs = plt.subplots(2, sharex=True)
# fig2.suptitle('Threshold = n-1')
#
# axs[0].set_title("Quorums Found")
# axs[0].set_xlabel("threshold")
# axs[0].set_ylabel("quorums")
# axs[0].set_yscale('log')
# axs[0].plot(n, numb_qs_n_1, color='red', lw=2)
#
# # ax2 = fig.add_subplot(2, 1, 2)
# ax[1].set_title("Ellapsed time")
# ax[1].set_xlabel("threshold")
# ax[1].set_ylabel("time")
# ax[1].set_yscale('log')
# ax[1].plot(n, timings_n_1, color='blue', lw=2)
#
#
# for ax in axs:
#     ax.label_outer()



plt.show()
