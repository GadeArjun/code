import heapq

class Node:
    def __init__(self, freq, char):
        self.freq = freq
        self.char = char
        self.right = None
        self.left = None

    def __lt__(self,other):
        return self.freq < other.freq
    


def haffman_encoding(text):
    freq = {}
    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1
    
    heap = [Node(freq, char) for char , freq in freq.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        new_node = Node(left.freq + right.freq, None)
        new_node.left = left
        new_node.right = right
        heapq.heappush(heap, new_node)

    root = heap[0]
    codes = {}

    def generate_code(node, code):
        if node.char is not None:
            codes[node.char] = code
            return
        
        generate_code(node.left , code + "0")
        generate_code(node.right, code + "1")
    
    generate_code(root, "")
    return codes


    

text = input("enter text")

code = haffman_encoding(text)

for ch in code:
    print(ch, "--->", code[ch])