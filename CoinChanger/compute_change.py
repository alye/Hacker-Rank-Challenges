# Enter your code here. Read input from STDIN. Print output to STDOUT
class ComputeChange(object):
    def __init__(self, coins):
        self.combinations = {0: [[0]]}
        self.coins = coins
        self.coins.sort()

    def compute_ways(self, amount):
        if amount <= 0:
            return len(self.combinations[0])
        if amount not in self.combinations:
            self.combinations[amount] = []
        for coin in self.coins:
            next_amount = amount - coin
            if next_amount < 0:
                break
            if next_amount not in self.combinations:
                self.compute_ways(next_amount)
            new_combinations = [sorted(x[:] + [coin]) for x in self.combinations[next_amount]]
            for new_combination in new_combinations:
                if new_combination not in self.combinations[amount]:
                    self.combinations[amount].append(new_combination)
        return len(self.combinations[amount])


def main():
    amount, m = map(int, raw_input().split())
    coins = [denomination for denomination in map(int, raw_input().split())]
    coins.sort()
    change_computer = ComputeChange(coins)
    print change_computer.compute_ways(amount)


if __name__ == "__main__":
    import sys
    sys.stdin = open('input.txt', 'r')
    main()
