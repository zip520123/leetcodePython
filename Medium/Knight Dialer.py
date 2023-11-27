# Knight Dialer
# O(n), O(1)
def knightDialer(self, n: int) -> int:
    if n == 1: return 10
    n1 = n2 = n3 = n4 = n6 = n7 = n8 = n9 = n0 = 1
    mod = 1E9+7
    for _ in range(1,n):
        new1 = (n6+n8) % mod
        new2 = (n7+n9) % mod
        new3 = (n4+n8) % mod
        new4 = (n3+n9+n0) % mod
        new6 = (n1+n7+n0) % mod
        new7 = (n2+n6) % mod
        new8 = (n1+n3) % mod
        new9 = (n2+n4) % mod
        new0 = (n4+n6) % mod
        n1,n2,n3,n4,n6,n7,n8,n9,n0 = new1,new2,new3,new4,new6,new7,new8,new9,new0
    return int(sum([n1,n2,n3,n4,n6,n7,n8,n9,n0]) % mod)