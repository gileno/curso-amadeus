# coding=utf-8

from rolepermissions.roles import AbstractUserRole


class Student(AbstractUserRole):

    pass


class Tutor(AbstractUserRole):

    available_permissions = {
        'create_course': False
    }


class SystemAdmin(AbstractUserRole):

    pass
