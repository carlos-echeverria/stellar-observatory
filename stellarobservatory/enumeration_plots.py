# Carlos: generate tikz figures (matplotlib2tikz) for section 3:
# Quorum enumeration: n=4,...10, 2 plots (t=n-1, t=floor(2/3 * n + 1)), timings and number of quorums
# Quorum intersection: 2 plots (same cases as quorum enumeration), only timings

import stellarobservatory
import matplotlib.pyplot as plt  # import Matplotlib sub-module

base_quorum_slice_definition = {
    'threshold': 5,
    'validators': set(),
    'innerQuorumSets': [
        {'threshold': 2, 'validators': {'blockdaemon-1', 'blockdaemon-2', 'blockdaemon-3'}, 'innerQuorumSets': []},
        {'threshold': 2, 'validators': {'coinqvest-de', 'coinqvest-fi', 'coinqvest-hk'}, 'innerQuorumSets': []},
        {'threshold': 2, 'validators': {'satoshipay-de-fra', 'satoshipay-sg-sin', 'satoshipay-us-iowa'}, 'innerQuorumSets': []},
        {'threshold': 2, 'validators': {'sdf1', 'sdf2', 'sdf3'}, 'innerQuorumSets': []},
        {'threshold': 3, 'validators': {'lobstr1', 'lobstr2', 'lobstr3', 'lobstr4', 'lobstr5'}, 'innerQuorumSets': []},
        {'threshold': 2, 'validators': {'keybase0', 'keybase1', 'keybase2'}, 'innerQuorumSets': []}
    ]
}


def get_nodes(qs_definition):
    nodes = set(qs_definition['validators'])
    for inner_qs_definition in qs_definition['innerQuorumSets']:
        nodes = nodes.union(get_nodes(inner_qs_definition))
    return nodes


nodes = get_nodes(base_quorum_slice_definition)

count = 0
for quorum_candidate in stellarobservatory.utils.sets.powerset(nodes):
    if len(quorum_candidate) > 0 and all([contains_slice(quorum_candidate, node) for node in quorum_candidate]):
        count += 1
print(count)


# counter = 0
# for quorum_candidate in stellarobservatory.quorums.enumerate_quorums(nodes):
#     if len(quorum_candidate) > 0 and all([contains_slice(quorum_candidate, node) for node in quorum_candidate]):
#         counter += 1
# print(counter)

# print(quorum_slice_definition_by_node)



# x = range(-10, 11)
# y = [x*x for x in x]
#
# plt.plot(x, y)
# plt.show()
