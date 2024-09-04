class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        a = []
        for i in licensePlate:
            if i.isalpha():
                a.append(i.lower())
        ac = Counter(a)
        aca = []
        for i in ac.items():
            aca.append(list(i))
        x = "..............................................."
        for i in words:
            c = 0
            for j in aca:
                if i.count(j[0]) >= j[1]:
                    c += 1
            if c == len(aca):
                if len(x) > len(i):
                    x = i
        return x