class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniqueEmails = set()

        for email in emails:
            emailAddress, domain = email.split('@')
            actualEmailAddress = ''

            for char in emailAddress:
                if char == '+':
                    break
                else:
                    if char != '.':
                        actualEmailAddress += char
            
            uniqueEmails.add(f'{actualEmailAddress}@{domain}')
        
        return len(uniqueEmails)