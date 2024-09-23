{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "def28062-21be-475b-beb5-42abf8bfad12",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask import Flask, render_template, redirect, url_for\n",
    "from models import db, Pet\n",
    "from forms import PetForm\n",
    "\n",
    "app = Flask(__name__)\n",
    "app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'\n",
    "app.config['SECRET_KEY'] = 'your_secret_key'\n",
    "db.init_app(app)\n",
    "\n",
    "@app.route('/', methods=['GET', 'POST'])\n",
    "def index():\n",
    "    form = PetForm()\n",
    "    if form.validate_on_submit():\n",
    "        pet = Pet(name=form.name.data, age=form.age.data, type=form.type.data)\n",
    "        db.session.add(pet)\n",
    "        db.session.commit()\n",
    "        return redirect(url_for('index'))\n",
    "    pets = Pet.query.all()\n",
    "    return render_template('view_pets.html', form=form, pets=pets)\n",
    "if __name__ == '__main__':\n",
    "    app.run(debug=True)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
