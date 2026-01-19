from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from main import app
from models import Comment, User, db, Post

#rotas
@app.route('/')
def homepage():
    posts = Post.query.order_by(Post.date_posted.desc()).all()
    return render_template('index.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', post=post)

@app.route('/add_post', methods=['GET', 'POST'])
@login_required
def add_post():
    
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_post = Post(title=title, content=content, user_id=current_user.id)
        db.session.add(new_post)
        db.session.commit()
        return redirect(url_for('homepage'))
    
    return render_template('add_post.html')

@app.route('/post/<int:post_id>/add_comment', methods=['GET', 'POST'])
@login_required
def add_comment(post_id):
    post = Post.query.get_or_404(post_id)
    
    if request.method == 'POST':
        content = request.form['content']
        user_id = current_user.id if current_user.is_authenticated else None
        new_comment = Comment(content=content, post_id=post.id, user_id=user_id)
        db.session.add(new_comment)
        db.session.commit()
        return redirect(url_for('post', post_id=post.id))
    
    return render_template('add_comment.html', post=post)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('homepage'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        existing_user = User.query.filter(User.username == username).first()
        if existing_user:
            flash('Username already exists. Please choose a different one.', 'danger')
            return redirect(url_for('register'))
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('login'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('homepage'))