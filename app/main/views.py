from flask import render_template,redirect,request,url_for,abort,flash
from . import main
#from PIL import Image
from flask_login import login_required,current_user
from ..models import User,Post,Comment
from .forms import UpdateProfile,PostForm,AddCommentForm#,UpdateAccountForm
from .. import db
from .. import db,photos
from app.request import getQuotes





@main.route('/')
def index():
    quotes= getQuotes()  
    '''
    View root page function that returns the index page and its data
    '''

    post 
   # popular_quotes = get_quotes('popular')
    #print(popular_quotes)  # popular_quotes = get_quotes('popular')
    #print(popular_quotes)

    title = 'Home - Welcome to The Blogwebsite Review  Online'
    return render_template('index.html', title = title, quotes=quotes)

@main.route('/views')
def view_page():
    all_posts = Post.query.all()
    return render_template('views.html',all_posts=all_posts)    

@main.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateProfile()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title='Account',
                           image_file=image_file, form=form) 

@main.route("/post/<int:post_id>")
def post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)                                

@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
       # user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        #return redirect(url_for('.profile',uname=user.username))

    return render_template('post_blog.html',form =form)    

@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))    


@main.route('/user/post',methods = ['GET','POST'])
# @login_required
def post_blog():
    uname = current_user.username
    form = PostForm()
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)
    if form.validate_on_submit:
        title = form.title.data
        blog = form.blog.data
        #users=form.users.data

        post = Post.query.filter_by(title = title ).first()
        if post == None:
            new_post = Post(title = title , blog = blog )
            db.session.add(new_post)
            db.session.commit()
 

    return render_template('post_blog.html',form =form)

@main.route("/post/<int:post_id>/update", methods=['GET', 'POST'])
@login_required
def update_post(post_id):
    post = Post.query.get_or_404(post_id)

    form = PostForm()
    if form.validate_on_submit():
        post.title = form.title.data
        post.blog = form.blog.data
        db.session.add(post)
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('post', post_id=post.id))
    elif request.method == 'GET':
        form.title.data = post.title
        form.blog.data = post.blog
    return render_template('create_post.html', title='Update Post',form=form, legend='Update Post')  


@main.route("/post/<int:post_id>/delete", methods=['POST'])
@login_required
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
 
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted!', 'success')
    return redirect(url_for('main.view_page'))                           



@main.route("/post/<int:post_id>/comment", methods=["GET", "POST"])
@login_required
def comment_post(post_id):
    
    comments = Comment.query.filter_by(post_id=post_id).all()
    post = Post.query.get_or_404(post_id)
    form = AddCommentForm()
    if request.method == 'POST': # this only gets executed when the form is submitted and not when the page loads
        if form.validate_on_submit():
            #all_comments = Comment.query.all()
            comment = Comment(body=form.body.data, article=post)
            db.session.add(comment)
            db.session.commit()
            flash("Your comment has been added to the post", "success")
            return render_template('views.html',comment=comment)
            #return redirect(url_for("main.post", post_id=post.id))
    return render_template("comment_post.html", title="Comment Post",form=form, post_id=post_id,comment='comment')