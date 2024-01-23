contents = ["All carrots are to be sliced longitudinally.",
            "The carrots were reported sliced.",
            "The slicing process was well presented."]

filenames = ["doc.txt", "report.txt", "presentation.txt"]

for content, filename in zip(contents, filenames):
    file = open(f"Files/{filename}", 'w')
    file.write(content)

for file in filenames:
    readme = open(f"Files/{file}", 'r')
    cont = readme.read()
    print(cont)