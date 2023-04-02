"""

This file is the place to write solutions for the
skills assignment called skills-sqlalchemy. Remember to
consult the exercise instructions for more complete
explanations of the assignment.

All classes from model.py are being imported for you
here, so feel free to refer to classes without the
[model.]User prefix.

"""

from model import *

init_app()

def get_ram():
    """Get the brand with the brand_id of ram"""
    return Brand.query.filter_by(brand_id='ram').one()

def get_Corvette_che():
    """Get all models with the name Corvette and the brand_id che"""
    return Model.query.filter_by(name='Corvette', brand_id='che').all()

def get_old_models():
    """Get all models that are older than 1960"""
    return Model.query.filter(Model.year < 1960).all()

def get_recently_founded():
    """Get all brands that were founded after 1920"""
    return Brand.query.filter(Brand.founded > 1920).all()

def get_cor():
    """Get all models with names that begin with Cor."""
    return Model.query.filter(Model.name.like('Cor%')).all()

def get_extant_1903():
    """Get all brands that were founded in 1903 and that are not yet discontinued."""
    return Brand.query.filter(Brand.founded == 1903, Brand.discontinued.is_(None)).all()

def get_discontinued_or_pre_1950():
    """Get all brands that are either 1) discontinued (at any time) or 2) founded before 1950."""
    return Brand.query.filter((Brand.discontinued.isnot(None)) | (Brand.founded < 1950)).all()


def get_not_for():
    """Get all models whose brand_id is not for."""
    return Model.query.filter(Model.brand_id != 'for').all()


# -------------------------------------------------------------------
# Part 2: Discussion Questions


# 1. What is the datatype of the returned value of
# ``Brand.query.filter_by(name='Ford')``?

# flask_sqlalchemy.BaseQuery object


# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?

# an association table exists to create the link between two tables with a fictional 'many to many' relationship. It creates a many to one relationship between each table and itself, and does not have any data independent of that relationship.


# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


# did this as part 1 - disconnect between prompts and this file? See above for functions for these.
# Get the brand with the brand_id of ``ram``.
q1 = None

# Get all models with the name ``Corvette`` and the brand_id ``che``.
q2 = None

# Get all models that are older than 1960.
q3 = None

# Get all brands that were founded after 1920.
q4 = None

# Get all models with names that begin with ``Cor``.
q5 = None

# Get all brands that were founded in 1903 and that are not yet discontinued.
q6 = None

# Get all brands that are either 1) discontinued (at any time) or 2) founded
# before 1950.
q7 = None

# Get all models whose brand_id is not ``for``.
q8 = None



# -------------------------------------------------------------------
# Part 4: Write Functions


def get_model_info(year):
    """Takes in a year and prints out each model name, brand name, and brand
    headquarters for that year using only ONE database query."""

    model_info = db.session.query(Model.year, Model.name, Brand.name, Brand.headquarters).join(Brand).all()

    for model_year, model_name, brand_name, headquarters in model_info:
        if model_year == year:
            print(f'model name: {model_name}, brand name: {brand_name}, headquarters: {headquarters}')


def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    brand_info = db.session.query(Brand.name, Model.name, Model.year).join(Model).all()

    brand_dict = {}
    for brand_name, model_name, model_year in brand_info:
        brand_dict[brand_name] = brand_dict.get(brand_name, [])
        brand_dict[brand_name].append((model_name, model_year))

    for brand, model_info in brand_dict.items():
        print(f'Brand: {brand}')
        for name, year in model_info:
            print(f'Model Name: {name}, Model Year: {year}')





def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    return Brand.query.filter(Brand.name.like(f'%{mystr}%')).all()


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    return Model.query.filter(Model.year >= start_year, Model.year < end_year).all()

