class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class BrowserHistory(object):
    def __init__(self, homepage):
        self.curr = ListNode(homepage)      # Creating home page

    def visit(self, url):
        self.curr.next = None               # Clear forward history
        new_node = ListNode(url)            # Create new node and link it
        new_node.prev = self.curr
        self.curr.next = new_node
        self.curr = new_node

    def back(self, steps):
            while steps > 0 and self.curr.prev:
                self.curr = self.curr.prev
                steps -= 1
            return self.curr.val

    def forward(self, steps):
        while steps > 0 and self.curr.next:
            self.curr = self.curr.next
            steps -= 1
        return self.curr.val


browserHistory = BrowserHistory("leetcode.com")
browserHistory.visit("google.com")
browserHistory.visit("facebook.com")
browserHistory.visit("youtube.com")
print(browserHistory.back(1))           # facebook.com
print(browserHistory.back(1))           # google.com
print(browserHistory.forward(1))        # facebook.com
browserHistory.visit("linkedin.com")
print(browserHistory.forward(2))        # linkedin.com
print(browserHistory.back(2))           # google.com
print(browserHistory.back(7))           # leetcode.com