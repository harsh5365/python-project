from flask import Blueprint
import controllers.userController as UserController
router = Blueprint('router', __name__)
router.route('users/', methods=['GET'])(UserController.index)
router.route('users/create', methods=['POST'])(UserController.store)
router.route('users/<int:user_id>', methods=['GET'])(UserController.show)
router.route('users/<int:user_id>/edit', methods=['POST'])(UserController.update)
router.route('users/<int:user_id>', methods=['DELETE'])(UserController.destroy)
