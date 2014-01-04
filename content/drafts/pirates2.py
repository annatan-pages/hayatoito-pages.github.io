#!/usr/bin/env python3

import sys


def pretty(proposal):
    return ''.join('x' if coin == -1 else 'G' if coin > 9 else str(coin)
                   for coin in proposal)


def main(num_pirates, coin):

    def solve(proposal):
        necessary_vote = len(proposal) // 2
        ranks = sorted((n, i) for i, n in enumerate(proposal))
        necessary_coin = sum(n + 1 for n, _ in ranks[:necessary_vote])
        if coin >= necessary_coin:
            return [(n + 1 if ranks.index((n, i)) < necessary_vote else 0)
                    for i, n in enumerate(proposal)] + [coin - necessary_coin]
        return proposal + [-1]

    optimal_proposal = []

    for member in range(num_pirates):
        optimal_proposal = solve(optimal_proposal)
        print('{:4}: {}'.format(member + 1, pretty(optimal_proposal)))


if __name__ == '__main__':
    main(int(sys.argv[1]), int(sys.argv[2]))
