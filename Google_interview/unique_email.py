#My solution to google unique email addresses problem

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        valid_emails = []
        for email in emails:
            # Extract the sender and domain parts from the email address
            sender_part, domain_part = email.split('@')
            # Ignore all parts after "+"
            sender_part = sender_part.split('+')[0]
            sender_part = sender_part.replace('.', '')
            new_email = f"{sender_part}@{domain_part}"
            if new_email not in valid_emails:
                valid_emails.append(new_email)
        return len(valid_emails)
            
            
        