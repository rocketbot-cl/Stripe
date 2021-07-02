# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"

    pip install <package> -t .

"""

import os
import sys
import datetime
import time

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + \
           'Stripe' + os.sep + 'libs' + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)

import stripe


base_path = tmp_global_obj["basepath"]
cur_path = base_path + "modules" + os.sep + "PeopleandItems" + os.sep + "libs" + os.sep
if cur_path not in sys.path:
    sys.path.append(cur_path)
from PeopleandItems import PeopleandItems

module = GetParams("module")

global mod_stripe

if module == "login":
    try:
        client_id = GetParams("client_id")
        stripe.api_key = client_id

    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

if module == "send_invoice":
    try:
        sent = stripe.Invoice.send_invoice(
            mod_stripe.getInvoice(),
        )
        print(sent)
    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

if module == "add_recipient":

    line1 = GetParams("line1")
    city = GetParams("city")
    country = GetParams("country")
    line2 = GetParams("line2")
    postal_code = GetParams("postal_code")
    state = GetParams("state")
    email = GetParams("email")
    name = GetParams("name")
    phone = GetParams("phone")

    try:
        address = {"line1": line1, "city": city, "country": country, "line2": line2, "postal_code": postal_code,
                   "state": state}
        customer = stripe.Customer.create(
            email=email,
            name=name,
            shipping={"address": address, "name": name, "phone": phone}
        )
        print(customer)
        id = customer["id"]
        print(id)
        mod_stripe = PeopleandItems(id)

    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

if module == "add_item":

    amount = GetParams("amount")
    quantity = GetParams("quantity")
    item = GetParams("item")
    currency = GetParams("currency")

    try:
        amount = int(amount) * 100
        quantity = int(quantity)
        added = stripe.InvoiceItem.create(
            customer=mod_stripe.getId(),
            currency=currency,
            unit_amount=amount,
            quantity=quantity,
            description=item
        )
        print(added)

    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e

if module == "create_invoice":

    due_date = GetParams("due_date")

    try:
        tim = due_date.split("-")
        datetime = datetime.datetime(int(tim[2]), int(tim[0]), int(tim[1]), 20, 20)

        unixtime = time.mktime(datetime.timetuple())
        inttime = int(unixtime)
        print(inttime)
        invoice = stripe.Invoice.create(
            customer=mod_stripe.getId(),
            collection_method="send_invoice",
            due_date=inttime
        )
        id = invoice["id"]
        mod_stripe.addInvoice(id)

    except Exception as e:
        print("\x1B[" + "31;40mError\x1B[" + "0m")
        PrintException()
        raise e
