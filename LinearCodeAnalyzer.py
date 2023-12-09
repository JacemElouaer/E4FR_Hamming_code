import numpy as np

def generate_systematic_matrix():
    g = np.array([
        [1, 0, 0, 0, 1, 1, 0],
        [0, 1, 0, 0, 0, 1, 1],
        [0, 0, 1, 0, 1, 1, 1],
        [0, 0, 0, 1, 1, 0, 1]
    ])
    return g

def generate_code_words(info_word, generator_matrix):
    return info_word.dot(generator_matrix) % 2

def calculate_syndrome(received_word, generator_matrix):
    return received_word.dot(generator_matrix.T) % 2

def minimum_distance(generator_matrix):
    code_words = [np.array([0, 0, 0, 0, 0, 0, 0])]
    for i in range(1, 2 ** generator_matrix.shape[0]):
        info_word = np.array(list(format(i, '0' + str(generator_matrix.shape[0]) + 'b')), dtype=int)
        code_word = generate_code_words(info_word, generator_matrix)
        code_words.append(code_word)

    min_distance = float('inf')
    for i in range(len(code_words)):
        for j in range(i + 1, len(code_words)):
            distance = np.sum((code_words[i] + code_words[j]) % 2)
            min_distance = min(min_distance, distance)

    return min_distance

def main():
    generator_matrix = generate_systematic_matrix()

    # Détermination des mots de code
    code_words = []
    for i in range(2 ** generator_matrix.shape[0]):
        info_word = np.array(list(format(i, '0' + str(generator_matrix.shape[0]) + 'b')), dtype=int)
        code_word = generate_code_words(info_word, generator_matrix)
        code_words.append((info_word, code_word))

    print("Mots d'information et mots de code correspondants :")
    for info_word, code_word in code_words:
        print(f"Info Word: {info_word}, Code Word: {code_word}")

    # Calcul des syndromes
    received_word = np.array([1, 0, 1, 1, 0, 1, 0])  # Exemple d'un mot reçu
    syndrome = calculate_syndrome(received_word, generator_matrix)
    print("\nSyndrome du mot reçu:", syndrome)

    # Détermination de la distance minimale
    min_dist = minimum_distance(generator_matrix)
    print("\nDistance minimale:", min_dist)

if __name__ == "__main__":
    main()

