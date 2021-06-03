from demos import generate_name, generate_emails, bisection_sort, analyzer


#Create List of Emails
domains = ['@yahoo.com','@gmail.com', '@aol.com']
unsorted_emails = generate_emails(10, domains, 1000000)

#Email to find

email = 'charlesl15@gmail.com'
unsorted_emails.append(email)

#Sort List of Emails
sorted_emails = sorted(unsorted_emails)

#Run Bisection

index, found = bisection_sort(email, sorted_emails)
print(found)

#Run Analysis of functions

analyzer(bisection_sort, email, sorted_emails)

analyzer(generate_emails, 10, domains, 1000000)
