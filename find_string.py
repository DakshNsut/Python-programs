print("Note: The query string would be found after capitalizing each word in the sentences and after capitalizing only the first word in query string")
num_sentences = int(input("Enter the number of sentences you want to search the query string in:- "))
list_sentences = []
list_matched = []

for i in range(num_sentences):
    sentence = input(f"Enter the {i+1} sentence you want to search the query string in:-")
    list_sentence_words = sentence.split(" ")
    Sentence = ""
    for k in range(len(list_sentence_words)):
        list_sentence_words[k] = list_sentence_words[k].capitalize()
        Sentence = Sentence + " " + list_sentence_words[k]
        continue
    list_sentences.append(Sentence)
    continue


query_string = input("Enter the query string you want to search.").capitalize()

# print(list_sentences)
# print(query_string)

for element in list_sentences:
    if query_string in element:
        list_matched.append(element)
        continue
    else:
        continue

dict_count={}
for i in range(len(list_matched)):
    dict_count[list_matched[i]] = list_matched[i].count(query_string)
    continue

dict_count = dict(sorted(dict_count.items(),key=lambda x:x[1]))
print(f"No. of {query_string} in->      Sentence")
for j in range(len(dict_count)):
    print(f"        {list(dict_count.values())[j]}              {list(dict_count.keys())[j]}")
    continue