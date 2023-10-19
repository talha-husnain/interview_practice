def count_vowels_consonants(s: str) -> tuple:
    vowels_count = 0
    consonants_count = 0
    vowels = "aeiouAEIOU"
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            else:
                consonants_count += 1
    return vowels_count, consonants_count




    
def count_vowels_consonants(s: str) -> tuple:
    vowels = [char for char in s if char.lower() in 'aeiou' and char.isalpha()]
    consonants = [char for char in s if char.lower(
    ) not in 'aeiou' and char.isalpha()]
    return len(vowels), len(consonants)
