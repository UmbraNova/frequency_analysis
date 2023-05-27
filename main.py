text_file, analysis = open('text.txt', 'r'), open('analysis.txt', 'w')

def freq_counter(text):
    freq = dict()
    for char in text.read().lower():
        if char in freq:
            freq[char] += 1
        elif char.isalpha():
            freq[char] = 1
    text.close()
    return freq


letters_freq = freq_counter(text_file)
letters_count = sum(letters_freq.values())
for letter in letters_freq:
    analysis.write('{} {:.3f}\n'.format(letter, letters_freq[letter]/letters_count))

analysis.close()
