class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        n = len(emails)
        for i in range(n):
            z = emails[i].index('@')
            y = emails[i].index('+') if '+' in emails[i][:z] else z
            emails[i] = emails[i][:y].replace('.', '')  + emails[i][emails[i].index('@'):]
        return len(set(emails))