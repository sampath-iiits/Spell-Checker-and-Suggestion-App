import tkinter as tk
from tkinter import messagebox, simpledialog
from tabulate import tabulate

class SpellSuggestionApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Spelling Suggestion App")

        self.setup_ui()

    def setup_ui(self):
        self.input_word_label = tk.Label(self.window, text="Enter the word:")
        self.input_word_label.grid(row=0, column=0, padx=10, pady=10)

        self.input_word = tk.Entry(self.window)
        self.input_word.grid(row=0, column=1, padx=10, pady=10)

        self.num_suggestions_label = tk.Label(self.window, text="Number of suggestions (<30):")
        self.num_suggestions_label.grid(row=1, column=0, padx=10, pady=10)

        self.num_suggestions = tk.Entry(self.window)
        self.num_suggestions.grid(row=1, column=1, padx=10, pady=10)

        self.get_suggestions_button = tk.Button(self.window, text="Get Suggestions", command=self.get_suggestions)
        self.get_suggestions_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.suggestions_text = tk.Text(self.window, height=33, width=80)
        self.suggestions_text.grid(row=3, column=0, columnspan=2, pady=10)

        self.ok_button = tk.Button(self.window, text="Give your Rating ", command=self.record_rating, state=tk.DISABLED)
        self.ok_button.grid(row=4, column=0, columnspan=2, pady=10)

    def run(self):
        self.window.mainloop()

    def check_spelling(self, word, ary):
        for string in ary:
            if string == word:
                return True
        return False

    def generate_ngrams(self, n, word):
        n_grams = []
        i = 0
        size = len(word)
        while (i + n - 1) < size:
            n_grams.append(word[i:i + n])
            i += 1
        return n_grams

    def create_ngram_index(self, n, vocabulary):
        n_index = dict()
        for word in vocabulary:
            n_grams = self.generate_ngrams(n, word)
            for gram in n_grams:
                if n_index.get(gram) is None:
                    n_index[gram] = [word]
                else:
                    t_list = n_index[gram]
                    t_list.append(word)
                    n_index[gram] = t_list
        return n_index

    def generate_suggested_list(self, word, n_index, n):
        size = len(word)
        i = 0
        s_list = []
        while (i + n - 1) < size:
            bg = word[i:i + n]
            pos_list = n_index.get(bg)
            if pos_list is not None:
                pos_list = list(set(pos_list))
                s_list.append(pos_list)
            i += 1
        return s_list

    def length_coefficient(self, word1, word2):
        len1 = len(word1)
        len2 = len(word2)
        if len1 > len2:
            k = len2 / len1
            return k
        else:
            k = len1 / len2
            return k

    def ranking(self, word, s_list, m):
        ranks = dict()
        
        for lst in s_list:
            for string in lst:
                freq = ranks.get(string)
                if freq is None:
                    ranks[string] = 1
                else:
                    ranks[string] = freq + 1

        sort_ranks = sorted(ranks.items(), key=lambda x: x[1], reverse=True)
        sort_ranks = dict(sort_ranks[0:m])

        for key in sort_ranks.keys():
            freq = sort_ranks.get(key)
            length_score = self.length_coefficient(word, key)

            score = freq + length_score
            sort_ranks[key] = score

        sort_ranks = sorted(sort_ranks.items(), key=lambda x: x[1], reverse=True)

        return dict(sort_ranks)

    def refine1(self, word, ranks):
        sorted_ranks = {}
        for key in ranks.keys():
            freq = 0
            if word[0] == key[0]:
                freq = 1
            score = freq + ranks.get(key)
            ranks[key] = score
        sorted_ranks = dict(sorted(ranks.items(), key=lambda x: x[1], reverse=True))
        return sorted_ranks

    def refine2(self, word, ranks):
        len1 = len(word)
        for key in ranks.keys():
            len2 = len(key)
            freq = 0
            if word[len1 - 1] == key[len2 - 1]:
                freq = 1
            score = freq + ranks.get(key)
            ranks[key] = score
        sorted_ranks = dict(sorted(ranks.items(), key=lambda x: x[1], reverse=True))
        return sorted_ranks

    def list_word_fun(self, ranks):
        print("-----------------------------------------------------------------------------")
        print("Suggested words and their score are :")
        print("-----------------------------------------------------------------------------")

        table_data = []
        for idx, (key, value) in enumerate(ranks.items(), start=1):
            table_data.append([f"{idx}:{key}", f"{value:.5f}"])

        headers = ["Word", "Score"]
        print(tabulate(table_data, headers=headers, tablefmt="grid"))
        print("-----------------------------------------------------------------------------")
        val = messagebox.askyesno("Satisfaction", "Are you satisfied with the above list?")
        print("-----------------------------------------------------------------------------")

        if val.lower() == 'yes':
            self.ok_button["state"] = tk.NORMAL
        else:
            with open('your_file.txt', 'a', encoding='utf-8') as file:
                file.write(self.input_word.get() + '\n')
            print("--------------------------------------------------------------------------------------")

            print('We will provide the best words asap.....')
            print("--------------------------------------------------------------------------------------")

    def record_rating(self):
        user_input = simpledialog.askfloat("Rating", "Please give your rating (1 to 5):")
        
        messagebox.showinfo("Rating Recorded", f"Your rating ({user_input}) has been recorded. Thank you!")

        adjusted_input = max(1, min(round(user_input), 5))

        with open('Review.txt', 'a', encoding='utf-8') as file:
            file.write(f'{adjusted_input}\n')

        if adjusted_input <= 3:
            remarks = simpledialog.askstring("Remarks", "Any remarks or feedback:")
            with open('remarks.txt', 'a', encoding='utf-8') as remarks_file:
                remarks_file.write(f'{remarks}----{self.input_word.get()}\n')
                

        messagebox.showinfo("Thank You!!!!", "Thank you for using the Spelling Suggestion App.")

        
    def record_rating2(self):
        user_input = simpledialog.askfloat("Rating", "Please give your rating based on the above suggestions (1 to 5):")
        
        messagebox.showinfo("Rating Recorded", f"Your rating ({user_input}) has been recorded. Thank you!")

        adjusted_input = max(1, min(round(user_input), 5))

        with open('Review.txt', 'a', encoding='utf-8') as file:
            file.write(f'{adjusted_input}\n')

        if adjusted_input <= 3:
            remarks = simpledialog.askstring("Remarks", "Any remarks or feedback:")
            with open('remarks.txt', 'a', encoding='utf-8') as remarks_file:
                remarks_file.write(f'{remarks}----{self.input_word.get()}\n')

                
        messagebox.showinfo("Thank You!", "Your rating and remarks are recorded.\nWe will provide the best words asap.....")
        
        messagebox.showinfo("Thank You!!!!", "Thank you for using the Spelling Suggestion App.")

        
    def get_suggestions(self):
        input_word = self.input_word.get()
        num_suggestions = int(self.num_suggestions.get())

        key_list = []
        with open("./dataset.txt", encoding="utf-8") as f:
            for line in f:
                temp = line.strip("\n")
                key_list.append(temp)

        key_list = set(key_list)
        key_list = list(key_list)

        n = 3
        n_index = self.create_ngram_index(n, key_list)
        status = self.check_spelling(input_word, key_list)

        if status:
            messagebox.showinfo("Spelling Check", f"The word '{input_word}' is correctly spelled.")
            self.record_rating()
        else:
            s_list = self.generate_suggested_list(input_word, n_index, n)
            ranks = self.ranking(input_word, s_list, num_suggestions)

            suggestions_text = self.display_suggestions(ranks)
            self.suggestions_text.delete(1.0, tk.END)  
            self.suggestions_text.insert(tk.END, suggestions_text)
            val = messagebox.askyesno("Satisfaction", "Did you satisfied????")
        
            if val:
                self.ok_button["state"] = tk.NORMAL
            else:
                refine_option = messagebox.askquestion("Refine Suggestions", "Would you like to refine suggestions?")
                if refine_option == 'yes':
                    refine_type = simpledialog.askinteger("Refine Suggestions", "Enter '1' if confident with the first letter; Enter '2' if confident with the last letter", minvalue=1, maxvalue=2)
                    if refine_type == 1:
                        ranks = self.refine1(input_word, ranks)
                    elif refine_type == 2:
                        ranks = self.refine2(input_word, ranks)


                    suggestions_text = self.display_suggestions(ranks)
                    self.suggestions_text.delete(1.0, tk.END)  
                    self.suggestions_text.insert(tk.END, suggestions_text)


                    val_after_refine = messagebox.askyesno("Satisfaction", "Are you satisfied with the refined suggestions?")
                    if val_after_refine:
                        self.ok_button["state"] = tk.NORMAL
                    else:
                        self.record_rating2()
                else:
                    self.record_rating2()

    def display_suggestions(self, ranks):
        suggestions_text = "Suggested words and their score are:\n\n"
        for idx, (key, value) in enumerate(ranks.items(), start=1):
            suggestions_text += f"{idx}:{key} - {value:.5f}\n"
        return suggestions_text


if __name__ == "__main__":
    app = SpellSuggestionApp()
    app.run()
