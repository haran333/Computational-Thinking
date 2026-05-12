def load_dictionary(filename):
    word_dict = {}
    with open(filename, "r", encoding='utf-8')as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(maxsplit=1)
            if len(parts) <2:
                continue
            rest =parts[1]

            tokens =rest.split(maxsplit=1)
            if len(tokens)<2:
                continue
            word =tokens[0].strip()
            meaning =tokens[1].strip().strip("")
            word_dict[word] = meaning
    return word_dict
    
def main():
    dictionary = load_dictionary('vocabulary.txt')

    print("영어단어사전 \n")
    print(f"총 {len(dictionary)}개의 단어가 등록되어 있습니다")
    print("\n 종료하려면 quit을 입력하세요")

    while True:
        word = input().strip()

        if word == 'quit':
          return False
        if word in dictionary:
            print(dictionary[word])
        else:
            print("사전에 없는 단어입니다")
            
main()