def stable_marriage(men_preferences, women_preferences):
    n = len(men_preferences)  # Number of men/women
    free_men = list(range(n))  # List of free men
    women_partner = [-1] * n  # Women partner list initialized to -1 (no partner)
    men_next_proposal = [0] * n  # Track next woman to propose for each man

    # Preference rankings for quick lookup
    women_rankings = [
        {man: rank for rank, man in enumerate(women_preferences[i])}
        for i in range(n)
    ]

    # Continue until there are free men
    while free_men:
        man = free_men[0]  # Take the first free man
        woman = men_preferences[man][men_next_proposal[man]]  # The woman to propose to next
        men_next_proposal[man] += 1  # Move to the next woman for the next proposal
        
        if women_partner[woman] == -1:
            # If the woman is free, engage her with the man
            women_partner[woman] = man
            free_men.pop(0)
        else:
            # If the woman is not free, decide if she prefers this man over her current partner
            current_partner = women_partner[woman]
            if women_rankings[woman][man] < women_rankings[woman][current_partner]:
                # She prefers the new man
                women_partner[woman] = man
                free_men[0] = current_partner  # The current partner becomes free
            # If she prefers her current partner, the man remains free and in the list

    # Create a list of pairs (man, woman)
    matches = [(women_partner[w], w) for w in range(n)]
    return matches

# Example usage
men_preferences = [
    [0, 1, 2],
    [1, 0, 2],
    [1, 2, 0]
]

women_preferences = [
    [2, 1, 0],
    [0, 1, 2],
    [2, 0, 1]
]

matches = stable_marriage(men_preferences, women_preferences)
print("Stable matches:", matches)
