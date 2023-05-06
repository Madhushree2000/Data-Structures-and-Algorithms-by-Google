# Write a function called "show_excitement" where the string
# "I am super excited for this course!" is returned exactly
# 5 times, where each sentence is separated by a single space.
# Return the string with "return".
# You can only have the string once in your code.
# Don't just copy/paste it 5 times into a single variable!


def show_excitement():
    st = 'I am super excited for this course! '
    st1 = ""
    for i in range(5):
        st1 = st1 + st
    return st1

print(show_excitement())