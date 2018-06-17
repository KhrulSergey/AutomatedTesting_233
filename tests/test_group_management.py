# -*- coding: utf-8 -*-

from models.group import Group


__author__ = 'Sergey Khrul'


def test_add_new_group(app):
    # Get list og existing groups
    old_groups_list = app.group_page.get_list()
    new_group = Group(name="test group", header="New Test Header", footer="New group footer")
    # Add new group to WEB
    app.group_page.create(new_group)
    # Get new list from WEB
    new_groups_list = app.group_page.get_list()

    assert len(old_groups_list) + 1 == len(new_groups_list)  # additional assert for list length in case of exception
    old_groups_list.append(new_group)
    assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)


def test_add_null_group(app):
    # Get list og existing groups
    old_groups_list = app.group_page.get_list()
    new_group = Group()
    # Add new group to WEB
    app.group_page.create(new_group)
    # Get new list from WEB
    new_groups_list = app.group_page.get_list()

    assert len(old_groups_list) + 1 == len(new_groups_list)  # additional assert for list length in case of exception
    old_groups_list.append(new_group)
    assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)


def test_edit_group(app):
    # Get list of existing groups
    old_groups_list = app.group_page.get_list()
    group_to_edit = Group(name="test group")
    # Check if certain group exist in list
    if group_to_edit not in old_groups_list:
        app.group_page.create(group_to_edit)  # if not then we create new group
        old_groups_list = app.group_page.get_list()
    # Find certain group in list
    modified_group_index = old_groups_list.index(group_to_edit)
    group_to_edit.id = old_groups_list[modified_group_index].id
    # Determinate fields to modify
    # group_modified = Group(name="Modified Group", footer="Modified footer", header="Modified header")
    group_modified = Group(name="Modified Group", _id=group_to_edit.id)  # at least name
    # Modify group in WEB
    app.group_page.edit(group_to_edit, group_modified)

    # Get updated group list
    new_groups_list = app.group_page.get_list()
    # Change modified group in old list
    old_groups_list[modified_group_index] = group_modified

    # Assert result
    assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)


def test_edit_first_group(app):
    # Get list og existing groups
    old_groups_list = app.group_page.get_list()
    group_to_edit = Group(name="! test")
    # Check if there is any group exist in list
    if len(old_groups_list) == 0:
        app.group_page.create(Group(name="! test"))

    # Find certain group in list
    group_to_edit.id = old_groups_list[0].id
    # Determinate fields to modify
    # group_modified = Group(name="Modified Group", footer="Modified footer", header="Modified header")
    group_modified = Group(name="Modified Group", _id=group_to_edit.id)  # at least name
    # Modify group in WEB
    app.group_page.edit_first(group_modified)

    # Get updated group list
    new_groups_list = app.group_page.get_list()
    # Change modified group in old list
    old_groups_list[0] = group_modified

    # Assert result
    assert sorted(old_groups_list, key=Group.id_or_max) == sorted(new_groups_list, key=Group.id_or_max)


def test_del_first_group(app):
    # Here is a teacher's code. I'd rather modified it, but for education purpose..let it be
    if app.group_page.count() == 0:
        app.group_page.create(Group(name="test"))

    old_groups_list = app.group_page.get_list()
    app.group_page.delete_first()
    new_groups_list = app.group_page.get_list()

    assert len(old_groups_list) - 1 == len(new_groups_list)
    old_groups_list[0:1] = []
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
    group_len_old = len(groups_list)
    #  Delete certain group from list
    app.group_page.delete(group_to_delete)

    # Get updated group list
    groups_list = app.group_page.get_list()

    assert group_len_old - 1 == len(groups_list)  # check new length of group list
    assert group_to_delete not in groups_list  # check for deleted element existed
