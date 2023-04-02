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



# 2. In your own words, what is an association table, and what type of
# relationship (many to one, many to many, one to one, etc.) does an
# association table manage?




# -------------------------------------------------------------------
# Part 3: SQLAlchemy Queries


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

    pass


def get_brands_summary():
    """Prints out each brand name (once) and all of that brand's models,
    including their year, using only ONE database query."""

    pass


def search_brands_by_name(mystr):
    """Returns all Brand objects corresponding to brands whose names include
    the given string."""

    pass


def get_models_between(start_year, end_year):
    """Returns all Model objects corresponding to models made between
    start_year (inclusive) and end_year (exclusive)."""

    pass

