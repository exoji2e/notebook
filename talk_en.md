#What to do when the competition starts (team competition)
1. Identify easy problems (atleast if it's ACM-rules)
  * Look at the size of the input and text. Size correlates with difficulty but is not always true (https://open.kattis.com/problems/nnnnn)
  * See if you can find any problem that can be sloved by some method you have used before
2. When someone finds an easy problem they should start to code.
3. If you can't access the computer currently, write pseudocode and then find another problem.

#What to do when I find a problem that I think is easy
Think about the complexity of your algorithm compared to the input
The following table is a small guideline to what time complexity is needed for specific inputsizes.
Don't take this literally. For n = 50000 you might be able to get away with a O(n^2) algorithm.
For n = 100000 I've never seen an O(n^2) algorithm work on Kattis. 

n > | n <= | O(f(n))
--- | --- | ---
10^6 | 10^9 | O(n)
30000 | 10^6 | O(nlogn)
1000 | 30000 | O(n^2)
100 | 1000 | O(n^3)
15 | 30 | O(2^n)
12 | 15 | O(4^n)
0 | 12 | O(n!)

#What to do when my code is _correct_ but isn't AC (Accepted)
"It is correct because I get the right result on the sample cases."
Probably your code is incorrect. Common nonobvoius errors _for beginners_:

* WA - Overflow switch from int to long (or long long) or BigInteger.
* WA - Off by 1 for some inputs. Find where by constructing your own test cases
* TLE - Error in time complexity analysis. Remove in an array is O(n) for example.
* TLE - The language you use cant do this quickly enough - change language. (If you use C/C++/Java this is almost never the case.)
* TLE in Java - Is the input large? Use Kattio instead of the java.util.Scanner. 
* RTE - Indexing outside an array <=> ArrayIndexOutOfBounds/segfault. Correlates to off by 1.

Kattio: https://open.kattis.com/download/Kattio.java?1a0093

#What language should I use?

On Kattis the following languages are currently(2016) supported:
- Java
- C
- C++
- C#
- Python2&3
- Go
- Haskell
- (JS,Obj-C,PHP,Prolog,Ruby)

Use the language you are most used to of these. Knowing the libraries by heart gives you alot of time advantage.

TODO: pros&cons of different languages.

#What editor should I use?

If it's a real competition: the editor you are most comfortabel with.
If you are training, avoid IDE's like Eclipse, Intellij, Visual studio.

Pros:
* Auto completion.
why you don't need auto completion:
You code 100 lines from scratch. No need to search in your code, and you should be familiar enough with the libraries you use.

Cons:
* Inserting 'package' that doesn't complie on the server if you use Java.
* The output and input in the console is to small and can't handle EOF-character correctly.
* You code time preassured, having to navigate with the mouse doesn't help with that. Also Error messages are very annoying.
* When I started to code I started in Eclipse and it was a trap. Since I started using normal texteditors/vim I've felt free.

Reccomendations and Alternatives:
* Vim/nvim master race - actually I've just started using vim, but I really like it you feel really efficient.
* Emacs - If you dont care about your pinky ;)
* Atom/sublime - I have used these a lot. Sublime is still my goto editor when I need to do something really fast (dec2016). These are the editors I'd recommend using for someone new or someone who has only used eclipse be4. Just basig TextEditing with syntaxhighlighting and snippets. Out of the box they do no black magic.
