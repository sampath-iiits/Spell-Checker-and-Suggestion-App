# Spell-Checker-and-Suggestion-App
An Information_retrival project

Introduction:

The Spell Suggestion App is a Python application that helps users check the spelling of a word and provides suggestions for possible correct spellings. It utilizes n-grams and ranking algorithms to generate and refine spelling suggestions.

Prerequisites :

1. Python 3.x installed on your machine
2. Required Python packages: 'tkinter' , 'tabulate' , 'simpledialog' .

Installation :

1. Open a terminal or command prompt.

2. Navigate to the project directory .

3. Install the required Python packages:

   ' pip install tk tabulate '

Running the Application :

1. Execute the following command in the terminal or command prompt:

   ' python  code.py'

2. The SpellSuggestionApp window will appear.
3. Enter the word in the provided input field and specify the number of suggestions (less than 30).
4. Click the "Get Suggestions" button to view spelling suggestions.
5. If satisfied, you can give a rating. If not, you have the option to refine suggestions.
6. After refining or giving a rating, the app will prompt you for feedback and record your input.

Files :

1. code.py: The main Python script containing the SpellSuggestionApp class.
2. dataset.txt: A sample dataset of words used for spelling suggestions.

Additional Information :

The app records user ratings in the Review.txt file.
If the rating is less than or equal to 3, user remarks and feedback are recorded in the remarks.txt file.


Link for downloading the dataset :

"https://drive.google.com/file/d/178SguEiFbGunHZ32wrPjLn7hWXCY3gwg/view?usp=drive_link"


# Project Description

1. We have to run the code first .
2. Enter any word you want to search and Enter a number (<30) …. How many suggestions do you want.
3. Click on “Get Suggestions”.
4. If the word you entered is present in the dataset ; It will give as word is correctly spelt ; later you can give your rating .
5. If the word you entered is not present in the dataset ; It will give the suggestions how many you want.
6. It will ask that whether we are satisfied with the given suggestion of words.
7. If you are satisfied ; you can click ‘yes’ and you can give your rating (1 to 5) .
8. If you are not satisfied ; you can click ‘no’ and It will ask whether you want to refine the before suggestions.
9. If you want to refine the suggestions , click on ‘yes’ and you can refine the suggestions based on first letter and last letter of the entered word .
10. Then ; it will refine and it will modify the before suggestions.
11. If you are satisfied with the modified suggestions ; you can click on ‘yes’ and you can give your rating (1 to 5) by clicking ‘Give your Rating’.
12. If you are not satisfied with the modified suggestions ; you can click on ‘no’ and you can give your rating (1 to 5) and later you can give your remarks/feedback .
13. If you don’t want to refine the suggestions , click on ‘no’ and you can give your rating ( 1 to 5 ) .
14. Remember that every rating and remarks will be recorded in the files ‘Review.txt’ and ‘remarks.txt’ automatically.
