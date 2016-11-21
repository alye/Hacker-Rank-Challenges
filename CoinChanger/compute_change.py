# Enter your code here. Read input from STDIN. Print output to STDOUT
class ComputeChange(object):
    def __init__(self, coins):
        self.combinations = {(0, 0): [[0]]}
        self.coins = coins
        self.coins.sort()

    def compute_ways(self, amount, coin_no="Default"):
        if coin_no == "Default":
            coin_no = len(self.coins)
        if amount == 0:
            return 1
        elif amount < 0:
            return 0
        elif coin_no <= 0:
            return 0
        elif (amount, coin_no) in self.combinations:
            return self.combinations[(amount, coin_no)]
        self.combinations[(amount, coin_no)] = self.compute_ways(amount, coin_no - 1) + self.compute_ways(
            amount - self.coins[coin_no - 1], coin_no)
        return self.combinations[(amount, coin_no)]


def main():
    amount, m = map(int, raw_input().split())
    coins = [denomination for denomination in map(int, raw_input().split())]
    coins.sort()
    change_computer = ComputeChange(coins)
    print change_computer.compute_ways(amount)


if __name__ == "__main__":
    main()
