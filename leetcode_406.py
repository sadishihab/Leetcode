class Solution:
    def reconstructQueue(self, people):
        # Step 1: Sort
        people.sort(key=lambda x: (-x[0], x[1]))

        # Step 2: Insert
        res = []
        for person in people:
            res.insert(person[1], person)

        return res
