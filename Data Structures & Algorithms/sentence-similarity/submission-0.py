class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        
        if len(sentence1) != len(sentence2):
            return False
        
        similarWord = defaultdict(set)

        for word1, word2 in similarPairs:
            similarWord[word1].add(word2)
            similarWord[word2].add(word1)
                
        for i in range(len(sentence2)):
            if sentence1[i] == sentence2[i] or sentence1[i] in similarWord[sentence2[i]]:
                continue
            return False

        return True