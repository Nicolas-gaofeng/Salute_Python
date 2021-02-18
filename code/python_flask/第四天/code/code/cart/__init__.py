# coding:utf-8

from flask import Blueprint


app_cart = Blueprint("carts", __name__, template_folder="templates")

# cart.app_cart
import views