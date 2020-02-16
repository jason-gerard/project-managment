from flask import request, Blueprint
import controllers.project_controller as project_controller

project_routes = Blueprint('project_routes', __name__)


@project_routes.route('', methods=['GET', 'POST'])
def project():
    if request.method == 'GET':
        return project_controller.get_all_projects()

    if request.method == 'POST':
        return project_controller.create_project()


@project_routes.route('/<project_id>', methods=['GET', 'PUT', 'DELETE'])
def project_by_id(project_id):
    if request.method == 'GET':
        return project_controller.get_project_by_id(project_id)

    if request.method == 'PUT':
        return project_controller.update_project_by_id(project_id)

    if request.method == 'DELETE':
        return project_controller.delete_project_by_id(project_id)


@project_routes.route('/<project_id>/getSubProjects', methods=['GET'])
def get_sub_projects_by_parent_project_id(project_id):
    if request.method == 'GET':
        return project_controller.get_sub_projects_by_parent_project_id(project_id)


@project_routes.route('/<project_id>/getParentProject', methods=['GET'])
def get_parent_project_by_sub_project_id(project_id):
    if request.method == 'GET':
        return project_controller.get_parent_project_by_sub_project_id(project_id)