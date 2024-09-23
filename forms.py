{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "29312792-c318-4b67-9b3b-b0de1d880b44",
   "metadata": {},
   "outputs": [],
   "source": [
    "#!/usr/bin/env python\n",
    "# coding: utf-8\n",
    "\n",
    "# In[ ]:\n",
    "\n",
    "\n",
    "from flask_wtf import FlaskForm\n",
    "from wtforms import StringField, IntegerField, SubmitField\n",
    "from wtforms.validators import DataRequired\n",
    "\n",
    "class PetForm(FlaskForm):\n",
    "    name = StringField('Name', validators=[DataRequired()])\n",
    "    age = IntegerField('Age', validators=[DataRequired()])\n",
    "    type = StringField('Type', validators=[DataRequired()])\n",
    "    submit = SubmitField('Add Pet')\n"
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
