def index():
    with open('temple/index.html') as temple:
        return temple.read()

def blog():
    with open('temple/blog.html') as temple:
        return temple.read()