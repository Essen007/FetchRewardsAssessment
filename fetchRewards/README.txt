$ docker build -t fr .
$ docker run -p 3000:3000 fr

1. Build docker and run it in terminals, with two lines of codes above.
2. Open up the browser and put the link http://localhost:3000/ in.
3. Type in the sentences in text1 and text2 window on the webpage, then hit "submit", should be able to see the similarity results.

The algorithm for this finding text similarity is determined by how much change do we need  to get from text1 to text2. Each change could be an adding word, deletion of a word, or changing a word in text1. Only count the words change, and the difference between two sentences would be the number of changes divided by the length of text2. Hence, the similarity percentage would be one subtract the difference. This metric is popularly used in speech recognition while I took the course, which I believe is useful in the current circumstances as well. 

Please let me know if you have any questions, thank you!
