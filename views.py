def index():
    with open('index.html') as temple:
        return temple.read()

def blog():
    with open('blog.html') as temple:
        return temple.read()
