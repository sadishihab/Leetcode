class UnionFind:
    def __init__(self, n):
        self.par = {}
        self.rank = {}

        for i in range(n):
            self.par[i] = i
            self.rank[i] = 0

    # Find with path compression (path halving)
    def find(self, n):
        p = self.par[n]
        while p != self.par[p]:
            self.par[p] = self.par[self.par[p]]
            p = self.par[p]
        return p

    # Union by rank
    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False

        if self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
        elif self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
        else:
            self.par[p1] = p2
            self.rank[p2] += 1

        return True


class Solution:
    def accountsMerge(self, accounts):
        n = len(accounts)
        uf = UnionFind(n)

        # Map email -> account index
        email_to_account = {}

        # Step 1: Union accounts that share emails
        for i, account in enumerate(accounts):
            for email in account[1:]:
                if email in email_to_account:
                    uf.union(i, email_to_account[email])
                else:
                    email_to_account[email] = i

        # Step 2: Group emails by root parent
        root_to_emails = {}

        for email, idx in email_to_account.items():
            root = uf.find(idx)
            if root not in root_to_emails:
                root_to_emails[root] = []
            root_to_emails[root].append(email)

        # Step 3: Build result
        result = []

        for root, emails in root_to_emails.items():
            name = accounts[root][0]
            result.append([name] + sorted(emails))

        return result
