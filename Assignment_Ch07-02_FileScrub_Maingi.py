
# Samuel Maingi
# Assignment 07-02
# 04/05/2023


def search_data():
    field = input("Enter the field to search: (f) for first name, (l) for last name, and (e) for email: ")
    query = input("Enter the search query: ").lower()
    results = []
    with open("Misc/data.txt", 'r') as file:
        for line in file:
            data = line.strip().split('\t')
            if field == 'f' and data[0].lower() == query:
                results.append(data)
            elif field == 'l' and data[1].lower() == query:
                results.append(data)
            elif field == 'e' and data[2].lower() == query:
                results.append(data)
    print("Results:")
    print("First Name\tLast Name\tEmail")
    for result in results:
        print('\t\t'.join(result))

if __name__ == "__main__":
    search_data()

