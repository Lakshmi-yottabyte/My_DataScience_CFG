When the code calls the API, it gets back JSON that shows:

"question": ".....",

"correct\_answer": "...",

"incorrect\_answers":\["List"],

"difficulty": "...",

"category": "..."



the code then needs to:

1\) pull these pieces out of JSON (decode\_question() function in code)

2\) Shuffle the 4 answers into random order (shuffle\_answers() function in code)

3\) Show them to the player as ABCD



https://opentdb.com/api\_category.php will show the id of every category



**At the very top of the code**

No API key needed as Open Trivia DB is completely free and open

html and random and other modules are built into python

when running in terminal, install requests with pip install requests



**The response\_code chack in fetch\_questions()**

API returns response\_code 0 if successful

Other codes mean that no results were found



**The html.unescape() calls in decode\_question()**

The API returns text with HTML entities e.g. \&amp; means \& and \&#039; means '

html.unescape() converts these back into normal readable characters



**for loop with zip() in run\_quiz()**

zip() pairs each label (A,B,C,D) with its answer so they display together

for label, ans in zip(labels, answers):



**enumerate() in run\_quiz()**

enumerate() gives us both the index (question number) and the question itself

starting at 1 so questions display as Q1, Q2... instead of Q0, Q1...

for i, raw in enumerate(questions, 1):



**save\_results function()**

Writes results to a .txt file named after the player

"w" mode creates the file if it doesn't exist, or overwrites it if it does



**At the very bottom of the code**

This ensures main() only runs when the file is executed directly

If this file were imported into another script, main() would NOT run automatically

