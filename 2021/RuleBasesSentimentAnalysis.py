# Rule-based sentiment analysis

# Task A
# I decided to separate the logic to multiple functions.
# This provides multiple benefits such as modularity and readability.
# Also, this supports the Single Responsibility Principle from SOLID, and DRY.
import string


def string_check(comment):
    return isinstance(comment, str)


def punctuation_remover(comment):
    if not string_check(comment):
        return ""
    return comment.translate(str.maketrans("", "", string.punctuation))


def lowercase_converter(comment):
    return punctuation_remover(comment).lower()


def comment_splitter(comment):
    comment = lowercase_converter(comment)
    return comment.split()


# Task B
print(comment1 := comment_splitter("Good for the price, but poor Bluetooth connections."))
print()
print(comment2 := comment_splitter("Excellent product. Awesome quality and good customer service."))
print()
print(comment3 := comment_splitter("The quality is terrible. I would not buy this product again."))
print()


# Task C


def list_comparer(comment_list, compare_list):
    counter = 0
    for word in comment_list:
        for compare in compare_list:
            if word == compare:
                counter += 1
    return counter


def sentiment_interpreter(comment_list):
    positive = list_comparer(comment_list, ["good", "awesome", "excellent", "great"])
    negative = list_comparer(comment_list, ["bad", "broke", "terrible", "poor"])
    if positive > negative:
        print("positive comment")
    elif positive < negative:
        print("negative comment")
    else:
        print("neutral comment")


# Task D
sentiment_interpreter(comment1)
print()
sentiment_interpreter(comment2)
print()
sentiment_interpreter(comment3)
