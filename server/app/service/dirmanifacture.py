# -*- coding: utf-8 -*-

from flask import g
from sqlalchemy import or_, func

from app.model import db

__author__ = 'admin'


def find(bag):
    sql = g.tran.query(db.DirManifacture).filter_by(_deleted='infinity')
    if bag.get('id'):
        sql = sql.filter(db.DirManifacture._id == bag['id'])
    elif bag.get('search'):
        search = bag['search'] if bag.get('search') else ''
        sql = sql.filter(or_(func.concat(db.DirManifacture.name, ' ', db.DirManifacture.name_kg, ' ', db.DirManifacture.name_en, ' ')).ilike(u"%{0}%".format(search)))

    return {'docs': sql.limit(str(bag.get('limit', 20))).all()}
