from flask import Flask, render_template
import os

app = Flask(__name__)

# Get environment variables from Azure Key Vault via DevOps Variable Groups
app_flag = os.environ.get('APP_FLAG', 'development')  # Default to 'development' if not set
app_color = os.environ.get('APP_COLOR', '#667eea')  # Default color
secret_word = os.environ.get('SECRET_WORD', 'default')

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
    return render_template('index.html', app_flag=app_flag, app_color=app_color, secret_word=secret_word)

@app.route('/about')
def about():
    return render_template('about.html', app_flag=app_flag)

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

@app.route('/debug')
def debug():
    env_vars = {
        'APP_FLAG': os.environ.get('APP_FLAG', 'NOT_SET'),
        'APP_COLOR': os.environ.get('APP_COLOR', 'NOT_SET'),
        'SECRET_WORD': os.environ.get('SECRET_WORD', 'NOT_SET')
    }
    return f"""
    <h1>Environment Variables Debug</h1>
    <p>APP_FLAG: {env_vars['APP_FLAG']}</p>
    <p>APP_COLOR: {env_vars['APP_COLOR']}</p>
    <p>SECRET_WORD: {env_vars['SECRET_WORD']}</p>
    <p>All env vars: {dict(os.environ)}</p>
    """
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)