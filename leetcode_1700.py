class Solution(object):
    def countStudents(self, students, sandwiches):
        count0 = students.count(0)  # Students who want circular sandwiches
        count1 = students.count(1)  # Students who want square sandwiches

        for sandwitch in sandwiches:
            if sandwitch == 0:
                if count0 == 0:     # No student wants circular anymore
                    break
                count0 -= 1         # One student takes a circular sandwich
            else:
                if count1 == 0:     # No student wants square anymore
                    break
                count1 -= 1         # One student takes a square sandwich

        return count0 + count1


students = [1,1,1,0,0,1]
sandwiches = [1,0,0,0,1,1]
print(Solution().countStudents(students, sandwiches))
