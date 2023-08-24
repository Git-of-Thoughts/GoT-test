from binary_word import BinaryWord
from binary_word_analyzer import BinaryWordAnalyzer

def main():
    words = [BinaryWord(word) for word in input().split()]
    analyzer = BinaryWordAnalyzer(words)

    print("Binary word with most zeros:", analyzer.find_most_zeros().word)
    print("Binary word with most ones:", analyzer.find_most_ones().word)

if __name__ == "__main__":
    main()
