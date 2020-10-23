def user_input():
    text = raw_input("Enter text to analyze\n$ ")
    return text


def letter_count(text):
    c = 0
    for i in range(0, len(text)):
        if text[i].isalpha():
            c += 1
    return c


def sentence_count(text):
    c = 0
    for i in range(0, len(text)):
        if text[i] == '!' or text[i] == '?' or text[i] == '.':
            c += 1
    return c


def word_count(text):
    c = 0
    for i in range(0, len(text)):
        if text[i] == ' ':
            c += 1
    c += 1
    return c


def analyze_text(let_c, sent_c, word_c):
    grade = 0.0588 * (float(let_c) * 100 / float(word_c)) - 0.296 * (float(sent_c) * 100 / float(word_c)) - 15.8
    return grade


def format_grade(grade):
    comp = grade % 1
    if comp < 0.5:
        return int(grade)
    else:
        grade += 1
        return int(grade)


text = user_input()
let_c = letter_count(text)
print("Letter count %d" % let_c)
sent_c = sentence_count(text)
print("Sentence count %d" % sent_c)
word_c = word_count(text)
print("Word count %d" % word_c)

grade = analyze_text(let_c, sent_c, word_c)
final_grade = format_grade(grade)

if final_grade < 1:
    print("Before grade 1")
elif final_grade > 16:
    print("Grade 16+")
else:
    print("Grade %d" % final_grade)
