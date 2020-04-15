import webbrowser

search = str(input("What do you want to search about ~> "))
reporter = 'https://www.google.com/search?q=' + search

print("****************************************")
print("Loading")
print("Displaying your results.....")

webbrowser.get().open_new_tab(reporter)

