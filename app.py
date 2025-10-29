from flask import Flask, render_template

app = Flask(__name__)

# Sample blog posts data (in a real app, this would come from a database)
blog_posts = [
    {
        'id': 1,
        'title': 'Welcome to Our Blog',
        'content': 'This is our first blog post. We\'re excited to share our thoughts and updates with you.',
        'date': '2025-10-29',
        'author': 'Admin'
    },
    {
        'id': 2,
        'title': 'The Power of Flask',
        'content': 'Flask is a lightweight WSGI web application framework. It\'s designed to make getting started quick and easy.',
        'date': '2025-10-28',
        'author': 'Developer'
    },
    {
        'id': 3,
        'title': 'Modern Web Design',
        'content': 'Modern web design focuses on user experience, accessibility, and responsive layouts.',
        'date': '2025-10-27',
        'author': 'Designer'
    }
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/blog')
def blog():
    return render_template('blog.html', posts=blog_posts)

@app.route('/blog/<int:post_id>')
def blog_post(post_id):
    post = next((p for p in blog_posts if p['id'] == post_id), None)
    if post:
        return render_template('blog_post.html', post=post)
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)