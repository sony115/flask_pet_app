{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f34e1db-fc4a-40be-a3af-072b9b8dd8c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "from flask_sqlalchemy import SQLAlchemy\n",
    "db = SQLAlchemy()\n",
    "class Pet(db.Model):\n",
    "    id = db.Column(db.Integer, primary_key=True)\n",
    "    name = db.Column(db.String(100), nullable=False)\n",
    "    age = db.Column(db.Integer, nullable=False)\n",
    "    type = db.Column(db.String(100), nullable=False)"
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
