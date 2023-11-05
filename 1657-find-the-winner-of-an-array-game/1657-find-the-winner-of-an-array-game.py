class Solution(object):
    def getWinner(self, arr, k):
        current_winner = arr[0]
        consecutive_wins = 0
        
        for i in range(1, len(arr)):
            if arr[i] > current_winner:
                current_winner = arr[i]
                consecutive_wins = 1
            else:
                consecutive_wins += 1

            if consecutive_wins == k:
                return current_winner

        return current_winner
