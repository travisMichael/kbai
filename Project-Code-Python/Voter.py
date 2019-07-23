
class Voter:
    def __init__(self):
        self.voting_map = {'1': 0, '2': 0, '3': 0, '4': 0, '5': 0, '6': 0, '7': 0, '8': 0}

    def vote(self):

        answer = -1
        highest_tally_count = 0
        for i in range(1, 9):
            tally_count = self.voting_map.get(str(i))
            if tally_count > highest_tally_count:
                highest_tally_count = tally_count
                answer = i
                continue
            if tally_count == highest_tally_count:
                answer = -1

        return answer

    def tally(self, answer):
        self.voting_map[str(answer)] = self.voting_map.get(str(answer)) + 1
