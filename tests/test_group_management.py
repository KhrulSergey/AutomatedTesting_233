# -*- coding: utf-8 -*-

from models.group import Group
from random import randrange


__author__ = 'Sergey Khrul'


def test_add_new_group(app):
    # Get list of existing groups
    old_groups_list = app.group_page.get_list()
    new_group = Group(name="test group", header="New Test Header", footer="New group footer")
    # Add new group to WEB
    app.group_page.create(new_group)

    # Assert result
    assert len(old_groups_list) + 1 == app.group_page.count()  # additional assert for list length in case of exception
    old_groups_list.append(new_group)
    # Get new list from WEB
    new_groups_list = app.group_page.get_list()
    assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)


def test_add_null_group(app):
    # Get list og existing groups
    old_groups_list = app.group_page.get_list()
    new_group = Group()
    # Add new group to WEB
    app.group_page.create(new_group)

    # Assert result
    assert len(old_groups_list) + 1 == app.group_page.count()  # additional assert for list length in case of exception
    old_groups_list.append(new_group)
    # Get new list from WEB
    new_groups_list = app.group_page.get_list()
    assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)


def test_modify_group(app):
    # Get list of existing groups
    old_groups_list = app.group_page.get_list()
    group_to_modify = Group(name="test group")
    # Check if certain group exist in list
    if group_to_modify not in old_groups_list:
        app.group_page.create(group_to_modify)  # if not then we create new group
        old_groups_list = app.group_page.get_list()
    # Find certain group in list
    modified_group_index = old_groups_list.index(group_to_modify)
    group_to_modify.id = old_groups_list[modified_group_index].id
    # Determinate fields to modify
    # group_modified = Group(name="Modified Group", footer="Modified footer", header="Modified header")
    group_modified = Group(name="Modified Group", _id=group_to_modify.id)  # at least name
    # Modify group in WEB
    app.group_page.edit(group_to_modify, group_modified)

    # Assert result
    assert len(old_groups_list) == app.group_page.count()  # additional assert for list length in case of exception
    # Get updated group list
    new_groups_list = app.group_page.get_list()
    # Change modified group in old list
    old_groups_list[modified_group_index] = group_modified
    assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)


def test_modify_some_group(app):
    # Get list og existing groups
    old_groups_list = app.group_page.get_list()
    group_to_modify = Group(name="! test")
    # Check if there is any group exist in list
    if len(old_groups_list) == 0:
        app.group_page.create(Group(name="! test"))

    # Generate index to modify
    index = randrange(len(old_groups_list))
    # Find certain group in list
    group_to_modify.id = old_groups_list[index].id
    # Determinate fields to modify
    # group_modified = Group(name="Modified Group", footer="Modified footer", header="Modified header")
    group_modified = Group(name="Modified Group", _id=group_to_modify.id)  # at least name
    # Modify group in WEB
    app.group_page.modify_by_index(index, group_modified)

    # Assert result
    assert len(old_groups_list) == app.group_page.count()  # additional assert for list length in case of exception
    # Get updated group list
    new_groups_list = app.group_page.get_list()
    # Change modified group in old list
    old_groups_list[index] = group_modified
    assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)


def test_del_some_group(app):
    # Here is a teacher's code. I'd rather modified it, but for education purpose..let it be
    if app.group_page.count() == 0:
        app.group_page.create(Group(name="test"))
    old_groups_list = app.group_page.get_list()
    index = randrange(len(old_groups_list))
    #  Delete some group from list
    app.group_page.delete_by_index(index)

    # Assert result
    assert len(old_groups_list) - 1 == app.group_page.count()  # additional assert for list length in case of exception
    # Get updated group list
    new_groups_list = app.group_page.get_list()
    old_groups_list[index:index+1] = []
    assert old_groups_list == new_groups_list


def test_del_group(app):
    # Get list og existing groups
    groups_list = app.group_page.get_list()
    group_to_delete = Group(name="Modified Group")
    # Check if certain group exist in list
    if group_to_delete not in groups_list:
        app.group_page.create(group_to_delete)  # if not then we create new group
        groups_list = app.group_page.get_list()
    # Find certain group in list
    group_to_delete_index = groups_list.index(group_to_delete)
    group_to_delete.id = groups_list[group_to_delete_index].id
    #  Delete certain group from list
    app.group_page.delete(group_to_delete)

    # Assert result
    assert len(groups_list) - 1 == app.group_page.count()  # additional assert for list length in case of exception
    # Get updated group list
    groups_list = app.group_page.get_list()
    assert group_to_delete not in groups_list  # check for deleted element existed
