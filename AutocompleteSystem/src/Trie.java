import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.TreeMap;

public class Trie {
    private static class TrieNode extends TreeMap<Character, TrieNode> {
        public boolean isWord;
    }

    private TrieNode root;

    public Trie(Iterable<String> content) {
        this();
        content.forEach(this::insert);
    }

    public Trie() {
        root = new TrieNode();
    }

    public void insert(String word) {
        TrieNode current = root;
        for (int i = 0; i < word.length(); i++) {
            current = current.computeIfAbsent(word.charAt(i),
                              k -> new TrieNode());
        }
        current.isWord = true;
    }

    public List<String> search(String word) {
        List<String> results = new ArrayList<>();

        TrieNode node = findNode(word, root, 0);
        if (node == null) {
            return results;
        }

        findWords(node, new StringBuilder(word), results);
        return results;
    }

    private TrieNode findNode(String word, TrieNode current, int index) {
        if (index == word.length()) {
            return current;
        }

        Character ch = word.charAt(index);
        if (!current.containsKey(ch)) {
            return null;
        }

        return findNode(word, current.get(ch), ++index);
    }

    private void findWords(TrieNode current, StringBuilder sb, List<String> results) {
        current.forEach((Character ch, TrieNode child) -> {
            StringBuilder word = new StringBuilder(sb).append(ch);
            if (child.isWord) {
                results.add(word.toString());
            }
            findWords(child, word, results);
        });
    }
    
    public static void main(String args[]) {
        Trie trie = new Trie(Arrays.asList(new String[] { "dog", "dee", "deer", "deal" }));

        trie.search("de").forEach(System.out::println);
        System.out.println();

        trie.search("do").forEach(System.out::println);
        System.out.println();
    }
}
