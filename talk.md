# Hur angriper man ett problem?
Problem aaaahh på kattis:
https://open.kattis.com/problems/aaah

* kolla på input/output
* läs problemet nedifrån och upp om in/out är litet.
* Kom ihåg att alla problem med små input/output inte är lätta, men att det ger en bra fingervisning.


# Innan du börjar skriva din lösning
kolla på input och fundera på om din lösning är snabb nog:

* n > [300000,10^9] => O(n)
* n = [10000,300000] => O(nlogn)
* n = [1000,10000] => O(n^2)
* n = [100,1000] => O(n^3)
* n < 30 => O(2^n)
* n < 15 => O(4^n)

i c/c++ har man ca 10^9 operationer (arraylookups/addition/multiplikation/jämförelser per sekund på kattis)
i java har man ca 5*10^8 arraylookups, men samma mängd av resten.

#Kvadratiska naivt, worst case, men går att göra bättre:

* konkatenering av n strängar (utskrift) => linjärt med en stringbuilder (dynamisk char array)

* sortering med bubblesort => använd mergesort Arrays.sort(Object []) i java

* sortering med quicksort (Arrays.sort(int [])) => mergesort: Arrays.sort(Integer []) i java.
	 * quicksort kan bli kvadratisk för obskyra inputs vilket ibland finns.

#Vilket spårk bör man använda?
Scala är inte supported på kattis :(((((

Det språk du är mest bekväm i, som finns på kattis, dvs inte scala.

Supported språk är:

- Java
- C
- C++
- C#
- Python2&3
- Go
- Haskell
- (JS,Obj-C,PHP,Prolog,Ruby)

Python:

+ Extremt bra för små problem (krävs lite boilerplate-kod jämfört med andra spårk, mycket gratis med list och mapoperationer).

- Pythons objekt är långsama jämfört med objekt i java/structs i c. Om tidsgränsen är satt tight för en grafalgoritm bör man undvika python.

- Vad jag vet finns det inte någon bra balancerande träd-datastruktur i pythons standardbibliotek, dvs varken heap eller redblack-tree. Att implementera dessa själv gör man inte gärna under en tävling, kräver problemet en sådan datastruktur => byt språk.

Java:

+ Standardbiblioteken är bra, och det finns en färdig stringbuilder som fungerar utmärkt för stora outputs.
+ NCPC-arrangörerna garanterar att finns javakod som går igenom testerna.

- Scanner är seg. om inputen är > 10^5: Använd Kattio (en klass som ligger på open.kattis.com för snabbare inläsning i java) eller BufferedReader direkt.
- Access i en array är långsammare än i c/c++. Om tidsgränsen är tight satt, använd en endimensionell array istället för en flerdimensionell.

https://open.kattis.com/download/Kattio.java?1a0093

C++:

+ NCPC-arrangörerna garanterar att det finns c++kod som går igenom testerna.
+ Standardspråket för tävlingsprogrammering. 

- Få av oss kan det ordentligt (inklusive jag).

#Att ta med sig:

* Välj ett språk och byt enbart om ni bestämt er för att koda grafalgoritmer i java om ni har python som standardspråk. 

* Eller okey man kan byta språk. Men om man vill implementera samma algoritm i ett annat språk skall det finnas en mycket god anledning. En O(n^2) algoritm på input av n = 10^5 kommer aldrig att fungera oavsett språk.

* Om det är första gången man är med i en tävling tror jag det mest är trassel att försöka lära sig/använda ovana språk. Oftast finns det fler problem som man kan försöka lösa istället, vilket jag rekomenderar.

#Dagens upplägg:

* problem A kommer vara enkelt, börja att lösa det för att vänja er vid kattis.

* Resten av problemen kommer inte att ligga i svårighetsordning. Det gäller att leta reda på de enkla problemen i början.
