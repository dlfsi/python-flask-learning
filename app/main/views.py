from flask import render_template, redirect, url_for, abort, flash
from flask.ext.login import login_required, current_user
from . import main
from .forms import EditProfileForm, EditProfileAdminForm, EditRoleForm
from .. import db
from ..models import Role, User
from ..decorators import admin_required


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/user/<username>')
def user(username):
    user = User.query.filter_by(username=username).first_or_404()
    return render_template('user.html', user=user)


#add below route for role edit
@main.route('/edit-role/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_role(id):
    user = User.query.get_or_404(id)
    role = Role.query.get_or_404(user.role_id)
    role.permissions=0x80
    print(role.id, role.name, role.default, role.permissions)
    form = EditRoleForm(role=role)
    if form.validate_on_submit():
        return render_template('edit_role.html', form=form, role=role)
'''
        current_role.name = form.name.data
        current_role.permissions = form.permissions.data
        current_role.default = form.default.data
        db.session.add(current_role)
        flash('Your role has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_role.name
    form.permissions.data = current_role.permissions
    form.default = current_role.default
'''

@main.route('/edit-profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    form = EditProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.location = form.location.data
        current_user.about_me = form.about_me.data
        db.session.add(current_user)
        flash('Your profile has been updated.')
        return redirect(url_for('.user', username=current_user.username))
    form.name.data = current_user.name
    form.location.data = current_user.location
    form.about_me.data = current_user.about_me
    return render_template('edit_profile.html', form=form)


@main.route('/edit-profile/<int:id>', methods=['GET', 'POST'])
@login_required
#@admin_required
def edit_profile_admin(id):
    user = User.query.get_or_404(id)
    print('----->%s,%d,%d',user.role.name,user.role.id,user.role.permissions)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        user.email = form.email.data
        user.username = form.username.data
        user.confirmed = form.confirmed.data
        user.role = Role.query.get(form.role.data)
        print(__file__,'--->',user.role.id,user.role.permissions)
        if user.role.id == 1:
            user.role.permissions = 128
        elif user.role.id == 2:
            user.role.permissions = 7
        user.name = form.name.data
        user.location = form.location.data
        user.about_me = form.about_me.data
        db.session.add(user)
        flash('The profile has been updated.')
        return redirect(url_for('.user', username=user.username))
    form.email.data = user.email
    form.username.data = user.username
    form.confirmed.data = user.confirmed
    form.role.data = user.role_id
    form.name.data = user.name
    form.location.data = user.location
    form.about_me.data = user.about_me
    return render_template('edit_profile.html', form=form, user=user)
