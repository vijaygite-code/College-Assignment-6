def suggest_completions(search_history, query):
    # Find completions by filtering the search history based on the query
    suggestions = [item for item in search_history if item.startswith(query)]
    
    return suggestions

# Example usage
search_history = [
    "apple",
    "banana",
    "carrot",
    "pear",
    "pineapple",
    "potato",
    "strawberry"
]

# Taking input from the user
query = input("Enter your partial search query: ")

# Get the suggestionsxdfjdrtdrj
suggestions = suggest_completions(search_history, query)

# Display the suggestions
if suggestions:
    print("Suggestions:")
    for suggestion in suggestions:
        print(suggestion)
else:
    print("No suggestions found.")
