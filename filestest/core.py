# Databricks notebook source
# -*- coding: utf-8 -*-
from . import helpers

def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())


# COMMAND ----------

get_hmm()

# COMMAND ----------

# -*- coding: utf-8 -*-
import helpers

def get_hmm():
    """Get a thought."""
    return 'hmmm...'


def hmm():
    """Contemplation..."""
    if helpers.get_answer():
        print(get_hmm())


# COMMAND ----------

get_hmm()
