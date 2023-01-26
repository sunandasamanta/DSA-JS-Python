A Trie, also known as a prefix tree, is a tree-like data structure that is used to store a collection of strings. Each node in a Trie represents a single character in a string, and each edge represents a progression from one character to the next. The root of the Trie represents the empty string, and the leaves of the Trie represent the strings that have been inserted into the Trie.

For example, consider a Trie that stores the words "bat", "batman", "batwoman", "batmobile", "batcave". The Trie would look like this:

             *
            / \
            b   c
            / \  
            a   m
            / \
            o   o
            /     \
            b       b
            |       |
            i       i
            |       |
            l       e
            |       |
            e       |
            |       |
            m       |
            |       |
            a       |
            |       |
            n       |
                    |

As you can see the first level of the Trie is the empty string, the second level has the character 'b', the next level has the character 'a', the next level has the character 't' and so on. Each word is represented by a path from the root to a leaf node.

Tries are commonly used in various applications such as dictionary, auto-completion and IP routing to name a few. They are efficient at searching for strings in a large collection of strings because each character in the search string is used to navigate the Trie and the search time is proportional to the length of the search string. They are also efficient at inserting new strings, as the time to insert a new string is proportional to the length of the string.