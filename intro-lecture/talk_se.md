# Hur angriper man ett problem?
Problem aaaahh på kattis:
https://open.kattis.com/problems/aaah

* Kolla på input/output
* Läs problemet nedifrån och upp om in/out är litet.
* Alla problem med små input/output inte är lätta.










# Innan du börjar skriva din lösning
kolla på input och fundera på om din lösning är snabb nog:

* n > [300000,10^9] => O(n)
* n = [30000,300000] => O(nlogn)
* n = [1000,30000] => O(n^2)
* n = [100,1000] => O(n^3)
* n < 30 => O(2^n)
* n < 15 => O(4^n)







i c/c++ har man ca 10^9 operationer (arraylookups/addition/multiplikation/jämförelser per sekund på kattis)
i java har man ca 5*10^8 arraylookups, men samma mängd av resten.







###Saker som naivt tar kvadratisk tid(worst case) 
###men går att göra bättre:

* konkatenering av n strängar (utskrift) => linjärt med en stringbuilder (dynamisk char array)

* sortering med bubblesort => använd mergesort Arrays.sort(Object []) i java

* sortering med quicksort (Arrays.sort(int [])) => mergesort: Arrays.sort(Integer []) i java.
	 * quicksort kan bli kvadratisk för obskyra inputs vilket ibland finns.







#Vilket språk bör man använda?















Scala är inte supported på kattis :(((((

Det språk du är mest bekväm i, som finns på kattis, dvs inte scala.













###Supported språk är:

- Java
- C
- C++
- C#
- Python2&3
- Go
- Haskell
- (JS,Obj-C,PHP,Prolog,Ruby)




# Python

















+ Extremt bra för små problem (krävs lite boilerplate-kod jämfört med andra spårk, mycket gratis med list och mapoperationer).

- Pythons objekt är långsama jämfört med objekt i java/structs i c. Om tidsgränsen är satt tight för en grafalgoritm bör man undvika python.

- Vad jag vet finns det inte någon bra balancerande träd-datastruktur i pythons standardbibliotek, dvs varken heap eller redblack-tree. Att implementera dessa själv gör man inte gärna under en tävling, kräver problemet en sådan datastruktur => byt språk. (eller problem)






# Java

















+ Standardbiblioteken är bra, och det finns en färdig stringbuilder som fungerar utmärkt för stora outputs.

+ NCPC-arrangörerna garanterar att finns javakod som går igenom testerna.

- Scanner är seg. om inputen är > 10^5: Använd Kattio (en klass som ligger på open.kattis.com för snabbare inläsning i java) eller BufferedReader direkt.

- Access i en array är långsammare än i c/c++. Om tidsgränsen är tight satt, använd en endimensionell array istället för en flerdimensionell.

+ https://open.kattis.com/download/Kattio.java?1a0093







#C++

















+ NCPC-arrangörerna garanterar att det finns c++kod som går igenom testerna.

+ Standardspråket för tävlingsprogrammering. 

- Få av oss kan det ordentligt (inklusive mig).




# Eclipse - Just dont.

















+ Autocompletion. (men här böjrar man från scratch, man vill ha koll på dokumentationen innan man börjar skriva sin lösning)

- Appendar package till filer vilket måste tas bort.

- Consolens output är liten

- Jag började programmera i Eclipse när jag började här - it was a trap.

- Nu kodar ni under tidspress, eclipse hjälper er inte med den.

* Alternativ: VIM, Atom, Emacs, (Sublime)





# Dagens upplägg:















* Tävling 18:15 - 21:15, sedan lösningsgenomgång

* 9 problem

* problem A kommer vara enkelt, börja att lösa det för att vänja er vid kattis.

* Resten av problemen kommer inte att ligga i svårighetsordning. Det gäller att leta reda på de enkla problemen i början.



### Regler

* Lag om max 3, använd bara ett kattis account.

* Man får ett poäng per löst problem.

* man sorterar först på antal lösta problem,

* sedan på sum(t) + w*20,

* där t är tiden det tog att lösa ett problem,

* och w totala antalet felaktiga försök på lösta problem.



# Kom ihåg
















* Välj ett språk och byt inte.

* Skojja bara, man får byta språk, men oftast kommer det inte hjälpa. Oftast bättre att byta problem.

* Hitta dem lätta problemen

* Använd snabb scanner om ni köra java.
