def lcs(str1, str2, m, n):
    # Create a DP table to store lengths of LCS for substrings of str1 and str2
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]

def min_insert_delete(str1, str2):
    m = len(str1)
    n = len(str2)
    
    # Find the length of LCS
    lcs_length = lcs(str1, str2, m, n)
    
    # Calculate minimum deletions and insertions
    deletions = m - lcs_length
    insertions = n - lcs_length
    
    return deletions, insertions

# Taking input from the user
str1 = input("Enter the first Word : ")
str2 = input("Enter the second Word: ")

# Get the minimum deletions and insertions
deletions, insertions = min_insert_delete(str1, str2)

# Display the results
print(f"Minimum Deletion = {deletions}")
print(f"Minimum Insertion = {insertions}")
